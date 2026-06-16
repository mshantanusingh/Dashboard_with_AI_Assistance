"""Mock data store for the Academics MCP Server.

Realistic academic data for a campus CS department. In production,
this would connect to the university's ERP/academic management system.
"""

from schemas import (
    ClassSession, Course, Faculty, ExamSchedule,
    AcademicCalendarEvent, Department,
)


# ─── Courses ─────────────────────────────────────────────────────────────────────

COURSES: list[Course] = [
    Course(
        code="CS101",
        name="Introduction to Computer Science",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Amit Kumar",
        description="Foundational course covering computational thinking, basic programming in Python, data types, control flow, functions, and introduction to algorithms.",
        prerequisites=[],
        syllabus_topics=[
            "Computational Thinking", "Python Basics", "Data Types & Variables",
            "Control Flow (if/else, loops)", "Functions & Recursion", "Lists & Dictionaries",
            "File I/O", "Introduction to OOP", "Basic Algorithms (Sorting, Searching)",
            "Introduction to Complexity Analysis"
        ],
        textbooks=["Think Python by Allen Downey", "Introduction to Computation and Programming Using Python by John Guttag"],
    ),
    Course(
        code="CS201",
        name="Data Structures and Algorithms",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Priya Sharma",
        description="Core course on data structures (arrays, linked lists, trees, graphs, hash tables) and algorithm design paradigms (divide & conquer, greedy, dynamic programming).",
        prerequisites=["CS101"],
        syllabus_topics=[
            "Arrays & Linked Lists", "Stacks & Queues", "Trees (BST, AVL, B-trees)",
            "Heaps & Priority Queues", "Hashing", "Graphs (BFS, DFS, Shortest Paths)",
            "Sorting Algorithms", "Divide & Conquer", "Greedy Algorithms",
            "Dynamic Programming", "Complexity Analysis (Big-O, Omega, Theta)"
        ],
        textbooks=["Introduction to Algorithms by CLRS", "Algorithm Design by Kleinberg & Tardos"],
    ),
    Course(
        code="CS301",
        name="Operating Systems",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Rajesh Gupta",
        description="Study of OS concepts including process management, memory management, file systems, concurrency, and system calls.",
        prerequisites=["CS201", "CS202"],
        syllabus_topics=[
            "Process Management", "CPU Scheduling", "Process Synchronization",
            "Deadlocks", "Memory Management", "Virtual Memory", "File Systems",
            "I/O Systems", "Protection & Security", "Linux Kernel Internals"
        ],
        textbooks=["Operating System Concepts by Silberschatz (Dinosaur Book)", "Modern Operating Systems by Tanenbaum"],
    ),
    Course(
        code="CS302",
        name="Database Management Systems",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Neha Verma",
        description="Relational databases, SQL, normalization, transaction management, query optimization, and introduction to NoSQL databases.",
        prerequisites=["CS201"],
        syllabus_topics=[
            "ER Model & Relational Model", "SQL (DDL, DML, Joins, Subqueries)",
            "Normalization (1NF to BCNF)", "Transaction Management (ACID)",
            "Concurrency Control", "Query Optimization", "Indexing (B+ Trees, Hashing)",
            "NoSQL Databases", "Distributed Databases", "Database Security"
        ],
        textbooks=["Database System Concepts by Silberschatz", "Fundamentals of Database Systems by Elmasri & Navathe"],
    ),
    Course(
        code="CS401",
        name="Artificial Intelligence",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Sanjay Mishra",
        description="Introduction to AI covering search algorithms, knowledge representation, machine learning basics, NLP fundamentals, and ethical AI.",
        prerequisites=["CS201", "MA201"],
        syllabus_topics=[
            "Intelligent Agents", "Search Algorithms (BFS, DFS, A*)",
            "Adversarial Search (Minimax, Alpha-Beta)", "Knowledge Representation",
            "Constraint Satisfaction Problems", "Probabilistic Reasoning",
            "Machine Learning Fundamentals", "Neural Networks Introduction",
            "Natural Language Processing Basics", "Ethics in AI"
        ],
        textbooks=["Artificial Intelligence: A Modern Approach by Russell & Norvig"],
    ),
    Course(
        code="CS402",
        name="Machine Learning",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Kavita Rao",
        description="Comprehensive ML course: supervised/unsupervised learning, deep learning, evaluation metrics, and practical implementation with Python.",
        prerequisites=["CS401", "MA201", "MA202"],
        syllabus_topics=[
            "Linear Regression", "Logistic Regression", "Decision Trees & Random Forests",
            "Support Vector Machines", "K-Nearest Neighbors", "Clustering (K-Means, DBSCAN)",
            "Dimensionality Reduction (PCA)", "Neural Networks & Backpropagation",
            "Convolutional Neural Networks", "Recurrent Neural Networks",
            "Evaluation Metrics", "Cross-Validation", "Bias-Variance Tradeoff"
        ],
        textbooks=["Pattern Recognition and Machine Learning by Bishop", "Deep Learning by Goodfellow, Bengio, Courville"],
    ),
    Course(
        code="CS202",
        name="Computer Organization and Architecture",
        department=Department.CSE,
        credits=3,
        instructor="Dr. Vivek Tiwari",
        description="Digital logic, processor design, memory hierarchy, pipelining, and introduction to parallel computing architectures.",
        prerequisites=["CS101"],
        syllabus_topics=[
            "Number Systems & Boolean Algebra", "Logic Gates & Combinational Circuits",
            "Sequential Circuits", "ALU Design", "CPU Organization",
            "Instruction Set Architecture (RISC-V)", "Pipelining",
            "Memory Hierarchy (Cache, RAM)", "I/O Organization", "Parallel Processing Basics"
        ],
        textbooks=["Computer Organization and Design by Patterson & Hennessy"],
    ),
    Course(
        code="CS303",
        name="Computer Networks",
        department=Department.CSE,
        credits=4,
        instructor="Dr. Amit Kumar",
        description="Networking fundamentals using a top-down approach: application layer, transport, network, link, and physical layers.",
        prerequisites=["CS201"],
        syllabus_topics=[
            "Application Layer (HTTP, DNS, SMTP)", "Transport Layer (TCP, UDP)",
            "Network Layer (IP, Routing)", "Link Layer (Ethernet, WiFi)",
            "Network Security (TLS, Firewalls)", "Socket Programming",
            "Congestion Control", "Software Defined Networking",
            "Content Distribution Networks", "Wireless Networks"
        ],
        textbooks=["Computer Networking: A Top-Down Approach by Kurose & Ross"],
    ),
    Course(
        code="MA201",
        name="Probability and Statistics",
        department=Department.MATH,
        credits=3,
        instructor="Dr. Anand Prakash",
        description="Probability theory, random variables, distributions, hypothesis testing, and regression analysis for engineers.",
        prerequisites=["MA101"],
        syllabus_topics=[
            "Probability Axioms", "Conditional Probability & Bayes' Theorem",
            "Random Variables", "Probability Distributions (Binomial, Poisson, Normal)",
            "Expectation & Variance", "Joint Distributions",
            "Central Limit Theorem", "Hypothesis Testing",
            "Confidence Intervals", "Linear Regression"
        ],
        textbooks=["Probability and Statistics for Engineers by Walpole & Myers"],
    ),
    Course(
        code="MA101",
        name="Mathematics I (Calculus & Linear Algebra)",
        department=Department.MATH,
        credits=4,
        instructor="Dr. Sunita Jain",
        description="Single & multivariable calculus, linear algebra, eigenvalues, and applications to engineering problems.",
        prerequisites=[],
        syllabus_topics=[
            "Limits & Continuity", "Differentiation", "Integration",
            "Sequences & Series", "Multivariable Calculus",
            "Vector Calculus (Gradient, Divergence, Curl)",
            "Matrices & Determinants", "Systems of Linear Equations",
            "Eigenvalues & Eigenvectors", "Linear Transformations"
        ],
        textbooks=["Thomas' Calculus", "Linear Algebra Done Right by Axler"],
    ),
]


# ─── Class Schedule (CSE, 2nd Year, Monsoon 2026) ────────────────────────────────

CLASS_SCHEDULE: list[ClassSession] = [
    # Monday
    ClassSession(course_code="CS201", course_name="Data Structures and Algorithms", instructor="Dr. Priya Sharma", day="Monday", start_time="08:00", end_time="09:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS202", course_name="Computer Organization", instructor="Dr. Vivek Tiwari", day="Monday", start_time="09:00", end_time="10:00", room="LHC-102", type="Lecture"),
    ClassSession(course_code="MA201", course_name="Probability and Statistics", instructor="Dr. Anand Prakash", day="Monday", start_time="11:00", end_time="12:00", room="LHC-201", type="Lecture"),
    ClassSession(course_code="CS201", course_name="DSA Tutorial", instructor="Dr. Priya Sharma", day="Monday", start_time="14:00", end_time="15:00", room="CS-Lab-1", type="Tutorial"),

    # Tuesday
    ClassSession(course_code="CS302", course_name="Database Management Systems", instructor="Dr. Neha Verma", day="Tuesday", start_time="08:00", end_time="09:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS201", course_name="Data Structures and Algorithms", instructor="Dr. Priya Sharma", day="Tuesday", start_time="09:00", end_time="10:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS303", course_name="Computer Networks", instructor="Dr. Amit Kumar", day="Tuesday", start_time="11:00", end_time="12:00", room="LHC-103", type="Lecture"),
    ClassSession(course_code="CS302", course_name="DBMS Lab", instructor="Dr. Neha Verma", day="Tuesday", start_time="14:00", end_time="16:00", room="CS-Lab-2", type="Lab"),

    # Wednesday
    ClassSession(course_code="CS202", course_name="Computer Organization", instructor="Dr. Vivek Tiwari", day="Wednesday", start_time="08:00", end_time="09:00", room="LHC-102", type="Lecture"),
    ClassSession(course_code="MA201", course_name="Probability and Statistics", instructor="Dr. Anand Prakash", day="Wednesday", start_time="09:00", end_time="10:00", room="LHC-201", type="Lecture"),
    ClassSession(course_code="CS303", course_name="Computer Networks", instructor="Dr. Amit Kumar", day="Wednesday", start_time="11:00", end_time="12:00", room="LHC-103", type="Lecture"),
    ClassSession(course_code="CS201", course_name="DSA Lab", instructor="Dr. Priya Sharma", day="Wednesday", start_time="14:00", end_time="16:00", room="CS-Lab-1", type="Lab"),

    # Thursday
    ClassSession(course_code="CS201", course_name="Data Structures and Algorithms", instructor="Dr. Priya Sharma", day="Thursday", start_time="08:00", end_time="09:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS302", course_name="Database Management Systems", instructor="Dr. Neha Verma", day="Thursday", start_time="09:00", end_time="10:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS202", course_name="CO Tutorial", instructor="Dr. Vivek Tiwari", day="Thursday", start_time="11:00", end_time="12:00", room="LHC-102", type="Tutorial"),
    ClassSession(course_code="MA201", course_name="Prob & Stats Tutorial", instructor="Dr. Anand Prakash", day="Thursday", start_time="14:00", end_time="15:00", room="LHC-201", type="Tutorial"),

    # Friday
    ClassSession(course_code="CS303", course_name="Computer Networks", instructor="Dr. Amit Kumar", day="Friday", start_time="08:00", end_time="09:00", room="LHC-103", type="Lecture"),
    ClassSession(course_code="CS302", course_name="Database Management Systems", instructor="Dr. Neha Verma", day="Friday", start_time="09:00", end_time="10:00", room="LHC-101", type="Lecture"),
    ClassSession(course_code="CS303", course_name="CN Lab", instructor="Dr. Amit Kumar", day="Friday", start_time="14:00", end_time="16:00", room="CS-Lab-3", type="Lab"),
]


# ─── Faculty Directory ───────────────────────────────────────────────────────────

FACULTY: list[Faculty] = [
    Faculty(
        id="FAC-001", name="Dr. Amit Kumar", department=Department.CSE,
        designation="Associate Professor", email="amit.kumar@campus.edu",
        office="CS Building, Room 205", specialization=["Computer Networks", "Distributed Systems", "IoT"],
        office_hours="Mon & Wed, 3-5 PM", phone="+91-1332-285001",
    ),
    Faculty(
        id="FAC-002", name="Dr. Priya Sharma", department=Department.CSE,
        designation="Assistant Professor", email="priya.sharma@campus.edu",
        office="CS Building, Room 312", specialization=["Algorithms", "Competitive Programming", "Graph Theory"],
        office_hours="Tue & Thu, 2-4 PM", phone="+91-1332-285002",
    ),
    Faculty(
        id="FAC-003", name="Dr. Rajesh Gupta", department=Department.CSE,
        designation="Professor", email="rajesh.gupta@campus.edu",
        office="CS Building, Room 101", specialization=["Operating Systems", "Systems Programming", "Linux Kernel"],
        office_hours="Mon & Fri, 10-12 AM", phone="+91-1332-285003",
    ),
    Faculty(
        id="FAC-004", name="Dr. Neha Verma", department=Department.CSE,
        designation="Associate Professor", email="neha.verma@campus.edu",
        office="CS Building, Room 208", specialization=["Databases", "Data Mining", "Big Data"],
        office_hours="Wed & Fri, 11-1 PM", phone="+91-1332-285004",
    ),
    Faculty(
        id="FAC-005", name="Dr. Sanjay Mishra", department=Department.CSE,
        designation="Professor", email="sanjay.mishra@campus.edu",
        office="CS Building, Room 103", specialization=["Artificial Intelligence", "NLP", "Knowledge Graphs"],
        office_hours="Tue & Thu, 4-6 PM", phone="+91-1332-285005",
    ),
    Faculty(
        id="FAC-006", name="Dr. Kavita Rao", department=Department.CSE,
        designation="Assistant Professor", email="kavita.rao@campus.edu",
        office="CS Building, Room 315", specialization=["Machine Learning", "Deep Learning", "Computer Vision"],
        office_hours="Mon & Wed, 11-1 PM", phone="+91-1332-285006",
    ),
    Faculty(
        id="FAC-007", name="Dr. Vivek Tiwari", department=Department.CSE,
        designation="Associate Professor", email="vivek.tiwari@campus.edu",
        office="CS Building, Room 210", specialization=["Computer Architecture", "VLSI", "Embedded Systems"],
        office_hours="Thu & Fri, 2-4 PM", phone="+91-1332-285007",
    ),
    Faculty(
        id="FAC-008", name="Dr. Anand Prakash", department=Department.MATH,
        designation="Professor", email="anand.prakash@campus.edu",
        office="Math Building, Room 105", specialization=["Probability Theory", "Stochastic Processes", "Mathematical Statistics"],
        office_hours="Mon & Wed, 4-6 PM", phone="+91-1332-286001",
    ),
    Faculty(
        id="FAC-009", name="Dr. Sunita Jain", department=Department.MATH,
        designation="Associate Professor", email="sunita.jain@campus.edu",
        office="Math Building, Room 202", specialization=["Linear Algebra", "Numerical Analysis", "Applied Mathematics"],
        office_hours="Tue & Thu, 10-12 AM", phone="+91-1332-286002",
    ),
]


# ─── Exam Schedule ───────────────────────────────────────────────────────────────

EXAM_SCHEDULE: list[ExamSchedule] = [
    ExamSchedule(course_code="CS201", course_name="Data Structures and Algorithms", date="2026-07-20", start_time="09:00", end_time="11:00", venue="Exam Hall A", type="Mid-Semester"),
    ExamSchedule(course_code="CS202", course_name="Computer Organization", date="2026-07-21", start_time="09:00", end_time="11:00", venue="Exam Hall A", type="Mid-Semester"),
    ExamSchedule(course_code="CS302", course_name="Database Management Systems", date="2026-07-22", start_time="14:00", end_time="16:00", venue="Exam Hall B", type="Mid-Semester"),
    ExamSchedule(course_code="CS303", course_name="Computer Networks", date="2026-07-23", start_time="09:00", end_time="11:00", venue="Exam Hall A", type="Mid-Semester"),
    ExamSchedule(course_code="MA201", course_name="Probability and Statistics", date="2026-07-24", start_time="14:00", end_time="16:00", venue="Exam Hall C", type="Mid-Semester"),
    # End-semester exams
    ExamSchedule(course_code="CS201", course_name="Data Structures and Algorithms", date="2026-11-15", start_time="09:00", end_time="12:00", venue="Exam Hall A", type="End-Semester"),
    ExamSchedule(course_code="CS202", course_name="Computer Organization", date="2026-11-17", start_time="09:00", end_time="12:00", venue="Exam Hall A", type="End-Semester"),
    ExamSchedule(course_code="CS302", course_name="Database Management Systems", date="2026-11-19", start_time="09:00", end_time="12:00", venue="Exam Hall B", type="End-Semester"),
    ExamSchedule(course_code="CS303", course_name="Computer Networks", date="2026-11-21", start_time="09:00", end_time="12:00", venue="Exam Hall A", type="End-Semester"),
    ExamSchedule(course_code="MA201", course_name="Probability and Statistics", date="2026-11-23", start_time="09:00", end_time="12:00", venue="Exam Hall C", type="End-Semester"),
]


# ─── Academic Calendar ───────────────────────────────────────────────────────────

ACADEMIC_CALENDAR: list[AcademicCalendarEvent] = [
    AcademicCalendarEvent(date="2026-07-15", event="Monsoon Semester Begins", type="Registration"),
    AcademicCalendarEvent(date="2026-07-20", event="Last Date for Course Registration", type="Deadline"),
    AcademicCalendarEvent(date="2026-07-20", event="Mid-Semester Exams Begin", type="Exam"),
    AcademicCalendarEvent(date="2026-07-24", event="Mid-Semester Exams End", type="Exam"),
    AcademicCalendarEvent(date="2026-08-15", event="Independence Day", type="Holiday"),
    AcademicCalendarEvent(date="2026-08-26", event="Janmashtami", type="Holiday"),
    AcademicCalendarEvent(date="2026-09-01", event="Last Date to Drop Courses", type="Deadline"),
    AcademicCalendarEvent(date="2026-10-02", event="Gandhi Jayanti", type="Holiday"),
    AcademicCalendarEvent(date="2026-10-20", event="Diwali Break Begins", type="Holiday"),
    AcademicCalendarEvent(date="2026-10-25", event="Diwali Break Ends", type="Holiday"),
    AcademicCalendarEvent(date="2026-11-10", event="Last Teaching Day", type="Deadline"),
    AcademicCalendarEvent(date="2026-11-12", event="Preparatory Leave Begins", type="Exam"),
    AcademicCalendarEvent(date="2026-11-15", event="End-Semester Exams Begin", type="Exam"),
    AcademicCalendarEvent(date="2026-11-25", event="End-Semester Exams End", type="Exam"),
    AcademicCalendarEvent(date="2026-11-28", event="Winter Vacation Begins", type="Holiday"),
    AcademicCalendarEvent(date="2026-12-25", event="Christmas", type="Holiday"),
    AcademicCalendarEvent(date="2027-01-01", event="New Year's Day", type="Holiday"),
    AcademicCalendarEvent(date="2027-01-05", event="Spring Semester Begins", type="Registration"),
]


# ─── Data Access Functions ───────────────────────────────────────────────────────

def get_class_schedule(department: str | None = None, year: int | None = None, day: str | None = None, student_id: str | None = None) -> list[dict]:
    """Get class schedule. Optionally filter by day and student_id."""
    results = [s.model_dump() for s in CLASS_SCHEDULE]
    
    # Mock Personalization
    if student_id == "STU-101":
        # Freshman CS - only keep 100/200 level courses
        results = [s for s in results if "10" in s["course_code"] or "20" in s["course_code"]]
    elif student_id == "STU-404":
        # Senior Math - only keep 300/400 level courses
        results = [s for s in results if "30" in s["course_code"] or "40" in s["course_code"]]

    if day:
        day_lower = day.lower()
        results = [s for s in results if s["day"].lower() == day_lower]
    return results


def get_course_syllabus(course_code: str) -> dict | None:
    """Get syllabus for a specific course."""
    code_upper = course_code.upper()
    for course in COURSES:
        if course.code == code_upper:
            return course.model_dump()
    # Fuzzy search by name
    code_lower = course_code.lower()
    for course in COURSES:
        if code_lower in course.name.lower():
            return course.model_dump()
    return None


def search_faculty(name: str | None = None, department: str | None = None) -> list[dict]:
    """Search faculty by name or department."""
    results = FACULTY
    if name:
        name_lower = name.lower()
        results = [f for f in results if name_lower in f.name.lower() or any(name_lower in s.lower() for s in f.specialization)]
    if department:
        dept_lower = department.lower()
        results = [f for f in results if dept_lower in f.department.value.lower()]
    return [f.model_dump() for f in results]


def get_exam_schedule(department: str | None = None, exam_type: str | None = None) -> list[dict]:
    """Get exam schedule. Optionally filter by type."""
    results = EXAM_SCHEDULE
    if exam_type:
        type_lower = exam_type.lower()
        results = [e for e in results if type_lower in e.type.lower()]
    return [e.model_dump() for e in results]


def get_academic_calendar(month: int | None = None) -> list[dict]:
    """Get academic calendar events. Optionally filter by month."""
    results = ACADEMIC_CALENDAR
    if month:
        results = [e for e in results if int(e.date.split("-")[1]) == month]
    return [e.model_dump() for e in results]


def get_all_courses() -> list[dict]:
    """Get all available courses."""
    return [c.model_dump() for c in COURSES]
