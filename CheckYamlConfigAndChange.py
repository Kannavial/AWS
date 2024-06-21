import yaml
import os
import re

path = (str)(input("Enter the path of the dict file: "))
pathYamlChange = (str)(input("Enter the path of the yaml file: "))

if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does not exist")
    exit()

def has_yaml_extension(filename):
    yaml_extension_pattern = r'\.yaml$'
    return re.search(yaml_extension_pattern, filename, re.IGNORECASE) is not None

contents = os.listdir(path)
yamlFiles = []
for file in contents:
    if(os.path.isdir(file)):
        continue
    if(has_yaml_extension(file)):
        yamlFiles.append(file)

with open (pathYamlChange, 'r') as file:
    data = yaml.safe_load(file)
_data = data

keyParentToChange = (str)(input("Enter the key parent you want to change: "))
keyToChange = (str)(input("Enter the key you want to change: "))
inputToChange = input("Enter the new value: ")

for yamlFile in yamlFiles:
    with open(path + yamlFile, 'r') as file:
        __data = yaml.safe_load(file)
    __data[keyParentToChange][keyToChange] = inputToChange
    with open(path + yamlFile, 'w') as file:
        yaml.dump(__data, file)


