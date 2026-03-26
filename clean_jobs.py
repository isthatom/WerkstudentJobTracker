


#importing pandas
import pandas as pd

# step 1: Loading the raw data

print(" Loading jobs_raw.xlsx")


df = pd.read_excel("jobs_raw.xlsx")  # reads the data from the excel file and stores it in a dataframe (tables in panda just like excel) called df

print(f"   Loaded {len(df)} rows and {len(df.columns)} columns.")


# step 2 : Removing duplicates

before = len(df) # Stores the number of rows before removing duplicates.

# Drop any rows where Job Title AND Company are exactly the same
df = df.drop_duplicates(subset=["Job Title", "Company"])

after = len(df) # Stores the number of rows after removing duplicates.

print(f"  Removed {before - after} duplicate rows. {after} rows remaining.") # Simple subtraction.


# step 3: Strip whitespace from text columns to avoid issues with filtering in Power BI

# .str.strip() removes accidental spaces at the start or end of text 

df["Job Title"] = df["Job Title"].str.strip()
df["Company"]   = df["Company"].str.strip()
df["City"]      = df["City"].str.strip()  # For example: "  München " becomes "München"

print("  Stripped whitespace from text columns.")


# step 4: Standardize city names

# e.g. "Nuremberg" and "Nuernberg" should all be "Nürnberg"

city_corrections = {
    "Munich":    "München",
    "Nuremberg": "Nürnberg",
    "Nuernberg": "Nürnberg",
    "Frankfurt am Main": "Frankfurt",
}



df["City"] = df["City"].replace(city_corrections) # Actual city name corrections part
print("  Corrected city names.")


# step 5: Extract hourly rate from "Salary" column and create a new "Hourly Rate (€)" column

# The "Salary" column has values like "14 €/hr" or "Not listed" and we want to pull out the number 14.00 s a new column for easier analysis in Power BI.


def extract_hourly_rate(salary_text):
    
   # Pull the number out of a salary string like '14 €/hr'.
   
    if salary_text == "Not listed" or pd.isna(salary_text):
        return None                        # Returns nothing if no salary given
    # Split "14 €/hr" by space and taking the firts part into float
    return float(salary_text.split(" ")[0])

df["Hourly Rate (€)"] = df["Salary"].apply(extract_hourly_rate)  # .apply() to run the function on every ow of the Salary column so you dont need loops

listed_count = df["Hourly Rate (€)"].notna().sum()
print(f"  Extracted hourly rate for {listed_count} of {len(df)} listings.")


# step 6: To calculate when the jobs was posted using days posted and today's date.This tells you how recent each job posting is

# pd.Timestamp("today") used to get today's date.
df["Date Posted"] = pd.to_datetime(df["Date Posted"])   # Used to convet text to date.
df["Days Since Posted"] = (pd.Timestamp("today") - df["Date Posted"]).dt.days

print("  Calculated days since each job was posted.")


# step 7: Count the number of skills required for each job

def count_skills(skills_text): # We split by comma and count how many items there are
    """Count the number of skills in a comma-separated string."""
    if pd.isna(skills_text): #checks if empty or missing value and returns 0
        return 0
    return len(skills_text.split(","))    # Split by comma, count the pieces

df["Skill Count"] = df["Skills Required"].apply(count_skills) #function + apply again here

print("  Counted number of skills per job.")


# step 8: creating a new column "Applied? for filtering in PowerBi

# Simple yes/no column to make filtering in Power BI easier
# If status is "Applied" or "Interview", mark as Yes
df["Applied?"] = df["Status"].apply(
    lambda s: "Yes" if s in ["Applied", "Interview"] else "No"
)

print("  Added 'Applied?' column.")


# step 9: Sorting by newest

df = df.sort_values("Date Posted", ascending=False)

print("  Sorted by date (newest first).")


# step 10: Saving and storing the clean data in a new file

output_file = "jobs_clean.xlsx"
df.to_excel(output_file, index=False)   # index=False means don't add row numbers

print(f"\n Done! Clean data saved to: {output_file}")
print(f"   Rows: {len(df)}")
print(f"   Columns: {list(df.columns)}")

