import json

# This class is responsible for reading and writing to the json file 
class FileHandler:
    # This class function reads from the json file and returns a list of top scores
    def read_json(self):
        # Read json file with error handling
        try:
            file = open("top_score/top_scores.json")
            top_scores_array = json.load(file)
            file.close()
        except:
            print("file_handler.py - Error loading JSON file")
        # Return list
        return top_scores_array

    # This class function writes to the json file updating the high scores
    def write_json(self, updated_score_list):
        # Initialise boolean to record json file writting success
        write_success = False
        # Write to json file with error handling
        try:
            with open("top_score/top_scores.json", "w", encoding="utf-8") as f:
                json.dump(updated_score_list, f, indent=1)
                write_success = True
        except:
            print("Error writing to JSON")
        # Return boolean
        return write_success