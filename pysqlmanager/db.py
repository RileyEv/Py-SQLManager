# -*- coding: utf-8 -*-

from sqlmanager import select, insert, update

import MySQLdb as mydb
import cgitb

cgitb.enable(True)


class Connection():
    def __init__(self, host, user, passwd, db):
        self.db = mydb.connect(
            host=host,
            user=user,
            passwd=passwd,
            db=db,
        )
        self.cursor = self.db.cursor()

    def _get_primary_column(self, table=None):
        if table is not None:
            self.cursor.execute("SHOW KEYS FROM {0} WHERE Key_name='PRIMARY'".format(table))
            return cursor.fetchone()
        else:
            return None

    def select(self, table, query, fetch=['*'], in_list=False):
        Query = select.Select(table, query, fetch)
        return self.sql_action(Query._sql, need_response=True, in_list=in_list)

    def insert(self, table, values, in_list=False):
        Query = insert.Insert(table, values)
        return [self.sql_action(Query._sql, need_response=False, in_list=in_list),
    self._get_primary_column(table)]

    def update(self, table, query, values, in_list=False):
        Query = update.Update(table, query, values)
        return self.sql_action(Query._sql, need_response=False, in_list=in_list)

    def sql_action(self, sql, need_response=False, in_list=False):
        self.cursor.execute(sql)
        self.db.commit()
        self._response = ''
        if need_response:
            self._response = self.cursor.fetchall()
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
