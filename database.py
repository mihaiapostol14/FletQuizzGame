import mysql.connector
from config import DATABASE, LOCALHOST, PASSWORD, USER
from mysql.connector import Error


class DatabaseManager:
  """Manages connections and queries for the MySQL database."""

  def __init__(
      self,
      host: str = LOCALHOST,
      database: str = DATABASE,
      user: str = USER,
      password: str = PASSWORD,
  ):
    self.config = {
        "host": host,
        "database": database,
        "user": user,
        "password": password,
    }

  def get_connection(self):
    """Creates and returns a new database connection."""
    try:
      connection = mysql.connector.connect(**self.config)
      if connection.is_connected():
        return connection
    except Error as e:
      print(f"Error while connecting to MySQL: {e}")
    return None

  def execute_query(self, query: str, params: tuple = None):
    """Executes write, update, or delete queries (INSERT, UPDATE, DELETE)."""
    connection = self.get_connection()
    if not connection:
      return

    cursor = connection.cursor()
    try:
      cursor.execute(query, params or ())
      connection.commit()
      print("Query executed successfully.")
    except Error as e:
      print(f"Error executing query: {e}")
    finally:
      cursor.close()
      connection.close()

  def fetch_all(self, query: str, params: tuple = None):
    """Fetches all rows from a SELECT query as a list of dictionaries."""
    connection = self.get_connection()
    if not connection:
      return []

    cursor = connection.cursor(dictionary=True)
    try:
      cursor.execute(query, params or ())
      return cursor.fetchall()
    except Error as e:
      print(f"Error fetching data: {e}")
      return []
    finally:
      cursor.close()
      connection.close()

  def create_tables(self):
    """Creates the necessary tables for the quiz game if they don't exist."""
    queries = [
        """
            CREATE TABLE IF NOT EXISTS questions (
                id INT AUTO_INCREMENT PRIMARY KEY,
                question_text TEXT NOT NULL,
                option_a VARCHAR(255) NOT NULL,
                option_b VARCHAR(255) NOT NULL,
                option_c VARCHAR(255) NOT NULL,
                option_d VARCHAR(255) NOT NULL,
                correct_option VARCHAR(255) NOT NULL
            )
            """,
        """
            CREATE TABLE IF NOT EXISTS scores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                score INT NOT NULL,
                played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """,
    ]

    connection = self.get_connection()
    if not connection:
      return

    cursor = connection.cursor()
    try:
      for query in queries:
        cursor.execute(query)
      connection.commit()
      print("Tables created successfully via Python code!")
    except Error as e:
      print(f"Error creating tables: {e}")
    finally:
      cursor.close()
      connection.close()


if __name__ == "__main__":
  print("Initializing database setup...")
  db = DatabaseManager()
  db.create_tables()
  print("Database setup finished successfully.")
