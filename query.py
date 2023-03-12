import sqlite3 as sq
from db_queries.web_interface import DataBase
from db_queries.db import TranslatedWords


def main():
    # db = DataBase('translate.db')
    # res2 = db.query_to_db("execute", query="SELECT * FROM words", fetch="fetchall", subfetch=3)
    # print(res2)

    db2 = TranslatedWords('translate.db')
    res3 = db2.query_to_db("execute", query="SELECT * FROM words", fetch="fetchall", subfetch=3)
    print(res3)
    res4 = db2.get_random_words(2)
    print(res4)
    # res3=db.query_to_db(None, "SELECT * FROM words")


if __name__ == '__main__':
    # b(1,2,3)
    main()



