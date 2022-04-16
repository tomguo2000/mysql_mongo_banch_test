import pymysql

class Singleton:

    def __init__(self, cls):
        self._cls = cls

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)


@Singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        self.db_host = '47.100.138.122'
        self.db_port = 33006
        self.db_user = 'message_center'
        self.db_password = 'a9U911VU2Ggz'
        self.db_database = 'message_center'
        self.db = pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            port=self.db_port,
            database=self.db_database,
            password=self.db_password
        )

    def __str__(self):
        return 'Database connection object'


if __name__ == '__main__':
    c1 = DBConnection.Instance()
    c2 = DBConnection.Instance()
    print(c1)
    print(type(c1))
    cur = c1.db.cursor()
    print(type(cur))

    print("Id of c1 : {}".format(str(id(c1))))
    print("Id of c2 : {}".format(str(id(c1))))