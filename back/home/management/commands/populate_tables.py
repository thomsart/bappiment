#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Module to populate the data base of all datas we need to use the API.
These datas belong to the API and are not the result of users actions. """

import psycopg2
from django.core.management.base import BaseCommand, CommandError

from api.settings.local import DATABASES
from .datas import LANGUAGE
from .datas.installation_states import INSTALLATION_STATES
from .datas.product_familys import PRODUCT_FAMILYS
from .datas.product_brands import PRODUCT_BRANDS
from .datas.product_states import PRODUCT_STATES
from .datas.user_states import USER_STATES
from .datas.user_status import STATUS
from .datas.vehicle_states import VEHICLE_STATES



class Command(BaseCommand):

    help = 'this command populate db from the built-in datas.'

    def handle(self, *args, **kwargs):

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

            # """ We populate the home_status table: """
            # for dicts in STATUS.items():
            #     level = ""
            #     status = ""
            #     for key, value in dicts[1].items():
            #         if key == 'level':
            #             level += value
            #         if key == LANGUAGE:
            #             status += value
            #     sql_block += f"INSERT INTO home_status (name, level) VALUES ('{status}', '{level}');\n"

            """ We populate the agenda_userstate table: """
            for dicts in USER_STATES.items():
                state = ""
                for key, value in dicts[1].items():
                    if key == LANGUAGE:
                        state += value
                sql_block += f"INSERT INTO agenda_userstate (state) VALUES ('{state}');\n"
                
            """ We populate the agenda_installationstate table: """
            for dicts in INSTALLATION_STATES.items():
                state = ""
                for key, value in dicts[1].items():
                    if key == LANGUAGE:
                        state += value
                sql_block += f"INSERT INTO agenda_installationstate (state) VALUES ('{state}');\n"

            """ We populate the product_productfamily table: """
            for dicts in PRODUCT_FAMILYS.items():
                family = ""
                for key, value in dicts[1].items():
                    if key == LANGUAGE:
                        family += value
                sql_block += f"INSERT INTO product_productfamily (family) VALUES ('{family}');\n"

            """ We populate the product_productbrand table: """
            for brand in PRODUCT_BRANDS:
                sql_block += f"INSERT INTO product_productbrand (brand) VALUES ('{brand}');\n"

            """ We populate the agenda_productstate table: """
            for dicts in PRODUCT_STATES.items():
                state = ""
                for key, value in dicts[1].items():
                    if key == LANGUAGE:
                        state += value
                sql_block += f"INSERT INTO agenda_productstate (state) VALUES ('{state}');\n"

            """ We populate the agenda_vehiclestate table: """
            for dicts in VEHICLE_STATES.items():
                state = ""
                for key, value in dicts[1].items():
                    if key == LANGUAGE:
                        state += value
                sql_block += f"INSERT INTO agenda_vehiclestate (state) VALUES ('{state}');\n"


            # print(sql_block)

            cur.execute(sql_block)
            cur.close()
            conn.commit()
            conn.close()

        except (Exception, psycopg2.Error) as error :
            print ("Erreur lors de la connexion à la base bappiment !\n", error)
