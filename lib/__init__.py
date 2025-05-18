# lib/__init__.py
import sqlite3

# Connect to the SQLite database
CONN = sqlite3.connect('company.db')
CURSOR = CONN.cursor()