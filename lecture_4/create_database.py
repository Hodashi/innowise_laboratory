import sqlite3
import os

def create_database():
    if os.path.exists('school.db'):
        os.remove('school.db')
    
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    with open('create_school.sql', 'r') as f:
        create_sql = f.read()
    
    with open('insert_data.sql', 'r') as f:
        insert_sql = f.read()
    
    cursor.executescript(create_sql)
    cursor.executescript(insert_sql)
    
    conn.commit()
    conn.close()
    
    print("База данных school.db успешно создана!")

if __name__ == "__main__":
    create_database()