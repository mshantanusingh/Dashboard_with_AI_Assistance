"""Mock data store for the Library MCP Server.

This module contains realistic campus library data. In production, this would
be replaced with database queries or API calls to the actual library system.
The data layer is cleanly separated so swapping is trivial.
"""

from schemas import Book, BookCategory, LibraryHours


# ─── Book Catalog ────────────────────────────────────────────────────────────────

BOOKS: list[Book] = [
    # ── Computer Science ──────────────────────────────────────────────────────
    Book(
        id="LIB-CS-001",
        title="Introduction to Algorithms",
        author="Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        isbn="978-0262033848",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=5,
        available_copies=3,
        shelf_location="CS-A-12",
        edition="4th Edition",
        year=2022,
        publisher="MIT Press",
        description="The leading textbook on algorithms, covering a broad range of algorithms in depth."
    ),
    Book(
        id="LIB-CS-002",
        title="Computer Networking: A Top-Down Approach",
        author="James Kurose, Keith Ross",
        isbn="978-0136681557",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=4,
        available_copies=2,
        shelf_location="CS-A-15",
        edition="8th Edition",
        year=2021,
        publisher="Pearson",
        description="Comprehensive introduction to computer networking using a top-down approach."
    ),
    Book(
        id="LIB-CS-003",
        title="Operating System Concepts",
        author="Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
        isbn="978-1119800361",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=6,
        available_copies=4,
        shelf_location="CS-B-03",
        edition="10th Edition",
        year=2021,
        publisher="Wiley",
        description="The definitive guide to operating system concepts, also known as the 'Dinosaur Book'."
    ),
    Book(
        id="LIB-CS-004",
        title="Database System Concepts",
        author="Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
        isbn="978-0078022159",
        category=BookCategory.COMPUTER_SCIENCE,
        available=False,
        total_copies=3,
        available_copies=0,
        shelf_location="CS-B-07",
        edition="7th Edition",
        year=2019,
        publisher="McGraw-Hill",
        description="Comprehensive coverage of database system concepts and design."
    ),
    Book(
        id="LIB-CS-005",
        title="Artificial Intelligence: A Modern Approach",
        author="Stuart Russell, Peter Norvig",
        isbn="978-0134610993",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=4,
        available_copies=1,
        shelf_location="CS-C-01",
        edition="4th Edition",
        year=2020,
        publisher="Pearson",
        description="The most widely used textbook on artificial intelligence."
    ),
    Book(
        id="LIB-CS-006",
        title="Design Patterns: Elements of Reusable Object-Oriented Software",
        author="Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides",
        isbn="978-0201633610",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=3,
        available_copies=2,
        shelf_location="CS-C-05",
        edition="1st Edition",
        year=1994,
        publisher="Addison-Wesley",
        description="The classic Gang of Four book on software design patterns."
    ),
    Book(
        id="LIB-CS-007",
        title="Clean Code: A Handbook of Agile Software Craftsmanship",
        author="Robert C. Martin",
        isbn="978-0132350884",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=3,
        available_copies=3,
        shelf_location="CS-C-08",
        edition="1st Edition",
        year=2008,
        publisher="Prentice Hall",
        description="Practical guide to writing clean, maintainable, and efficient code."
    ),
    Book(
        id="LIB-CS-008",
        title="The C Programming Language",
        author="Brian W. Kernighan, Dennis M. Ritchie",
        isbn="978-0131103627",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=8,
        available_copies=5,
        shelf_location="CS-A-01",
        edition="2nd Edition",
        year=1988,
        publisher="Prentice Hall",
        description="The definitive reference for the C programming language by its creators."
    ),
    Book(
        id="LIB-CS-009",
        title="Computer Organization and Design: The Hardware/Software Interface",
        author="David A. Patterson, John L. Hennessy",
        isbn="978-0128201091",
        category=BookCategory.COMPUTER_SCIENCE,
        available=False,
        total_copies=4,
        available_copies=0,
        shelf_location="CS-D-02",
        edition="6th Edition",
        year=2020,
        publisher="Morgan Kaufmann",
        description="RISC-V edition covering computer architecture and organization."
    ),
    Book(
        id="LIB-CS-010",
        title="Deep Learning",
        author="Ian Goodfellow, Yoshua Bengio, Aaron Courville",
        isbn="978-0262035613",
        category=BookCategory.COMPUTER_SCIENCE,
        available=True,
        total_copies=3,
        available_copies=1,
        shelf_location="CS-C-03",
        edition="1st Edition",
        year=2016,
        publisher="MIT Press",
        description="Comprehensive textbook on deep learning covering mathematical and conceptual background."
    ),

    # ── Mathematics ───────────────────────────────────────────────────────────
    Book(
        id="LIB-MA-001",
        title="Linear Algebra Done Right",
        author="Sheldon Axler",
        isbn="978-3319110790",
        category=BookCategory.MATHEMATICS,
        available=True,
        total_copies=4,
        available_copies=2,
        shelf_location="MA-A-05",
        edition="3rd Edition",
        year=2015,
        publisher="Springer",
        description="An elegant approach to linear algebra that avoids determinants until the end."
    ),
    Book(
        id="LIB-MA-002",
        title="Thomas' Calculus",
        author="Joel Hass, Christopher Heil, Maurice Weir",
        isbn="978-0134438986",
        category=BookCategory.MATHEMATICS,
        available=True,
        total_copies=10,
        available_copies=6,
        shelf_location="MA-A-01",
        edition="14th Edition",
        year=2017,
        publisher="Pearson",
        description="The standard calculus textbook used in engineering programs worldwide."
    ),
    Book(
        id="LIB-MA-003",
        title="Probability and Statistics for Engineers and Scientists",
        author="Ronald E. Walpole, Raymond H. Myers",
        isbn="978-0134115856",
        category=BookCategory.MATHEMATICS,
        available=True,
        total_copies=5,
        available_copies=3,
        shelf_location="MA-B-02",
        edition="9th Edition",
        year=2016,
        publisher="Pearson",
        description="Classic text on probability and statistics for engineering students."
    ),
    Book(
        id="LIB-MA-004",
        title="Discrete Mathematics and Its Applications",
        author="Kenneth H. Rosen",
        isbn="978-1259676512",
        category=BookCategory.MATHEMATICS,
        available=False,
        total_copies=6,
        available_copies=0,
        shelf_location="MA-B-08",
        edition="8th Edition",
        year=2018,
        publisher="McGraw-Hill",
        description="Comprehensive introduction to discrete mathematics for computer science."
    ),
    Book(
        id="LIB-MA-005",
        title="Complex Analysis",
        author="Lars Ahlfors",
        isbn="978-0070006577",
        category=BookCategory.MATHEMATICS,
        available=True,
        total_copies=3,
        available_copies=1,
        shelf_location="MA-C-04",
        edition="3rd Edition",
        year=1979,
        publisher="McGraw-Hill",
        description="The standard graduate text on complex analysis."
    ),

    # ── Physics ───────────────────────────────────────────────────────────────
    Book(
        id="LIB-PH-001",
        title="Concepts of Physics",
        author="H.C. Verma",
        isbn="978-8177091878",
        category=BookCategory.PHYSICS,
        available=True,
        total_copies=12,
        available_copies=8,
        shelf_location="PH-A-01",
        edition="Volume 1 & 2",
        year=2017,
        publisher="Bharati Bhawan",
        description="The most popular physics textbook for Indian engineering entrance exams."
    ),
    Book(
        id="LIB-PH-002",
        title="Classical Mechanics",
        author="Herbert Goldstein, Charles Poole, John Safko",
        isbn="978-0201657029",
        category=BookCategory.PHYSICS,
        available=True,
        total_copies=4,
        available_copies=2,
        shelf_location="PH-B-03",
        edition="3rd Edition",
        year=2001,
        publisher="Addison-Wesley",
        description="The definitive graduate-level textbook on classical mechanics."
    ),
    Book(
        id="LIB-PH-003",
        title="Introduction to Quantum Mechanics",
        author="David J. Griffiths, Darrell F. Schroeter",
        isbn="978-1107189638",
        category=BookCategory.PHYSICS,
        available=True,
        total_copies=5,
        available_copies=3,
        shelf_location="PH-C-01",
        edition="3rd Edition",
        year=2018,
        publisher="Cambridge University Press",
        description="Clear and accessible introduction to quantum mechanics."
    ),
    Book(
        id="LIB-PH-004",
        title="Introduction to Electrodynamics",
        author="David J. Griffiths",
        isbn="978-1108420419",
        category=BookCategory.PHYSICS,
        available=False,
        total_copies=5,
        available_copies=0,
        shelf_location="PH-B-07",
        edition="4th Edition",
        year=2017,
        publisher="Cambridge University Press",
        description="The standard undergraduate textbook on electrodynamics."
    ),

    # ── Electrical Engineering ────────────────────────────────────────────────
    Book(
        id="LIB-EE-001",
        title="Signals and Systems",
        author="Alan V. Oppenheim, Alan S. Willsky",
        isbn="978-0138147570",
        category=BookCategory.ELECTRICAL_ENGINEERING,
        available=True,
        total_copies=5,
        available_copies=3,
        shelf_location="EE-A-04",
        edition="2nd Edition",
        year=1996,
        publisher="Prentice Hall",
        description="Classic textbook on signals and systems for electrical engineering."
    ),
    Book(
        id="LIB-EE-002",
        title="Microelectronic Circuits",
        author="Adel S. Sedra, Kenneth C. Smith",
        isbn="978-0199339136",
        category=BookCategory.ELECTRICAL_ENGINEERING,
        available=True,
        total_copies=4,
        available_copies=1,
        shelf_location="EE-B-02",
        edition="7th Edition",
        year=2014,
        publisher="Oxford University Press",
        description="The leading textbook on microelectronic circuit design."
    ),

    # ── Literature ────────────────────────────────────────────────────────────
    Book(
        id="LIB-LT-001",
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        isbn="978-0743273565",
        category=BookCategory.LITERATURE,
        available=True,
        total_copies=3,
        available_copies=3,
        shelf_location="LT-A-02",
        edition="Scribner Edition",
        year=2004,
        publisher="Scribner",
        description="Classic American novel about the Jazz Age and the American Dream."
    ),
    Book(
        id="LIB-LT-002",
        title="1984",
        author="George Orwell",
        isbn="978-0451524935",
        category=BookCategory.LITERATURE,
        available=True,
        total_copies=4,
        available_copies=2,
        shelf_location="LT-A-05",
        edition="Signet Classic",
        year=1961,
        publisher="Signet Classic",
        description="Dystopian novel about totalitarianism and mass surveillance."
    ),

    # ── Economics ──────────────────────────────────────────────────────────────
    Book(
        id="LIB-EC-001",
        title="Principles of Economics",
        author="N. Gregory Mankiw",
        isbn="978-0357038314",
        category=BookCategory.ECONOMICS,
        available=True,
        total_copies=5,
        available_copies=4,
        shelf_location="EC-A-01",
        edition="9th Edition",
        year=2020,
        publisher="Cengage Learning",
        description="The most widely used introductory economics textbook."
    ),
]


# ─── Library Operating Hours ─────────────────────────────────────────────────────

LIBRARY_HOURS: list[LibraryHours] = [
    LibraryHours(day="Monday", open_time="08:00", close_time="23:00"),
    LibraryHours(day="Tuesday", open_time="08:00", close_time="23:00"),
    LibraryHours(day="Wednesday", open_time="08:00", close_time="23:00"),
    LibraryHours(day="Thursday", open_time="08:00", close_time="23:00"),
    LibraryHours(day="Friday", open_time="08:00", close_time="22:00"),
    LibraryHours(day="Saturday", open_time="09:00", close_time="20:00"),
    LibraryHours(day="Sunday", open_time="10:00", close_time="18:00"),
]


# ─── Data Access Functions ───────────────────────────────────────────────────────

def search_books(query: str, category: str | None = None) -> list[dict]:
    """Search books by title, author, or keyword. Optionally filter by category."""
    query_lower = query.lower()
    results = []
    for book in BOOKS:
        if category and book.category.value != category:
            continue
        if (query_lower in book.title.lower() or
            query_lower in book.author.lower() or
            (book.description and query_lower in book.description.lower())):
            results.append(book.model_dump())
    return results


def get_book_by_id(book_id: str) -> dict | None:
    """Get a specific book by its ID."""
    for book in BOOKS:
        if book.id == book_id:
            return book.model_dump()
    return None


def check_availability(title: str) -> dict | None:
    """Check availability of a book by title (fuzzy match)."""
    title_lower = title.lower()
    for book in BOOKS:
        if title_lower in book.title.lower():
            return {
                "title": book.title,
                "author": book.author,
                "available": book.available,
                "available_copies": book.available_copies,
                "total_copies": book.total_copies,
                "shelf_location": book.shelf_location,
            }
    return None


def get_popular_books(limit: int = 5, student_id: str | None = None) -> list[dict]:
    """Get popular books — simulated by returning books with fewest available copies."""
    books_to_sort = [b for b in BOOKS if b.total_copies > 0]
    
    # Mock Personalization
    if student_id == "STU-101":
        # Freshman CS - recommend algorithms and C
        books_to_sort = [b for b in books_to_sort if "CS" in b.id]
    elif student_id == "STU-404":
        # Senior Math - recommend Math and Physics
        books_to_sort = [b for b in books_to_sort if "MA" in b.id or "PH" in b.id]

    sorted_books = sorted(
        books_to_sort,
        key=lambda b: b.available_copies / b.total_copies
    )
    return [b.model_dump() for b in sorted_books[:limit]]


def get_library_hours(day: str | None = None) -> list[dict]:
    """Get library operating hours. Optionally filter by day."""
    if day:
        day_lower = day.lower()
        return [h.model_dump() for h in LIBRARY_HOURS if h.day.lower() == day_lower]
    return [h.model_dump() for h in LIBRARY_HOURS]


def get_all_categories() -> list[str]:
    """Get all available book categories."""
    return [cat.value for cat in BookCategory]


def get_stats() -> dict:
    """Get library statistics."""
    total_books = len(BOOKS)
    available_count = sum(1 for b in BOOKS if b.available)
    total_copies = sum(b.total_copies for b in BOOKS)
    available_copies = sum(b.available_copies for b in BOOKS)
    return {
        "total_titles": total_books,
        "available_titles": available_count,
        "unavailable_titles": total_books - available_count,
        "total_copies": total_copies,
        "available_copies": available_copies,
        "checked_out_copies": total_copies - available_copies,
        "categories": len(set(b.category for b in BOOKS)),
    }
