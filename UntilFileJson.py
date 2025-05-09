import json,os

workspace = os.path.dirname(os.path.abspath(__file__))

def ReadJson(filepath:str) -> dict:
    with open(os.path.join(workspace,filepath)) as file:
        return json.load(file)

def WriteJson(filepath:str,jsonDirt:dict):
    with open(os.path.join(workspace,filepath),'w') as file:
        json.dump(jsonDirt,file,indent=4)