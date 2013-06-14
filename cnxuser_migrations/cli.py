# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
import os
import argparse
import psycopg2


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'migration.sql'), 'r') as fp:
    MIGRATION_SQL = fp.read()
with open(os.path.join(here, 'alteration.sql'), 'r') as fp:
    ALTERATION_SQL = fp.read()


# parser.add_argument('--initialize', action='store_true',
#                     help="trigger the database initialization process")


def main(argv=None):
    """Main commandline interface"""
    parser = argparse.ArgumentParser('migratory behavior')
    parser.add_argument('-u', '--username', default='cnxuser',
                        help="database username")
    parser.add_argument('-p', '--password', default='cnxuser',
                        help="database password")
    parser.add_argument('-d', '--database', default='cnxuser',
                        help="database name")

    args = parser.parse_args(argv)

    connection_string = "dbname={} user={} password={}".format(
            args.database, args.username, args.password)
    with psycopg2.connect(connection_string) as db_connection:
        with db_connection.cursor() as cursor:
            # Run the table alteration
            try:
                cursor.execute(ALTERATION_SQL)
            except psycopg2.ProgrammingError as exc:
                if exc.message.find('uuid-ossp') >= 0:
                    # Alteration already in place...
                    db_connection.rollback()
        with db_connection.cursor() as cursor:
            # Run the migration...
            cursor.execute(MIGRATION_SQL)

    return 0

if __name__ == '__main__':
    main()
