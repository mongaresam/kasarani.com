# KTSSD ERP Portal v2.0
**Kasarani Treeside Secondary School for the Deaf — Nairobi, Kenya**

## Quick Start
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # set your SECRET_KEY
flask db init && flask db migrate && flask db upgrade
python run.py
```
Open http://localhost:5000 — password for all demo roles: **demo1234**

## Project Structure
See the full tree in the spec document.

## Blueprints
| Blueprint | URL prefix | Module |
|-----------|------------|--------|
| auth | / | Login, logout |
| dashboard | /dashboard | Overview & charts |
| academic | /academic | CBC/CBE + 8-4-4 |
| results | /results | KCSE result portal |
| library | /library | Resource management |
| store | /store | Inventory |
| students | /students | Profiles + IEP |
| communication | /communication | Messaging |
| timetable | /timetable | Weekly schedule |
| reports | /reports | Analytics + AI insights |
| announcements | /announcements | Notice board |
| settings | /settings | Accessibility + account |
