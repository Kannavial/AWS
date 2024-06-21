import yaml
import os
import re

path = (str)(input("Enter the path of the dict file: "))
if os.path.exists(path):
    print("Directory exists")
else:
    print("Directory does not exist")
    exit()

pathYamlChange = (str)(input("Enter the path of the yaml file: "))


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

with open (pathYamlChange, 'r') as ___file:
    data = yaml.safe_load(___file)

keyParentToChange = (str)(input("Enter the key parent you want to change: "))
keyToChange = (str)(input("Enter the key you want to change: "))
inputToChange = input("Enter the new value: ")

for yamlFile in yamlFiles:
    with open(f"{path}\{yamlFile}", 'r') as _file:
        __data = yaml.safe_load(_file)
    try:
        __data[keyParentToChange][keyToChange] = inputToChange
    except:
        _file.close()
        continue
    with open(f"{path}\{yamlFile}", 'w') as __file:
        yaml.dump(__data, __file)
        __file.close()


