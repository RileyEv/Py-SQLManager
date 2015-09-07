# -*- coding: utf-8 -*-


class Verify():
    def __init__(self, table, query, fetch=['*']):
        self._table = table
        self._query = query
        self._fetch = fetch
        self._table_valid = False
        self._query_valid = False
        self._table_valid = False
        verify_table()
        verify_query()
        verify_fetch()
    
    def verify_table(self):
        if type(self._table).__name__ == 'str':
            self._table_valid = True
        else:
            raise TypeError('The table needs to be a string')
    
    def verify_query(self):
        if type(self._query).__name__ == 'dict':
            for k, v in query:
                if type(v).__name__ == 'dict':
                    for a, b in v:
                        if type(b).__name__ != 'str':
                            raise TypeError('You have entered your query in an incorrect format')
                else:
                    raise TypeError('You have entered your query in an incorrect format')
            self._query_valid = True
        else:
            raise TypeError('The query needs to be a dict')
    
    def verify_fetch(self):
        if type(self._fetch).__name__ == 'list':
            for i in fetch:
                if type(i).__name__ != 'str':
                    raise TypeError(
                        "Only strings allowed in the fetch list. This isnt a string '{0}'".format(
                            i
                        )
                    )
            self._fetch_valid = True
        else:
            raise TypeError('The fetch needs to be a list')
            
    def valid(self):
        if self._table_valid and self._query_valid and self._fetch_valid:
            return True
        else:
            return False
