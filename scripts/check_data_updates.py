import pandas as pd, os
r = r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw'

# Check art cohort file - count of participants
a = pd.read_excel(os.path.join(r, 'art_cohort_attendees_atleast_3times_between_2024_to_2026.xlsx'))
print("=== ART COHORT FILE ===")
print(f"Shape: {a.shape[0]} rows x {a.shape[1]} cols")
print(f"Columns: {list(a.columns)}")
if 'First Name' in a.columns:
    # 🔒 Names are PII — count only, not printed
    print(f"Participants: {len(a)}")
if 'CCC_NO' in a.columns:
    a['ccc'] = a['CCC_NO'].astype(str).str.strip()
    art_ccc = set(a['ccc'].values)
    print(f"\nUnique CCC numbers: {len(art_ccc)}")

# Check VL data with AYP 10-24
v = pd.read_csv(os.path.join(r, 'vl_tests_may_2023_to_june_2026.csv'))
ccc_col = v.columns[2]
print(f"\n=== VL DATA ===")
print(f"Total records: {len(v)}")
v['Age'] = pd.to_numeric(v['Age'], errors='coerce')
v['ccc_str'] = v[ccc_col].astype(str).str.strip()
v['Cohort'] = v['ccc_str'].apply(lambda x: 'Painting' if x in art_ccc else 'Standard Care')

ayp = v[v['Age'].between(10, 24)]
print(f"AYP 10-24 records: {len(ayp)}")
print(f"  Painting cohort: {(ayp['Cohort']=='Painting').sum()}")
print(f"  Standard care:   {(ayp['Cohort']=='Standard Care').sum()}")
print(f"Unique patients in AYP: {ayp['ccc_str'].nunique()}")
print(f"Unique Painting in AYP: {ayp[ayp['Cohort']=='Painting']['ccc_str'].nunique()}")

# Check linelist
ll = pd.read_excel(os.path.join(r, 'active_art_may2026.xls'))
print(f"\n=== 2026 LINELIST ===")
print(f"Total records: {len(ll)}")
ll['ccc_str'] = ll['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
ll['Cohort'] = ll['ccc_str'].apply(lambda x: 'Painting' if x in art_ccc else 'Standard Care')
ll['Age'] = pd.to_numeric(ll['Age at Reporting'], errors='coerce')
ll_ayp = ll[ll['Age'].between(10, 24)]
print(f"AYP 10-24: {len(ll_ayp)}")
print(f"  Painting: {(ll_ayp['Cohort']=='Painting').sum()}")
print(f"  Standard care: {(ll_ayp['Cohort']=='Standard Care').sum()}")

# Establishment
print(f"\n=== ESTABLISHMENT (Painting Cohort, AYP 10-24) ===")
paint = ll_ayp[ll_ayp['Cohort'] == 'Painting']
print(paint['Establishment'].value_counts())
print(f"\n=== ESTABLISHMENT (Standard Care, AYP 10-24) ===")
sc = ll_ayp[ll_ayp['Cohort'] == 'Standard Care']
print(sc['Establishment'].value_counts())
