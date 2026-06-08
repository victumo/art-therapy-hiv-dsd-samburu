# 🎨 Art as Therapy: Can Painting Improve HIV Outcomes for Adolescents?

### A Differentiated Service Delivery (DSD) Model for AYP in Samburu, Kenya

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IAS 2026](https://img.shields.io/badge/IAS_HIV_Conference-2026_Rio-red.svg)](https://www.iasociety.org/)

**Author:** Victor Cheptumo — Biomedical Scientist | Community Volunteer | Health Data Analyst, Samburu County, Kenya  


---

## 📊 At a Glance

| Metric | 🎨 Painting Cohort | 🏥 Standard Care | Difference |
|--------|:---:|:---:|:---:|
| **Established in Care** | **77.8%** | 46.2% | **+31.6 pp** |
| **Viral Suppression (<200)** | **89.5%** | 73.6% | **+15.9 pp** |
| **Retention (visit ≤6mo)** | **100.0%** | 98.1% | +1.9 pp |

> 167 AYP (10–24 years) | May 2023 – June 2026 | Samburu County Referral Hospital (MFL 15126)

---

## 📖 The Story Behind This Project

In May 2024, I was working as a medical lab technologist at Samburu County Referral Hospital (SCRH), collecting viral load samples from kids living with HIV. Many would get excited and want to touch my computer. Some days, 5 of them would be using it during Friday clinics. I'd opened them a **student account** — no risk to my data!

This curiosity led me to start teaching them basic computer skills. These kids are from **marginalised areas in northern Kenya** with limited access to devices, tech, and infrastructure. I'd pool computers from clinic service points and we'd learn on **Saturdays** — a relaxed, no-pressure environment.

These Saturday workshops became more than just computer classes. **The kids would take their medications, get their lab samples collected, and then paint.** In a region where **HIV stigma is high** and walking into a clinic during busy days can expose adolescents to gossip and discrimination, these quiet Saturday sessions offered a safe space.

We outgrew the space, **collaborated with Painting for an Education**, and introduced art painting — which the kids loved. **Painting helps them relax and express themselves in ways they don't usually talk about.** We now do monthly remote sessions with artists.

Today, **27 AYP** have attended 3 or more painting sessions since May 2024.

In early 2025, the **global USAID funding freeze** hit. Clinics were disrupted everywhere — reagent stock-outs, supply chain breakdowns, staff layoffs. I was among the healthcare workers who lost their jobs. **My 7-year career ended overnight.** But I kept showing up. Every last Saturday, I'm still there with the kids — **now as a volunteer** — because these painting sessions have become bigger than any one of us.

---

## 🧬 The Research Question

> *"Can monthly community painting sessions — a low-cost, creative, peer-supported intervention — improve HIV treatment outcomes (viral suppression, establishment in care, retention) for adolescents and young people compared to standard care alone?"*

Adolescents and Young People (AYP, 10–24) have the **lowest viral suppression rates** of any age group in Kenya. Stigma, mental health struggles, and treatment fatigue drive poor outcomes. Standard clinical care rarely addresses psychosocial needs.

This repo contains the first quantitative analysis of whether a creative, community-led Saturday program can change that.

---

## 📁 Repository Structure

```
art-therapy-hiv-dsd-samburu/
│
├── README.md                          ← You are here
├── .gitignore                         ← Raw patient data excluded
│
├── networks/
│   └── samburu_art_therapy_dsd_model.ipynb   ← Full analysis notebook
│
├── slides/
│   ├── chart1_suppression_trends.png          ← Quarterly trends (line chart)
│   ├── chart2_pre_post_comparison.png         ← Before/after intervention
│   ├── chart3_clinical_outcomes_dashboard.png ← Establishment, suppression, retention
│   └── chart4_vl_detailed_breakdown.png      ← Detailed VL categories
│
├── data/
│   └── processed/                     ← Anonymised CSVs (P-0001 IDs, no PII)
│       ├── samburu_dsd_anonymised_vl_data.csv
│       ├── samburu_dsd_latest_vl_per_patient.csv
│       └── samburu_dsd_linelist_summary.csv
│
└── scripts/                           ← Exploration & cohort analysis scripts
    ├── explore_data.py
    ├── cohort_analysis.py
    └── ...
```

> 🔒 **Raw patient data is NOT published.** Names, CCC numbers, DOBs, and facility identifiers are excluded. The `data/raw/` directory is gitignored.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/victumo/art-therapy-hiv-dsd-samburu.git
cd art-therapy-hiv-dsd-samburu

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn scipy openpyxl xlrd

# 3. Open the notebook
jupyter notebook networks/samburu_art_therapy_dsd_model.ipynb
```

> ⚠️ The notebook will look for raw data in `data/raw/` — you'll need access to the source files (not public). The processed anonymised CSVs in `data/processed/` are included and can be used directly.

---

## 📈 Key Findings

### 1. The Painting Cohort Stayed Suppressed Through a Crisis

Standard care AYP suppression **dropped from 88.2% to 75.7%** after the USAID funding freeze (2025). The painting cohort held steady at **~94%** throughout.

![Suppression Trends](slides/chart1_suppression_trends.png)

### 2. Painting Participants Are More Established in Care

**77.8%** of the painting cohort are classified as "Established" vs only **46.2%** of age-matched peers — a 31.6 percentage point gap.

![Clinical Outcomes](slides/chart3_clinical_outcomes_dashboard.png)

### 3. Detailed Viral Load Breakdown

The painting cohort had **zero patients** in the Low Level Viremia (50–199) warning zone and only 1 in High Level Viremia (200–999), compared to 9 and 8 respectively in standard care.

![VL Breakdown](slides/chart4_vl_detailed_breakdown.png)

---

## 🌍 Context: The USAID Funding Freeze (2025)

In early 2025, the USAID global funding freeze caused reagent stock-outs and clinic disruptions at SCRH. VL testing was interrupted and services only began recovering from late 2025. **This analysis shows how a low-cost, community-led intervention can buffer against health system shocks** — the painting sessions continued throughout.

---

## 🎯 Call to Action

This was a pilot with 26 participants. The evidence is directional, not definitive — but the magnitude of effect is clinically meaningful. We're seeking:

- **Formal DSD pilot** — Test the model in 3–5 additional sites
- **Operational research** — Optimal frequency, cost-effectiveness, integration into national guidelines
- **Partnerships** — Ministry of Health Kenya DSD technical working group, donors, IAS

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** (pandas, numpy) | Data cleaning, transformation, aggregation |
| **Matplotlib + Seaborn** | All visualisations |
| **SciPy** | Chi-square statistical testing |
| **Jupyter Notebook** | Literate programming — code + narrative |
| **Excel/CSV** | Source data from KenyaEMR |

---

## 🔒 Data Privacy

- All patient identifiers (names, CCC numbers, NUPI, DOB) are **removed** before export
- Processed datasets use anonymous IDs (`P-0001`, `P-0002`, etc.)
- Raw clinical data remains local and is **never published**
- Institutional permission obtained from Samburu County Referral Hospital

---

## 👤 About the Author

**Victor Cheptumo** is a Biomedical Scientist and Health Data Analyst from Samburu County, Kenya. For 7 years, he ran the viral load testing program at Samburu County Referral Hospital. When the 2025 USAID funding freeze ended his career overnight, he chose to stay — now as a **community volunteer** — because the Saturday painting initiative he founded had grown bigger than any job title. He continues to show up every last Saturday for the kids, combining his lab expertise with data analytics to build the evidence base for creative, community-led DSD models.

📧 GitHub: [@victumo](https://github.com/victumo)
---

## 📄 License

MIT — see [LICENSE](LICENSE) file.

