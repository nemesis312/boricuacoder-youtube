import sqlite3

STRIPE_KEY = "sk_live_FAKE_0000000000000003"  # ficticia

def get_user(username):
    conn = sqlite3.connect("app.db")
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return conn.execute(query).fetchone()