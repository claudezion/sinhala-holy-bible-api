from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from typing import Union, List
from datetime import datetime
from database import get_books_from_db, get_random_verse, get_chapters_from_db

# Global variables to store the current "Verse of the Day" and its date
current_verse_of_the_day = None
current_verse_date = None

app = FastAPI()

@app.get("/")
async def read_root():
    return RedirectResponse('/docs')


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


@app.get("/bible/books")
async def get_books():
    books = get_books_from_db()

    # Check if books were found
    if not books:
        raise HTTPException(status_code=404, detail="books not found")

    return books


@app.get("/bible/chapters")
async def get_chapters():
    chapters = get_chapters_from_db()

    # Check if chapters were found
    if not chapters:
        raise HTTPException(status_code=404, detail="chapters not found")
    
    return chapters