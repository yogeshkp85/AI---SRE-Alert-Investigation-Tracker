# ============================================================================
# AI - SRE Alert Investigation Tracker - Open All Interfaces
# ============================================================================
# This script opens all three interfaces in your default browser
# The backend (Flask) is already running in the background
# ============================================================================

Write-Host ""
Write-Host "============================================================================"
Write-Host "  Opening AI - SRE Alert Investigation Tracker Interfaces"
Write-Host "============================================================================"
Write-Host ""

# Wait a moment to ensure backend is ready
Start-Sleep -Seconds 2

# Open Dashboard
Write-Host "Opening Dashboard..."
Start-Process "http://localhost:5000/dashboard.html"

# Wait a moment
Start-Sleep -Seconds 1

# Open Admin Panel
Write-Host "Opening Admin Panel..."
Start-Process "http://localhost:5000/admin.html"

# Wait a moment
Start-Sleep -Seconds 1

# Open Form
Write-Host "Opening Incident Entry Form..."
Start-Process "http://localhost:5000/form.html"

Write-Host ""
Write-Host "============================================================================"
Write-Host "  All interfaces opened successfully!"
Write-Host "============================================================================"
Write-Host ""
Write-Host "Dashboard: http://localhost:5000/dashboard.html"
Write-Host "Admin:     http://localhost:5000/admin.html (PIN: 9999)"
Write-Host "Form:      http://localhost:5000/form.html (PIN: 1111/2222/3333)"
Write-Host ""
Write-Host "Backend is running in the background and will continue to run."
Write-Host ""
