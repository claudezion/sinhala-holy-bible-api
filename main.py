from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from datetime import datetime
from database import get_books_from_db, get_chapters_by_book_from_db, get_random_verse, get_chapters_from_db, get_verses_by_book_from_db, get_verses_by_chapter_from_db, search_verses_from_db

# Global variables to store the current "Verse of the Day" and its date
current_verse_of_the_day = None
current_verse_date = None

app = FastAPI()

@app.get("/")
async def read_root():
    return RedirectResponse('/docs')


# Verse of the Day function
@app.get("/bible/verses/day")
async def verse_of_the_day():
    global current_verse_of_the_day
    global current_verse_date

    # Get the current date and time
    now = datetime.now()

    # If it's a new day, update the "Verse of the Day"
    if current_verse_date is None or now.date() > current_verse_date:
        random_verse = get_random_verse()

        if random_verse is None:
            raise HTTPException(status_code=404, detail="Verse not found")
        
        current_verse_of_the_day = {
            'id': random_verse[0],
            'chapter_id': random_verse[1],
            'osisID': random_verse[2],
            'vnumber': random_verse[3],
            '_text': random_verse[4]
        }
        current_verse_date = now.date()

    return current_verse_of_the_day


# Random Verse function
@app.get("/bible/verses/random")
async def random_verse():
    random_verse = get_random_verse()

    if random_verse is None:
        raise HTTPException(status_code=404, detail="Verse not found")
    
    verse = {
        'id': random_verse[0],
        'chapter_id': random_verse[1],
        'osisID': random_verse[2],
        'vnumber': random_verse[3],
        '_text': random_verse[4]
    }

    return verse


# Get Books
@app.get("/bible/books")
async def get_books():
    books = get_books_from_db()

    # Check if books were found
    if not books:
        raise HTTPException(status_code=404, detail="books not found")

    return books


# Get Chapters
@app.get("/bible/chapters")
async def get_chapters():
    chapters = get_chapters_from_db()

    # Check if chapters were found
    if not chapters:
        raise HTTPException(status_code=404, detail="chapters not found")
    
    return chapters


# Get Verses by Book
@app.get("/bible/books/{book_id}/verses")
async def get_verses_by_book(book_id:int):
    verses = get_verses_by_book_from_db(book_id)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="chapters not found")
    
    return verses


# Get chapters by Book
@app.get("/bible/books/{book_id}/chapters")
async def get_chapters_by_book(book_id:int):
    chapters = get_chapters_by_book_from_db(book_id)

    # Check if chapters were found
    if not chapters:
        raise HTTPException(status_code=404, detail="chapters not found")
    
    return chapters


# Get Verse by Chapter
@app.get("/bible/books/{cnumber}/verses")
async def get_verse_by_chapter(cnumber:int):
    verses = get_verses_by_chapter_from_db(cnumber)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="chapters not found")
    
    return verses


# Search Verses
@app.get("/bible/verses/search")
async def search_verses(query: str):
    verses = search_verses_from_db(query)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="Verses not found")

    return verses
