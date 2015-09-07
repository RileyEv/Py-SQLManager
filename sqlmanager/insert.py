# -*- coding: utf-8 -*-

from .verify import Verify

class Select():
    def __init__(self, table, query):
        verify = Verify(table, query)
        if verify.valid():
            self._table = table
            self._query = query
        self.sql = self.sql_gen()
    
    def _dict_to_list(self):
        new_list = []
        for k,v in self._query:
            new_list.append([k,v])
        self._query = new_list
        
    def sql_gen(self):
        sql = 'INSERT INTO ' + self._table
        sql += self.query_gen()
        return sql

    def query_gen(self):
        query = ''
        count = 0
        query += '('
        for i in self._query:
            if count == 0:
                query += i[0]
            else:
                query += ',' + i[0]
        query += ') VALUES ('
        count = 0
        for i in self._query:
            if count == 0:
                query += i[1]
            else:
                query += ',' + i[1]
        return query
