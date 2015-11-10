# -*- coding: utf-8 -*-

from .verify import Verify

class Select():
    def __init__(self, table, query, fetch=['*']):
        verify = Verify(table, query, fetch)
        if verify.valid():
            self._table = table
            self._query = query
            self._fetch = fetch
        self._sql = self.sql_gen()

    def sql_gen(self):
        sql = 'SELECT ' + self.fetch_gen()
        sql += ' FROM {}'.format(self._table)
        sql += ' WHERE ' + self.query_gen()
        return sql

    def fetch_gen(self):
        fetch = ''
        for i in range(len(self._fetch)):
            if i == 0:
                fetch += '{}'.format(self._fetch[i])
            else:
                fetch += ',{}'.format(self._fetch[i])
        return fetch

    def query_gen(self):
        operators = {
            'equal': "{}='{}'",
            'notequal': "{}!='{}'",
            'greater': '{}>{}',
            'greaterequal': '{}>={}',
            'less': '{}<{}',
            'lessequal': '{}<{}',
            'like': '{} LIKE {}',
        }
        query = ''
        for k, v in self._query.iteritems():
            for a, b in v.iteritems():
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
