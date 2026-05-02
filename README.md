#  Werkstudent Job Market Tracker

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


### Application Tracker

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

### Salary Insights

**Bar chart — Average Salary by City:**
- X-axis: `City`
- Y-axis: Average of `Hourly Rate (€)`

**Bar chart — Average Salary by Category:**
- X-axis: `Category`
- Y-axis: Average of `Hourly Rate (€)`

**Tip:** Add a slicer for `Platform` so you can filter by LinkedIn vs Indeed etc.

---

##  Technologies USed

| Tool | Purpose |
|---|---|
| Python | Data cleaning and enrichment |
| pandas | Reading/writing Excel, data manipulation |
| openpyxl | Excel file handling |
| Power BI | Interactive dashboard |

