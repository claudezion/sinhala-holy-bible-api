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


def get_verses_by_book_from_db(book_id):
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # Execute the SQL query to get the first and last chapters
    cursor.execute("SELECT MIN(id), MAX(id) FROM chapter WHERE book_id = ?;", (book_id,))
    chapters = cursor.fetchone()

    # Check if chapters were found
    if not chapters:
        # Handle the case where no chapters were found for the given book_id
        cursor.close()
        connection.close()
        return None

    # Unpack the first and last chapter IDs
    first_chapter_id, last_chapter_id = chapters

    # Execute the SQL query to get verses
    cursor.execute("SELECT * FROM verse WHERE chapter_id BETWEEN ? AND ?;", (first_chapter_id, last_chapter_id))

    # Fetch all the records
    verses = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    # Convert the data to a list of dictionaries
    verse_list = [{'id': row[0], 'chapter_id': row[1], 'osisID': row[2], 'vnumber': row[3], '_text': row[4]} for row in verses]

    return verse_list


def get_chapters_by_book_from_db(book_id):
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM chapter WHERE book_id = ?;", (book_id,))

    # Fetch all the records
    chapters = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    # Convert the data to a list of dictionaries
    chapter_list = [{'id': row[0], 'book_id': row[1], 'cnumber': row[2]} for row in chapters]

    return chapter_list


def get_verses_by_chapter_from_db(cnumber):
    connection = sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True)
    cursor = connection.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM verse WHERE chapter_id = ?;", (cnumber))

    # Fetch all the records
    verses = cursor.fetchall()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    # Convert the data to a list of dictionaries
    verse_list = [{'id': row[0], 'chapter_id': row[1], 'osisID': row[2], 'vnumber': row[3], '_text': row[4]} for row in verses]

    return verse_list


def search_verses_from_db(query):
    # Use a context manager to handle connections and ensure they are properly closed
    with sqlite3.connect('bible.db', detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread=False, isolation_level=None, uri=True) as connection:
        cursor = connection.cursor()

        # Execute the SQL query to search for verses containing the query
        cursor.execute("SELECT * FROM verse WHERE _text LIKE ?;", ('%' + query + '%',))

        # Fetch all the matching verses
        verses = cursor.fetchall()

        # Convert the data to a list of dictionaries
        verse_list = [{'id': row[0], 'chapter_id': row[1], 'osisID': row[2], 'vnumber': row[3], '_text': row[4]} for row in verses]

    return verse_list