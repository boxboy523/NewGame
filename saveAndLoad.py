import json

def load(directory):
    with open(directory,'rt',encoding='UTF8') as file:
        save_data = json.load(file)
    print(json.dumps(save_data, indent="\t", ensure_ascii = False))
    #미완성