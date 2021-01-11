import json


class HackerrankData(object):
    def __init__(self, name, score, selected=False):
        self.Name = name
        self.Score = score
        self.Selected = selected


class DataManager(object):
    def __init__(self):
        self.data = []
        self.jsonData = None

    def loadJsonFile(self):
        with open("hackerrank_challenges_list.json") as jsonFile:
            self.jsonData = json.load(jsonFile)
        self.jsonData = self.jsonData["div"]["a"]
        for item in self.jsonData:
            if item["@class"] == "js-track-click challenge-list-item":
                self.data.append(HackerrankData(item["@data-attr1"], item["@data-attr7"]))
