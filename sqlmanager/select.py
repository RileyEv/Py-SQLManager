# -*- coding: utf-8 -*-


class Select():
    def __init__(self, table, query, fetch=['*']):
        if type(fetch).__name__ == 'list':
            for i in fetch:
                if type(i).__name__ != 'str':
                    raise TypeError(
                        "Only strings allowed in the fetch list. This isnt a string '{0}'".format(
                            i
                        )
                    )
            self._fetch = fetch
        else:
            raise TypeError('The fetch needs to be a list')
        if type(query).__name__ == 'dict':
            for k, v in query:
                if type(v).__name__ == 'dict':
                    for a, b in v:
                        if type(b).__name__ != 'str':
                            raise TypeError('You have entered your query in an incorrect format')
                else:
                    raise TypeError('You have entered your query in an incorrect format')
            self._query = query
        else:
            raise TypeError('The query needs to be a dict')
        if type(table).__name__ == 'str':
            self._table = table
        else:
            raise TypeError('The table needs to be a string')
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

    def query_gen():
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
                        query += operators[k].format(a,b)
                    except:
                        raise KeyError("'{}' is not a valid operator".format(k))
                else:
                    try:
                        query += ' AND ' + operators[k].format(a,b)
                    except:
                        raise KeyError("'{}' is not a valid operator".format(k))
        return query
