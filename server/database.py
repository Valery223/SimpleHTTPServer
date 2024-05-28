import psycopg2

def insert_data_into_database(data):
    try:
        connection = psycopg2.connect(
            dbname="test_db",
            user="user1",
            password="user1",
            host="localhost"
        )
        cursor = connection.cursor()

        # Вставка данных в таблицу
        cursor.execute("INSERT INTO test_data (data) VALUES (%s)", (data,))
        connection.commit()

        cursor.close()
        connection.close()
    except psycopg2.Error as e:
        print("Error: Could not connect to the database.")
        print(e)