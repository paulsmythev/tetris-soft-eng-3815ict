#Class is responsible for reading and writing to the JSON file 
import json

filePath = "top_score/top-scores.json"

class fileHandler():
    def __init__(self):
        pass

#readJson() loads the top scores saved in the "top_score/top-scores.json", if the file cant be found then a error is diplayed here and in the top_score_screen.py   
def readJson():
    try:
        file = open(filePath)
        topScoresArray = json.load(file)
        file.close()
    except:
        print("file_handler.py - Error loading JSON file")

    return topScoresArray

#writeJson(updatedScoreList) receives an array that then over-writes the data in "top_score/top-scores.json" then returns a Boolean depending on success 
def writeJson(updatedScoreList):
    writeSuccess = False
    try:
        with open(filePath, "w", encoding="utf-8") as f:
            json.dump(updatedScoreList, f, indent=1)
            writeSuccess = True
    except:
        print("Error writing to JSON")

    return writeSuccess