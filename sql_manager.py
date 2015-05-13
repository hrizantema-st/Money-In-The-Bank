import sqlite3
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


class ManageClientsTable:

    UPDATE_USER_MESSAGE = """UPDATE clients
                        SET message = ?
                        WHERE id = ?"""

    UPDATE_USER_PASSWD = """UPDATE clients
                            SET password = ?
                            WHERE id = ?"""

    REGISTER_USER = """INSERT INTO clients (username, password)
                       VALUES(? ,?) """

    LOGIN_USER = """SELECT id, username, balance, message
                    FROM clients
                    WHERE username = ? AND password = ?
                    LIMIT 1"""

    def __init__(self, conn):
        self.__conn = conn

    def change_message(self, new_message, logged_user):
        cursor = self.__conn.cursor()
        cursor.execute(self.__class__.UPDATE_USER_MESSAGE,
                       (new_message, logged_user.get_id()))
        conn.commit()

    def change_pass(self, new_pass, logged_user):
        cursor = self.__conn.cursor()
        cursor.execute(
            self.__class__.UPDATE_USER_PASSWD, (new_pass, logged_user.get_id()))
        conn.commit()

    def register(self, username, password):
        cursor = self.__conn.cursor()
        cursor.execute(self.__class__.REGISTER_USER)
        conn.commit()

    def login(self, username, password):
        cursor = self.__conn.cursor()
        cursor.execute(self.__class__.LOGIN_USER, (username, password))
        user = cursor.fetchone()

        if(user):
            return Client(user[0], user[1], user[2], user[3])
        else:
            return False
