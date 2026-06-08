import json
path = r'C:\Users\victu\Documents\Painting Classes Data Analyis\networks\samburu_art_therapy_dsd_model.ipynb'
with open(path, 'r', encoding='utf-8') as f:
    nb = json.load(f)
all_src = ''.join([''.join(c['source']) for c in nb['cells']])

print("=== VERIFICATION ===")
print(f"AYP 10-24:      {'OK' if '10-24' in all_src else 'FAIL'}")
print(f"AYP 10-25 gone: {'OK' if '10-25' not in all_src else 'FAIL - still present'}")
print(f"Painting cohort: {'OK' if 'Painting' in all_src else 'FAIL'}")
print(f"Standard Care:   {'OK' if 'Standard Care' in all_src else 'FAIL'}")
art_count = all_src.count("'Art'")
sc_count = all_src.count("Standard Care")
paint_count = all_src.count("Painting")
print(f"Old Art label:   {'OK (0)' if art_count == 0 else 'WARN: found ' + str(art_count)}")
print(f"Non-Art removed: {'OK' if 'Non-Art' not in all_src else 'FAIL - still present'}")
print(f"27 participants: {'OK' if '27' in all_src else 'FAIL'}")
print(f"Stigma context:  {'OK' if 'stigma' in all_src.lower() else 'FAIL'}")
print(f"Relax context:   {'OK' if 'relax' in all_src.lower() else 'FAIL'}")
print(f"Express context: {'OK' if 'express' in all_src.lower() else 'FAIL'}")
print(f"Cell count: {len(nb['cells'])}")
