import sqlite3

def create_tables():
    conn = sqlite3.connect('vetpatientmanager.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS animals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        type TEXT NOT NULL,
        breed TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        animal_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        symptoms TEXT NOT NULL,
        time_in TEXT NOT NULL,
        FOREIGN KEY (animal_id) REFERENCES animals(id),
        FOREIGN KEY (doctor_id) REFERENCES doctors(id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
