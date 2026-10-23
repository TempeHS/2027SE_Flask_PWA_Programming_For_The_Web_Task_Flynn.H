import database_manager as dbHandler

# Test inserting a contact
try:
    dbHandler.insertContact("test@example.com", "Test User")
    print("✅ Contact inserted successfully!")
except Exception as e:
    print(f"❌ Error: {e}")

# Verify it worked
import sqlite3

con = sqlite3.connect("database/data_source.db")
cur = con.cursor()
cur.execute("SELECT * FROM contact_list WHERE email = 'test@example.com'")
result = cur.fetchone()
print(f"Retrieved: {result}")
con.close()

# Clean up
dbHandler.deleteContact("test@example.com")  # You'll need to add this function
