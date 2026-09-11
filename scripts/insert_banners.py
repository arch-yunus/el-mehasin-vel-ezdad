from pathlib import Path

readme_path = Path("README.md")
content = readme_path.read_text(encoding="utf-8")

# 1. Section 2
content = content.replace(
    "## 🏛️ Tarihsel, Felsefi ve Epistemolojik Arka Plan\n",
    "## 🏛️ Tarihsel, Felsefi ve Epistemolojik Arka Plan\n\n<div align=\"center\">\n<img src=\"assets/banner_1_philosophy.svg\" alt=\"Philosophy Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 2. Section 3
content = content.replace(
    "## 🧐 Müelliflik ve Metin Tenkidi: Câhiz mi, Beyhakî mi?\n",
    "## 🧐 Müelliflik ve Metin Tenkidi: Câhiz mi, Beyhakî mi?\n\n<div align=\"center\">\n<img src=\"assets/banner_2_authorship.svg\" alt=\"Authorship Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 3. Section 5
content = content.replace(
    "## ⚖️ Diyalektik Kurgu Mimarisi ve İki Kutuplu Mantık (Bipolar Logic)\n",
    "## ⚖️ Diyalektik Kurgu Mimarisi ve İki Kutuplu Mantık (Bipolar Logic)\n\n<div align=\"center\">\n<img src=\"assets/banner_3_dialectic_triad.svg\" alt=\"Dialectic Triad Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 4. Section 6
content = content.replace(
    "## 📜 20 Diyalektik Kutbun Kapsamlı Monografileri ve Şevâhid Külliyatı\n",
    "## 📜 20 Diyalektik Kutbun Kapsamlı Monografileri ve Şevâhid Külliyatı\n\n<div align=\"center\">\n<img src=\"assets/banner_4_shawahid_poetry.svg\" alt=\"Shawahid Poetry Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 5. Section 8
content = content.replace(
    "## 🔬 Klasik Belagat ve Retorik Figürler Rehberi\n",
    "## 🔬 Klasik Belagat ve Retorik Figürler Rehberi\n\n<div align=\"center\">\n<img src=\"assets/banner_5_balaghah_rhetoric.svg\" alt=\"Balaghah Rhetoric Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 6. Section 10
content = content.replace(
    "## 🐍 `el_mehasin` Python SDK ve Kapsamlı API Rehberi\n",
    "## 🐍 `el_mehasin` Python SDK ve Kapsamlı API Rehberi\n\n<div align=\"center\">\n<img src=\"assets/banner_6_sdk_code.svg\" alt=\"Python SDK Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

# 7. Section 12
content = content.replace(
    "## 🤖 Modern NLP, LLM ve Hesaplamalı Retorik Senaryoları\n",
    "## 🤖 Modern NLP, LLM ve Hesaplamalı Retorik Senaryoları\n\n<div align=\"center\">\n<img src=\"assets/banner_7_nlp_ai.svg\" alt=\"NLP AI Banner\" width=\"100%\" style=\"border-radius: 10px; margin-bottom: 20px;\"/>\n</div>\n"
)

readme_path.write_text(content, encoding="utf-8")
print("README.md successfully updated with 7 equal-spaced section banners!")
