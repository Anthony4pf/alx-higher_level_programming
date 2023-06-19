#!/usr/bin/python3
"""This module lists all states from a database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE BINARY states.name = '{}' \
                ORDER BY cities.id ASC" .format(sys.argv[4]))

    rows = cur.fetchall()

    for i, row in enumerate(rows):
        city_id, city_name, state_name = row
        print(f"{city_name}", end=", " if i < len(rows) - 1 else "\n")

    cur.close()
    db.close()
