import sqlite3
from Tests import MainHotel


class HotelDataBase:
    def __init__(self):
        self.Connect = sqlite3.connect('DataBaseHotel.db')
        self.Cursor = self.Connect.cursor()
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS MainBase(
        SerializationText TEXT);
        """)
    def Loaded(self):
        self.Cursor.execute("SELECT * FROM MainBase;")
        one_result = self.Cursor.fetchone()
        print(one_result)
        MainHotel.Parser.SetFromString(one_result)
        return one_result
    def Unload(self):
        string = MainHotel.Parser.GetAsString()
        self.Cursor.execute("""CREATE TABLE IF NOT EXISTS MainBase(
        SerializationText TEXT);
        """)

DataBase = HotelDataBase()