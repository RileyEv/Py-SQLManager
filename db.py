# -*- coding: utf-8 -*-

from sqlmanager import select, insert, update

import MySQLdb as mydb


class Connection():
    def __init__(self, host, user, passwd, db):
        self.db = mydb.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db,
        )
        self.cursor = self.db.cursor()

    def select(self, query, table, fetch=['*'], in_list=False):
        Query = select.Select(table, query, fetch)
        self.sql_action(Query._sql, need_response=True, in_list=in_list)
    
    def insert(self, table, values, in_list=False):
        Query = insert.Insert(table, values)
        self.sql_action(Query._sql, need_response=True, in_list=in_list)
        
    def update(self, table, query, values, in_list=False):
        Query = update.Update(table, query, values)
        self.sql_action(Query._sql, need_response=True, in_list=in_list)

    def sql_action(self, sql, need_response=False, in_list=False):
        self.cursor.execute(sql)
        #cursor = self.cursor
        #cursor.execute(sql)
        response = ''
        if need_response:
            self._response = self.cursor.fetchall()
            #response = cursor.fetchall()
        if in_list:
            self._response = self._tupletolist(self._response)
        return self._response

    def _tupletolist(self, input_tuple):
        input_tuple = list(input_tuple)
        for i in range(len(input_tuple)):
            input_tuple[i] = list(input_tuple[i])
        return input_tuple

    def __del__(self):
        self.cursor.close()
        self.db.close()
