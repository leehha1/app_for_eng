import docx
import numpy as np
import pandas as pd

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

def splitWords(mass):

    listWords = []

    for strr in mass:

        strr = strr.replace('\xa0', '')
        strr = strr.replace('[', '—')
        strr = strr.replace(']', '')
        splitStr = strr.split('—')
        listWords.append(splitStr)
        
    return listWords


def createCSV(listWords):
    df = pd.DataFrame(listWords, columns=['en', 'transcription', 'ru'])
    return df


path = "D:/python/app_for_eng/1000_words/words.docx"
text = getText(path)

listWords = splitWords(text)
print(listWords)
df = createCSV(listWords)
df[df.columns] = df.apply(lambda x: x.str.strip())
# print(df.head(5))
path_to_save = "D:/python/app_for_eng/1000_words/words.csv"
df.to_csv(path_to_save, index=False)

