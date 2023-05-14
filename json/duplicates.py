import json

filename = "./test.json"
items_field = "items"
unique_field = "id"

def main():
    with open(filename) as file:
        data = json.load(filename)
        items = data[items_field]
        seen = {}
        for item in items:
            item_id = item[unique_field]
            if item_id in seen:
                print(f"Duplicate found: {item_id}")
            else:
                seen[item_id] = True


if __name__ == "__main__":
    main()
