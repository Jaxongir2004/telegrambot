import sqlite3

def init_db():
    conn = sqlite3.connect("movies.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS movies (
        code TEXT PRIMARY KEY,
        message_id INTEGER
    )""")
    conn.commit()
    conn.close()

def add_movie(code: str, message_id: int):
    conn = sqlite3.connect("movies.db")
    c = conn.cursor()
    c.execute("REPLACE INTO movies (code, message_id) VALUES (?, ?)", (code, message_id))
    conn.commit()
    conn.close()

def get_message_id(code: str):
    conn = sqlite3.connect("movies.db")
    c = conn.cursor()
    c.execute("SELECT message_id FROM movies WHERE code = ?", (code,))
    row = c.fetchone()
    conn.close()
    return row[0] if row else None
