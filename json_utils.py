import json
import jsondiff


def get_delta(filename_a: str, filename_b: str) -> dict:
    '''Return the difference (delta) between two json files.'''

    with open(filename_a) as file_a, \
            open(filename_b) as file_b:

        data_a = json.load(file_a)
        data_b = json.load(file_b)

        diff = jsondiff.diff(data_a, data_b)
        print(diff)


if __name__ == "__main__":
    get_delta("a.json", "b.json")
