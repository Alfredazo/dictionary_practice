def open_json_from_file(file_path):
    import json

    with open(file_path, "r") as file:
        return json.load(file)


dictionary = open_json_from_file("simple_json.json")
print(dictionary.get("word"))  # Output: example
