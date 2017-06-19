import json
from pprint import pprint
import os
import re
import string

def cleanDoc(doc):
    aposRegex = re.compile(" ’")
    doc = re.sub(aposRegex, "’", doc)
    aposRegex = re.compile(" '")
    doc = re.sub(aposRegex, "'", doc)
    transDict = {key:None for key in string.punctuation}
    transDict.update({"’":"’", "'":"'", "-":"-"})
    translator = str.maketrans(transDict)
    doc = doc.translate(translator)
    return doc

def replaceCorefs(filename, pathToStanCoreNLP):
    currDir = os.getcwd()
    os.chdir(pathToStanCoreNLP)
    doc = ""
    properNouns = []
    with open(filename, "r") as data_file:    
        data = json.load(data_file)
    senten = {}
    for i in range(len(data["sentences"])):
        senten[i + 1] = {}
        for word in data["sentences"][i]["tokens"]:
            senten[i + 1][word["index"]] = word["originalText"]
            if word["pos"] in ["NNP", "NNPS"]:
                properNouns.append(word["originalText"])
    for key, coref in data["corefs"].items():
        for curr in coref:
            if curr["isRepresentativeMention"]:
                hold = curr["text"]
                break
        for curr in coref:
            if not curr["isRepresentativeMention"]:
                senten[curr["sentNum"]][curr["startIndex"]] = hold
                for i in range(curr["startIndex"] + 1, curr["endIndex"]):
                    try:
                        del senten[curr["sentNum"]][i]
                    except KeyError:
                        continue
    os.chdir(currDir)
    for x in sorted(senten):
        for y in sorted(senten[x]):
            doc += senten[x][y] + " "
    return properNouns, doc