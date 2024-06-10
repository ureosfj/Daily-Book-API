base = 'http://127.0.0.1:5000'

window.onload = function() {
    fetchBookOfTheDay();
};

function fetchBookOfTheDay() {
    fetch(base + '/api/book-of-the-day')
        .then(response => response.json())
        .then(data => {
            displayBookOfTheDay(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayBookOfTheDay(book) {
    document.getElementById('botdTitle').textContent = book.title;
    document.getElementById('botdAuthor').textContent = book.author;
    document.getElementById('botdSummary').textContent = book.summary;
}

function addBook() {
    const title = document.getElementById('title').value;
    const author = document.getElementById('author').value;
    const genre = document.getElementById('genre').value;
    const summary = document.getElementById('summary').value;

    // Verifica che tutti i campi siano riempiti
    if (!title || !author || !genre || !summary) {
        alert('Please fill in all fields.');
        return;  // Interrompe l'esecuzione della funzione se uno dei campi è vuoto
    }
    fetch(base+'/api/add-book', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, author, genre, summary })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert('Book added successfully!');
        clearForm();
    })
    .catch(error => console.error('Error:', error));
}

function showAllBooks() {
    fetch(base+'/api/all')
        .then(response => response.json())
        .then(data => {
            displayBooks(data);
        })
        .catch(error => console.error('Error:', error));
}

function searchBooks() {
    const genre = document.getElementById('searchQuery').value;
    fetch(base+`/api/search?genre=${genre}`)
        .then(response => response.json())
        .then(data => {
            displayBooks(data);
        })
        .catch(error => console.error('Error:', error));
}

function displayBooks(books) {
    const booksContainer = document.getElementById('books');
    booksContainer.innerHTML = ''; // Clear previous results
    books.forEach(book => {
        const bookElement = document.createElement('div');
        bookElement.className = 'card mb-3';
        bookElement.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${book.title}</h5>
                <h6 class="card-subtitle mb-2 text-muted">${book.author}</h6>
                <p class="card-text">${book.summary}</p>
            </div>
        `;
        booksContainer.appendChild(bookElement);
    });
}

function clearForm() {
    document.getElementById('title').value = '';
    document.getElementById('author').value = '';
    document.getElementById('genre').value = '';
    document.getElementById('summary').value = '';
}

