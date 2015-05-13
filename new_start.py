import sqlite3
from settings import DB_NAME
from bank_interface import BankInterface
from cinema_db import ManageClientsTable


def main():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    bank_manager = ManageClientsTable(conn)
    interface = BankInterface(bank_manager)

    interface.start()

if __name__ == "__main__":
    main()
