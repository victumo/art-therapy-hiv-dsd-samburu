import pandas as pd
import os

raw = r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw'

# 1. VL data from May 2023 onwards
print("=== VL DATA FROM MAY 2023 TO DATE ===")
df = pd.read_csv(os.path.join(raw, 'tujenge_jamii_vl.csv'))
df['Date Collected'] = pd.to_datetime(df['Date Collected'], format='%m/%d/%Y', errors='coerce')
recent = df[df['Date Collected'] >= '2023-05-01'].copy()
total_records = len(recent)
print(f"Total records from May 2023: {total_records}")
print(f"Date range: {recent['Date Collected'].min()} to {recent['Date Collected'].max()}")
print(f"Unique patients: {recent['CCC_NO'].nunique()}")

# AYP 10-25
ayp = recent[recent['Age'].between(10, 25)]
print(f"AYP 10-25 records: {len(ayp)} ({len(ayp)/total_records*100:.1f}%)")
print(f"AYP unique patients: {ayp['CCC_NO'].nunique()}")

# 2. Art cohort in the VL data
df_art = pd.read_excel(os.path.join(raw, 'art_cohort_attendees.xlsx'))
df_art['ccc'] = df_art['CCC_NO'].astype(str).str.strip()
art_ccc = set(df_art['ccc'].values)

df['ccc_str'] = df['CCC_NO'].astype(str).str.strip()
df['Cohort'] = df['ccc_str'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')
recent['ccc_str'] = recent['CCC_NO'].astype(str).str.strip()
recent['Cohort'] = recent['ccc_str'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')
ayp['ccc_str'] = ayp['CCC_NO'].astype(str).str.strip()
ayp['Cohort'] = ayp['ccc_str'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')

print(f"\nArt cohort records in VL data (May 2023+): {len(recent[recent['Cohort']=='Art'])}")
print(f"Art cohort in AYP 10-25: {len(ayp[ayp['Cohort']=='Art'])}")
print(f"Non-Art AYP 10-25: {len(ayp[ayp['Cohort']=='Non-Art'])}")

# 3. Top regimens in AYP
print("\n=== TOP REGIMENS IN AYP 10-25 ===")
print(ayp['Regimen'].value_counts().head(15))

# 4. Result distribution
print("\n=== RESULT DISTRIBUTION IN AYP 10-25 ===")
print(ayp['Result'].value_counts().head(20))

# 5. Gender in AYP
print("\n=== GENDER IN AYP 10-25 ===")
print(ayp['Gender'].value_counts())

# 6. Check 2024/2026 linelists for AYP 10-25
print("\n=== 2024 LINELIST - AYP 10-25 ===")
d24 = pd.read_excel(os.path.join(raw, 'active_art_may2024.xls'))
d24['ccc'] = d24['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
d24['Cohort'] = d24['ccc'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')
d24_ayp = d24[d24['Age at Reporting'].between(10, 25)]
print(f"Total: {len(d24)} | AYP 10-25: {len(d24_ayp)}")
print(f"Art in AYP: {len(d24_ayp[d24_ayp['Cohort']=='Art'])}")
print(f"Non-Art in AYP: {len(d24_ayp[d24_ayp['Cohort']=='Non-Art'])}")
print("Establishment in Art AYP:")
print(d24_ayp[d24_ayp['Cohort']=='Art']['Establishment'].value_counts())

print("\n=== 2026 LINELIST - AYP 10-25 ===")
d26 = pd.read_excel(os.path.join(raw, 'active_art_may2026.xls'))
d26['ccc'] = d26['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
d26['Cohort'] = d26['ccc'].apply(lambda x: 'Art' if x in art_ccc else 'Non-Art')
d26_ayp = d26[d26['Age at Reporting'].between(10, 25)]
print(f"Total: {len(d26)} | AYP 10-25: {len(d26_ayp)}")
print(f"Art in AYP: {len(d26_ayp[d26_ayp['Cohort']=='Art'])}")
print(f"Non-Art in AYP: {len(d26_ayp[d26_ayp['Cohort']=='Non-Art'])}")
print("Establishment in Art AYP:")
print(d26_ayp[d26_ayp['Cohort']=='Art']['Establishment'].value_counts())

print("\n=== 2026 Differentiated Care Models (AYP) ===")
print(d26_ayp['Differentiated Care Model'].value_counts())

print("\n=== 2026 Risk Categorization (AYP) ===")
print(d26_ayp['Risk Categorization'].value_counts())

print("\n=== 2026 Mental Health / NCDs (AYP) ===")
if 'NCDs' in d26_ayp.columns:
    print(d26_ayp['NCDs'].value_counts())
if 'AHD Client' in d26_ayp.columns:
    print(d26_ayp['AHD Client'].value_counts())
