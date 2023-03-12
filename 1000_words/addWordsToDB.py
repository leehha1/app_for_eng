import numpy as np
import pandas as pd
import sqlite3 as sq

def createTableWords(cur):
    cur.execute("""CREATE TABLE IF NOT EXISTS words (
        word_id INTEGER PRIMARY KEY AUTOINCREMENT,
        eng TEXT NOT NULL,
        ru TEXT,
        ua TEXT,
        transcr TEXT
        )
        """)

# def test(func, *args):
#     func(*args)
#
#
# def test2(a):
#     print(a)
#
# # a = test2(2,3)
# test(test2, 5)



path = "D:/python/app_for_eng/1000_words/words.csv"
df = pd.read_csv(path)
df = df.dropna()
# listdf = df.values.tolist()
listdf = list()
listdf.append(list(df.columns))
listdf.append(list(df.itertuples(index=False, name=None)))

for i in listdf[1]:
    print(i[0])
# print(*listdf[1][1][0])
# print(f'INSERT INTO words ({", ".join(listdf[0])}) VALUES(?,?,?)')
# with sq.connect("translation.db") as con:
#     cur = con.cursor()
#
#     createTableWords(cur)
#     cur.executemany('INSERT INTO words (eng, transcr, ru) VALUES(?,?,?)', listdf)
#

# temp = df[df[]]
# print(listdf[0])
# print(df.shape)