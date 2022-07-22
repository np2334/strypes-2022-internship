import json

json_file_lines = []
with open("example_json.json", "r") as reader:
    line = reader.readline()

    while line != '':
        json_file_lines.append(line)
        line = reader.readline()

json_file = ""
for line in json_file_lines:
    json_file += line

#print(json_file)

with open("example_json.json", "r") as reader:
    json_file = json.load(reader)
    print(json_file)