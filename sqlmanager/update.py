# -*- coding: utf-8 -*-

from .verify import Verify

class Select():
    def __init__(self, table, query, fetch=['*'], values):
        verify = Verify(table, query, fetch, values)
        if verify.valid():
            self._table = table
            self._query = query
            self._fetch = fetch
            self._values = values
        self.sql = self.sql_gen()
    
    def _dict_to_list(self):
        new_list = []
        for k,v in self._values:
            new_list.append([k,v])
        self._query = new_list
        
    def sql_gen(self):
        sql = 'UPDATE ' + self._table
        sql += ' SET ' + self.values_gen()
        sql += ' WHERE ' + self.query_gen()
        return sql

    def values_gen(self):
        values = ''
        for k, v in self._values:
            if values == '':
                values += '{}={}'.format(k, v)
            else:
                values += ',{}={}'.format(k, v)
        return values
        
    def query_gen(self):
        operators = {
            'equal': '{}={}',
            'notequal': '{}!={}',
            'greater': '{}>{}',
            'greaterequal': '{}>={}',
            'less': '{}<{}',
            'lessequal': '{}<{}',
            'like': '{} LIKE {}',
        }
        query = ''
        for k, v in self._query:
            for a, b in v:
                if query == '':
                    try:
                        query += operators[k].format(a, b)
                    except:
                        raise KeyError("'{}' is not a valid operator".format(k))
                else:
                    try:
                        query += ' AND ' + operators[k].format(a, b)
                    except:
                        raise KeyError("'{}' is not a valid operator".format(k))
        return query
