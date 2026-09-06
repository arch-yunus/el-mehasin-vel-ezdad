"""
Rhetorical device detection and classical figures matcher.
"""
from typing import List, Dict, Any

class RhetoricDetector:
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
