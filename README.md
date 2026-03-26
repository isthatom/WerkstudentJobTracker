#  Werkstudent Job Market Tracker

A beginner-friendly data project that collects, cleans, and visualizes Werkstudent job postings using **Python** and **Power BI**.

---

##  Project Structure

```
WerkstudentJobTracker/
├── generate_sample_data.py   ← Creates sample data to get started immediately
├── clean_jobs.py             ← Cleans and enriches the raw Excel file
├── jobs_raw.xlsx             ← Raw data (you fill this with real jobs)
├── jobs_clean.xlsx           ← Output: ready for Power BI
└── README.md
```

---

##  How to Run

### Step 1 : Install Python libraries

Open your terminal and run:

```bash
pip install pandas openpyxl
```

### Step 2 : Generate sample data (or use your own)

```bash
python generate_sample_data.py
```

This creates `jobs_raw.xlsx` with 80 realistic job postings so you can build the dashboard immediately.

**To use real data instead:** Open `jobs_raw.xlsx` and fill in jobs you find on LinkedIn, Indeed, or StepStone. Keep the same column names.

### Step 3 : Clean the data

```bash
python clean_jobs.py
```

This produces `jobs_clean.xlsx` — the file you load into Power BI.

---

##  Power BI Dashboard 

### Load the data

1. Open **Power BI Desktop**
2. Click **Home → Get Data → Excel Workbook**
3. Select `jobs_clean.xlsx`
4. Check the table checkbox → click **Load**

---

### Page 1: Overview

**Cards (KPI tiles) — drag "Card" visual onto canvas:**
- Total Jobs → field: `Job Title` (Count)
- Jobs Applied → field: `Applied?` filtered to "Yes" (Count)
- Avg Hourly Rate → field: `Hourly Rate (€)` (Average)

**Bar chart — Jobs by City:**
- Visual: Clustered Bar Chart
- Y-axis: `City`
- X-axis: `Job Title` (Count)
- Sort descending

**Donut chart — Jobs by Category:**
- Visual: Donut Chart
- Legend: `Category`
- Values: `Job Title` (Count)

---

### Page 2: Skills Analysis

**Bar chart — Most In-Demand Skills:**

First, you need to split the skills column. In Power BI:

1. Go to **Transform Data (Power Query)**
2. Select the `Skills Required` column
3. Click **Split Column → By Delimiter** → use `, ` (comma space)
4. Then **Unpivot** the resulting columns
5. Rename the value column to `Skill`
6. Click **Close & Apply**

Now build:
- Visual: Bar Chart
- Y-axis: `Skill`
- X-axis: Count of `Skill`
- Sort descending → shows Python, SQL, Excel etc. ranked

---

### Page 3: Application Tracker

**Table visual:**
- Columns: `Job Title`, `Company`, `City`, `Status`, `Date Posted`, `Hourly Rate (€)`
- Add conditional formatting on `Status`:
  - Applied → Blue
  - Interview → Green
  - Rejected → Red

**Slicer — filter by Status:**
- Visual: Slicer
- Field: `Status`

**Line chart — Postings over time:**
- X-axis: `Date Posted` (by week)
- Y-axis: Count of `Job Title`

---

### Page 4: Salary Insights

**Bar chart — Average Salary by City:**
- X-axis: `City`
- Y-axis: Average of `Hourly Rate (€)`

**Bar chart — Average Salary by Category:**
- X-axis: `Category`
- Y-axis: Average of `Hourly Rate (€)`

**Tip:** Add a slicer for `Platform` so you can filter by LinkedIn vs Indeed etc.

---

##  Technologies

| Tool | Purpose |
|---|---|
| Python | Data cleaning and enrichment |
| pandas | Reading/writing Excel, data manipulation |
| openpyxl | Excel file handling |
| Power BI | Interactive dashboard |

---

##  Skills Demonstrated

- Data wrangling with Python and pandas
- ETL pipeline (Extract → Transform → Load)
- Data visualization in Power BI
- Excel data management
- Git / GitHub version control
