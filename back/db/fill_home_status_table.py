#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psycopg2

from api.settings import LANGUAGE_CODE
from api.settings.local import DATABASES
from const import STATUS

""" We did this script to fill the status table cause it's not something
the user will do. """

def main():

    try:
        conn = psycopg2.connect(
            user = DATABASES['default']['USER'],
            password = DATABASES['default']['PASSWORD'],
            host = DATABASES['default']['HOST'],
            port = DATABASES['default']['PORT'],
            database = DATABASES['default']['NAME']
        )
        cur = conn.cursor()
        sql_block = ""

        for dicts in STATUS.items():
            for dict in dicts[1].items():
                sql_block += f"INSERT INTO home_status (name, level) VALUES ('{dict[1][LANGUAGE_CODE]}', '{dict[1]['level']}');\n"

        cur.execute(sql_block)
        cur.close()
        conn.commit()
        conn.close()

        return True

    except (Exception, psycopg2.Error) as error :
        print ("Erreur lors de la connexion à la base bappiment !\n", error)

if __name__ == '__main__':
    main()