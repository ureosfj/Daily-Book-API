import requests

# L'URL dell'API per aggiungere libri; assicurati che corrisponda all'URL effettivo del tuo server Flask.
url = "http://127.0.0.1:5000/api/add-book"

# Lista di libri da aggiungere

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "genre": "Romanzo", "summary": "La storia di un giovane pastore in cerca del suo destino."},
    {"title": "Animal Farm", "author": "George Orwell", "genre": "Politico", "summary": "Una favola satirica sulla corruzione del potere."},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Distopico", "summary": "Un futuro distopico dove la libertà è scambiata per sicurezza e felicità."},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "genre": "Psicologico", "summary": "Il dramma di un ex studente che commette un omicidio."},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "genre": "Avventura", "summary": "Le avventure di un nobile spagnolo e del suo scudiero."},
    {"title": "Frankenstein", "author": "Mary Shelley", "genre": "Gothic", "summary": "Il racconto di un giovane scienziato che crea una creatura vivente."},
    {"title": "Gone with the Wind", "author": "Margaret Mitchell", "genre": "Storico", "summary": "La storia di amore e sopravvivenza durante la Guerra Civile Americana."},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "genre": "Romanzo", "summary": "La vita e le tribolazioni di una giovane orfana."},
    {"title": "Les Misérables", "author": "Victor Hugo", "genre": "Storico", "summary": "La lotta per la giustizia e la redenzione nel XIX secolo in Francia."},
    {"title": "Life of Pi", "author": "Yann Martel", "genre": "Avventura", "summary": "La storia di un ragazzo che sopravvive in mare con una tigre di Bengala."},
    {"title": "Lolita", "author": "Vladimir Nabokov", "genre": "Romanzo", "summary": "Il controverso racconto di un uomo ossessionato da una giovane ragazza."},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "genre": "Magico Realismo", "summary": "La saga di una famiglia attraverso diverse generazioni."},
    {"title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "genre": "Satira", "summary": "Un prigioniero di guerra vive e rivive gli eventi della sua vita in un ordine non cronologico."},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "genre": "Filosofico", "summary": "Un dramma familiare che esplora la moralità, la fede e il dubbio."},
    {"title": "The Catch-22", "author": "Joseph Heller", "genre": "Satira", "summary": "Le esperienze surreali e assurde di un pilota durante la Seconda Guerra Mondiale."},
    {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "genre": "Distopico", "summary": "La vita sotto un regime teocratico e distopico."},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "genre": "Gothic", "summary": "Un giovane uomo rimane eternamente giovane mentre il suo ritratto invecchia."},
    {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "genre": "Romanzo", "summary": "Il racconto della generazione perduta post-prima guerra mondiale."},
    {"title": "To the Lighthouse", "author": "Virginia Woolf", "genre": "Modernista", "summary": "Un'esplorazione delle complessità psicologiche e delle dinamiche familiari attraverso la metafora di un viaggio al faro."},
    {"title": "A Farewell to Arms", "author": "Ernest Hemingway", "genre": "Guerra", "summary": "La storia d'amore tra un volontario americano in Italia durante la Prima Guerra Mondiale e un'infermiera britannica."},
    {"title": "The Master and Margarita", "author": "Mikhail Bulgakov", "genre": "Fantastico", "summary": "Un romanzo satirico in cui il diavolo visita l'Unione Sovietica degli anni '30."},
    {"title": "The Bell Jar", "author": "Sylvia Plath", "genre": "Autobiografico", "summary": "La lotta di una giovane donna contro la depressione nella New York degli anni '50."},
    {"title": "On the Road", "author": "Jack Kerouac", "genre": "Beat", "summary": "La storia di viaggi attraverso l'America che rappresentano la ricerca di libertà e autenticità."},
    {"title": "Dune", "author": "Frank Herbert", "genre": "Fantascienza", "summary": "Un epico racconto di politica e potere ambientato in un futuro lontano su un pianeta desertico."},
    {"title": "Atlas Shrugged", "author": "Ayn Rand", "genre": "Filosofico", "summary": "Una narrazione che esplora l'impatto del governo e delle regolazioni sull'innovazione e sull'industria."},
    {"title": "The Kite Runner", "author": "Khaled Hosseini", "genre": "Drammatico", "summary": "Una potente storia di amicizia e redenzione ambientata in Afghanistan."},
    {"title": "The Shining", "author": "Stephen King", "genre": "Horror", "summary": "Un romanzo di terrore psicologico che si svolge in un albergo isolato."},
    {"title": "Angela's Ashes", "author": "Frank McCourt", "genre": "Memoriale", "summary": "Un commovente racconto autobiografico dell'infanzia irlandese caratterizzata da povertà estrema."},
    {"title": "The Road", "author": "Cormac McCarthy", "genre": "Post-apocalittico", "summary": "La struggente avventura di un padre e suo figlio in un mondo devastato."},
    {"title": "In Cold Blood", "author": "Truman Capote", "genre": "Narrativa criminale", "summary": "Un dettagliato resoconto di un brutale omicidio e delle sue conseguenze."},
    {"title": "A Brief History of Time", "author": "Stephen Hawking", "genre": "Scienza", "summary": "Una spiegazione accessibile delle complesse teorie che riguardano l'universo."},
    {"title": "The Godfather", "author": "Mario Puzo", "genre": "Crimine", "summary": "Il racconto epico di una famiglia mafiosa e la loro lotta per il potere."},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens", "genre": "Storico", "summary": "Un dramma ambientato durante la Rivoluzione Francese."},
    {"title": "Catch-22", "author": "Joseph Heller", "genre": "Satira", "summary": "La surreale storia di un pilota dell'aeronautica militare durante la Seconda Guerra Mondiale."},
    {"title": "A Clockwork Orange", "author": "Anthony Burgess", "genre": "Distopico", "summary": "Un giovane delinquente viene sottoposto a terapie per rieducarlo alla società."},
    {"title": "Macbeth", "author": "William Shakespeare", "genre": "Tragedia", "summary": "L'ascesa e la caduta di Macbeth, ossessionato dal potere e dalla propria rovina."},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Romanzo", "summary": "La storia di Holden Caulfield, un adolescente alienato che cerca il suo posto nel mondo."},
    {"title": "1984", "author": "George Orwell", "genre": "Distopico", "summary": "Una visione orwelliana di un futuro totalitario dove tutto e tutti sono sotto controllo."},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romanzo", "summary": "Le vicende amorose di Elizabeth Bennet e del suo atteggiamento verso il matrimonio."},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Romanzo", "summary": "Un potente racconto di crescita e di lotta contro il razzismo nel Sud degli Stati Uniti."},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Romanzo", "summary": "La storia di Jay Gatsby e del suo desiderio irraggiungibile per il vero amore durante gli anni '20."},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "genre": "Fantasy", "summary": "Un epico viaggio per distruggere un anello di potere che può decidere il destino del mondo."},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "genre": "Fantasy", "summary": "Le avventure di bambini che scoprono un mondo magico chiamato Narnia."},
    {"title": "The Time Machine", "author": "H.G. Wells", "genre": "Fantascienza", "summary": "Le avventure di un uomo che viaggia nel tempo e scopre il futuro dell'umanità."},
    {"title": "The War of the Worlds", "author": "H.G. Wells", "genre": "Fantascienza", "summary": "La drammatica invasione della Terra da parte di marziani."},
    {"title": "Frankenstein", "author": "Mary Shelley", "genre": "Gothic", "summary": "Un giovane scienziato crea vita artificiale, con conseguenze tragiche."},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Avventura", "summary": "La caccia ossessiva di una balena bianca da parte del capitano Ahab."},
    {"title": "Dracula", "author": "Bram Stoker", "genre": "Horror", "summary": "Il conte Dracula cerca di trasferirsi dall'Europa orientale a Londra per diffondere la maledizione del non morto."},
    {"title": "The Metamorphosis", "author": "Franz Kafka", "genre": "Esistenzialista", "summary": "Un uomo si trasforma in un enorme insetto, cambiando irrevocabilmente la sua vita e quella della sua famiglia."}
]

def add_books():
    for book in books:
        response = requests.post(url, json=book)
        if response.status_code == 201:
            print("Success: Book added:", book["title"])
        else:
            print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    add_books()
