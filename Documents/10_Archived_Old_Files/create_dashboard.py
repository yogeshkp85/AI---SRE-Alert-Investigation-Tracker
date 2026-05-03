#!/usr/bin/env python3
"""Create Dashboard.html"""

html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - SRE Alert Tracker</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.9.1/chart.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #001F3F 0%, #003366 100%);
            min-height: 100vh;
            padding: 20px;
            color: #001F3F;
        }
        .container { max-width: 1600px; margin: 0 auto; }
        .header {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .header h1 { font-size: 24px; color: #001F3F; }
        .header-info { font-size: 13px; color: #666; }
        .filters {
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
        }
        .filter-row {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 15px;
            margin-bottom: 15px;
        }
        .filter-group {
            display: flex;
            flex-direction: column;
        }
        .filter-group label {
            font-size: 12px;
            font-weight: 600;
            color: #001F3F;
            margin-bottom: 5px;
            text-transform: uppercase;
        }
        .filter-group select {
            padding: 8px 12px;
            border: 1px solid #003366;
            border-radius: 4px;
            font-size: 13px;
            background: white;
            color: #001F3F;
        }
        .filter-buttons {
            display: flex;
            gap: 10px;
        }
        button {
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s;
        }
        .btn-apply {
            background: #001F3F;
            color: white;
        }
        .btn-apply:hover {
            background: #003366;
        }
        .btn-clear {
            background: #f5f5f5;
            color: #001F3F;
            border: 1px solid #003366;
        }
        .btn-clear:hover {
            background: #e8e8e8;
        }
        .kpi-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        .kpi-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
            border-left: 4px solid #001F3F;
        }
        .kpi-label {
            font-size: 12px;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        .kpi-value {
            font-size: 28px;
            font-weight: 700;
            color: #001F3F;
        }
        .charts-section {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }
        .chart-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
        }
        .chart-title {
            font-size: 14px;
            font-weight: 600;
            color: #001F3F;
            margin-bottom: 15px;
        }
        .table-section {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
            overflow: hidden;
        }
        .table-header {
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .table-header h2 {
            font-size: 16px;
            color: #001F3F;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th {
            background: #f5f5f5;
            padding: 12px;
            text-align: left;
            font-size: 12px;
            font-weight: 600;
            color: #001F3F;
            border-bottom: 2px solid #003366;
            cursor: pointer;
            user-select: none;
        }
        th:hover {
            background: #e8e8e8;
        }
        td {
            padding: 12px;
            border-bottom: 1px solid #e0e0e0;
            font-size: 13px;
        }
        tr:hover {
            background: #f9f9f9;
            cursor: pointer;
        }
        .category-p1 { color: #dc3545; font-weight: 600; }
        .category-p2 { color: #fd7e14; font-weight: 600; }
        .category-p3 { color: #ffc107; font-weight: 600; }
        .category-p4 { color: #28a745; font-weight: 600; }
        .pagination {
            padding: 15px 20px;
            display: flex;
            justify-content: center;
            gap: 5px;
            border-top: 1px solid #e0e0e0;
        }
        .pagination button {
            padding: 6px 10px;
            font-size: 12px;
            background: #f5f5f5;
            color: #001F3F;
            border: 1px solid #003366;
        }
        .pagination button.active {
            background: #001F3F;
            color: white;
        }
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }
        .modal.active {
            display: flex;
        }
        .modal-content {
            background: white;
            border-radius: 8px;
            max-width: 800px;
            max-height: 90vh;
            overflow-y: auto;
            width: 90%;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        }
        .modal-header {
            padding: 20px;
            border-bottom: 1px solid #e0e0e0;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #f5f5f5;
        }
        .modal-header h2 {
            font-size: 18px;
            color: #001F3F;
        }
        .modal-close {
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #666;
        }
        .modal-body {
            padding: 20px;
        }
        .modal-section {
            margin-bottom: 20px;
        }
        .modal-section-title {
            font-size: 13px;
            font-weight: 600;
            color: #001F3F;
            text-transform: uppercase;
            margin-bottom: 10px;
            padding-bottom: 8px;
            border-bottom: 2px solid #001F3F;
        }
        .modal-row {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-bottom: 10px;
        }
        .modal-field {
            display: flex;
            flex-direction: column;
        }
        .modal-label {
            font-size: 11px;
            color: #666;
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .modal-value {
            font-size: 13px;
            color: #001F3F;
            word-break: break-word;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1>📊 Incident Dashboard</h1>
                <p class="header-info">Real-time incident monitoring and analytics</p>
            </div>
            <div class="header-info">
                <div id="currentTime"></div>
                <div id="connectionStatus">● Connected</div>
            </div>
        </div>
        
        <div class="filters">
            <div class="filter-row">
                <div class="filter-group">
                    <label>Year</label>
                    <select id="filterYear">
                        <option value="">All Years</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Month</label>
                    <select id="filterMonth">
                        <option value="">All Months</option>
                        <option value="1">January</option>
                        <option value="2">February</option>
                        <option value="3">March</option>
                        <option value="4">April</option>
                        <option value="5">May</option>
                        <option value="6">June</option>
                        <option value="7">July</option>
                        <option value="8">August</option>
                        <option value="9">September</option>
                        <option value="10">October</option>
                        <option value="11">November</option>
                        <option value="12">December</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Category</label>
                    <select id="filterCategory">
                        <option value="">All Categories</option>
                        <option value="P1">P1</option>
                        <option value="P2">P2</option>
                        <option value="P3">P3</option>
                        <option value="P4">P4</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Status</label>
                    <select id="filterStatus">
                        <option value="">All Status</option>
                        <option value="In Progress">In Progress</option>
                        <option value="Pending">Pending</option>
                        <option value="Completed">Completed</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Assigned To</label>
                    <select id="filterAssignedTo">
                        <option value="">All Members</option>
                    </select>
                </div>
                <div class="filter-group">
                    <label>Shift Lead</label>
                    <select id="filterShiftLead">
                        <option value="">All Leads</option>
                    </select>
                </div>
            </div>
            <div class="filter-row">
                <div class="filter-buttons">
                    <button class="btn-apply" onclick="applyFilters()">Apply Filters</button>
                    <button class="btn-clear" onclick="clearFilters()">Clear All</button>
                </div>
            </div>
        </div>
        
        <div class="kpi-section" id="kpiSection"></div>
        
        <div class="charts-section">
            <div class="chart-card">
                <div class="chart-title">Incidents by Category</div>
                <canvas id="categoryChart"></canvas>
            </div>
            <div class="chart-card">
                <div class="chart-title">Status Distribution</div>
                <canvas id="statusChart"></canvas>
            </div>
        </div>
        
        <div class="table-section">
            <div class="table-header">
                <h2>Incidents</h2>
                <div id="incidentCount">0 incidents</div>
            </div>
            <table id="incidentsTable">
                <thead>
                    <tr>
                        <th onclick="sortTable(0)">Date</th>
                        <th onclick="sortTable(1)">Shift</th>
                        <th onclick="sortTable(2)">Category</th>
                        <th onclick="sortTable(3)">Status</th>
                        <th onclick="sortTable(4)">Alert</th>
                        <th onclick="sortTable(5)">Assigned To</th>
                        <th onclick="sortTable(6)">Shift Lead</th>
                        <th onclick="sortTable(7)">RITM</th>
                    </tr>
                </thead>
                <tbody id="tableBody"></tbody>
            </table>
            <div class="pagination" id="pagination"></div>
        </div>
    </div>
    
    <div class="modal" id="detailModal">
        <div class="modal-content">
            <div class="modal-header">
                <h2 id="modalTitle">Incident Details</h2>
                <button class="modal-close" onclick="closeModal()">×</button>
            </div>
            <div class="modal-body" id="modalBody"></div>
        </div>
    </div>
    
    <script>
        let allIncidents = [];
        let filteredIncidents = [];
        let currentPage = 1;
        const rowsPerPage = 25;
        let sortColumn = 0;
        let sortAscending = true;
        let categoryChart = null;
        let statusChart = null;
        
        document.addEventListener("DOMContentLoaded", () => {
            loadIncidents();
            updateTime();
            setInterval(updateTime, 1000);
            setInterval(loadIncidents, 10000);
        });
        
        function updateTime() {
            const now = new Date();
            document.getElementById("currentTime").textContent = now.toLocaleString();
        }
        
        async function loadIncidents() {
            try {
                const response = await fetch("http://localhost:5000/api/incidents");
                const data = await response.json();
                allIncidents = data.incidents || [];
                populateFilterDropdowns();
                applyFilters();
            } catch (error) {
                console.error("Error loading incidents:", error);
                document.getElementById("connectionStatus").textContent = "● Disconnected";
            }
        }
        
        function populateFilterDropdowns() {
            const years = new Set();
            const assignedTo = new Set();
            const shiftLeads = new Set();
            
            allIncidents.forEach(incident => {
                if (incident.Date) {
                    const year = new Date(incident.Date).getFullYear();
                    years.add(year);
                }
                if (incident["Assigned To"]) assignedTo.add(incident["Assigned To"]);
                if (incident["Shift Lead"]) shiftLeads.add(incident["Shift Lead"]);
            });
            
            const yearSelect = document.getElementById("filterYear");
            const currentYear = yearSelect.value;
            yearSelect.innerHTML = '<option value="">All Years</option>';
            [...years].sort().reverse().forEach(year => {
                const option = document.createElement("option");
                option.value = year;
                option.textContent = year;
                yearSelect.appendChild(option);
            });
            yearSelect.value = currentYear;
            
            const assignedSelect = document.getElementById("filterAssignedTo");
            const currentAssigned = assignedSelect.value;
            assignedSelect.innerHTML = '<option value="">All Members</option>';
            [...assignedTo].sort().forEach(name => {
                const option = document.createElement("option");
                option.value = name;
                option.textContent = name;
                assignedSelect.appendChild(option);
            });
            assignedSelect.value = currentAssigned;
            
            const leadSelect = document.getElementById("filterShiftLead");
            const currentLead = leadSelect.value;
            leadSelect.innerHTML = '<option value="">All Leads</option>';
            [...shiftLeads].sort().forEach(name => {
                const option = document.createElement("option");
                option.value = name;
                option.textContent = name;
                leadSelect.appendChild(option);
            });
            leadSelect.value = currentLead;
        }
        
        function applyFilters() {
            const year = document.getElementById("filterYear").value;
            const month = document.getElementById("filterMonth").value;
            const category = document.getElementById("filterCategory").value;
            const status = document.getElementById("filterStatus").value;
            const assignedTo = document.getElementById("filterAssignedTo").value;
            const shiftLead = document.getElementById("filterShiftLead").value;
            
            filteredIncidents = allIncidents.filter(incident => {
                if (year) {
                    const incidentYear = new Date(incident.Date).getFullYear();
                    if (incidentYear != year) return false;
                }
                if (month) {
                    const incidentMonth = new Date(incident.Date).getMonth() + 1;
                    if (incidentMonth != month) return false;
                }
                if (category && incident["Incident Category"] !== category) return false;
                if (status && incident.Status !== status) return false;
                if (assignedTo && incident["Assigned To"] !== assignedTo) return false;
                if (shiftLead && incident["Shift Lead"] !== shiftLead) return false;
                return true;
            });
            
            currentPage = 1;
            updateKPIs();
            updateCharts();
            renderTable();
        }
        
        function clearFilters() {
            document.getElementById("filterYear").value = "";
            document.getElementById("filterMonth").value = "";
            document.getElementById("filterCategory").value = "";
            document.getElementById("filterStatus").value = "";
            document.getElementById("filterAssignedTo").value = "";
            document.getElementById("filterShiftLead").value = "";
            applyFilters();
        }
        
        function updateKPIs() {
            const kpiSection = document.getElementById("kpiSection");
            kpiSection.innerHTML = "";
            
            const totalIncidents = filteredIncidents.length;
            const p1 = filteredIncidents.filter(i => i["Incident Category"] === "P1").length;
            const p2 = filteredIncidents.filter(i => i["Incident Category"] === "P2").length;
            const p3 = filteredIncidents.filter(i => i["Incident Category"] === "P3").length;
            const p4 = filteredIncidents.filter(i => i["Incident Category"] === "P4").length;
            
            const inProgress = filteredIncidents.filter(i => i.Status === "In Progress").length;
            const pending = filteredIncidents.filter(i => i.Status === "Pending").length;
            const completed = filteredIncidents.filter(i => i.Status === "Completed").length;
            
            const kpis = [
                { label: "Total Incidents", value: totalIncidents },
                { label: "P1 (Critical)", value: p1 },
                { label: "P2 (High)", value: p2 },
                { label: "P3 (Medium)", value: p3 },
                { label: "P4 (Low)", value: p4 },
                { label: "In Progress", value: inProgress },
                { label: "Pending", value: pending },
                { label: "Completed", value: completed }
            ];
            
            kpis.forEach(kpi => {
                const card = document.createElement("div");
                card.className = "kpi-card";
                card.innerHTML = `<div class="kpi-label">${kpi.label}</div><div class="kpi-value">${kpi.value}</div>`;
                kpiSection.appendChild(card);
            });
        }
        
        function updateCharts() {
            const categoryData = { P1: 0, P2: 0, P3: 0, P4: 0 };
            const statusData = { "In Progress": 0, "Pending": 0, "Completed": 0 };
            
            filteredIncidents.forEach(incident => {
                const cat = incident["Incident Category"];
                if (cat in categoryData) categoryData[cat]++;
                const stat = incident.Status;
                if (stat in statusData) statusData[stat]++;
            });
            
            const categoryCtx = document.getElementById("categoryChart").getContext("2d");
            if (categoryChart) categoryChart.destroy();
            categoryChart = new Chart(categoryCtx, {
                type: "bar",
                data: {
                    labels: ["P1", "P2", "P3", "P4"],
                    datasets: [{
                        label: "Incidents",
                        data: [categoryData.P1, categoryData.P2, categoryData.P3, categoryData.P4],
                        backgroundColor: ["#dc3545", "#fd7e14", "#ffc107", "#28a745"]
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
            
            const statusCtx = document.getElementById("statusChart").getContext("2d");
            if (statusChart) statusChart.destroy();
            statusChart = new Chart(statusCtx, {
                type: "pie",
                data: {
                    labels: ["In Progress", "Pending", "Completed"],
                    datasets: [{
                        data: [statusData["In Progress"], statusData["Pending"], statusData["Completed"]],
                        backgroundColor: ["#667eea", "#ffc107", "#28a745"]
                    }]
                },
                options: { responsive: true, maintainAspectRatio: true }
            });
        }
        
        function renderTable() {
            const tbody = document.getElementById("tableBody");
            tbody.innerHTML = "";
            
            const start = (currentPage - 1) * rowsPerPage;
            const end = start + rowsPerPage;
            const pageIncidents = filteredIncidents.slice(start, end);
            
            pageIncidents.forEach(incident => {
                const row = document.createElement("tr");
                row.onclick = () => showModal(incident);
                
                const categoryClass = `category-${incident["Incident Category"].toLowerCase()}`;
                row.innerHTML = `
                    <td>${incident.Date || "--"}</td>
                    <td>${incident.Shift || "--"}</td>
                    <td><span class="${categoryClass}">${incident["Incident Category"] || "--"}</span></td>
                    <td>${incident.Status || "--"}</td>
                    <td>${(incident.Alert || "").substring(0, 50)}...</td>
                    <td>${incident["Assigned To"] || "--"}</td>
                    <td>${incident["Shift Lead"] || "--"}</td>
                    <td>${incident.RITM || "--"}</td>
                `;
                tbody.appendChild(row);
            });
            
            document.getElementById("incidentCount").textContent = `${filteredIncidents.length} incidents`;
            renderPagination();
        }
        
        function renderPagination() {
            const pagination = document.getElementById("pagination");
            pagination.innerHTML = "";
            
            const totalPages = Math.ceil(filteredIncidents.length / rowsPerPage);
            
            for (let i = 1; i <= totalPages; i++) {
                const btn = document.createElement("button");
                btn.textContent = i;
                btn.className = i === currentPage ? "active" : "";
                btn.onclick = () => {
                    currentPage = i;
                    renderTable();
                };
                pagination.appendChild(btn);
            }
        }
        
        function sortTable(column) {
            if (sortColumn === column) {
                sortAscending = !sortAscending;
            } else {
                sortColumn = column;
                sortAscending = true;
            }
            
            const columns = ["Date", "Shift", "Incident Category", "Status", "Alert", "Assigned To", "Shift Lead", "RITM"];
            const columnName = columns[column];
            
            filteredIncidents.sort((a, b) => {
                let aVal = a[columnName] || "";
                let bVal = b[columnName] || "";
                
                if (aVal < bVal) return sortAscending ? -1 : 1;
                if (aVal > bVal) return sortAscending ? 1 : -1;
                return 0;
            });
            
            currentPage = 1;
            renderTable();
        }
        
        function showModal(incident) {
            const modal = document.getElementById("detailModal");
            const modalBody = document.getElementById("modalBody");
            
            let html = "";
            const sections = {
                "Basic Information": ["Date", "Shift", "Incident Category", "Shift Lead", "Time Slot"],
                "Incident Details": ["Alert Report Time", "Alert", "Assigned To", "Status"],
                "Reference Information": ["RITM", "STIP Incident", "Incident Raised"],
                "Communication": ["Email", "DB Giant", "Type Comms", "Incident Comms"],
                "Actions": ["Batch Reportable", "Final Comms", "CR", "Implementation"],
                "Verification": ["Verification", "Issue Communication", "Additional Task/Improvement"],
                "Metrics": ["Created At", "Completed At", "MTTR (minutes)"]
            };
            
            for (const [section, fields] of Object.entries(sections)) {
                html += `<div class="modal-section"><div class="modal-section-title">${section}</div><div class="modal-row">`;
                fields.forEach(field => {
                    const value = incident[field] || "--";
                    html += `<div class="modal-field"><div class="modal-label">${field}</div><div class="modal-value">${value}</div></div>`;
                });
                html += "</div></div>";
            }
            
            modalBody.innerHTML = html;
            modal.classList.add("active");
        }
        
        function closeModal() {
            document.getElementById("detailModal").classList.remove("active");
        }
    </script>
</body>
</html>'''

with open('templates/dashboard.html', 'w') as f:
    f.write(html)
print('✓ Dashboard.html created successfully')
