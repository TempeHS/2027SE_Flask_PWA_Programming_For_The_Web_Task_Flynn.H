import sqlite3

# Connect to database
con = sqlite3.connect("data_source.db")
cur = con.cursor()

# Create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS contact_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL
    )
""")

# Commit changes
con.commit()
con.close()

print("✅ contact_list table created successfully!")
