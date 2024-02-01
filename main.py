from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import RedirectResponse
from datetime import datetime
from database import get_books_from_db, get_chapters_by_book_from_db, get_random_verse, get_chapters_from_db, get_verse_by_reference_from_db, get_verse_from_db, get_verses_by_book_from_db, get_verses_by_chapter_from_db, get_verses_from_db, search_verses_from_db

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
        raise HTTPException(status_code=404, detail="Random verse not found.")
    
    verse = {
        'id': random_verse[0],
        'chapter_id': random_verse[1],
        'osisID': random_verse[2],
        'vnumber': random_verse[3],
        '_text': random_verse[4]
    }

    return verse


# Retrieve All Book:
@app.get("/bible/books")
async def retrieve_all_books():
    books = get_books_from_db()

    # Check if books were found
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")

    return books


# Retrieve All Chapters:
@app.get("/bible/chapters")
async def retrieve_all_chapters():
    chapters = get_chapters_from_db()

    # Check if chapters were found
    if not chapters:
        raise HTTPException(status_code=404, detail="Chapters not found")
    
    return chapters


# Retrieve Verses by Book:
@app.get("/bible/books/{book_id}/verses")
async def retrieve_verses_by_book(book_id: int = Path(description="ID of the desired book to retrieve verses from")):
    verses = get_verses_by_book_from_db(book_id)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="Verses not found for the specified book.")
    
    return verses


# Retrieve Chapters by Book:
@app.get("/bible/books/{book_id}/chapters")
async def retrieve_chapters_by_book(book_id: int = Path(description="ID of the desired book to retrieve chapters from")):
    chapters = get_chapters_by_book_from_db(book_id)

    # Check if chapters were found
    if not chapters:
        raise HTTPException(status_code=404, detail="Chapters not found for the specified book.")
    
    return chapters


# Retrieve Verses by Chapter:
@app.get("/bible/books/{cnumber}/verses")
async def retrieve_verse_by_chapter(cnumber: int = Path(description="Chapter number (cnumber) for which verses are requested")):
    verses = get_verses_by_chapter_from_db(cnumber)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="Verses not found for the specified chapter.")
    
    return verses


# Search Verses:
@app.get("/bible/verses/search")
async def search_verses(query: str):
    verses = search_verses_from_db(query)

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="Verses not found for the specified search query.")

    return verses


# Retrieve Verse by Reference:
@app.get("/bible/verses/reference")
async def retrieve_verse_by_reference(reference: str):
    verse = get_verse_by_reference_from_db(reference)

    # Check if verse were found
    if not verse:
        raise HTTPException(status_code=404, detail="Verse not found for the specified reference.")

    return verse



#Get Next Verse:
@app.get("/bible/verse/next")
async def retrieve_next_verse(id: int):
    verse = get_verse_from_db(id + 1)

    # Check if verse were found
    if not verse:
        raise HTTPException(status_code=404, detail="Next verse not found.")

    return verse

#Get Previous Verse:
@app.get("/bible/verse/previous")
async def retrieve_previous_verse(id: int):
    verse = get_verse_from_db(id - 1)

    # Check if verse were found
    if not verse:
        raise HTTPException(status_code=404, detail="Previous verse not found.")

    return verse

#Get Verses:
@app.get("/bible/verses")
async def retrieve_all_verses():
    verses = get_verses_from_db()

    # Check if verses were found
    if not verses:
        raise HTTPException(status_code=404, detail="Verses not found")

    return verses

# Note: You Can't Try Out The Retrieve All Verse Function In The Doc