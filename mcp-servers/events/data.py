"""Mock data store for the Events MCP Server.

Realistic campus event and club data. In production, this would
connect to Google Calendar APIs, club management systems, etc.
"""

from schemas import Event, Club, EventCategory, EventStatus


# ─── Campus Events ───────────────────────────────────────────────────────────────

EVENTS: list[Event] = [
    # ── Tech Events ───────────────────────────────────────────────────────────
    Event(
        id="EVT-001",
        title="CodeSprint 2026 — 24hr Hackathon",
        description="Annual 24-hour hackathon organized by the coding club. Build innovative solutions to real-world problems. Prizes worth ₹50,000!",
        category=EventCategory.HACKATHON,
        date="2026-06-28",
        start_time="09:00",
        end_time="09:00",
        venue="Main Auditorium & CS Labs",
        organizer="Coding Club",
        club="Coding Club",
        registration_link="https://codesprint2026.devfolio.co",
        max_participants=200,
        current_participants=156,
        status=EventStatus.UPCOMING,
        tags=["hackathon", "coding", "prizes", "teams"],
        contact_email="codingclub@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-002",
        title="Introduction to Machine Learning Workshop",
        description="Hands-on workshop covering ML fundamentals — regression, classification, neural networks. Bring your laptop with Python installed.",
        category=EventCategory.WORKSHOP,
        date="2026-06-20",
        start_time="14:00",
        end_time="17:00",
        venue="CS Department, Room 301",
        organizer="AI/ML Society",
        club="AI/ML Society",
        max_participants=60,
        current_participants=52,
        status=EventStatus.UPCOMING,
        tags=["ML", "AI", "workshop", "python", "beginner-friendly"],
        contact_email="aiml@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-003",
        title="Web Development Bootcamp",
        description="3-day intensive bootcamp on modern web development — React, Next.js, and deploying to the cloud. Certificate provided.",
        category=EventCategory.WORKSHOP,
        date="2026-07-05",
        start_time="10:00",
        end_time="16:00",
        venue="Computer Center, Lab 2",
        organizer="Google Developer Student Club",
        club="GDSC",
        max_participants=40,
        current_participants=28,
        status=EventStatus.UPCOMING,
        tags=["web", "react", "nextjs", "bootcamp", "certificate"],
        contact_email="gdsc@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-004",
        title="Competitive Programming Contest — Weekly",
        description="Weekly CP contest on Codeforces. Solve problems, improve your rating, and compete with peers. All skill levels welcome.",
        category=EventCategory.TECH,
        date="2026-06-18",
        start_time="20:00",
        end_time="22:00",
        venue="Online (Discord)",
        organizer="Coding Club",
        club="Coding Club",
        status=EventStatus.UPCOMING,
        tags=["CP", "competitive-programming", "codeforces", "weekly"],
        contact_email="codingclub@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-005",
        title="Cybersecurity CTF Challenge",
        description="Capture The Flag competition — test your hacking skills in a safe environment. Topics: web exploitation, cryptography, reverse engineering.",
        category=EventCategory.HACKATHON,
        date="2026-07-12",
        start_time="10:00",
        end_time="22:00",
        venue="CS Lab 4",
        organizer="InfoSec Club",
        club="InfoSec Club",
        max_participants=100,
        current_participants=45,
        status=EventStatus.UPCOMING,
        tags=["cybersecurity", "CTF", "hacking", "infosec"],
        contact_email="infosec@campus.edu",
        is_free=True,
    ),

    # ── Cultural Events ───────────────────────────────────────────────────────
    Event(
        id="EVT-006",
        title="Rhythms 2026 — Annual Cultural Fest",
        description="The biggest cultural fest on campus! 3 days of music, dance, drama, art, and celebrity performances. Don't miss it!",
        category=EventCategory.CULTURAL,
        date="2026-08-15",
        start_time="10:00",
        end_time="23:00",
        venue="Campus Grounds & Main Auditorium",
        organizer="Cultural Council",
        max_participants=5000,
        current_participants=2800,
        status=EventStatus.UPCOMING,
        tags=["cultural-fest", "music", "dance", "drama", "celebrity"],
        contact_email="cultural@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-007",
        title="Open Mic Night",
        description="Share your talent! Poetry, stand-up comedy, singing, or any performance. Registration open to all students.",
        category=EventCategory.CULTURAL,
        date="2026-06-22",
        start_time="19:00",
        end_time="22:00",
        venue="Student Activity Center",
        organizer="Literary Society",
        club="Literary Society",
        max_participants=30,
        current_participants=18,
        status=EventStatus.UPCOMING,
        tags=["open-mic", "poetry", "comedy", "singing"],
        contact_email="literary@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-008",
        title="Photography Exhibition — Campus Through Our Lens",
        description="Student photography exhibition showcasing the beauty of campus life. Submit your entries by June 25th.",
        category=EventCategory.CULTURAL,
        date="2026-06-30",
        start_time="11:00",
        end_time="18:00",
        venue="Art Gallery, SAC Building",
        organizer="Photography Club",
        club="Photography Club",
        status=EventStatus.UPCOMING,
        tags=["photography", "exhibition", "art", "campus-life"],
        contact_email="photoclub@campus.edu",
        is_free=True,
    ),

    # ── Sports Events ─────────────────────────────────────────────────────────
    Event(
        id="EVT-009",
        title="Inter-Hostel Cricket Tournament",
        description="Annual inter-hostel T20 cricket tournament. Register your hostel team. Matches at the cricket ground.",
        category=EventCategory.SPORTS,
        date="2026-07-01",
        start_time="06:00",
        end_time="18:00",
        venue="Cricket Ground",
        organizer="Sports Council",
        max_participants=160,
        current_participants=120,
        status=EventStatus.UPCOMING,
        tags=["cricket", "inter-hostel", "tournament", "T20"],
        contact_email="sports@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-010",
        title="5K Campus Run",
        description="Morning fitness run around the campus. Open to all students and faculty. Refreshments provided at the finish line.",
        category=EventCategory.SPORTS,
        date="2026-06-25",
        start_time="06:00",
        end_time="08:00",
        venue="Starting Point: Main Gate",
        organizer="Fitness Club",
        club="Fitness Club",
        max_participants=300,
        current_participants=95,
        status=EventStatus.UPCOMING,
        tags=["running", "fitness", "5K", "morning"],
        contact_email="fitness@campus.edu",
        is_free=True,
    ),

    # ── Academic Events ───────────────────────────────────────────────────────
    Event(
        id="EVT-011",
        title="Guest Lecture: Future of Quantum Computing",
        description="Dr. Priya Sharma from IISc Bangalore discusses the latest breakthroughs in quantum computing and their practical applications.",
        category=EventCategory.SEMINAR,
        date="2026-06-23",
        start_time="15:00",
        end_time="16:30",
        venue="Lecture Hall Complex, LHC-101",
        organizer="Physics Department",
        status=EventStatus.UPCOMING,
        tags=["quantum", "computing", "guest-lecture", "physics"],
        contact_email="physics@campus.edu",
        is_free=True,
    ),
    Event(
        id="EVT-012",
        title="Research Paper Writing Workshop",
        description="Learn how to write and publish research papers. Covers literature review, methodology, LaTeX formatting, and journal submission.",
        category=EventCategory.WORKSHOP,
        date="2026-07-08",
        start_time="10:00",
        end_time="13:00",
        venue="Central Library, Seminar Hall",
        organizer="Research Scholar Association",
        max_participants=50,
        current_participants=32,
        status=EventStatus.UPCOMING,
        tags=["research", "paper-writing", "LaTeX", "academic"],
        contact_email="rsa@campus.edu",
        is_free=True,
    ),

    # ── Social Events ─────────────────────────────────────────────────────────
    Event(
        id="EVT-013",
        title="Fresher's Welcome Party",
        description="Welcome event for the new batch! Games, performances, and refreshments. Meet your seniors and make new friends.",
        category=EventCategory.SOCIAL,
        date="2026-08-01",
        start_time="18:00",
        end_time="22:00",
        venue="Open Air Theatre",
        organizer="Student Council",
        status=EventStatus.UPCOMING,
        tags=["freshers", "welcome", "party", "social"],
        contact_email="studentcouncil@campus.edu",
        is_free=True,
    ),

    # ── Past Events (for testing) ─────────────────────────────────────────────
    Event(
        id="EVT-014",
        title="TechNova 2026 — Annual Tech Fest",
        description="The annual technical festival featuring robotics competitions, coding challenges, and industry talks. Was a massive success!",
        category=EventCategory.TECH,
        date="2026-03-15",
        start_time="09:00",
        end_time="21:00",
        venue="Entire Campus",
        organizer="Technical Council",
        max_participants=3000,
        current_participants=2650,
        status=EventStatus.COMPLETED,
        tags=["tech-fest", "robotics", "coding", "industry"],
        contact_email="techcouncil@campus.edu",
        is_free=True,
    ),
]


# ─── Student Clubs ───────────────────────────────────────────────────────────────

CLUBS: list[Club] = [
    Club(
        id="CLB-001",
        name="Coding Club",
        description="The premier programming club on campus. We organize hackathons, CP contests, and coding workshops throughout the year.",
        category="Tech",
        president="Rahul Sharma",
        email="codingclub@campus.edu",
        member_count=450,
        meeting_schedule="Every Wednesday, 8 PM, CS Lab 1",
        social_links={"instagram": "@codingclub", "discord": "codingclub-server", "github": "campus-coding-club"},
    ),
    Club(
        id="CLB-002",
        name="AI/ML Society",
        description="Dedicated to artificial intelligence and machine learning. Weekly paper reading groups, project showcases, and Kaggle competitions.",
        category="Tech",
        president="Ananya Gupta",
        email="aiml@campus.edu",
        member_count=280,
        meeting_schedule="Every Friday, 6 PM, CS Department Room 301",
        social_links={"instagram": "@aiml_society", "linkedin": "aiml-campus"},
    ),
    Club(
        id="CLB-003",
        name="Google Developer Student Club (GDSC)",
        description="Google-backed student community for learning and building with Google technologies. Workshops, study jams, and solution challenges.",
        category="Tech",
        president="Vikram Singh",
        email="gdsc@campus.edu",
        member_count=350,
        meeting_schedule="Every Saturday, 11 AM, Computer Center",
        social_links={"instagram": "@gdsc_campus", "youtube": "GDSC-Campus"},
    ),
    Club(
        id="CLB-004",
        name="InfoSec Club",
        description="Cybersecurity enthusiasts club. CTF competitions, security workshops, and bug bounty hunting. Learn to hack ethically!",
        category="Tech",
        president="Karan Mehta",
        email="infosec@campus.edu",
        member_count=150,
        meeting_schedule="Every Thursday, 9 PM, Online (Discord)",
        social_links={"discord": "infosec-campus", "twitter": "@infosec_campus"},
    ),
    Club(
        id="CLB-005",
        name="Literary Society",
        description="For lovers of literature, poetry, and creative writing. Open mics, debates, and the annual literary magazine.",
        category="Cultural",
        president="Priya Nair",
        email="literary@campus.edu",
        member_count=200,
        meeting_schedule="Every Tuesday, 7 PM, SAC Room 202",
        social_links={"instagram": "@lit_soc"},
    ),
    Club(
        id="CLB-006",
        name="Photography Club",
        description="Capturing campus life one frame at a time. Photo walks, editing workshops, and annual exhibitions.",
        category="Cultural",
        president="Arjun Reddy",
        email="photoclub@campus.edu",
        member_count=180,
        meeting_schedule="Every Sunday, 7 AM (Photo Walk), 5 PM (Editing Session)",
        social_links={"instagram": "@photo_campus", "flickr": "campus-photographers"},
    ),
    Club(
        id="CLB-007",
        name="Fitness Club",
        description="Stay fit, stay healthy! Yoga sessions, gym training, running groups, and sports nutrition talks.",
        category="Sports",
        president="Deepak Verma",
        email="fitness@campus.edu",
        member_count=320,
        meeting_schedule="Daily, 6 AM, Sports Complex",
        social_links={"instagram": "@fit_campus"},
    ),
    Club(
        id="CLB-008",
        name="Robotics Club",
        description="Build robots, compete nationally! We work on drones, autonomous vehicles, and industrial automation projects.",
        category="Tech",
        president="Sneha Patil",
        email="robotics@campus.edu",
        member_count=120,
        meeting_schedule="Every Saturday, 2 PM, Robotics Lab (ME Department)",
        social_links={"instagram": "@robo_campus", "youtube": "RoboticsCampus"},
    ),
]


# ─── Data Access Functions ───────────────────────────────────────────────────────

def get_upcoming_events(days: int = 30, category: str | None = None) -> list[dict]:
    """Get upcoming events within the next N days."""
    from datetime import datetime, timedelta
    now = datetime.now()
    cutoff = now + timedelta(days=days)

    results = []
    for event in EVENTS:
        if event.status in [EventStatus.CANCELLED, EventStatus.COMPLETED]:
            continue
        try:
            event_date = datetime.strptime(event.date, "%Y-%m-%d")
        except ValueError:
            continue
        if now <= event_date <= cutoff:
            if category and event.category.value.lower() != category.lower():
                continue
            results.append(event.model_dump())

    results.sort(key=lambda e: e["date"])
    return results


def search_events(query: str) -> list[dict]:
    """Search events by keyword in title, description, or tags."""
    query_lower = query.lower()
    results = []
    for event in EVENTS:
        if (query_lower in event.title.lower() or
            query_lower in event.description.lower() or
            any(query_lower in tag.lower() for tag in event.tags)):
            results.append(event.model_dump())
    return results


def get_event_details(event_id: str) -> dict | None:
    """Get full details for a specific event."""
    for event in EVENTS:
        if event.id == event_id:
            return event.model_dump()
    return None


def get_club_info(club_name: str | None = None) -> list[dict]:
    """Get info about student clubs. If club_name given, search by name."""
    if club_name:
        name_lower = club_name.lower()
        return [c.model_dump() for c in CLUBS if name_lower in c.name.lower()]
    return [c.model_dump() for c in CLUBS]


def get_events_by_club(club_name: str) -> list[dict]:
    """Get events organized by a specific club."""
    name_lower = club_name.lower()
    return [
        e.model_dump() for e in EVENTS
        if e.club and name_lower in e.club.lower()
    ]
