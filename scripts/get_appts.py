import pandas as pd

not_estab_ccc = ['1512601276', '1512600831', '1512602218', '1512602540', 
                 '1512600522', '1512602890', '1512602968', '2008900093']

df = pd.read_excel(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\active_art_may2026.xls')
df['CCC_str'] = df['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
p = df[df['CCC_str'].isin(not_estab_ccc)].copy()

print(f"{'Name':<22} {'Last VL':<10} {'VL Date':<14} {'Last Visit':<14} {'Next Appt':<14} {'Rx':<5} {'Risk'}")
print("=" * 95)
for _, r in p.iterrows():
    name = str(r['Name'])[:22]
    vl = str(r['Last VL'])
    vl_date = str(r['Last VL Date'])
    visit = str(r['Last Visit Date'])
    appt = str(r['Next Appointment Date'])
    rx = str(r['Months Of Prescription'])
    risk = str(r['Risk Categorization'])
    print(f"{name:<22} {vl:<10} {vl_date:<14} {visit:<14} {appt:<14} {rx:<5} {risk}")
