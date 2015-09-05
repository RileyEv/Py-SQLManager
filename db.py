# -*- coding: utf-8 -*-

from gaigo.settings import DATABASE
from gaigo.backend.sqlmanager import select

import MySQLdb as mydb


class Connection():
    def __init__(self):
        self.db = mydb.connect(
            host=DATABASE['host'],
            user=DATABASE['user'],
            passwd=DATABASE['passwd'],
            db=DATABASE['db'],
        )
        self.cursor = self.db.cursor()

    def select(self, query, table, fetch=['*'], response=True, in_list=False):
        Query = select.Select(query, table, fetch)
        sql = Query.sql_gen()
        self.sql_action(sql, response, in_list)

    def sql_action(self, sql, response=True, in_list=False):
        pass

    def __del__(self):
        self.cursor.close()
        self.db.close()
