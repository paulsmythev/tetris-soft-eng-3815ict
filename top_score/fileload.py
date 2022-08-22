import json

class fileLoad():
    def __init__(self, topScoresImport):
        self.topScoresImport = topScoresImport

def loadJson():
    topScoresArray = []
    concatArray = []

    try:
        file = open("top_score/top-scores.json")
        topScoresImport = json.load(file)
        file.close()

        #writes each line to array
        for x in topScoresImport:
            topScoresArray.append(x)
        
        for x in range(len(topScoresArray)):
            brk = json.dumps(topScoresArray[x])
            test = json.loads(brk)
            strName = test["name"]
            strScore = "{:,}".format(test["score"])
            concatArray.append(strName + " - " + strScore)
    except:
        print("Error loading JSON file")
        concatArray.append("JSON Read Error!")

    return concatArray