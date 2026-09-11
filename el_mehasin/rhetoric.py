"""
Rhetorical device detection, categorization, and classical Arabic balaghah matcher.
"""
import re
from typing import List, Dict, Any


class RhetoricClassifier:
    """
    Identifies classical Arabic rhetoric devices (Meânî, Beyân, Bedî')
    and provides semantic scoring for dialectic texts.
    """

    RHETORICAL_TAXONOMY = {
        "Tibak": {
            "name_ar": "الطباق",
            "branch": "İlmü'l-Bedî'",
            "description": "Zıt anlamlı iki kavramın bir ibarede toplanması.",
            "patterns": [
                r"صمت|سكوت|كلام|نطق|بيان|جود|بخل|شح|شجاع|حزم|غنى|فقر|شباب|شيب|عفو|انتقام|ضحك|بكاء|حسن|قبح|علم|جهل|عزل|خلط",
                r"zıt|karşıt|tezat|mehâsin|ezdâd|mesâvî|sükût|kelâm|cömert|cimri|cesaret|ihtiyat"
            ]
        },
        "Mukabele": {
            "name_ar": "المقابلة",
            "branch": "İlmü'l-Bedî'",
            "description": "Cümle düzeyinde birden çok kavramın zıtlarıyla simetrik sıralanması.",
            "patterns": [
                r"يرفع.*يهدم|يشقى.*ينعم|قريب.*بعيد|العليا.*السفلى|خير.*شر",
                r"mukâbele|simetri|karşılıklı|iki kutup"
            ]
        },
        "Irsal-i Mesel": {
            "name_ar": "إرسال المثل",
            "branch": "İlmü'l-Bedî'",
            "description": "Sözü darb-ı mesel haline gelmiş atasözü ve hikmetlerle mühürleme.",
            "patterns": [
                r"السموأل|حاتم|القناعة كنز|صبر ساعة|ما عال من اقتصد|ذهب|فضة",
                r"darb-ı mesel|atasözü|mesel|hikmet"
            ]
        },
        "Husn-i Talil": {
            "name_ar": "حسن التعليل",
            "branch": "İlmü'l-Bedî'",
            "description": "Bir hadiseye şairane, felsefi ve hayali bir gerekçe bulma sanatı.",
            "patterns": [
                r"وداوني|خمس فوائد|يسعد|فساد",
                r"ta'lîl|gerekçe|vesile|fayda"
            ]
        },
        "Icaz-i Kasr": {
            "name_ar": "إيجاز القصر",
            "branch": "İlmü'l-Meânî",
            "description": "Az lafızla çok katmanlı derin manaları vazetme.",
            "patterns": [
                r"قصاص حياة|علمه البيان|الصبر ضياء|من تواضع|حب الوطن",
                r"icâz|özlü|veciz|vecize|az söz|vakar|gümüş|altın"
            ]
        },
        "Cinas": {
            "name_ar": "الجناس",
            "branch": "İlmü'l-Bedî'",
            "description": "Telaffuz benzerliği ve mana farklılığı sanatı.",
            "patterns": [
                r"لسانه.*طيلسانه|الجود.*الوجود|الشباب.*المشيب",
                r"cinâs|cinas|ses benzerliği"
            ]
        },
        "Isti'la": {
            "name_ar": "الاستعلاء",
            "branch": "İlmü'l-Meânî",
            "description": "Kibirli hasma karşı vakar ve heybet kurma üslubu.",
            "patterns": [
                r"التكبر على المتكبر|مذلّة|النجوم",
                r"isti'lâ|celadet|vakar|dik duruş"
            ]
        }
    }

    @classmethod
    def analyze_text(cls, text: str) -> List[Dict[str, Any]]:
        detected = []
        for device_key, meta in cls.RHETORICAL_TAXONOMY.items():
            matches = []
            for pattern in meta["patterns"]:
                found = re.findall(pattern, text, re.IGNORECASE)
                if found:
                    matches.extend(found)
            if matches:
                detected.append({
                    "device": device_key,
                    "arabic_name": meta["name_ar"],
                    "branch": meta["branch"],
                    "description": meta["description"],
                    "match_count": len(matches)
                })
        return detected

    @classmethod
    def calculate_rhetorical_density(cls, text: str) -> float:
        words = text.split()
        if not words:
            return 0.0
        results = cls.analyze_text(text)
        total_matches = sum(r["match_count"] for r in results)
        return round((total_matches / len(words)) * 100, 2)


class RhetoricDetector:
    """Legacy compatibility class for quick keyword-based detection."""
    RHETORICAL_PATTERNS = {
        "Tibak": ["zıt", "karşıt", "övgü", "yergi", "الصمت", "الكلام", "الجود", "البخل", "sükût", "kelâm"],
        "Mukabele": ["iki kutup", "karşılıklı", "simetri", "kutup"],
        "Irsal-i Mesel": ["darb-ı mesel", "atasözü", "مثل", "السموأل", "حاتم"],
        "Icaz": ["az söz", "özlü", "veciz", "altın", "gümüş", "vakar"]
    }

    @classmethod
    def identify_potential_devices(cls, text: str) -> List[str]:
        text_lower = text.lower()
        found = []
        for device, keywords in cls.RHETORICAL_PATTERNS.items():
            for kw in keywords:
                if kw.lower() in text_lower:
                    found.append(device)
                    break
        return found
