# -*- coding: utf-8 -*-

from .verify import Verify


class Insert():
    def __init__(self, table, values):
        verify = Verify(table=table, values=values)
        if verify.valid():
            self._table = table
            self._values = values
        self._sql = self.sql_gen()

    def sql_gen(self):
        sql = 'INSERT INTO ' + self._table
        sql += self.values_gen()
        return sql

    def values_gen(self):
        query = ' '
        count = 0
        query += '('
        for i in self._values:
            if count == 0:
                query += str(i[0])
            else:
                query += ',' + str(i[0])
            count += 1
        query += ') VALUES ('
        count = 0
        for i in self._values:
            if count == 0:
                query += "'{}'".format(str(i[1]))
            else:
                query += ', "{}"'.format(str(i[1]))
            count += 1
        query += ')'
        return query
