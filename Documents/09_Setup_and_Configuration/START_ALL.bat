@echo off
REM ============================================================================
REM AI - SRE Alert Investigation Tracker - START ALL INTERFACES
REM ============================================================================
REM This is a simple one-click launcher to open all three interfaces
REM ============================================================================

cls
echo.
echo ============================================================================
echo   AI - SRE Alert Investigation Tracker
echo   Opening All Interfaces...
echo ============================================================================
echo.

REM Open Dashboard
echo [1/3] Opening Dashboard...
start http://localhost:5000/dashboard.html
timeout /t 1 /nobreak

REM Open Admin Panel
echo [2/3] Opening Admin Panel...
start http://localhost:5000/admin.html
timeout /t 1 /nobreak

REM Open Form
echo [3/3] Opening Incident Entry Form...
start http://localhost:5000/form.html

echo.
echo ============================================================================
echo   SUCCESS! All interfaces are now open in your browser.
echo ============================================================================
echo.
echo DASHBOARD:  http://localhost:5000/dashboard.html
echo ADMIN:      http://localhost:5000/admin.html (PIN: 9999)
echo FORM:       http://localhost:5000/form.html (PIN: 1111/2222/3333)
echo.
echo Backend Status: RUNNING (in background)
echo.
echo Press any key to close this window...
pause >nul
