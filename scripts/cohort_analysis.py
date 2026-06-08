import pandas as pd
import numpy as np

# Load art cohort
df_art = pd.read_excel(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\art_cohort_attendees.xlsx')
df_art['CCC_str'] = df_art['CCC_NO'].astype(str).str.strip()
art_ccc = set(df_art['CCC_str'].values)

def analyze(filepath, year_label):
    df = pd.read_excel(filepath)
    df['CCC_str'] = df['CCC_No'].apply(lambda x: str(int(float(x))) if pd.notna(x) else '')
    df['Cohort'] = df['CCC_str'].apply(lambda x: 'Art' if x in art_ccc else 'SC')
    df_adol = df[df['Age at Reporting'].between(10, 24)].copy()
    
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"{year_label} SNAPSHOT - Ages 10-24 Only")
    print(sep)
    
    for cohort in ['Art', 'SC']:
        cd = df_adol[df_adol['Cohort'] == cohort]
        n = len(cd)
        label = 'Art Cohort' if cohort == 'Art' else 'Standard Care'
        print(f"\n--- {label} (n={n}) ---")
        
        estab = cd['Establishment'].value_counts()
        e_count = estab.get("Established", 0)
        ne_count = estab.get("Not Established", 0)
        print(f"  Established: {e_count} ({e_count/n*100:.1f}%)")
        print(f"  Not Established: {ne_count} ({ne_count/n*100:.1f}%)")
        
        valid_vl = cd[cd['Last VL'].notna()]
        suppressed = (valid_vl['Last VL'].astype(str).str.strip() == '0').sum()
        tvl = len(valid_vl)
        if tvl > 0:
            print(f"  VL=0 (suppressed): {suppressed}/{tvl} ({suppressed/tvl*100:.1f}%)")
        else:
            print(f"  No valid VLs")
        
        # Also show VL <200 using our function logic
        def is_suppressed(v):
            if pd.isna(v):
                return False
            s = str(v).strip().lower()
            if s in ['< ldl copies/ml', '<40 copies/ml', 'ldl', '< 40 copies/ ml', '0']:
                return True
            try:
                return float(s.replace(',', '')) < 200
            except:
                return False
        
        suppressed_all = sum(valid_vl['Last VL'].apply(is_suppressed))
        print(f"  VL <200 (all suppressed): {suppressed_all}/{tvl} ({suppressed_all/tvl*100:.1f}%)")
        
        risk = cd['Risk Categorization'].value_counts()
        print(f"  Risk - High:{risk.get('High Risk',0)} Med:{risk.get('Medium Risk',0)} Low:{risk.get('Low Risk',0)}")
        
        print(f"  Age range: {cd['Age at Reporting'].min()} - {cd['Age at Reporting'].max()}")
        print(f"  Sex - M:{len(cd[cd['Sex']=='M'])} F:{len(cd[cd['Sex']=='F'])}")
        
        visit_dates = pd.to_datetime(cd['Last Visit Date'], dayfirst=True, errors='coerce')
        cutoff = pd.Timestamp('2023-12-01') if year_label == '2024' else pd.Timestamp('2025-12-01')
        retained = (visit_dates >= cutoff).sum()
        print(f"  Retained (visit <=6mo): {retained}/{n} ({retained/n*100:.1f}%)")

analyze(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\active_art_may2024.xls', '2024')
analyze(r'C:\Users\victu\Documents\Painting Classes Data Analyis\data\raw\active_art_may2026.xls', '2026')
