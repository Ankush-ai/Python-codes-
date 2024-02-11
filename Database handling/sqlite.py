# CRUD operation using sqlite3
import sqlite3

conn=sqlite3.connect('example.db')
cursor=conn.cursor()

cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
    )
''')
conn.commit()

def create_user(name,email):
    '''Create a new user.'''
    try:
        #validate input
        if not name or not email:
            raise ValueError("Name and email are reqired fields")
        
        cursor.execute('INSERT INTO users(name,email) VALUES(?,?)',(name,email))
        conn.commit()
        print(f"usser '{name} with email {email} created successfully")

    except Exception as e:
        print(f"Error Creating user:{e}")

    def read_users():
        """Read all users."""
        try:
            cursor.execute('SELECT * FROM USERS')
            users=cursor.fetchall()
            if users:
                print("Users:")
                for user in users:
                    print(f"ID:{user[0]},Name:{user[1]}, Email: {user[2]}")

            else:
                print("No Users found.")
        except Exception as e:
            print(f"Error creating users:{e}")

    def update_users(user_id,new_name,new_email):
        """Update user information."""
        try:
            #Validate Input
            if not new_name or not new_email:
                raise ValueError("Name and email fieldsa are requred for update.")
            
            cursor.execute('UPDATE users SET name=?,email=?',(new_name,new_email,user_id))
            conn.commit()
            print(f"User with ID{user_id} updated successfully")
        except Exception as e:
            print(f"Error updating usier:{e}")

    
    def delete_user(user_id):
        """Delete User."""
        try:
            cursor.execute('DELETE FROM users WHERE id=?',(user_id))
            conn.commit()
            print(f"user with ID {user_id} deleted sucessfully")
        except Exception as e:
            print(f"Error Deleting eserL{e}")

conn.close()

