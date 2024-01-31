import random
import sqlite3

def get_books_from_db():
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # Execute your SQL query to retrieve chapters
    cursor.execute("SELECT * FROM book;")
    books = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    return books

def get_random_verse():
    # Establish a connection to the SQLite database
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # the total number of verses in the database is 31067.
    total_verses = 31067

    # Generate a random verse ID
    random_verse_id = random.randint(1, total_verses)

    # Execute a query to retrieve the random verse
    cursor.execute("SELECT * FROM verse WHERE id = ?;", (random_verse_id,))
    random_verse = cursor.fetchone()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    return random_verse

def get_chapters_from_db():
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # Execute your SQL query to retrieve chapters
    cursor.execute("SELECT * FROM chapter;")
    chapters = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    # Convert the data to a list of dictionaries
    chapter_list = [{'id': row[0], 'book_id': row[1], 'cnumber': row[2]} for row in chapters]


    return chapter_list