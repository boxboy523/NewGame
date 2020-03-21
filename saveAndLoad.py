import json,os
from Place import place
from Unit import unit

def strToBool(s):
    return s == "True"

def load(directory,window): # TODO : 클래스의 변수를 동적으로 읽어들이게 하기
    PlaceList =[]
    UnitList =[]
    try:
        placeFileList = os.listdir(directory+"/Places")
        unitFileList = os.listdir(directory+"/Units")
        for i in range(len(placeFileList)):#세이브파일의 Place를 읽어들여 PlaceList에 저장
            with open(directory+"/Places/"+placeFileList[i],'rt',encoding='UTF8') as file:
                save_data = json.load(file)
                newPlace = place(save_data['Name'],save_data['ConnectedPlace'])
                newPlace.Units = save_data['Units']
                newPlace.Things = save_data['Things']
                PlaceList.append(newPlace)
        for i in range(len(unitFileList)): #세이브파일의 Unit을 읽어들여 UnitList에 저장
            with open(directory+"/Units/"+unitFileList[i],'rt',encoding='UTF8') as file:
                save_data = json.load(file)
                newUnit = unit(save_data['Name'],save_data['MaxHP'],save_data['Atk'],save_data['Def'],save_data['Place'],window)
                newUnit.item = save_data['item']
                newUnit.Live = strToBool(save_data['Live'])
                UnitList.append(newUnit)
        return(PlaceList,UnitList)
    except:
        return -1

def save(directory,window):
    pL = window.PlaceList
    uL = window.UnitList
    placeDir = directory+"/Places"
    unitDir = directory+"/Units"

    createFolder(placeDir)
    createFolder(unitDir)
    for i in range(len(pL)):
        save_data = pL[i].returnDict()
        with open(placeDir+"/"+pL[i].Name+".json", 'w', encoding='UTF8') as f:
            json.dump(save_data,f,indent="\t")
    for i in range(len(uL)):
        save_data = uL[i].returnDict()
        with open(unitDir+"/"+uL[i].Name+".json", 'w', encoding='UTF8') as f:
            json.dump(save_data,f,indent="\t")

def createFolder(directory):
    try:
        if not (os.path.isdir(directory)):
            os.makedirs(os.path.join(directory))
    except OSError as e:
        print('Error: Creating directory.'+directory)