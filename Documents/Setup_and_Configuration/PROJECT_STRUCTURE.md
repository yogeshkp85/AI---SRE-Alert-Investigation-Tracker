# 📁 Project Structure & Organization

## Current Project: AI - SRE Alert Investigation Tracker

---

## 📂 Organized Folder Structure

```
incident-tracker/
│
├── 📁 src/
│   ├── 📁 backend/
│   │   ├── app.py                          # Flask application
│   │   ├── requirements.txt                # Python dependencies
│   │   └── config.py                       # Configuration settings
│   │
│   └── 📁 frontend/
│       ├── 📁 templates/
│       │   ├── dashboard.html              # Main dashboard
│       │   ├── form.html                   # Incident entry form
│       │   └── admin.html                  # Admin panel
│       │
│       └── 📁 static/
│           ├── 📁 css/
│           │   └── styles.css              # Global styles
│           │
│           └── 📁 js/
│               └── main.js                 # Global JavaScript
│
├── 📁 data/
│   ├── incident-tracker.xlsx               # Main data file
│   └── 📁 backups/
│       └── incident-tracker-backup.xlsx    # Backup copies
│
├── 📁 docs/
│   ├── README.md                           # Project overview
│   ├── SETUP.md                            # Setup instructions
│   ├── USER_GUIDE.md                       # User guide
│   ├── ADMIN_GUIDE.md                      # Admin guide
│   ├── API_DOCUMENTATION.md                # API docs
│   ├── DEPLOYMENT.md                       # Deployment guide
│   └── TROUBLESHOOTING.md                  # Troubleshooting
│
├── 📁 scripts/
│   ├── setup.py                            # Setup script
│   ├── migrate.py                          # Data migration
│   ├── backup.py                           # Backup script
│   └── deploy.py                           # Deployment script
│
├── 📁 tests/
│   ├── test_api.py                         # API tests
│   ├── test_dashboard.py                   # Dashboard tests
│   └── test_form.py                        # Form tests
│
├── 📁 .github/
│   ├── 📁 workflows/
│   │   ├── ci.yml                          # CI/CD pipeline
│   │   └── deploy.yml                      # Deployment workflow
│   │
│   └── ISSUE_TEMPLATE.md                   # Issue template
│
├── 📁 .kiro/
│   └── 📁 specs/
│       └── incident-tracker-enhancements/
│           ├── requirements.md
│           ├── design.md
│           └── tasks.md
│
├── .gitignore                              # Git ignore rules
├── .env.example                            # Environment variables template
├── docker-compose.yml                      # Docker compose file
├── Dockerfile                              # Docker configuration
├── LICENSE                                 # License file
├── CHANGELOG.md                            # Version history
└── README.md                               # Main README

```

---

## 📋 File Organization Guide

### Backend Files (src/backend/)
- **app.py** - Main Flask application with all routes
- **requirements.txt** - Python package dependencies
- **config.py** - Configuration for different environments

### Frontend Files (src/frontend/)
- **templates/** - HTML files
  - dashboard.html - Analytics and monitoring
  - form.html - Incident entry
  - admin.html - Admin panel
- **static/** - CSS and JavaScript
  - css/styles.css - Global styles
  - js/main.js - Global JavaScript

### Data Files (data/)
- **incident-tracker.xlsx** - Main Excel data file
- **backups/** - Automatic backup copies

### Documentation (docs/)
- **README.md** - Project overview
- **SETUP.md** - Installation and setup
- **USER_GUIDE.md** - How to use the system
- **ADMIN_GUIDE.md** - Admin operations
- **API_DOCUMENTATION.md** - API reference
- **DEPLOYMENT.md** - Deployment instructions
- **TROUBLESHOOTING.md** - Common issues and solutions

### Scripts (scripts/)
- **setup.py** - Initial setup
- **migrate.py** - Data migration
- **backup.py** - Backup automation
- **deploy.py** - Deployment automation

### Tests (tests/)
- **test_api.py** - API endpoint tests
- **test_dashboard.py** - Dashboard tests
- **test_form.py** - Form validation tests

### GitHub Files (.github/)
- **workflows/** - CI/CD automation
  - ci.yml - Continuous integration
  - deploy.yml - Automated deployment
- **ISSUE_TEMPLATE.md** - Issue reporting template

---

## 🗂️ Migration Steps

### Step 1: Create New Folder Structure
```bash
mkdir -p incident-tracker/{src/{backend,frontend/{templates,static/{css,js}}},data/backups,docs,scripts,tests,.github/workflows}
```

### Step 2: Move Files
```bash
# Backend files
mv app.py incident-tracker/src/backend/
mv requirements.txt incident-tracker/src/backend/

# Frontend files
mv templates/*.html incident-tracker/src/frontend/templates/
mv static/css/*.css incident-tracker/src/frontend/static/css/
mv static/js/*.js incident-tracker/src/frontend/static/js/

# Data files
mv incident-tracker.xlsx incident-tracker/data/

# Documentation
mv *.md incident-tracker/docs/

# Scripts
mv *_script.py incident-tracker/scripts/
```

### Step 3: Create Configuration Files
```bash
# Create .env.example
cp .env .env.example

# Create .gitignore
echo "*.pyc
__pycache__/
.env
.DS_Store
*.xlsx
venv/
node_modules/" > incident-tracker/.gitignore
```

---

## 📝 File Naming Conventions

### Python Files
- `app.py` - Main application
- `config.py` - Configuration
- `models.py` - Data models
- `routes.py` - API routes
- `utils.py` - Utility functions
- `test_*.py` - Test files

### HTML Files
- `dashboard.html` - Dashboard page
- `form.html` - Form page
- `admin.html` - Admin page
- `index.html` - Home page (if needed)

### CSS Files
- `styles.css` - Global styles
- `dashboard.css` - Dashboard specific
- `form.css` - Form specific
- `admin.css` - Admin specific

### JavaScript Files
- `main.js` - Global JavaScript
- `dashboard.js` - Dashboard specific
- `form.js` - Form specific
- `admin.js` - Admin specific

### Documentation Files
- `README.md` - Project overview
- `SETUP.md` - Setup instructions
- `USER_GUIDE.md` - User documentation
- `ADMIN_GUIDE.md` - Admin documentation
- `API_DOCUMENTATION.md` - API reference
- `DEPLOYMENT.md` - Deployment guide
- `TROUBLESHOOTING.md` - Troubleshooting guide
- `CHANGELOG.md` - Version history

---

## 🔄 File Organization Checklist

- [ ] Create new folder structure
- [ ] Move backend files to src/backend/
- [ ] Move frontend files to src/frontend/
- [ ] Move data files to data/
- [ ] Move documentation to docs/
- [ ] Move scripts to scripts/
- [ ] Create .gitignore
- [ ] Create .env.example
- [ ] Create docker-compose.yml
- [ ] Create Dockerfile
- [ ] Create GitHub workflows
- [ ] Update all import paths
- [ ] Test all functionality
- [ ] Commit to Git

---

## 📊 Benefits of Organization

✅ **Clarity** - Easy to find files
✅ **Scalability** - Easy to add new features
✅ **Maintainability** - Easy to maintain code
✅ **Collaboration** - Easy for team to work together
✅ **Deployment** - Easy to deploy to production
✅ **Testing** - Easy to test components
✅ **Documentation** - Easy to document changes

---

## 🚀 Next Steps

1. Create new folder structure
2. Move files to appropriate locations
3. Update import paths in code
4. Test all functionality
5. Commit to Git
6. Push to GitHub

