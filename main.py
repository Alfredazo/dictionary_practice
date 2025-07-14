def open_json_from_file(file_path):
    import json

    with open(file_path, "r") as file:
        return json.load(file)


dictionary = open_json_from_file("simple_json.json")
print(dictionary.get("word"))  # Output: example


# Como obtener la lista de valores synonyms
synonyms = dictionary.get("synonyms")
print(synonyms)  # Output: ['sample', 'case', 'illustration']
for synonym in synonyms:
    if synonym == "case":
        print("Bad Performance", synonym)  # Output: sample, case, illustration

# Version optima
print("Good Performance", dictionary.get("synonyms")[1])  # Output: ['sample', 'case', 'illustration']

# message = f"Good Performance {dictionary.get('synonyms')[1]}"
# message_2 = "Good Performance {}".format(dictionary.get("synonyms")[1])
# message_3 = "Good performance %s", dictionary.get("synonyms")[1]

print(dictionary.get("word"))
print(dictionary.get("definition"))
print(dictionary.get("prt_of_speech",None))
print(dictionary.get("synonyms"))
print(dictionary.get("usage"))
#print(dictionary.get("number"))
number = dictionary.get("number",None)
if number is None:
    dictionary["number"]=7

print(dictionary)