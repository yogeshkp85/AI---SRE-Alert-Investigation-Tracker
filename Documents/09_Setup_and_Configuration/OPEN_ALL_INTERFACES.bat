@echo off
REM ============================================================================
REM AI - SRE Alert Investigation Tracker - Open All Interfaces
REM ============================================================================
REM This script opens all three interfaces in your default browser
REM The backend (Flask) is already running in the background
REM ============================================================================

echo.
echo ============================================================================
echo   Opening AI - SRE Alert Investigation Tracker Interfaces
echo ============================================================================
echo.

REM Wait a moment to ensure backend is ready
timeout /t 2 /nobreak

REM Open Dashboard
echo Opening Dashboard...
start http://localhost:5000/dashboard.html

REM Wait a moment
timeout /t 1 /nobreak

REM Open Admin Panel
echo Opening Admin Panel...
start http://localhost:5000/admin.html

REM Wait a moment
timeout /t 1 /nobreak

REM Open Form
echo Opening Incident Entry Form...
start http://localhost:5000/form.html

echo.
echo ============================================================================
echo   All interfaces opened successfully!
echo ============================================================================
echo.
echo Dashboard: http://localhost:5000/dashboard.html
echo Admin:     http://localhost:5000/admin.html (PIN: 9999)
echo Form:      http://localhost:5000/form.html (PIN: 1111/2222/3333)
echo.
echo Backend is running in the background and will continue to run.
echo.
pause
