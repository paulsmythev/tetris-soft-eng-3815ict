#Class is responsible for reading and writing to the JSON file 
import json

FILE_PATH = "top_score/top-scores.json"

class FileHandler:
    #readJson() loads the top scores saved in the "top_score/top-scores.json", if the file cant be found then a error is diplayed here and in the top_score_screen.py   
    def read_json(self):
        try:
            file = open(FILE_PATH)
            top_scores_array = json.load(file)
            file.close()
        except:
            print("file_handler.py - Error loading JSON file")

        return top_scores_array

    #writeJson(updatedScoreList) receives an array that then over-writes the data in "top_score/top-scores.json" then returns a Boolean depending on success 
    def write_json(self, updated_score_list):
        write_success = False
        try:
            with open(FILE_PATH, "w", encoding="utf-8") as f:
                json.dump(updated_score_list, f, indent=1)
                write_success = True
        except:
            print("Error writing to JSON")

        return write_success