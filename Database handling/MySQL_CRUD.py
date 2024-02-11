import mysql.connector

class MySQLConnector:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

class UserDAO:
    def __init__(self, connector):
        self.connector = connector

    def create_user(self, name, email):
        query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        values = (name, email)
        self.connector.execute_query(query, values)

    def read_users(self):
        query = "SELECT * FROM users"
        return self.connector.fetch_data(query)

    def update_user(self, user_id, new_name, new_email):
        query = "UPDATE users SET name=%s, email=%s WHERE id=%s"
        values = (new_name, new_email, user_id)
        self.connector.execute_query(query, values)

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id=%s"
        values = (user_id,)
        self.connector.execute_query(query, values)

def main():
    # Replace with your MySQL credentials
    db_config = {
        'host': 'localhost',
        'user': 'your_username',
        'password': 'your_password',
        'database': 'your_database'
    }

    # Create a MySQLConnector instance
    connector = MySQLConnector(**db_config)

    # Create a UserDAO instance
    user_dao = UserDAO(connector)

    # Example usage:
    user_dao.create_user('John Doe', 'john@example.com')
    user_dao.create_user('Jane Doe', 'jane@example.com')

    users = user_dao.read_users()
    if users:
        print("Users:")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    user_dao.update_user(1, 'John Updated', 'john.updated@example.com')

    users_after_update = user_dao.read_users()
    if users_after_update:
        print("Users after update:")
        for user in users_after_update:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    user_dao.delete_user(2)

    users_after_delete = user_dao.read_users()
    if users_after_delete:
        print("Users after delete:")
        for user in users_after_delete:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

if __name__ == "__main__":
    main()
