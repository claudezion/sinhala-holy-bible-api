# Holy Bible Sinhala API - FastAPI Version

This is the updated version of the Holy Bible Sinhala API, migrated from Flask to FastAPI to improve performance, scalability, and add more robust features. The FastAPI version provides a RESTful API that allows users to access the Holy Bible in the Sinhala language with various functionalities such as retrieving verses, searching scriptures, and more.

## Key Features

1. **Verse of the Day**
   - Get a randomly selected verse to inspire your day.

2. **Random Verse**
   - Retrieve a random verse from the Bible.

3. **Retrieve All Books**
   - Get a list of all books available in the Holy Bible.

4. **Retrieve All Chapters**
   - Access all chapters from the Bible.

5. **Retrieve Verses by Book**
   - Get all verses from a specific book.

6. **Retrieve Chapters by Book**
   - Get all chapters from a specific book.

7. **Retrieve Verses by Chapter**
   - Retrieve all verses from a specific chapter.

8. **Search Verses**
   - Search for verses based on a keyword or phrase.

9. **Retrieve Verse by Reference**
   - Get a verse by providing its reference (e.g., John 3:16).

10. **Get Next and Previous Verses**
    - Navigate through the Bible by getting the next or previous verse.

## Live API

The FastAPI version of the Holy Bible Sinhala API is live and can be accessed at:

- [https://holybibleapi.pythonanywhere.com/](https://holybibleapi.pythonanywhere.com/)

## Installation and Usage

To use the FastAPI version locally:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/claudezion/sinhala-holy-bible-api
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI application:**

   ```bash
   uvicorn app:app --reload
   ```

5. **Access the API documentation:**

   The API documentation can be accessed at `http://127.0.0.1:8000/docs` after running the application.

## Archived Version

The previous version of this API, which was built using Flask, is still available and operational. However, it has been archived, and future updates will only be applied to the FastAPI version. You can access the archived Flask version at:

- [Holy Bible Sinhala API - Flask Version]()

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
