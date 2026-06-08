import pandas as pd

df_art = pd.read_excel(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\art_cohort_attendees.xlsx')
df_art['CCC_str'] = df_art['CCC_NO'].astype(str).str.strip()
art_ccc = set(df_art['CCC_str'].values)

# Use 2026 linelist
df = pd.read_excel(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\active_art_may2026.xls')
df['CCC_str'] = df['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
df['Cohort'] = df['CCC_str'].apply(lambda x: 'Art' if x in art_ccc else 'SC')

# All art cohort patients (any age)
art = df[df['Cohort'] == 'Art'].copy()

# Get Not Established
not_estab = art[art['Establishment'] == 'Not Established']

print("=== ART COHORT - NOT ESTABLISHED ===")
print()

header = f"{'Name':<25} {'CCC No':<15} {'Age':<5} {'Sex':<5} {'Last VL':<12} {'Risk':<12} {'Last Visit':<15}"
print(header)
print("-" * 90)

for _, r in not_estab.iterrows():
    name = str(r['Name'])
    ccc = r['CCC_str']
    age = str(r['Age at Reporting'])
    sex = r['Sex']
    vl = str(r['Last VL'])
    risk = str(r['Risk Categorization'])
    visit = str(r['Last Visit Date'])
    print(f"{name:<25} {ccc:<15} {age:<5} {sex:<5} {vl:<12} {risk:<12} {visit:<15}")

print()
print("=== ONLY THE 8 CCC NUMBERS (copy-paste ready) ===")
print()
for _, r in not_estab.iterrows():
    print(r['CCC_str'])
