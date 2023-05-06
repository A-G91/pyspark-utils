import json

def read_file(bucket: str, filename: str):
    '''Reads object at bucket/filename. If it does not exist, returns None'''
    filename = f"./{bucket}/{filename}"
    try:
        with open(filename) as file:
            data = json.load(file)
            return data
    except:
        return None

def write_file(bucket: str, filename: str, json_dict: dict):
    '''Writes object to bucket/filename.'''
    filename = f"./{bucket}/{filename}"
    with open(filename, "w") as file:
        json.dump(json_dict, file)

# NOTE: Use below if reading/writing to s3

# def read_file(bucket: str, filename: str):
#     '''Reads object at bucket/filename. If it does not exist, returns None'''
#     try:
#         content = s3.Object(bucket, filename)
#         file_resonse = content.get()
#
#         s3_object_body = s3_response.get("Body")
#         content = s3_object_body.read()
#
#         json_dict = json.loads(content)
#         return json_dict
#     except Exception as e:
#         print(f"read_file({bucket}, {filename}) returning None - {e}")
#         return None
#
#
# def write_file(bucket: str, filename: str, json_dict: dict):
#     '''Writes object to bucket/filename.'''
#     try:
#         s3object = s3.Object(bucket, filename)
#         s3object.put(
#             Body=(bytes(json.dumps(json_dict).encode("UTF-8")))
#         )
#     except Exception as e:
#         print(f"write_file({bucket}, {filename}) threw exception - {e}")
#
