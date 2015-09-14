# -*- coding: utf-8 -*-


class Verify():
    def __init__(self, table, query, fetch=['*'], values={}):
        self._table = table
        self._query = query
        self._fetch = fetch
        self._values = values
        self._table_valid = False
        self._query_valid = False
        self._table_valid = False
        self._values_valid = False
        self.verify_table()
        self._query_valid = self.verify_query(self._query)
        self._values_valid = self.verify_query(self._values)
        self.verify_fetch()
    
    def verify_table(self):
        if type(self._table).__name__ == 'str':
            self._table_valid = True
        else:
            raise TypeError('The table needs to be a string')
    
    def verify_query(self, query):
        if type(query).__name__ == 'dict':
            for k, v in query.iteritems():
                if type(v).__name__ == 'dict':
                    for a, b in v.iteritems():
                        if type(b).__name__ != 'str':
                            raise TypeError('You have entered your query in an incorrect format')
                            return False
                else:
                    raise TypeError('You have entered your query in an incorrect format')
                    return False
            return True
        else:
            raise TypeError('The query needs to be a dict')
            return False
    
    def verify_fetch(self):
        if type(self._fetch).__name__ == 'list':
            for i in self._fetch:
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
        if self._table_valid and self._query_valid and self._fetch_valid and self._values_valid:
            return True
        else:
            return False
