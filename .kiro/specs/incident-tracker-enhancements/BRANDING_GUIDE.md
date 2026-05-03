# AI - SRE Alert Investigation Tracker - Branding Guide

## Project Identity

**Project Name:** AI - SRE Alert Investigation Tracker
**Industry:** Banking/Financial Institution
**Design Level:** Enterprise Grade
**Target Audience:** Financial Services Professionals

---

## Color Palette

### Primary Colors

| Color | Hex Code | RGB | Usage |
|-------|----------|-----|-------|
| Navy Blue (Dark) | #001F3F | 0, 31, 63 | Primary backgrounds, headers, borders |
| Navy Blue (Medium) | #003366 | 0, 51, 102 | Secondary elements, hover states |
| Navy Blue (Light) | #004080 | 0, 64, 128 | Accents, highlights |
| White | #FFFFFF | 255, 255, 255 | Main background, text on Navy |

### Status Colors

| Status | Color | Hex Code | RGB | Usage |
|--------|-------|----------|-----|-------|
| Success | Green | #28A745 | 40, 167, 69 | Completed, OK, Success |
| Critical | Red | #DC3545 | 220, 53, 69 | Error, Critical, SLA Breach |
| Warning | Yellow | #FFC107 | 255, 193, 7 | Warning, Caution, Pending |
| Info | Blue | #17A2B8 | 23, 162, 184 | Information, In Progress |

### Text Colors

| Element | Color | Hex Code | Usage |
|---------|-------|----------|-------|
| Primary Text | Navy Blue | #001F3F | Main content, headers |
| Secondary Text | Gray | #666666 | Secondary content, labels |
| Light Text | White | #FFFFFF | Text on Navy Blue backgrounds |
| Disabled Text | Light Gray | #CCCCCC | Disabled fields, inactive elements |

---

## Logo Specifications

### Logo Placement

**All Interfaces:** Form.html, Dashboard.html, Admin.html

```
┌─────────────────────────────────────────────────────────────┐
│ [LOGO]  AI - SRE Alert Investigation Tracker               │
│ (PNG)   Banking/Financial Institution Grade                │
│ 100x50px                                                    │
└─────────────────────────────────────────────────────────────┘
```

### Logo Requirements

- **Format:** PNG with transparency
- **Size:** 100x50px (recommended)
- **Location:** Top-left corner of all interfaces
- **Background:** Navy Blue (#001F3F)
- **Padding:** 10px from top and left edges
- **Alignment:** Left-aligned with title
- **Aspect Ratio:** 2:1 (width:height)

### Logo Placement in Code

```html
<!-- Header with Logo -->
<header class="navbar-banking">
  <div class="logo-container">
    <img src="logo.png" alt="AI - SRE Alert Investigation Tracker" 
         class="logo" width="100" height="50">
    <h1 class="project-title">AI - SRE Alert Investigation Tracker</h1>
  </div>
  <div class="header-right">
    <span class="connection-status">✓ Connected</span>
  </div>
</header>
```

### Logo CSS Styling

```css
.logo-container {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 10px 20px;
  background-color: #001F3F;
}

.logo {
  width: 100px;
  height: 50px;
  object-fit: contain;
}

.project-title {
  color: #FFFFFF;
  font-size: 18px;
  font-weight: 600;
  margin: 0;
}
```

---

## Typography

### Font Family
- **Primary:** System fonts (Arial, Helvetica, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif)
- **Fallback:** sans-serif

### Font Sizes

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| Page Title | 32px | Bold (600) | Navy Blue (#001F3F) |
| Section Title | 20px | Semi-bold (600) | Navy Blue (#001F3F) |
| Subsection | 16px | Semi-bold (600) | Navy Blue (#001F3F) |
| Body Text | 14px | Regular (400) | Navy Blue (#001F3F) |
| Small Text | 12px | Regular (400) | Gray (#666666) |
| Label | 13px | Semi-bold (500) | Navy Blue (#001F3F) |
| Button | 14px | Semi-bold (600) | White on Navy |

### Line Height
- **Headers:** 1.2
- **Body:** 1.5
- **Labels:** 1.4

---

## Component Styling

### Buttons

```css
/* Primary Button (Navy Blue) */
.btn-primary {
  background-color: #001F3F;
  color: #FFFFFF;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.btn-primary:hover {
  background-color: #003366;
}

/* Secondary Button (White with Navy Border) */
.btn-secondary {
  background-color: #FFFFFF;
  color: #001F3F;
  border: 2px solid #001F3F;
  padding: 10px 20px;
  border-radius: 4px;
  font-weight: 600;
  cursor: pointer;
}

.btn-secondary:hover {
  background-color: #F5F5F5;
}
```

### Cards

```css
.card {
  background-color: #FFFFFF;
  border-left: 4px solid #001F3F;
  border-radius: 6px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 31, 63, 0.1);
  transition: box-shadow 0.3s;
}

.card:hover {
  box-shadow: 0 4px 16px rgba(0, 31, 63, 0.15);
}
```

### Input Fields

```css
input[type="text"],
input[type="date"],
input[type="time"],
select,
textarea {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #003366;
  border-radius: 4px;
  font-size: 13px;
  font-family: inherit;
  background-color: #FFFFFF;
  color: #001F3F;
}

input:focus,
select:focus,
textarea:focus {
  outline: none;
  border-color: #001F3F;
  box-shadow: 0 0 0 3px rgba(0, 31, 63, 0.1);
}
```

### Headers

```css
.navbar-banking {
  background-color: #001F3F;
  color: #FFFFFF;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 8px rgba(0, 31, 63, 0.2);
}

.navbar-banking h1 {
  margin: 0;
  font-size: 20px;
  font-weight: 600;
}
```

---

## Layout & Spacing

### Spacing Scale
- **XS:** 4px
- **S:** 8px
- **M:** 16px
- **L:** 24px
- **XL:** 32px
- **XXL:** 48px

### Grid System
- **Base Unit:** 8px
- **Column Gap:** 16px
- **Row Gap:** 16px
- **Container Padding:** 20px

### Responsive Breakpoints
- **Mobile:** < 768px
- **Tablet:** 768px - 1024px
- **Desktop:** > 1024px

---

## Accessibility

### Color Contrast
- **Navy Blue (#001F3F) on White (#FFFFFF):** 13.5:1 ✅ WCAG AAA
- **Navy Blue (#003366) on White (#FFFFFF):** 11.2:1 ✅ WCAG AAA
- **White (#FFFFFF) on Navy Blue (#001F3F):** 13.5:1 ✅ WCAG AAA

### Font Sizes
- **Minimum:** 12px for body text
- **Recommended:** 14px for body text
- **Headers:** 16px or larger

### Keyboard Navigation
- All interactive elements must be keyboard accessible
- Tab order should be logical
- Focus indicators must be visible

### Screen Readers
- All images must have alt text
- Form labels must be associated with inputs
- Semantic HTML must be used

---

## Implementation Guidelines

### Header Template (All Interfaces)

```html
<header class="navbar-banking">
  <div class="logo-container">
    <img src="logo.png" alt="AI - SRE Alert Investigation Tracker" 
         class="logo" width="100" height="50">
    <h1 class="project-title">AI - SRE Alert Investigation Tracker</h1>
  </div>
  <div class="header-right">
    <span class="connection-status">✓ Connected</span>
    <span class="timestamp" id="currentTime">14:30:45</span>
  </div>
</header>
```

### CSS Variables (For Consistency)

```css
:root {
  /* Primary Colors */
  --navy-dark: #001F3F;
  --navy-medium: #003366;
  --navy-light: #004080;
  --white: #FFFFFF;
  --light-gray: #F5F5F5;
  
  /* Status Colors */
  --success: #28A745;
  --critical: #DC3545;
  --warning: #FFC107;
  --info: #17A2B8;
  
  /* Text Colors */
  --text-primary: #001F3F;
  --text-secondary: #666666;
  --text-light: #FFFFFF;
  --text-disabled: #CCCCCC;
  
  /* Spacing */
  --spacing-xs: 4px;
  --spacing-s: 8px;
  --spacing-m: 16px;
  --spacing-l: 24px;
  --spacing-xl: 32px;
  
  /* Shadows */
  --shadow-sm: 0 2px 8px rgba(0, 31, 63, 0.1);
  --shadow-md: 0 4px 16px rgba(0, 31, 63, 0.15);
  --shadow-lg: 0 8px 24px rgba(0, 31, 63, 0.2);
}
```

### Usage Example

```css
.card {
  background-color: var(--white);
  border-left: 4px solid var(--navy-dark);
  padding: var(--spacing-l);
  box-shadow: var(--shadow-sm);
}

.btn-primary {
  background-color: var(--navy-dark);
  color: var(--text-light);
  padding: var(--spacing-m) var(--spacing-l);
}
```

---

## Banking/Financial Institution Aesthetic

### Design Principles

1. **Trust & Security**
   - Navy Blue conveys stability, trust, and security
   - Professional appearance builds confidence
   - Clean design reduces cognitive load

2. **Professionalism**
   - Minimal, clean design with clear hierarchy
   - Consistent spacing and alignment
   - Enterprise-grade quality

3. **Clarity**
   - High contrast for readability
   - Clear visual hierarchy
   - Intuitive navigation

4. **Consistency**
   - Uniform styling across all interfaces
   - Consistent component behavior
   - Predictable user experience

5. **Enterprise Grade**
   - Suitable for financial institutions
   - Meets regulatory requirements
   - Professional appearance

### Visual Hierarchy

1. **Primary:** Navy Blue (#001F3F) - Main content, headers
2. **Secondary:** Navy Blue (#003366) - Secondary elements
3. **Tertiary:** Light Gray (#F5F5F5) - Backgrounds
4. **Accent:** Status colors - Success, warning, critical

### Spacing & Alignment

- **Consistent margins:** 16px, 24px, 32px
- **Consistent padding:** 12px, 16px, 20px
- **8px grid system** for alignment
- **Clear visual separation** between sections

---

## Quality Checklist

### Color & Branding
- [ ] Navy Blue (#001F3F) used as primary color
- [ ] White (#FFFFFF) used as background
- [ ] Logo placed at top-left corner (100x50px)
- [ ] Project title "AI - SRE Alert Investigation Tracker" displayed
- [ ] Status colors used correctly (green, red, yellow, blue)
- [ ] WCAG AA contrast compliance verified

### Typography
- [ ] Consistent font family (system fonts)
- [ ] Appropriate font sizes (12px minimum)
- [ ] Proper font weights (400, 500, 600)
- [ ] Line heights optimized for readability

### Components
- [ ] Buttons styled with Navy Blue
- [ ] Cards have Navy Blue left border
- [ ] Input fields have Navy Blue borders
- [ ] Headers have Navy Blue background
- [ ] Shadows are subtle and professional

### Layout
- [ ] Consistent spacing (8px grid)
- [ ] Responsive design verified
- [ ] Mobile layout tested
- [ ] Tablet layout tested
- [ ] Desktop layout tested

### Accessibility
- [ ] Color contrast verified (WCAG AA)
- [ ] Keyboard navigation works
- [ ] Screen reader compatible
- [ ] Focus indicators visible
- [ ] Alt text on images

---

## File References

### Logo File
- **Filename:** `logo.png`
- **Location:** Root directory or `/assets/` folder
- **Size:** 100x50px
- **Format:** PNG with transparency

### CSS Files
- **Main Stylesheet:** `styles.css` or `main.css`
- **Banking Theme:** `banking-theme.css`
- **Responsive:** `responsive.css`

### HTML Templates
- **Form:** `form.html`
- **Dashboard:** `dashboard.html`
- **Admin:** `admin.html`

---

## Deployment Checklist

Before deploying to production:

- [ ] Logo file (PNG) prepared and placed
- [ ] All CSS variables defined
- [ ] Color scheme applied to all interfaces
- [ ] Typography verified
- [ ] Spacing and alignment checked
- [ ] Responsive design tested
- [ ] Accessibility verified
- [ ] Cross-browser testing completed
- [ ] Performance optimized
- [ ] Security reviewed

---

## Support & Questions

For branding questions or clarifications:
1. Refer to this Branding Guide
2. Check FEATURE_OVERVIEW.md for visual examples
3. Review IMPLEMENTATION_GUIDE.md for technical details
4. Contact project manager for approval

---

**Branding Guide Version:** 1.0  
**Last Updated:** 2024-05-15  
**Status:** Ready for Implementation

