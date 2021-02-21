import os
import googletrans
from googletrans import Translator

def readTextFile(fileName):
    f = open(fileName, "r", encoding = "utf-8")
    s = f.read()
    f.close()
    return s

def mkdir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

# ---------------------------------------------------

outputDirName = "Translations"
mkdir(outputDirName)

inputFileName = "doc.txt"
content = readTextFile(inputFileName)

supportedLanguages = googletrans.LANGUAGES

# ---------------------------------------------------

translator = Translator()
langAmount = len(supportedLanguages)
counter = 1
for code, name in supportedLanguages.items():
    name = name.capitalize().strip().replace(" ", "_")

    print("Translating to [" + name + "] (" + code + ")... (" + str(counter) + " / " + str(langAmount) + ") ", end = "")
    counter += 1

    t = ""
    try:
        s = translator.translate(content, dest = code).text
    except ValueError:
        print("[FAILED]")
        continue

    outputFileName = name + "_" + code + ".txt"
    f = open("./{}/{}".format(outputDirName, outputFileName), "w+", encoding = "utf-8")
    f.write(s)
    f.close()

    print("[SUCCESS]")