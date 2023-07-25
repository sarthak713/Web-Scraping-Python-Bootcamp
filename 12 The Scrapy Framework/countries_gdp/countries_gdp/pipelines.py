# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import sqlite3

class CountriesGdpPipeline:
    def process_item(self, item, spider):
        if not isinstance(item['gdp'], float):
            raise DropItem('Missing GDP Value, Item Excluded')
        return item
    

class SaveToDatabasePipeline:
    # executes automatically everytime instance is created
    # self is instance of pipeline
    def __init__(self): 
        # sqlite is local db, supported in STL
        # create connection
        self.con=sqlite3.connect('countries_gdp.db')    # id DB does not exist it creates DB
        # pointer to DB to execute queries
        self.cur=self.con.cursor()

    # this is called everytime spider is open, when spider starts scraping
    def open_spider(self, spider):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS countries_gdp 
            (country_name TEXT PRIMARY KEY,
             region TEXT,
             gdp REAL,
             year INTEGER)
        """)
        self.con.commit()

    def process_item(self, item, spider):
        # insert item in table
        self.con.execute("""
            INSERT INTO countries_gdp (country_name, region, gdp, year) VALUES (?,?,?,?)       
        """, (item['country_name'],item['region'],item['gdp'],item['year']))
        self.con.commit()

    def close_spider(self,spider):
        self.con.close()
