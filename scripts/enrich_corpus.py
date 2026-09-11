import json
from pathlib import Path

data_file = Path("data/dialectic_pairs.jsonl")
tr_dir = Path("corpus/turkish_annotated")

with open(data_file, "r", encoding="utf-8") as f:
    pairs = [json.loads(line) for line in f if line.strip()]

slug_map = {
    "pair_001_samt_beyan": "01_sukut_ve_kelam.md",
    "pair_002_cud_buhl": "02_comertlik_ve_cimrilik.md",
    "pair_003_secaat_hazm": "03_cesaret_ve_ihtiyat.md",
    "pair_004_isk_silvan": "04_ask_ve_silvan.md",
    "pair_005_vefa_igtirar": "05_vefa_ve_ihtiyat.md",
    "pair_006_ilim_cehil": "06_ilim_ve_cehalet.md",
    "pair_007_uzlet_muhasere": "07_uzlet_ve_muasere.md",
    "pair_008_medh_zemm": "08_medih_ve_hiciv.md",
    "pair_009_sabr_cez": "09_sabir_ve_teessuf.md",
    "pair_010_tevazu_kibr": "10_tevazu_ve_izzet.md",
    "pair_011_gina_fakr": "11_zenginlik_ve_yoksulluk.md",
    "pair_012_hadar_bedeviyyet": "12_sehir_ve_col_hayati.md",
    "pair_013_vatan_gurbet": "13_vatan_ve_gurbet.md",
    "pair_014_sebab_seyb": "14_genclik_ve_yaslilik.md",
    "pair_015_hurriyet_itaat": "15_hurriyet_ve_itaat.md",
    "pair_016_afv_intikam": "16_af_ve_intikam.md",
    "pair_017_ketm_ifsa": "17_sir_ve_aciklik.md",
    "pair_018_dahik_buka": "18_mizah_ve_vakar.md",
    "pair_019_hirs_zuhd": "19_hirs_ve_zuhd.md",
    "pair_020_husn_kubh": "20_guzellik_ve_cirkinlik.md",
}

for p in pairs:
    fname = slug_map.get(p["entry_id"])
    if not fname:
        continue

    thesis = p["thesis"]
    anti = p["antithesis"]

    content = f"""# Bölüm {p.get("metadata", {}).get("chapter_index", "")}: {p["topic_slug"].replace("-", " ").title()} ({p["classical_arabic_title"]})

## 📜 Tematik Giriş ve Filolojik Arka Plan
Bu bölüm, klasik Arap adab külliyatında **{thesis["concept"]}** ile **{anti["concept"]}** arasındaki iki kutuplu gerilimi ve felsefi muvazeneyi ele almaktadır. Eserin genel mimarisinde olduğu gibi müellif, her iki kutbu da en yetkin nasslar, şevâhid beyitleri ve darb-ı mesellerle tahkim eder.

---

## 🟢 1. Mehâsin Kutbu (El-Mehâsin - المحاسن)
* **Kavramsal Odak:** {thesis["concept"]}
* **Temel Felsefi Öncül:** {thesis["core_premise"]}
* **Delil ve Şahit Gücü:** {thesis["evidence_count"]} Temel Dayanak

### Birincil Şahit ve İktibas:
> **"{thesis["top_quote"]["arabic"]}"**  
> *"{thesis["top_quote"]["turkish"]}"*  
> — **Kaynak:** {thesis["top_quote"]["source"]}

### Ek Şiir Şahitleri ve Rivayetler:
"""
    for q in thesis.get("additional_quotes", []):
        content += f"""> *{q["arabic"]}*  
> *"{q["turkish"]}"*  
> — **Kaynak:** {q["source"]}
>
"""

    content += f"""---

## 🔴 2. Ezdâd / Mesâvî Kutbu (El-Ezdâd - الأضداد)
* **Kavramsal Odak:** {anti["concept"]}
* **Temel Felsefi Öncül:** {anti["core_premise"]}
* **Delil ve Şahit Gücü:** {anti["evidence_count"]} Temel Dayanak

### Birincil Şahit ve İktibas:
> **"{anti["top_quote"]["arabic"]}"**  
> *"{anti["top_quote"]["turkish"]}"*  
> — **Kaynak:** {anti["top_quote"]["source"]}

### Ek Şiir Şahitleri ve Rivayetler:
"""
    for q in anti.get("additional_quotes", []):
        content += f"""> *{q["arabic"]}*  
> *"{q["turkish"]}"*  
> — **Kaynak:** {q["source"]}
>
"""

    content += f"""---

## ⚖️ 3. Diyalektik Sentez ve Belagat Tahlili
* **Diyalektik Sentez (Muvazene):** {p["dialectic_synthesis"]}
* **Öne Çıkan Belagat Sanatları:** {', '.join(p.get("metadata", {}).get("rhetorical_devices", []))}
* **Geleneksel İsnad:** {p.get("metadata", {}).get("traditional_attribution", "Pseudo-Jahiz / al-Bayhaqi")}
"""

    target_path = tr_dir / fname
    with open(target_path, "w", encoding="utf-8") as f_out:
        f_out.write(content)

print("All 20 Turkish annotated corpus files successfully enriched and updated!")
