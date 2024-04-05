# Book Shop Django Application
This is a simple Django application that allows users to view 
the list of books available in the store. Users can also view
a detailed description of each book in the JSON format.

## Installation
1. Clone the repository
2. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```
3. Run the server using the following command:
```bash
python manage.py runserver
```

## Usage
The application can be accessed at the following URL:
- `/` - View the home page
- `books/` - View the list of books available in the store
- `books/<int:book_id>/` - View the detailed description of a book

At this point, the creation of the books is done manually through the Django admin panel.
where you can create, update, and delete books.

Also, you can search for books by name and author using the search bar.

