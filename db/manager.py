# -*- coding=utf-8 -*-
import psycopg2
from uiauto import config


class Dbmanager(object):

    conn = psycopg2.connect(config.DBServer.UIAUTO_DB_DSN)
    dbmanager = conn.cursor()

    @staticmethod
    def update(sql):
        Dbmanager.dbmanager.execute(sql)
        Dbmanager.conn.commit()

    @staticmethod
    def select_one(sql):
        Dbmanager.dbmanager.execute(sql)
        return Dbmanager.dbmanager.fetchone()

    @staticmethod
    def disconnect():
        Dbmanager.dbmanager.close()
