# -*- coding: utf-8 -*-


class Verify():
    def __init__(self, table='', query={}, fetch=['*'], values=[]):
        self._table = table
        self._query = query
        self._fetch = fetch
        self._values = values
        self._table_valid = False
        self._query_valid = False
        self._table_valid = False
        self._values_valid = False
        self.verify_table()
        self.verify_query()
        self.verify_values()
        self.verify_fetch()

    def verify_table(self):
        try:
            self._table = str(self._table)
        except TypeError:
            raise TypeError('The table need to be a string')
        else:
            self._table_valid = True

    def verify_query(self):
        if not isinstance(self._query, dict):
            raise TypeError('The query needs to be a dict')
        else:
            for k, v in self._query.iteritems():
                if not isinstance(v, dict):
                    raise TypeError('You have entered your query in an incorrect format')
                else:
                    for a, b in v.iteritems():
                        try:
                            b = str(b)
                        except TypeError:
                            raise TypeError('You have entered your query in an incorrect format')
            self._query_valid = True

    def verify_values(self):
        try:
            values = list(self._values)
        except TypeError:
            raise TypeError('The values needs to be a list')
        else:
            for i in self._values:
                try:
                    i = list(i)
                except TypeError:
                    raise TypeError('You have entered your values in an incorrect format')
                else:
                    for a in i:
                        try:
                            a = str(a)
                        except TypeError:
                            raise TypeError('You have entered your values in an incorrect format')
            self._values_valid = True

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
