# -*- coding: utf-8 -*-

from sqlmanager import select, insert, update, verify

import MySQLdb as mydb
import cgitb
import uuid

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
            return self.cursor.fetchone()[4]
        else:
            return None

    def _check_primary_key(table, pk):
        self.cursor.execute("select * from {0} where {1}='{2}'".format(table, pk[0], pk[1]))
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def select(self, table, query, fetch=['*'], in_list=False):
        Query = select.Select(table, query, fetch)
        return self.sql_action(Query._sql, need_response=True, in_list=in_list)

    def insert(self, table, values, in_list=False):
        pk = self._get_primary_column(table)
        verify = verify.Verify(values=values)
        if verify:
            pkfound = None
            for i in values:
                if i[0] == pk:
                    pkfound = i
                    break
        if pkfound is not None:
            pkexist = _check_primary_key(table, pkfound)
            if pkexist:
                raise KeyError('The primary key already exists')
        else:
            pkexist = True
            while pkexist:
                pkfound = [pk, str(uuid.uuid4())]
                pkexist = _check_primary_key(table, pkfound)
            values.append(pkfound)

        Query = insert.Insert(table, values)
        return self.sql_action(Query._sql, need_response=False, in_list=in_list)

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
