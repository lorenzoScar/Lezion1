import pathlib

import mysql.connector

class DBConnect:
    _myPool = None

    def __init__(self):
        raise RuntimeError("Attenzione! Non devi creare un'istanza di questa classe."
                           "Usa i metodi di classe.")

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(
                    pool_size = 3,
                    pool_name = "myPool",
                    option_files = f"{pathlib.Path(__file__).resolve().parent}/connector.cfg"
                )
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None
        else:
            return cls._myPool.get_connection()
