"""Centralised demo/seed data used by all blueprints."""

USERS = {
    "admin":       {"name": "John Kamau",       "role": "Admin",       "dept": "Administration",     "icon": "🏛️", "id": "ADM001"},
    "principal":   {"name": "Patrick Muriithi", "role": "Principal",   "dept": "Leadership",         "icon": "👔", "id": "PRI001"},
    "teacher":     {"name": "Grace Wanjiku",    "role": "Teacher",     "dept": "Mathematics",        "icon": "📚", "id": "TCH023"},
    "hod":         {"name": "David Ochieng",    "role": "HOD",         "dept": "Sciences",           "icon": "🎓", "id": "HOD005"},
    "librarian":   {"name": "Faith Njeri",      "role": "Librarian",   "dept": "Library",            "icon": "📖", "id": "LIB001"},
    "storekeeper": {"name": "Peter Mwangi",     "role": "Storekeeper", "dept": "Stores",             "icon": "🏪", "id": "STR001"},
    "ict":         {"name": "James Kariuki",    "role": "ICT Admin",   "dept": "ICT",                "icon": "💻", "id": "ICT001"},
    "student":     {"name": "Amina Hassan",     "role": "Student",     "dept": "Form 3 – Stream A",  "icon": "🧑‍🎓", "id": "KT2024/F/012"},
}

STUDENTS = [
    {"id": "KT2024/M/001", "name": "Brian Otieno",    "form": "Form 4", "stream": "A", "gender": "M", "county": "Kisumu",   "hearing": "Profound", "gpa": 7.2},
    {"id": "KT2024/F/002", "name": "Sharon Wambui",   "form": "Form 4", "stream": "A", "gender": "F", "county": "Nairobi",  "hearing": "Severe",   "gpa": 8.1},
    {"id": "KT2024/M/003", "name": "Kevin Mutua",     "form": "Form 3", "stream": "A", "gender": "M", "county": "Machakos", "hearing": "Profound", "gpa": 6.8},
    {"id": "KT2024/F/004", "name": "Amina Hassan",    "form": "Form 3", "stream": "A", "gender": "F", "county": "Mombasa",  "hearing": "Severe",   "gpa": 7.5},
    {"id": "KT2024/M/005", "name": "James Kipchoge",  "form": "Form 2", "stream": "B", "gender": "M", "county": "Eldoret",  "hearing": "Profound", "gpa": 6.5},
    {"id": "KT2024/F/006", "name": "Rose Njoroge",    "form": "Form 2", "stream": "A", "gender": "F", "county": "Nyeri",    "hearing": "Moderate", "gpa": 7.8},
    {"id": "KT2024/M/007", "name": "Michael Oduya",   "form": "Form 1", "stream": "A", "gender": "M", "county": "Siaya",    "hearing": "Profound", "gpa": 6.2},
    {"id": "KT2024/F/008", "name": "Faith Achieng",   "form": "Form 1", "stream": "B", "gender": "F", "county": "Homa Bay", "hearing": "Severe",   "gpa": 7.0},
]

INVENTORY = [
    {"id": "BK001",  "name": "KCSE Mathematics Topical",    "category": "Textbook",      "qty": 28, "issued": 22, "available": 6,  "condition": "Good", "dept": "Mathematics"},
    {"id": "BK002",  "name": "Biology Form 4",              "category": "Textbook",      "qty": 25, "issued": 20, "available": 5,  "condition": "Good", "dept": "Sciences"},
    {"id": "BK003",  "name": "English Grammar Mastery",     "category": "Revision",      "qty": 30, "issued": 18, "available": 12, "condition": "Good", "dept": "Languages"},
    {"id": "BK004",  "name": "Kenyan Sign Language Vol 1",  "category": "SL Material",   "qty": 15, "issued": 10, "available": 5,  "condition": "Good", "dept": "Special Needs"},
    {"id": "IT001",  "name": "Dell Laptop",                 "category": "ICT Device",    "qty": 12, "issued": 8,  "available": 4,  "condition": "Fair", "dept": "ICT"},
    {"id": "IT002",  "name": "Epson Projector",             "category": "AV Equipment",  "qty": 4,  "issued": 3,  "available": 1,  "condition": "Good", "dept": "All"},
    {"id": "SP001",  "name": "Football",                    "category": "Sports",        "qty": 6,  "issued": 4,  "available": 2,  "condition": "Good", "dept": "PE"},
    {"id": "LAB001", "name": "Microscope",                  "category": "Lab Equipment", "qty": 8,  "issued": 5,  "available": 3,  "condition": "Good", "dept": "Sciences"},
    {"id": "OFF001", "name": "Whiteboard Markers (Box)",    "category": "Office Supply", "qty": 20, "issued": 15, "available": 5,  "condition": "New",  "dept": "All"},
    {"id": "SL001",  "name": "Sign Language Visual Chart",  "category": "SL Material",   "qty": 10, "issued": 7,  "available": 3,  "condition": "Good", "dept": "Special Needs"},
]

ANNOUNCEMENTS = [
    {"id": 1, "title": "KCSE 2024 Mock Exams – Form 4",         "date": "20 May 2026", "type": "Academic",      "urgent": True,  "body": "Mock examinations for Form 4 students begin Monday 25th May. Timetable posted on the noticeboard and available in the portal."},
    {"id": 2, "title": "Term 2 Opening Date",                   "date": "18 May 2026", "type": "General",       "urgent": False, "body": "Term 2 2026 officially opens on June 2nd. All students should report by 8AM with all required materials."},
    {"id": 3, "title": "Sign Language Communication Week",      "date": "15 May 2026", "type": "Special Event", "urgent": False, "body": "KTSSD joins the national Sign Language Awareness Week. Special activities and competitions scheduled for the whole school."},
    {"id": 4, "title": "New Digital Learning Resources Available","date": "12 May 2026","type": "Library",       "urgent": False, "body": "The library has received new digital tablets and learning materials for KCSE candidates. Visit the library to access."},
]

MESSAGES = [
    {"id": 1, "from": "Principal Muriithi",       "subject": "KCSE Preparation Meeting", "time": "09:30", "date": "Today",     "read": False, "priority": "high",   "body": "All Form 4 class teachers to meet in the staffroom at 2PM today for KCSE prep discussion."},
    {"id": 2, "from": "HOD Sciences",             "subject": "Lab Resources Request",    "time": "08:15", "date": "Today",     "read": False, "priority": "normal", "body": "Requesting 3 additional microscopes for Biology practicals next week."},
    {"id": 3, "from": "Faith Njeri (Librarian)",  "subject": "Books Due for Return",     "time": "14:20", "date": "Yesterday", "read": True,  "priority": "normal", "body": "Reminder: All Form 4 students should return borrowed books by end of term."},
    {"id": 4, "from": "Deputy Principal",         "subject": "Staff Meeting Reminder",   "time": "11:00", "date": "Yesterday", "read": True,  "priority": "normal", "body": "Monthly staff meeting scheduled for Friday 3PM in the conference room."},
    {"id": 5, "from": "ICT Admin",                "subject": "System Maintenance Notice","time": "16:45", "date": "2 days ago","read": True,  "priority": "low",    "body": "The school server will undergo maintenance this Saturday 8AM-12PM."},
]
