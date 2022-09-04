import json

filePath = "top_score/top-scores.json"

class fileHandler():
    def __init__(self):
        pass

def readJson():
    try:
        file = open(filePath)
        topScoresArray = json.load(file)
        file.close()
    except:
        print("file_handler.py - Error loading JSON file")

    return topScoresArray

def writeJson(updatedScoreList): #needs to be passed array
    writeSuccess = False
    try:
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(updatedScoreList, f, indent=1)
            writeSuccess = True
    except:
        print("Error writing to JSON")

    return writeSuccess