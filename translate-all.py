import os
import requests
from googletrans import Translator
from bs4 import BeautifulSoup as bs

# It turns out that the API has "googletrans.LANGUAGES"
def getSupportedLanguages():
    docURL = "https://cloud.google.com/translate/docs/languages"
    html = bs(requests.get(docURL).text, 'html.parser')
    lansFull = html.find_all("td")

    names = []
    dests = []

    counter = 0
    for td in lansFull:
        s = td.text

        # print(str(counter) + " | " + s)
        if (counter % 2 == 0):
            names.append(s.replace(" ", "_"))
        else:
            dests.append(s.split(" ")[0])
        
        counter += 1

    d = dict(zip(names, dests))
    return d

def readTextFile(fileName):
    f = open(fileName, "r", encoding = "utf-8")
    s = f.read()
    f.close()
    return s

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

# -----------------------------------------------------

outputDirName = "Translations"
mkdir(outputDirName)

inputFileName = "doc.txt"
content = readTextFile(inputFileName)

d = getSupportedLanguages()
langAmount = len(d)

translator = Translator()

# For counting languages
counter = 1
for full, short in d.items():
    print("Translating to [" + full + "] (" + short + ")... (" + str(counter) + " / " + str(langAmount) + ") ", end = "")
    counter += 1

    s = ""
    try:
        s = translator.translate(content, dest = short).text
    except ValueError:
        print("[FAILED]")
        continue

    outputFileName = full + "_" + short + ".txt"
    f = open("./{}/{}".format(outputDirName, outputFileName), "w+", encoding = "utf-8")
    f.write(s)
    f.close()

    print("[SUCCESS]")