import yaml
import os
import re

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
    configChange = (str)(input("Key To Change, Use Space every path parent: "))
    _config = configChange.split(" ")
    inputToChange = (str)(input("Enter the value to change: "))
    ChangeConfig(_config, inputToChange)


def ChangeConfig(configYamlPath, inputToChange):
    for yamlFile in yamlFiles:
        try:
            with open(f"{yamlFile}", 'r') as _file:
                __data = yaml.safe_load(_file)
            _data___ = __data
            for key in range (len(configYamlPath)):
                if(configYamlPath[key] == len(configYamlPath) - 1):
                    _data___[configYamlPath[key]] = inputToChange
                else:
                    __data = _data___[configYamlPath[key]]
                _file.close()

            with open(f"{yamlFile}", 'w') as __file:
                yaml.dump(__data, __file)
                __file.close() 
        except:  
            _file.close()
            continue
path = (str)(input("Enter the path of the dict file: "))
CheckDirExistOrNot()

CheckDir(path)

CheckYamlConfig()
