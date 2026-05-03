#!/usr/bin/env python3
"""
AI - SRE Alert Investigation Tracker - File Generator
Generates dashboard.html, admin.html, and migration script
"""

import os
import json
from datetime import datetime
import shutil

def create_dashboard_html():
    """Create comprehensive dashboard.html"""
    dashboard_code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI - SRE Alert Investigation Tracker - Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.9.1/dist/chart.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
            background: linear-gradient(135deg, #001F3F 0%, #003366 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .navbar {
            background: linear-gradient(135deg, #001F3F 0%, #003366 100%);
            color: white;
            padding: 15px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0, 31, 63, 0.2);
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }
        .logo-container {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .logo-placeholder {
            width: 100px;
            height: 50px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px dashed rgba(255, 255, 255, 0.3);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 11px;
            color: rgba(255, 255, 255, 0.5);
        }
        .navbar h1 { font-size: 18px; font-weight: 600; margin: 0; }
        .navbar-right { display: flex; gap: 20px; align-items: center; font-size: 13px; }
        .status-indicator { display: flex; align-items: center; gap: 8px; }
        .dot { width: 10px; height: 10px; border-radius: 50%; background: #28A745; animation: pulse 2s infinite; }
        @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
        .controls {
            max-width: 1400px;
            margin: 0 auto 20px;
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }
        input[type="date"], select {
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 13px;
            background: white;
            cursor: pointer;
        }
        input[type="date"]:focus, select:focus {
            outline: none;
            border-color: #001F3F;
            box-shadow: 0 0 0 3px rgba(0, 31, 63, 0.1);
        }
        .btn-refresh {
            padding: 8px 16px;
            background: #001F3F;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 13px;
        }
        .btn-refresh:hover { background: #003366; }
        .btn-export {
            padding: 8px 16px;
            background: #28A745;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            font-size: 13px;
        }
        .btn-export:hover { background: #229954; }
        .dashboard {
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }
        .metric-card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            border-left: 4px solid #001F3F;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }
        .metric-label { font-size: 12px; color: #999; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
        .metric-value { font-size: 28px; font-weight: bold; color: #001F3F; }
        .metric-card.success { border-left-color: #28A745; }
        .metric-card.danger { border-left-color: #DC3545; }
        .chart-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .chart-container h3 { color: #001F3F; margin-bottom: 15px; }
        table { width: 100%; border-collapse: collapse; }
        thead { background: #001F3F; color: white; }
        th { padding: 12px; text-align: left; cursor: pointer; border-right: 1px solid #ddd; }
        td { padding: 12px; border-bottom: 1px solid #ddd; border-right: 1px solid #ddd; }
        tr:hover { background: #f5f5f5; }
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 1000; overflow-y: auto; }
        .modal-content { background: white; margin: 20px auto; max-width: 800px; border-radius: 8px; box-shadow: 0 4px 16px rgba(0,0,0,0.2); }
        .modal-header { background: linear-gradient(135deg, #001F3F 0%, #003366 100%); color: white; padding: 20px; display: flex; justify-content: space-between; align-items: center; border-radius: 8px 8px 0 0; }
        .modal-body { padding: 20px; max-height: 600px; overflow-y: auto; }
        .modal-footer { padding: 20px; border-top: 1px solid #ddd; display: flex; gap: 10px; justify-content: flex-end; }
        @media (max-width: 768px) {
            .controls { flex-direction: column; }
            input[type="date"], select { width: 100%; }
            table { font-size: 12px; }
            th, td { padding: 8px; }
        }
    </style>
</head>
<body>
    <div class="navbar">
        <div class="logo-container">
            <div class="logo-placeholder">LOGO</div>
            <h1>AI - SRE Alert Investigation Tracker</h1>
        </div>
        <div class="navbar-right">
            <div class="status-indicator">
                <div class="dot"></div>
                <span id="status">Connecting...</span>
            </div>
            <span id="currentTime">--:--:--</span>
        </div>
    </div>
    
    <div class="controls">
        <select id="filterYear"><option value="">All Years</option></select>
        <select id="filterMonth"><option value="">All Months</option><option value="1">January</option><option value="2">February</option><option value="3">March</option><option value="4">April</option><option value="5">May</option><option value="6">June</option><option value="7">July</option><option value="8">August</option><option value="9">September</option><option value="10">October</option><option value="11">November</option><option value="12">December</option></select>
        <input type="date" id="filterDate">
        <select id="filterPerson"><option value="">All Persons</option></select>
        <select id="filterShiftLead"><option value="">All Shift Leads</option></select>
        <select id="filterShift"><option value="">All Shifts</option><option value="S1">S1</option><option value="S2">S2</option><option value="On Call">On Call</option></select>
        <select id="filterStatus"><option value="">All Statuses</option><option value="In Progress">In Progress</option><option value="Pending">Pending</option><option value="Completed">Completed</option></select>
        <select id="filterCategory"><option value="">All Categories</option><option value="P1">P1</option><option value="P2">P2</option><option value="P3">P3</option><option value="P4">P4</option></select>
        <button class="btn-refresh" onclick="refreshData()">🔄 Refresh</button>
        <button class="btn-refresh" onclick="clearAllFilters()" style="background: #DC3545;">✕ Clear All</button>
        <button class="btn-export" onclick="exportToCSV()">📥 Export CSV</button>
        <span id="filterCount" style="color: white; font-size: 13px; padding: 8px 12px;">Incidents: 0</span>
    </div>
    
    <div class="dashboard" id="metrics">
        <div class="metric-card">
            <div class="metric-label">Total Incidents</div>
            <div class="metric-value" id="totalIncidents">0</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">P1 | P2 | P3 | P4</div>
            <div class="metric-value" id="categoryBreakdown">0|0|0|0</div>
        </div>
        <div class="metric-card">
            <div class="metric-label">In Progress | Pending | Completed</div>
            <div class="metric-value" id="statusBreakdown">0|0|0</div>
        </div>
        <div class="metric-card success">
            <div class="metric-label">Average MTTR</div>
            <div class="metric-value" id="avgMTTR">--</div>
        </div>
        <div class="metric-card danger">
            <div class="metric-label">SLA Breaches</div>
            <div class="metric-value" id="slaBreaches">0</div>
        </div>
    </div>
    
    <div style="max-width: 1400px; margin: 30px auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 20px;">
        <div class="chart-container"><h3>Incidents by Category</h3><canvas id="categoryChart"></canvas></div>
        <div class="chart-container"><h3>Status Distribution</h3><canvas id="statusChart"></canvas></div>
        <div class="chart-container"><h3>Incident Trends (30 Days)</h3><canvas id="trendsChart"></canvas></div>
        <div class="chart-container"><h3>MTTR Trend (30 Days)</h3><canvas id="mttrChart"></canvas></div>
    </div>
    
    <div style="max-width: 1400px; margin: 30px auto;">
        <div style="background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.05);">
            <table id="incidentsTable">
                <thead>
                    <tr>
                        <th onclick="sortTable('Date')">Date ↕</th>
                        <th onclick="sortTable('Shift')">Shift ↕</th>
                        <th onclick="sortTable('Incident Category')">Category ↕</th>
                        <th onclick="sortTable('Status')">Status ↕</th>
                        <th onclick="sortTable('Alert')">Alert ↕</th>
                        <th onclick="sortTable('Assigned To')">Assigned To ↕</th>
                        <th onclick="sortTable('Shift Lead')">Shift Lead ↕</th>
                        <th onclick="sortTable('RITM')">RITM ↕</th>
                        <th onclick="sortTable('Alert Report Time')">Time ↕</th>
                        <th>SLA Status</th>
                    </tr>
                </thead>
                <tbody id="tableBody"><tr><td colspan="10" style="text-align: center; color: #999;">Loading...</td></tr></tbody>
            </table>
        </div>
        <div style="margin-top: 15px; display: flex; justify-content: center; gap: 10px;" id="pagination"></div>
    </div>
    
    <div id="detailModal" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>Incident Details</h2>
                <button onclick="closeModal()" style="background: none; border: none; color: white; font-size: 24px; cursor: pointer;">✕</button>
            </div>
            <div id="modalContent" class="modal-body"></div>
            <div class="modal-footer">
                <button onclick="printIncident()" style="padding: 10px 20px; background: #001F3F; color: white; border: none; border-radius: 6px; cursor: pointer;">🖨️ Print</button>
                <button onclick="closeModal()" style="padding: 10px 20px; background: #DC3545; color: white; border: none; border-radius: 6px; cursor: pointer;">Close</button>
            </div>
        </div>
    </div>
    
    <script>
        let allIncidents = [];
        let filteredIncidents = [];
        let currentPage = 1;
        const rowsPerPage = 25;
        let sortColumn = 'Date';
        let sortOrder = 'desc';
        let charts = {};
        const SLA_TIMES = { 'P1': 5, 'P2': 10, 'P3': 15, 'P4': 30 };
        
        document.addEventListener('DOMContentLoaded', () => {
            setDefaultDate();
            setupEventListeners();
            loadIncidents();
            setupAutoRefresh();
            updateClock();
            setInterval(updateClock, 1000);
        });
        
        function setDefaultDate() {
            const today = new Date().toISOString().split('T')[0];
            document.getElementById('filterDate').value = today;
        }
        
        function setupEventListeners() {
            ['filterYear', 'filterMonth', 'filterDate', 'filterPerson', 'filterShiftLead', 'filterShift', 'filterStatus', 'filterCategory'].forEach(id => {
                document.getElementById(id).addEventListener('change', applyFilters);
            });
        }
        
        async function loadIncidents() {
            try {
                const response = await fetch('http://localhost:5000/api/incidents');
                const data = await response.json();
                allIncidents = data.incidents || [];
                populateFilterDropdowns();
                applyFilters();
                updateStatus('connected');
            } catch (error) {
                console.error('Error loading incidents:', error);
                updateStatus('error');
            }
        }
        
        function populateFilterDropdowns() {
            const years = new Set();
            const persons = new Set();
            const shiftLeads = new Set();
            
            allIncidents.forEach(i => {
                if (i['Date']) years.add(new Date(i['Date']).getFullYear());
                if (i['Assigned To']) persons.add(i['Assigned To']);
                if (i['Shift Lead']) shiftLeads.add(i['Shift Lead']);
            });
            
            const yearSelect = document.getElementById('filterYear');
            [...years].sort((a, b) => b - a).forEach(year => {
                const option = document.createElement('option');
                option.value = year;
                option.textContent = year;
                yearSelect.appendChild(option);
            });
            
            const personSelect = document.getElementById('filterPerson');
            [...persons].sort().forEach(person => {
                const option = document.createElement('option');
                option.value = person;
                option.textContent = person;
                personSelect.appendChild(option);
            });
            
            const leadSelect = document.getElementById('filterShiftLead');
            [...shiftLeads].sort().forEach(lead => {
                const option = document.createElement('option');
                option.value = lead;
                option.textContent = lead;
                leadSelect.appendChild(option);
            });
        }
        
        function applyFilters() {
            let filtered = [...allIncidents];
            
            const year = document.getElementById('filterYear').value;
            const month = document.getElementById('filterMonth').value;
            const date = document.getElementById('filterDate').value;
            const person = document.getElementById('filterPerson').value;
            const shiftLead = document.getElementById('filterShiftLead').value;
            const shift = document.getElementById('filterShift').value;
            const status = document.getElementById('filterStatus').value;
            const category = document.getElementById('filterCategory').value;
            
            if (year) filtered = filtered.filter(i => new Date(i['Date']).getFullYear() == year);
            if (month) filtered = filtered.filter(i => new Date(i['Date']).getMonth() + 1 == month);
            if (date) filtered = filtered.filter(i => i['Date'] === date);
            if (person) filtered = filtered.filter(i => i['Assigned To'] === person);
            if (shiftLead) filtered = filtered.filter(i => i['Shift Lead'] === shiftLead);
            if (shift) filtered = filtered.filter(i => i['Shift'] === shift);
            if (status) filtered = filtered.filter(i => i['Status'] === status);
            if (category) filtered = filtered.filter(i => i['Incident Category'] === category);
            
            filteredIncidents = filtered;
            currentPage = 1;
            updateMetrics();
            updateCharts();
            renderTable();
            document.getElementById('filterCount').textContent = `Incidents: ${filtered.length}`;
        }
        
        function updateMetrics() {
            const total = filteredIncidents.length;
            const p1 = filteredIncidents.filter(i => i['Incident Category'] === 'P1').length;
            const p2 = filteredIncidents.filter(i => i['Incident Category'] === 'P2').length;
            const p3 = filteredIncidents.filter(i => i['Incident Category'] === 'P3').length;
            const p4 = filteredIncidents.filter(i => i['Incident Category'] === 'P4').length;
            const inProgress = filteredIncidents.filter(i => i['Status'] === 'In Progress').length;
            const pending = filteredIncidents.filter(i => i['Status'] === 'Pending').length;
            const completed = filteredIncidents.filter(i => i['Status'] === 'Completed').length;
            const breaches = filteredIncidents.filter(i => calculateSLA(i).class === 'overdue').length;
            
            document.getElementById('totalIncidents').textContent = total;
            document.getElementById('categoryBreakdown').textContent = `${p1}|${p2}|${p3}|${p4}`;
            document.getElementById('statusBreakdown').textContent = `${inProgress}|${pending}|${completed}`;
            document.getElementById('slaBreaches').textContent = breaches;
            
            const mttrValues = filteredIncidents
                .filter(i => i['Status'] === 'Completed' && i['Created At'] && i['Completed At'])
                .map(i => {
                    const created = new Date(i['Created At']);
                    const completed = new Date(i['Completed At']);
                    return Math.floor((completed - created) / 60000);
                });
            
            if (mttrValues.length > 0) {
                const avgMTTR = Math.floor(mttrValues.reduce((a, b) => a + b) / mttrValues.length);
                const hours = Math.floor(avgMTTR / 60);
                const mins = avgMTTR % 60;
                document.getElementById('avgMTTR').textContent = hours > 0 ? `${hours}h ${mins}m` : `${mins}m`;
            } else {
                document.getElementById('avgMTTR').textContent = '--';
            }
        }
        
        function updateCharts() {
            const categories = { 'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0 };
            filteredIncidents.forEach(i => {
                if (categories.hasOwnProperty(i['Incident Category'])) {
                    categories[i['Incident Category']]++;
                }
            });
            
            if (charts.category) charts.category.destroy();
            const categoryCtx = document.getElementById('categoryChart').getContext('2d');
            charts.category = new Chart(categoryCtx, {
                type: 'bar',
                data: {
                    labels: ['P1', 'P2', 'P3', 'P4'],
                    datasets: [{
                        label: 'Incidents',
                        data: [categories.P1, categories.P2, categories.P3, categories.P4],
                        backgroundColor: ['#DC3545', '#FFC107', '#17A2B8', '#28A745']
                    }]
                },
                options: { responsive: true, plugins: { legend: { display: false } } }
            });
            
            const statuses = { 'In Progress': 0, 'Pending': 0, 'Completed': 0 };
            filteredIncidents.forEach(i => {
                if (statuses.hasOwnProperty(i['Status'])) {
                    statuses[i['Status']]++;
                }
            });
            
            if (charts.status) charts.status.destroy();
            const statusCtx = document.getElementById('statusChart').getContext('2d');
            charts.status = new Chart(statusCtx, {
                type: 'pie',
                data: {
                    labels: ['In Progress', 'Pending', 'Completed'],
                    datasets: [{
                        data: [statuses['In Progress'], statuses['Pending'], statuses['Completed']],
                        backgroundColor: ['#17A2B8', '#FFC107', '#28A745']
                    }]
                },
                options: { responsive: true }
            });
            
            const last30Days = {};
            const today = new Date();
            for (let i = 29; i >= 0; i--) {
                const date = new Date(today);
                date.setDate(date.getDate() - i);
                const dateStr = date.toISOString().split('T')[0];
                last30Days[dateStr] = 0;
            }
            
            filteredIncidents.forEach(i => {
                if (i['Date'] && last30Days.hasOwnProperty(i['Date'])) {
                    last30Days[i['Date']]++;
                }
            });
            
            if (charts.trends) charts.trends.destroy();
            const trendsCtx = document.getElementById('trendsChart').getContext('2d');
            charts.trends = new Chart(trendsCtx, {
                type: 'line',
                data: {
                    labels: Object.keys(last30Days),
                    datasets: [{
                        label: 'Incidents',
                        data: Object.values(last30Days),
                        borderColor: '#001F3F',
                        backgroundColor: 'rgba(0, 31, 63, 0.1)',
                        tension: 0.4
                    }]
                },
                options: { responsive: true, plugins: { legend: { display: false } } }
            });
            
            const mttrByDate = {};
            filteredIncidents.forEach(i => {
                if (i['Status'] === 'Completed' && i['Created At'] && i['Completed At']) {
                    const created = new Date(i['Created At']);
                    const completed = new Date(i['Completed At']);
                    const mttr = Math.floor((completed - created) / 60000);
                    const dateStr = completed.toISOString().split('T')[0];
                    if (!mttrByDate[dateStr]) mttrByDate[dateStr] = [];
                    mttrByDate[dateStr].push(mttr);
                }
            });
            
            const mttrData = {};
            for (let i = 29; i >= 0; i--) {
                const date = new Date(today);
                date.setDate(date.getDate() - i);
                const dateStr = date.toISOString().split('T')[0];
                if (mttrByDate[dateStr]) {
                    mttrData[dateStr] = Math.floor(mttrByDate[dateStr].reduce((a, b) => a + b) / mttrByDate[dateStr].length);
                } else {
                    mttrData[dateStr] = 0;
                }
            }
            
            if (charts.mttr) charts.mttr.destroy();
            const mttrCtx = document.getElementById('mttrChart').getContext('2d');
            charts.mttr = new Chart(mttrCtx, {
                type: 'line',
                data: {
                    labels: Object.keys(mttrData),
                    datasets: [{
                        label: 'Avg MTTR (minutes)',
                        data: Object.values(mttrData),
                        borderColor: '#28A745',
                        backgroundColor: 'rgba(40, 167, 69, 0.1)',
                        tension: 0.4
                    }]
                },
                options: { responsive: true, plugins: { legend: { display: false } } }
            });
        }
        
        function renderTable() {
            const tbody = document.getElementById('tableBody');
            const start = (currentPage - 1) * rowsPerPage;
            const end = start + rowsPerPage;
            const pageData = filteredIncidents.slice(start, end);
            
            tbody.innerHTML = pageData.map(incident => {
                const sla = calculateSLA(incident);
                const slaColor = sla.class === 'overdue' ? '#f8d7da' : sla.class === 'warning' ? '#fff3cd' : '#d4edda';
                return `
                    <tr onclick="showModal('${incident._row_number}')" style="cursor: pointer; background: ${slaColor};">
                        <td>${incident['Date'] || '--'}</td>
                        <td>${incident['Shift'] || '--'}</td>
                        <td><span style="background: #001F3F; color: white; padding: 4px 8px; border-radius: 4px;">${incident['Incident Category'] || '--'}</span></td>
                        <td>${incident['Status'] || '--'}</td>
                        <td style="max-width: 150px; overflow: hidden; text-overflow: ellipsis;">${incident['Alert'] || '--'}</td>
                        <td>${incident['Assigned To'] || '--'}</td>
                        <td>${incident['Shift Lead'] || '--'}</td>
                        <td>${incident['RITM'] || '--'}</td>
                        <td>${incident['Alert Report Time'] || '--'}</td>
                        <td>${sla.text}</td>
                    </tr>
                `;
            }).join('');
            
            const totalPages = Math.ceil(filteredIncidents.length / rowsPerPage);
            const pagination = document.getElementById('pagination');
            pagination.innerHTML = '';
            
            for (let i = 1; i <= totalPages; i++) {
                const btn = document.createElement('button');
                btn.textContent = i;
                btn.style.cssText = `padding: 8px 12px; background: ${i === currentPage ? '#001F3F' : '#ddd'}; color: ${i === currentPage ? 'white' : '#001F3F'}; border: none; border-radius: 4px; cursor: pointer;`;
                btn.onclick = () => { currentPage = i; renderTable(); };
                pagination.appendChild(btn);
            }
        }
        
        function sortTable(column) {
            if (sortColumn === column) {
                sortOrder = sortOrder === 'asc' ? 'desc' : 'asc';
            } else {
                sortColumn = column;
                sortOrder = 'asc';
            }
            
            filteredIncidents.sort((a, b) => {
                const aVal = a[column] || '';
                const bVal = b[column] || '';
                const comparison = aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
                return sortOrder === 'asc' ? comparison : -comparison;
            });
            
            currentPage = 1;
            renderTable();
        }
        
        function calculateSLA(incident) {
            try {
                const category = incident['Incident Category'] || 'P4';
                const slaTarget = SLA_TIMES[category] || 30;
                const incidentTime = new Date(`${incident['Date']}T${incident['Alert Report Time']}`);
                const now = new Date();
                const diffMins = Math.floor((now - incidentTime) / 60000);
                
                if (diffMins > slaTarget) {
                    return { text: `🚨 BREACHED (${diffMins - slaTarget}m)`, class: 'overdue' };
                } else if (diffMins > slaTarget * 0.8) {
                    return { text: `⚠️ ${slaTarget - diffMins}m left`, class: 'warning' };
                } else {
                    return { text: `✓ ${slaTarget - diffMins}m left`, class: 'on-track' };
                }
            } catch (e) {
                return { text: '--', class: 'on-track' };
            }
        }
        
        function showModal(rowNumber) {
            const incident = allIncidents.find(i => i._row_number == rowNumber);
            if (!incident) return;
            
            const sections = {
                'Basic Information': ['Date', 'Shift', 'Time Slot', 'Incident Category', 'Shift Lead'],
                'Incident Details': ['Alert Report Time', 'Alert', 'Assigned To', '
