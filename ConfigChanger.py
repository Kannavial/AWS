import yaml
import os
import re

#Masih ada 2 masalah tidak bisa ubah list dan ubah key yang nestnya tidak sama.
yamlFiles = []
path = ""

def CheckDirExistOrNot():
    if os.path.exists(path):
        print("Directory exists")
    else:
        print("Directory does not exist")
        exit()

def has_yaml_extension(filename):
    yaml_extension_pattern = r'\.yaml$'
    return re.search(yaml_extension_pattern, filename, re.IGNORECASE) is not None

def CheckDir(_path_):
    contents = os.listdir(_path_)
    for file in contents:
        full_path = os.path.join(_path_, file)
        if(os.path.isdir(full_path)):
            pathInsideDir = f"{full_path}"
            CheckDir(pathInsideDir)
        elif(has_yaml_extension(full_path)):
            yamlFiles.append(full_path)

def CheckYamlConfig():
    configChange = (str)(input("Key To Change, Delimiter (.): "))
    _config = configChange.split(".")
    inputToChange = (str)(input("Enter the input value: "))
    ChangeConfig(_config, inputToChange)


def ChangeConfig(configYamlPath, inputToChange):
    for yamlFile in yamlFiles:
        try:
            with open(f"{yamlFile}", 'r') as _file:
                __data = yaml.safe_load(_file)
            current_level = __data 
            for key in (configYamlPath[:-1]):
                current_level = current_level[key]
            current_level[configYamlPath[-1]] = inputToChange
            with open(f"{yamlFile}", 'w') as __file:
                print(__data)
                yaml.dump(__data, __file,)
        except Exception as e:  
            print(f"Error is {yamlFile}: {e}")
            _file.close()
            continue
path = (str)(input("Enter the path of the dictionary parent: "))
CheckDirExistOrNot()

CheckDir(path)

CheckYamlConfig()
