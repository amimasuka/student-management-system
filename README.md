# Student Management System — GUI CRUD, Analytics, and Charts 🎓🖥️📊

[![Releases](https://img.shields.io/badge/Releases-%20Download-blue.svg)](https://github.com/amimasuka/student-management-system/releases)

Overview
- A desktop app for managing students and academic data.
- Built with Python and Tkinter. Uses material design styling.
- Supports full CRUD, CSV import/export, charts, and basic analytics.
- Good fit for educators, admins, and learners building a portfolio.

Get the release file from the releases page and run it:
Download the release file from https://github.com/amimasuka/student-management-system/releases and execute it.

Demo image
![Student Management Screenshot](https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=1200&auto=format&fit=crop&ixlib=rb-4.0.3&s=3b16b0bd2b2c1b44a1a5f7ff5d5ef8f2)

Key features
- Create, read, update, delete student records.
- Import and export CSV files for bulk data tasks.
- Visualize data: grade histograms, attendance trends, enrollment by program.
- Simple analytics: GPA averages, pass/fail rates, top performers.
- Search, filter, and sort across all student fields.
- Export charts as PNG for reports.
- Local storage via lightweight SQLite.
- Material-like UI with responsive layout for desktop screens.

Why use this
- Works offline on common platforms.
- Keeps data local and simple.
- Uses standard Python libraries so you can extend it.
- Good project to learn GUI, data handling, and visualization.

Repository topics
analytics, crud, csv, data-visualization, desktop-app, educational, gui, material-design, portfolio-project, python, student-management, tkinter

Quick start — run from release
1. Visit the releases page:
   https://github.com/amimasuka/student-management-system/releases
2. Download the release file for your OS. The release contains an executable or packaged app. Download the file and execute it.
3. The app opens a window. Use the menu to add students or import CSV.

Development setup (source version)
- Requirements: Python 3.8+.
- Tested with CPython on Windows, macOS, and Linux.

Install steps
1. Clone the repo:
   git clone https://github.com/amimasuka/student-management-system.git
   cd student-management-system
2. Create a venv and activate:
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
3. Install dependencies:
   pip install -r requirements.txt
   - Core libs: tkinter (system), matplotlib, pandas, sqlalchemy
4. Launch:
   python run_app.py

App layout
- Dashboard
  - Overview cards with counts and averages.
  - Mini charts for quick insight.
- Students
  - Table view with pagination.
  - Add / Edit forms with validation.
- Attendance
  - Record sessions and mark status.
  - Filter by date and student.
- Analytics
  - Grade distribution histogram.
  - GPA trend line per cohort.
  - Export chart button.
- Settings
  - Backup / restore data.
  - Configure storage path.

Data model
- SQLite tables:
  - students (id, first_name, last_name, dob, program, enrollment_date, email, phone)
  - grades (id, student_id, course, term, grade, credits)
  - attendance (id, student_id, date, status)
- Uses SQLAlchemy ORM for data access.

CSV format
- Import: students CSV must have header row with these columns:
  id,first_name,last_name,dob,program,enrollment_date,email,phone
- Export: app writes the same format for portability.

Example usage — CLI commands
- Launch UI:
  python run_app.py
- Run a data migration:
  python tools/migrate.py
- Export sample report:
  python tools/export_report.py --out report.pdf

Screenshots
- Dashboard
  ![Dashboard](https://images.unsplash.com/photo-1557800636-894a64c1696f?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&s=8f3b0a5f5b6f1f6a8f9e4f1f1e2a3b4c)
- Student table
  ![Table](https://images.unsplash.com/photo-1494790108377-be9c29b29330?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&s=6f0d9f0f1a2b3c4d5e6f7a8b9c0d1e2f)

Analytics examples
- GPA average per cohort
- Top 10 students by GPA
- Grade distribution by course
- Attendance heatmap by month

Extending the app
- Add new report types using pandas and matplotlib.
- Replace SQLite with a networked DB by swapping SQLAlchemy engine.
- Add authentication for multi-user environments.
- Swap UI theme or use a framework like PyQt for richer widgets.

Testing
- Unit tests for data layer live in tests/.
- Run tests:
  pytest -q

Common commands
- Lint:
  flake8 .
- Format:
  black .
- Run single test:
  pytest tests/test_models.py::test_student_create -q

Contributing
- Fork the repo and open a PR.
- Create a branch per feature or fix.
- Keep commits small and focused.
- Add tests for new logic.
- Use clear commit messages.

Troubleshooting
- If the app fails to start, check Python and dependency versions.
- For UI errors, check Tkinter availability on the system. On some Linux systems install python3-tk.
- For DB issues, delete the local database file to reset data.

Security
- The app keeps data local by default.
- Validate CSV inputs before import to avoid malformed rows.
- Avoid running untrusted binaries. Prefer running the source in a venv if you audit code.

License
- MIT License. See LICENSE file.

Credits
- Built with Python, Tkinter, matplotlib, pandas, SQLAlchemy.
- Icons and images from public sources (Unsplash and open icon sets).

Contact
- Open issues on GitHub for bugs and features.
- Link to releases: https://github.com/amimasuka/student-management-system/releases

Files and structure (high level)
- run_app.py — app entry point
- app/ — GUI code and widgets
- models/ — ORM models and DB logic
- tools/ — helper scripts (export, migrate)
- data/ — sample CSV and DB
- requirements.txt
- README.md

How to package
- Use PyInstaller to create a single executable:
  pip install pyinstaller
  pyinstaller --onefile run_app.py
- Or build OS-specific installers with native tools.

Release notes and downloads
- Check the releases page for packaged builds and installers:
  https://github.com/amimasuka/student-management-system/releases
- Download the release file and execute it for your OS.

Project roadmap
- Add role-based access and multi-user sync.
- Add export to Excel and PDF reports.
- Add chart interactivity and export themes.

If you need a walkthrough, open an issue and request a step-by-step guide or a video demo.