# 🚀 Setup Guide: AI - SRE Alert Investigation Tracker

Complete step-by-step guide for cloning and setting up the project on a new system.

---

## 📋 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Step 1: Clone the Repository](#step-1-clone-the-repository)
3. [Step 2: Set Up Python Environment](#step-2-set-up-python-environment)
4. [Step 3: Install Dependencies](#step-3-install-dependencies)
5. [Step 4: Verify Installation](#step-4-verify-installation)
6. [Step 5: Run the Application](#step-5-run-the-application)
7. [Step 6: Access the Interfaces](#step-6-access-the-interfaces)
8. [Troubleshooting](#troubleshooting)
9. [Project Structure](#project-structure)
10. [Next Steps](#next-steps)

---

## Prerequisites

Before you start, ensure you have the following installed on your system:

### Required Software

1. **Git** (for cloning the repository)
   - Download: https://git-scm.com/download
   - Verify installation: Open terminal/command prompt and run:
     ```bash
     git --version
     ```
   - Expected output: `git version 2.x.x` or higher

2. **Python 3.8 or Higher**
   - Download: https://www.python.org/downloads/
   - During installation, **CHECK** the box: "Add Python to PATH"
   - Verify installation: Open terminal/command prompt and run:
     ```bash
     python --version
     ```
   - Expected output: `Python 3.8.x` or higher

3. **A Code Editor (Optional but Recommended)**
   - Visual Studio Code: https://code.visualstudio.com/
   - PyCharm: https://www.jetbrains.com/pycharm/
   - Or any text editor of your choice

### System Requirements

- **Operating System:** Windows, macOS, or Linux
- **RAM:** Minimum 2GB (4GB recommended)
- **Disk Space:** At least 500MB free space
- **Internet Connection:** Required for cloning and installing dependencies

---

## Step 1: Clone the Repository

### On Windows (Command Prompt or PowerShell)

1. **Open Command Prompt or PowerShell**
   - Press `Win + R`, type `cmd` or `powershell`, and press Enter

2. **Navigate to where you want to store the project**
   ```bash
   cd Desktop
   ```
   Or any other location you prefer:
   ```bash
   cd Documents
   cd C:\Users\YourUsername\Projects
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yogeshkp85/AI---SRE-Alert-Investigation-Tracker.git
   ```

4. **Navigate into the project directory**
   ```bash
   cd AI---SRE-Alert-Investigation-Tracker
   ```

### On macOS or Linux

1. **Open Terminal**
   - macOS: Press `Cmd + Space`, type `terminal`, and press Enter
   - Linux: Press `Ctrl + Alt + T`

2. **Navigate to where you want to store the project**
   ```bash
   cd ~/Desktop
   ```
   Or:
   ```bash
   cd ~/Documents
   mkdir Projects && cd Projects
   ```

3. **Clone the repository**
   ```bash
   git clone https://github.com/yogeshkp85/AI---SRE-Alert-Investigation-Tracker.git
   ```

4. **Navigate into the project directory**
   ```bash
   cd AI---SRE-Alert-Investigation-Tracker
   ```

### Verify Clone Was Successful

You should see these files and folders:
```
AI---SRE-Alert-Investigation-Tracker/
├── app.py
├── README.md
├── SETUP_GUIDE_FOR_NEW_USERS.md
├── incident-tracker.xlsx
├── templates/
│   ├── form.html
│   ├── dashboard.html
│   ├── admin.html
│   └── urls.html
├── Documents/
├── .kiro/
└── .gitignore
```

---

## Step 2: Set Up Python Environment

A virtual environment isolates project dependencies from your system Python.

### On Windows

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   ```bash
   venv\Scripts\activate
   ```

   You should see `(venv)` at the beginning of your command prompt line.

### On macOS or Linux

1. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate
   ```

   You should see `(venv)` at the beginning of your terminal prompt.

### Verify Virtual Environment is Active

Run this command:
```bash
python --version
```

It should show Python 3.8 or higher. If it shows a different version, the virtual environment might not be activated correctly.

---

## Step 3: Install Dependencies

With the virtual environment activated, install the required Python packages.

### Install Flask and openpyxl

```bash
pip install flask openpyxl
```

This will install:
- **Flask:** Web framework for the backend
- **openpyxl:** Library for reading/writing Excel files

### Verify Installation

```bash
pip list
```

You should see:
```
Flask          2.x.x
openpyxl       3.x.x
```

---

## Step 4: Verify Installation

Before running the application, verify everything is set up correctly.

### Check Project Files

Ensure these critical files exist:
```bash
# On Windows
dir app.py
dir templates\form.html
dir incident-tracker.xlsx

# On macOS/Linux
ls app.py
ls templates/form.html
ls incident-tracker.xlsx
```

### Check Python Packages

```bash
python -c "import flask; import openpyxl; print('All packages installed successfully!')"
```

Expected output:
```
All packages installed successfully!
```

---

## Step 5: Run the Application

### Start the Flask Server

```bash
python app.py
```

### Expected Output

You should see something like:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Keep the Server Running

**Important:** Keep this terminal window open while using the application. The server must be running for the interfaces to work.

---

## Step 6: Access the Interfaces

Once the Flask server is running, open your web browser and navigate to these URLs:

### 1. **Incident Submission Form**
   - URL: http://localhost:5000/form.html
   - Purpose: Submit new incidents/alerts
   - Features:
     - Fill in incident details
     - Automatic timestamp tracking
     - Real-time Excel synchronization
     - Success notifications

### 2. **Analytics Dashboard**
   - URL: http://localhost:5000/dashboard.html
   - Purpose: View and analyze incidents
   - Features:
     - Real-time incident visualization
     - Advanced filtering (Year, Month, Date, Person, Category, Shift, Status)
     - KPI metrics and charts
     - Sortable table with pagination
     - Modal detail view
     - Auto-refresh every 10 seconds
     - Export to CSV

### 3. **Admin Panel**
   - URL: http://localhost:5000/admin.html
   - Purpose: Manage incidents and team members
   - Features:
     - Secure PIN-based authentication (default PIN: 9999)
     - Create, Read, Update, Delete incidents
     - Team member management
     - Audit log viewer
     - Batch operations

### 4. **URLs Reference Page**
   - URL: http://localhost:5000/urls.html
   - Purpose: Quick reference for all system URLs
   - Features:
     - Links to all interfaces
     - API endpoint documentation
     - System information

---

## Troubleshooting

### Issue 1: "Python is not recognized"

**Solution:**
- Python is not installed or not added to PATH
- Reinstall Python and check "Add Python to PATH" during installation
- Restart your computer after installation

### Issue 2: "No module named 'flask'"

**Solution:**
- Virtual environment is not activated
- Run: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
- Then run: `pip install flask openpyxl`

### Issue 3: "Port 5000 is already in use"

**Solution:**
- Another application is using port 5000
- Option 1: Close the other application
- Option 2: Modify `app.py` line to use a different port:
  ```python
  app.run(debug=True, port=5001)  # Change 5000 to 5001
  ```

### Issue 4: "Cannot find incident-tracker.xlsx"

**Solution:**
- Ensure you're in the correct directory
- Run: `ls` (macOS/Linux) or `dir` (Windows) to verify files
- The Excel file should be in the project root directory

### Issue 5: "Connection refused" when accessing localhost:5000

**Solution:**
- Flask server is not running
- Go back to Step 5 and start the server with: `python app.py`
- Ensure the terminal shows "Running on http://127.0.0.1:5000"

### Issue 6: "ModuleNotFoundError: No module named 'openpyxl'"

**Solution:**
- openpyxl is not installed
- Activate virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (macOS/Linux)
- Install: `pip install openpyxl`

### Issue 7: "Git is not recognized"

**Solution:**
- Git is not installed
- Download and install from: https://git-scm.com/download
- Restart your terminal/command prompt after installation

---

## Project Structure

Understanding the project layout:

```
AI---SRE-Alert-Investigation-Tracker/
│
├── app.py                              # Flask backend application
│   ├── API endpoints
│   ├── Excel file handling
│   ├── Authentication logic
│   └── Data processing
│
├── incident-tracker.xlsx               # Excel database
│   └── Contains all incident records
│
├── templates/                          # HTML interfaces
│   ├── form.html                       # Incident submission form
│   ├── dashboard.html                  # Analytics dashboard
│   ├── admin.html                      # Admin management panel
│   └── urls.html                       # URLs reference page
│
├── Documents/                          # Comprehensive documentation
│   ├── 01_Project_Overview/            # Project information
│   ├── 02_System_Status_Reports/       # Status reports
│   ├── 03_Implementation_Guides/       # Implementation details
│   ├── 04_Task_Completion_Reports/     # Task reports
│   ├── 05_Bug_Fixes_and_Debugging/     # Bug fixes
│   ├── 06_Testing_Guides/              # Testing procedures
│   ├── 07_Feature_Documentation/       # Feature docs
│   ├── 08_Quick_References/            # Quick guides
│   ├── 09_Setup_and_Configuration/     # Setup scripts
│   └── 10_Archived_Old_Files/          # Old files
│
├── .kiro/                              # Kiro specification files
│   └── specs/
│       └── incident-tracker-enhancements/
│           ├── requirements.md         # Feature requirements
│           ├── design.md               # System design
│           └── tasks.md                # Implementation tasks
│
├── README.md                           # Project documentation
├── SETUP_GUIDE_FOR_NEW_USERS.md        # This file
├── .gitignore                          # Git configuration
└── venv/                               # Virtual environment (created locally)
```

---

## Next Steps

### 1. **Explore the Application**
   - Submit a test incident through the form
   - View it on the dashboard
   - Try different filters and analytics

### 2. **Access Admin Panel**
   - Go to: http://localhost:5000/admin.html
   - Login with PIN: `9999`
   - Explore admin features

### 3. **Review Documentation**
   - Check `Documents/` folder for detailed guides
   - Read `README.md` for project overview
   - Review `Documents/06_Testing_Guides/` for testing procedures

### 4. **Understand the Data**
   - Open `incident-tracker.xlsx` to see the data structure
   - Review the 27 columns and their purposes
   - Understand how data flows between interfaces

### 5. **Customize for Your Needs**
   - Modify team member names in `app.py`
   - Adjust admin PIN if needed
   - Customize styling in HTML templates
   - Add new fields or features as needed

### 6. **Set Up Version Control (Optional)**
   - Create your own GitHub fork
   - Make changes and commit them
   - Push to your repository

---

## Common Tasks

### How to Stop the Server

Press `Ctrl + C` in the terminal where Flask is running.

### How to Restart the Server

1. Press `Ctrl + C` to stop
2. Run `python app.py` again

### How to Deactivate Virtual Environment

```bash
deactivate
```

### How to Reactivate Virtual Environment

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### How to Update Dependencies

```bash
pip install --upgrade flask openpyxl
```

---

## System Requirements Summary

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 2GB | 4GB+ |
| Disk Space | 500MB | 1GB+ |
| Internet | Required for setup | Not needed after setup |
| OS | Windows/macOS/Linux | Any |

---

## Support & Help

### If You Get Stuck

1. **Check the Troubleshooting section** above
2. **Review the README.md** for project overview
3. **Check Documents/ folder** for detailed guides
4. **Review app.py** for code comments and logic
5. **Check browser console** (F12) for JavaScript errors

### Common Error Messages

| Error | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'flask'` | Activate venv and run `pip install flask openpyxl` |
| `Port 5000 already in use` | Change port in app.py or close other applications |
| `Cannot find incident-tracker.xlsx` | Ensure you're in the project root directory |
| `git: command not found` | Install Git from https://git-scm.com/download |
| `python: command not found` | Install Python from https://www.python.org/downloads/ |

---

## Quick Reference Commands

### Windows
```bash
# Clone
git clone https://github.com/yogeshkp85/AI---SRE-Alert-Investigation-Tracker.git
cd AI---SRE-Alert-Investigation-Tracker

# Setup
python -m venv venv
venv\Scripts\activate
pip install flask openpyxl

# Run
python app.py

# Stop (in terminal)
Ctrl + C

# Deactivate
deactivate
```

### macOS/Linux
```bash
# Clone
git clone https://github.com/yogeshkp85/AI---SRE-Alert-Investigation-Tracker.git
cd AI---SRE-Alert-Investigation-Tracker

# Setup
python3 -m venv venv
source venv/bin/activate
pip install flask openpyxl

# Run
python app.py

# Stop (in terminal)
Ctrl + C

# Deactivate
deactivate
```

---

## Verification Checklist

Before considering setup complete, verify:

- [ ] Git is installed and working
- [ ] Python 3.8+ is installed
- [ ] Repository is cloned successfully
- [ ] Virtual environment is created
- [ ] Virtual environment is activated
- [ ] Flask and openpyxl are installed
- [ ] Flask server starts without errors
- [ ] Form interface loads at http://localhost:5000/form.html
- [ ] Dashboard loads at http://localhost:5000/dashboard.html
- [ ] Admin panel loads at http://localhost:5000/admin.html
- [ ] Can submit a test incident
- [ ] Incident appears on dashboard

---

## Additional Resources

- **Flask Documentation:** https://flask.palletsprojects.com/
- **Python Documentation:** https://docs.python.org/3/
- **openpyxl Documentation:** https://openpyxl.readthedocs.io/
- **Git Documentation:** https://git-scm.com/doc
- **GitHub Help:** https://docs.github.com/

---

## Version Information

- **Project Version:** 1.0.0
- **Python Version Required:** 3.8+
- **Flask Version:** 2.x
- **openpyxl Version:** 3.x
- **Last Updated:** May 3, 2026

---

## Next: Getting Started with the Application

Once setup is complete, refer to:
- `README.md` - Project overview and features
- `Documents/06_Testing_Guides/` - Testing procedures
- `Documents/Setup_and_Configuration/` - Configuration guides
- `Documents/07_Feature_Documentation/` - Feature documentation

---

**Happy coding! 🚀**

If you have any questions or issues, refer to the Troubleshooting section or review the comprehensive documentation in the Documents/ folder.
