import sqlite3 as sql


def listExtension():
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        data = cur.execute("SELECT * FROM extension").fetchall()
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
    try:
        with sql.connect("database/data_source.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO contact_list (email,name) VALUES (?,?)", (email, name)
            )
            con.commit()
    except sql.Error as e:
        raise RuntimeError(f"Database error: {e}")


def listExtensionByLanguage(language):
    with sql.connect("database/data_source.db") as con:
        cur = con.cursor()
        data = cur.execute(
            "SELECT * FROM extension WHERE language = ?", (language,)
        ).fetchall()
        return data
