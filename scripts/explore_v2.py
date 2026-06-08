import pandas as pd, os

r = r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw'

# Load VL data
v = pd.read_csv(os.path.join(r, 'vl_tests_may_2023_to_june_2026.csv'))
ccc_col = v.columns[2]  # 'Patient CCC No'
print("CCC column name:", ccc_col)
print("Shape:", v.shape)
print("Date range:", v['Date Collected'].min(), "-", v['Date Collected'].max())
v['Age'] = pd.to_numeric(v['Age'], errors='coerce')
print("Age range:", v['Age'].min(), "-", v['Age'].max())
print("Unique patients:", v[ccc_col].nunique())

# AYP 10-25
ayp = v[v['Age'].between(10, 25)].copy()
print("AYP 10-25 records:", len(ayp))
print("AYP unique patients:", ayp[ccc_col].nunique())

# Art cohort
a = pd.read_excel(os.path.join(r, 'art_cohort_attendees_atleast_3times_between_2024_to_2026.xlsx'))
a['ccc'] = a['CCC_NO'].astype(str).str.strip()
art_ccc = set(a['ccc'].values)
print("\nArt cohort participants:", len(art_ccc))

v['ccc_str'] = v[ccc_col].astype(str).str.strip()
v['Cohort'] = v['ccc_str'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')
ayp['ccc_str'] = ayp[ccc_col].astype(str).str.strip()
ayp['Cohort'] = ayp['ccc_str'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')

print("Art in VL:", (v['Cohort']=='Art').sum())
print("Art in AYP:", (ayp['Cohort']=='Art').sum())
print("Non-Art in AYP:", (ayp['Cohort']=='Non-Art').sum())

print("\n=== RESULTS (AYP ART) ===")
art_ayp = ayp[ayp['Cohort']=='Art']
print(art_ayp['Result'].value_counts())

print("\n=== RESULTS (AYP NON-ART) ===")
non_art_ayp = ayp[ayp['Cohort']=='Non-Art']
print(non_art_ayp['Result'].value_counts().head(20))

print("\n=== REGIMENS (AYP ART) ===")
print(art_ayp['Regimen'].value_counts())

print("\n=== GENDER (AYP) ===")
print("Art:", art_ayp['Gender'].value_counts().to_dict())
print("Non-Art:", non_art_ayp['Gender'].value_counts().to_dict())
