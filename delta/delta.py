import utils

class DeltaHelper:

    def __init__(self, **kwargs):
        s3_client = kwargs.get("s3_client", None)
        aws_account = kwargs.get("aws_account", "test")
        aws_region = kwargs.get("aws_region", "local")
        self.bucket = f'{aws_account}-{aws_region}'

    def write_delta(self, current_data: list, id_field: str, items_field: str, filename: str):
        '''
        Computes delta from the given list of dictionaries and then writes to s3
        Current data is passed into function, while the previous data is loaded from s3.
        After the delta is computed, write the current_data to the previous bucket.
        id_field - this is the key in the dictionaries that will be used for comparison.
        items_field - this is the key in the dictionaries that contains the items.
        '''

        if current_data is None:
            current_data = []
        
        current_items = self.join_list(current_data, items_field)
        previous_items = self.load_previous_data(items_field, filename)

        delta = self.get_delta(current_items, previous_items, id_field)
        utils.write_file(self.bucket, self.delta_filename(filename), delta)

        # After delta is computed, write current data to previous
        utils.write_file(self.bucket, self.previous_filename(filename), current_data)


    def get_delta(self, current_items: list, previous_items: list, id_field: str):

        current_info = {item[id_field]: item for item in current_items}
        previous_info = {item[id_field]: item for item in previous_items}

        removed = [{id_field: item_id, "remove": True} for item_id in previous_info.keys() if item_id not in current_info.keys()]
        added = [current_info[item_id] for item_id in current_info.keys() if item_id not in previous_info.keys()]

        updated = []
        for item_id, current_item in current_info.items():
            if item_id not in previous_info:
                continue

            
            prev_item = previous_info[item_id]
            changes = {id_field: item_id}
            
            for k, v in current_item.items():
                if k not in prev_item or v != prev_item[k]:
                    changes[k] = v

            if len(changes) > 1:
                updated.append(changes)
        
        return added + updated + removed

    
    def load_previous_data(self, items_field: str, filename: str) -> list:

        previous_data = utils.read_file(self.bucket, self.previous_filename(filename))
        if previous_data is None:
            return None
        
        previous_items = self.join_list(previous_data, items_field)
        return previous_items

    def join_list(self, objects: list, items_field: str) -> list:
        retval = []
        for obj in objects:
            items = obj[items_field]
            retval.extend(items)
        return retval

    def previous_filename(self, filename: str) -> str:
        return f"previous/{filename}"

    def delta_filename(self, filename: str) -> str:
        return f"delta/{filename}"

if __name__ == "__main__":
    helper = DeltaHelper()
    helper.write_delta(None, "id", "items", "mock.json")

         



    




