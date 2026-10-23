import sqlite3 as sql


def listExtension():
    con = sql.connect("database/data_source.db")
    cur = con.cursor()
    data = cur.execute("SELECT * FROM extension").fetchall()
    con.close()
    return data


def insertContact(email, name):
    """
    Insert a new contact into the contact_list table.

    Args:
        email (str): Contact's email address
        name (str): Contact's name

    Returns:
        None

    Raises:
        sqlite3.IntegrityError: If email already exists (UNIQUE constraint)
    """
    con = sql.connect("database/data_source.db")
    cur = con.cursor()

    # Using parameterised query to prevent SQL injection
    cur.execute("INSERT INTO contact_list (email, name) VALUES (?, ?)", (email, name))

    con.commit()
    con.close()
