import eel
import pandas as pd
import sqlite3 as sq
import sys
from typing import Union


# def query_filter(mode="error"):
#     def decorator(fun):
#         def wrapper(*args, **kwargs):
#             print(args)
#             b_func = kwargs["func"] in ["execute", "executemany", "executescript"]
#             b_fetch = kwargs["fetch"] in ["fetchall", "fetchone", "fetchmany"]
#             message = ""
#             if not b_func:
#                 message.join('Invalid function name, select one of the options '
#                              '["execute", "executemany", "executescript"]/n')
#             if not b_fetch:
#                 message.join('Invalid function name, select one of the options '
#                              '["fetchall", "fetchone", "fetchmany"]')
#             if mode == "error":
#                 assert b_func and b_fetch, message
#             elif mode == "warning":
#                 print(message)
#             else:
#                 return fun(*args, **kwargs)
#
#         return wrapper
#
#     return decorator



class DataBase:
    __query_create_table = """CREATE TABLE IF NOT EXISTS words (
            word_id INTEGER PRIMARY KEY AUTOINCREMENT,
            en TEXT NOT NULL,
            ru TEXT,
            ua TEXT,
            transcription TEXT
            );
            """
    __lang_cols = ["en", "ru", "ua"]

    def __init__(self, db_path):
        try:
            self.con = sq.connect(db_path)
            self.cur = self.con.cursor()
        except sq.Error as err:
            print(err)

        res = self.query_to_db("execute", self.__query_create_table)
        if isinstance(res, sq.Error):
            print(res)
        else:
            pass

    def __del__(self):
        self.con.close()

    def query_to_db(self, func="execute", query="", subquery="", fetch="fetchall", subfetch=1):

        func_filter = self.query_filter(func, fetch, mode="warning")

        if func_filter:
            try:
                func_res = "self.cur.{}".format(func)

                res = eval(func_res)(query, subquery)

                fetch_res = "res.{}".format(fetch)

                self.con.commit()

                if fetch == "fetchmany":
                    return eval(fetch_res)(subfetch)
                else:
                    return eval(fetch_res)()

            except sq.Error as err:
                return err

    @staticmethod
    def query_filter(func, fetch, mode="error"):
        mode = mode.lower()

        b_func = func in ["execute", "executemany", "executescript"]
        b_fetch = fetch in ["fetchall", "fetchone", "fetchmany"]
        message = ""

        if not b_func:
            message += ('Invalid function name, select one of the options '
                        '["execute", "executemany", "executescript"]\n')
        if not b_fetch:
            message += ('Invalid function name, select one of the options '
                        '["fetchall", "fetchone", "fetchmany"]')

        if mode == "error":
            if not (b_func and b_fetch):
                raise ValueError(message)
            else:
                return True
        elif mode == "warning":
            if not (b_func and b_fetch):
                print(message)
                return False
            else:
                return True

    @staticmethod
    def from_csv_to_list(path_to_words: str) -> list[list]:
        """Reads data from a csv file and writes it to a list.

        Input: path to csv file.

        Returns: A list of lists, where the first list is the names of the columns,
        and the second list is a set of file rows, each row is a tuple.

        (example [[colName1, colName2], [(col1_value1, col2_value1), (col1_value2, col2_value2)]]).
        """

        df = pd.read_csv(path_to_words)
        df = df.dropna()
        df = df.drop_duplicates()

        list_df = list()
        list_df.append(list(df.columns))
        list_df.append(list(df.itertuples(index=False, name=None)))
        return list_df

    def add_words(self, path_to_words: str = None, not_duplicate: Union[str, list] = None, words_list: list = None):
        """

        :param path_to_words:
        :param not_duplicate:
        :param words_list:
        :return:
        """

        if path_to_words:
            list_df = self.from_csv_to_list(path_to_words)

        if isinstance(not_duplicate, str):
            not_duplicate = [not_duplicate]

        if words_list:
            list_df = words_list

        counter = 0

        for i in self.__lang_cols:
            if i in list_df[0]:
                counter += 1

        if counter > 1:
            for line in list_df[1]:
                q_where = ""
                counter2 = 0
                for i, name in enumerate(list_df[0]):
                    if not_duplicate and name in not_duplicate:
                        q_where += " WHERE "
                        if counter2 != 0:
                            q_where += " AND "
                        q_where = q_where + name + " = '" + line[i] + "'"
                        counter2 += 1

                res = None
                if q_where != "":
                    query_select = f"SELECT * FROM words{q_where}"
                    res = self.query_to_db(self.cur.execute, query_select).fetchall()

                if not res:
                    query_insert = f"INSERT INTO words ({', '.join(list_df[0])}) VALUES(?,?,?)"
                    self.query_to_db(self.cur.execute, query_insert, line)
                else:
                    print(str(line) + " already in database!")

    def delete_duplicates(self):
        query = """DELETE FROM words WHERE rowid NOT IN
                    (SELECT MIN(rowid) FROM words
                        GROUP BY en, ru, ua
                );"""

        res = self.query_to_db(self.cur.execute, query)

    def get_random_words(self, num_words):
        query = f"SELECT * FROM words ORDER BY RANDOM() LIMIT {num_words};"
        res = self.query_to_db(self.cur.execute, query).fetchall()
        return res

    def delete_all_rows(self):
        query = f"DELETE FROM words"
        res = self.query_to_db(self.cur.execute, query)
        return res


if __name__ == "__main__":
    path_to_csv = "../1000_words/words.csv"
    path_to_db = "../translate.db"
    test = DataBase(path_to_db)
    test.add_words(path_to_csv, )
    # test.delete_duplicates()
    # test.delete_all_rows()

    # mas = [['en', 'transcription', 'ru'], [('price', 'praɪs', 'цена')]]
    # test.add_words(words_list=mas, not_duplicate='en')
    # test.delete_duplicates()
