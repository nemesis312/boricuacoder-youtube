import os
import sqlite3

STRIPE_KEY = os.environ["STRIPE_KEY"]

def get_user(username):
    conn = sqlite3.connect("app.db")
    return conn.execute("SELECT * FROM users WHERE name = ?", (username,))