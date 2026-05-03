# 🚀 GitHub Setup & Deployment Guide

## Moving Project from G Drive to GitHub/Company Network

---

## 📋 Prerequisites

- Git installed on your machine
- GitHub account (or company GitLab/Bitbucket)
- Access to company network/repository
- Admin access to create repositories

---

## 🔧 Step 1: Prepare Local Repository

### 1.1 Initialize Git Repository

```bash
cd incident-tracker
git init
git config user.name "Your Name"
git config user.email "your.email@company.com"
```

### 1.2 Create .gitignore File

```bash
cat > .gitignore << 'EOF'
# Python
*.pyc
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Environment
.env
.env.local
.env.*.local

# Data
*.xlsx
*.xls
data/backups/

# Logs
*.log
logs/

# OS
.DS_Store
Thumbs.db

# Node (if using frontend build tools)
node_modules/
npm-debug.log
yarn-error.log

# Testing
.pytest_cache/
.coverage
htmlcov/

# Docker
.dockerignore
EOF
```

### 1.3 Create .env.example File

```bash
cat > .env.example << 'EOF'
# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=sqlite:///incident-tracker.db

# Admin Password
ADMIN_PASSWORD=change-me-in-production

# Form PINs
FORM_PIN_S1=1111
FORM_PIN_S2=2222
FORM_PIN_ONCALL=3333

# Email Configuration (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Logging
LOG_LEVEL=INFO
EOF
```

### 1.4 Create README.md

```bash
cat > README.md << 'EOF'
# AI - SRE Alert Investigation Tracker

A comprehensive incident tracking system for SRE teams to manage, monitor, and analyze alerts and incidents.

## Features

- 📊 Real-time incident dashboard
- 📝 Incident entry form with validation
- 👨‍💼 Admin panel for management
- 📈 Advanced analytics and reporting
- 🔐 Role-based access control
- 📱 Responsive design
- 🔄 Auto-refresh capabilities
- 📥 CSV export functionality

## Quick Start

### Prerequisites
- Python 3.8+
- Flask
- openpyxl (for Excel support)

### Installation

1. Clone the repository
```bash
git clone https://github.com/company/incident-tracker.git
cd incident-tracker
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r src/backend/requirements.txt
```

4. Configure environment
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run the application
```bash
python src/backend/app.py
```

6. Access the application
- Dashboard: http://localhost:5000/dashboard.html
- Form: http://localhost:5000/form.html
- Admin: http://localhost:5000/admin.html

## Documentation

- [Setup Guide](docs/SETUP.md)
- [User Guide](docs/USER_GUIDE.md)
- [Admin Guide](docs/ADMIN_GUIDE.md)
- [API Documentation](docs/API_DOCUMENTATION.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## Project Structure

```
incident-tracker/
├── src/
│   ├── backend/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   └── config.py
│   └── frontend/
│       ├── templates/
│       │   ├── dashboard.html
│       │   ├── form.html
│       │   └── admin.html
│       └── static/
├── data/
│   └── incident-tracker.xlsx
├── docs/
├── scripts/
├── tests/
└── .github/
    └── workflows/
```

## URLs

- **Dashboard**: http://localhost:5000/dashboard.html
- **Form**: http://localhost:5000/form.html
- **Admin**: http://localhost:5000/admin.html
- **API**: http://localhost:5000/api/incidents

## Form PIN Codes

- Shift 1 (S1): 1111
- Shift 2 (S2): 2222
- On Call: 3333
- Admin: 9999

## Contributing

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Commit your changes (`git commit -m 'Add amazing feature'`)
3. Push to the branch (`git push origin feature/amazing-feature`)
4. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions, please create an issue on GitHub or contact the development team.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
EOF
```

---

## 🌐 Step 2: Create GitHub Repository

### 2.1 Create Repository on GitHub

1. Go to https://github.com/new
2. Enter repository name: `incident-tracker`
3. Add description: "AI - SRE Alert Investigation Tracker"
4. Choose visibility: Private (for company use)
5. Do NOT initialize with README (we have one)
6. Click "Create repository"

### 2.2 Add Remote and Push

```bash
# Add remote repository
git remote add origin https://github.com/company/incident-tracker.git

# Rename branch to main (if needed)
git branch -M main

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI - SRE Alert Investigation Tracker"

# Push to GitHub
git push -u origin main
```

---

## 🔐 Step 3: Configure GitHub Settings

### 3.1 Branch Protection Rules

1. Go to Settings → Branches
2. Add rule for `main` branch
3. Enable:
   - Require pull request reviews before merging
   - Require status checks to pass before merging
   - Require branches to be up to date before merging
   - Include administrators

### 3.2 Secrets Configuration

1. Go to Settings → Secrets and variables → Actions
2. Add secrets:
   - `ADMIN_PASSWORD` - Admin panel password
   - `DATABASE_URL` - Database connection string
   - `SECRET_KEY` - Flask secret key

### 3.3 Collaborators

1. Go to Settings → Collaborators
2. Add team members with appropriate roles:
   - Admin: Full access
   - Maintain: Can manage without access to sensitive actions
   - Write: Can push to branches
   - Triage: Can manage issues and pull requests
   - Read: Read-only access

---

## 🔄 Step 4: Setup CI/CD Pipeline

### 4.1 Create GitHub Actions Workflow

```bash
mkdir -p .github/workflows
cat > .github/workflows/ci.yml << 'EOF'
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r src/backend/requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 src/backend/ --count --select=E9,F63,F7,F82 --show-source --statistics
EOF
```

### 4.2 Create Deployment Workflow

```bash
cat > .github/workflows/deploy.yml << 'EOF'
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy to server
      env:
        DEPLOY_KEY: ${{ secrets.DEPLOY_KEY }}
        DEPLOY_HOST: ${{ secrets.DEPLOY_HOST }}
        DEPLOY_USER: ${{ secrets.DEPLOY_USER }}
      run: |
        mkdir -p ~/.ssh
        echo "$DEPLOY_KEY" > ~/.ssh/deploy_key
        chmod 600 ~/.ssh/deploy_key
        ssh-keyscan -H $DEPLOY_HOST >> ~/.ssh/known_hosts
        ssh -i ~/.ssh/deploy_key $DEPLOY_USER@$DEPLOY_HOST 'cd /app/incident-tracker && git pull origin main && pip install -r src/backend/requirements.txt && systemctl restart incident-tracker'
EOF
```

---

## 📦 Step 5: Setup Company Network Deployment

### 5.1 For Company GitLab

```bash
# Change remote to GitLab
git remote remove origin
git remote add origin https://gitlab.company.com/team/incident-tracker.git
git push -u origin main
```

### 5.2 For Company Bitbucket

```bash
# Change remote to Bitbucket
git remote remove origin
git remote add origin https://bitbucket.org/company/incident-tracker.git
git push -u origin main
```

### 5.3 For Company Git Server

```bash
# Change remote to company server
git remote remove origin
git remote add origin ssh://git@git.company.com/incident-tracker.git
git push -u origin main
```

---

## 🚀 Step 6: Team Collaboration Setup

### 6.1 Create Development Branch

```bash
git checkout -b develop
git push -u origin develop
```

### 6.2 Create Feature Branch Template

```bash
# For new features
git checkout -b feature/feature-name

# For bug fixes
git checkout -b bugfix/bug-name

# For hotfixes
git checkout -b hotfix/hotfix-name
```

### 6.3 Pull Request Template

```bash
cat > .github/PULL_REQUEST_TEMPLATE.md << 'EOF'
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests pass locally
EOF
```

---

## 📋 Step 7: Documentation Setup

### 7.1 Create CONTRIBUTING.md

```bash
cat > CONTRIBUTING.md << 'EOF'
# Contributing to Incident Tracker

## Getting Started

1. Fork the repository
2. Clone your fork
3. Create a feature branch
4. Make your changes
5. Submit a pull request

## Code Style

- Follow PEP 8 for Python
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions

## Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests liberally after the first line

## Pull Request Process

1. Update documentation
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md
5. Request review from maintainers
EOF
```

### 7.2 Create CHANGELOG.md

```bash
cat > CHANGELOG.md << 'EOF'
# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-05-03

### Added
- Initial release
- Dashboard with real-time analytics
- Incident entry form
- Admin panel
- Advanced filtering
- CSV export
- Auto-refresh functionality

### Changed
- N/A

### Fixed
- N/A

### Security
- Password-protected admin panel
- Role-based access control
EOF
```

---

## 🔐 Step 8: Security Configuration

### 8.1 Create Security Policy

```bash
cat > SECURITY.md << 'EOF'
# Security Policy

## Reporting Security Issues

Please do not open public issues for security vulnerabilities. Instead, email security@company.com with:

1. Description of the vulnerability
2. Steps to reproduce
3. Potential impact
4. Suggested fix (if any)

## Security Best Practices

1. Keep dependencies updated
2. Use strong passwords
3. Enable two-factor authentication
4. Review access logs regularly
5. Rotate secrets periodically
EOF
```

### 8.2 Add CODEOWNERS

```bash
cat > .github/CODEOWNERS << 'EOF'
# Global owners
* @team-lead @senior-dev

# Backend
/src/backend/ @backend-team

# Frontend
/src/frontend/ @frontend-team

# Documentation
/docs/ @documentation-team

# DevOps
/.github/ @devops-team
/docker* @devops-team
EOF
```

---

## 📊 Step 9: Monitoring & Maintenance

### 9.1 Setup GitHub Issues Template

```bash
mkdir -p .github/ISSUE_TEMPLATE

cat > .github/ISSUE_TEMPLATE/bug_report.md << 'EOF'
---
name: Bug Report
about: Report a bug
title: "[BUG] "
labels: bug
---

## Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. Step 3

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: 
- Browser: 
- Version: 

## Screenshots
If applicable, add screenshots
EOF

cat > .github/ISSUE_TEMPLATE/feature_request.md << 'EOF'
---
name: Feature Request
about: Suggest a new feature
title: "[FEATURE] "
labels: enhancement
---

## Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should this be implemented?

## Alternatives
Any alternative solutions?
EOF
```

---

## 🎯 Step 10: Final Checklist

- [ ] Repository created on GitHub/GitLab
- [ ] All files committed and pushed
- [ ] Branch protection rules configured
- [ ] Secrets configured
- [ ] Collaborators added
- [ ] CI/CD pipeline setup
- [ ] Documentation complete
- [ ] Security policy created
- [ ] CODEOWNERS configured
- [ ] Issue templates created
- [ ] README updated
- [ ] CHANGELOG created
- [ ] Team notified

---

## 📞 Team Access URLs

### For Team Members to Access

**Dashboard**: http://your-company-domain.com/dashboard.html
**Form**: http://your-company-domain.com/form.html
**Admin**: http://your-company-domain.com/admin.html (Password protected)

### GitHub Repository

**Repository**: https://github.com/company/incident-tracker
**Issues**: https://github.com/company/incident-tracker/issues
**Pull Requests**: https://github.com/company/incident-tracker/pulls
**Wiki**: https://github.com/company/incident-tracker/wiki

---

## 🚀 Deployment to Production

### Option 1: Docker Deployment

```bash
# Build Docker image
docker build -t incident-tracker:latest .

# Run container
docker run -p 5000:5000 -e ADMIN_PASSWORD=your-password incident-tracker:latest
```

### Option 2: Server Deployment

```bash
# SSH to server
ssh user@server.com

# Clone repository
git clone https://github.com/company/incident-tracker.git
cd incident-tracker

# Setup
python -m venv venv
source venv/bin/activate
pip install -r src/backend/requirements.txt

# Run with systemd
sudo systemctl start incident-tracker
```

### Option 3: Cloud Deployment (AWS/Azure/GCP)

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for cloud-specific instructions.

---

## 📞 Support

For questions or issues with GitHub setup, contact:
- DevOps Team: devops@company.com
- Project Lead: project-lead@company.com

---

**Status**: ✅ **READY FOR GITHUB DEPLOYMENT**

