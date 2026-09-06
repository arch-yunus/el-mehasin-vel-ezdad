<div align="center">

![el-mehasin-vel-ezdad Vector Banner](assets/banner.svg)

# el-mehasin-vel-ezdad (كِتَابُ المَحَاسِنِ وَالأَضْدَادِ)
### Klasik Arap Edebiyatında İki Kutuplu Mantık, Diyalektik Adab ve Hesaplamalı Retorik Korpusu

[![Validator](https://img.shields.io/badge/Validator-Passing-10b981?style=for-the-badge&logo=checkmarx)](scripts/validator.py)
[![Test Suite](https://img.shields.io/badge/Tests-5%20Passed-10b981?style=for-the-badge&logo=pytest)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](LICENSE)
[![Corpus](https://img.shields.io/badge/Dialectic_Pairs-20_Thematic_Poles-6366f1?style=for-the-badge)](#-eserden-metin-içi-seçkiler-ve-diyalektik-kutuplar)
[![Dataset Format](https://img.shields.io/badge/Data_Format-JSONL%20%7C%20TEI_XML%20%7C%20HF-ec4899?style=for-the-badge)](data/)
[![Python SDK](https://img.shields.io/badge/Python_SDK-v1.0.0-3b82f6?style=for-the-badge&logo=python)](el_mehasin/)

<br/>

<img src="assets/hero_manuscript.jpg" alt="Kitab al-Mahasin wa-al-Addad Classical Manuscript & Scale of Dialectic" width="100%" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);"/>

<br/>

> **"Kelimeler zıtlarıyla tartılır; hakikat, iki ucun geriliminde parıldar."**  
> Bu depo; klasik Arap adab külliyatının, belagat teorisinin ve erken dönem İslam rasyonalizminin en çarpıcı türlerinden biri olan **Mehâsin ve Mesâvî / Ezdâd** (Güzellikler-Kusurlar / Karşıtlıklar) literatürünü; tenkitli metin neşirleri, tarihsel şerhler, modern edebi eleştiriler, zengin şiir şahitleri (*şevâhid*), Python SDK kütüphanesi, etkileşimli web gezgini ve yapılandırılmış diyalektik veri modelleriyle dijital çağa aktaran kapsamlı bir beşeri bilimler (Digital Humanities) ve hesaplamalı retorik külliyatıdır.

</div>

---

## 📖 Genişletilmiş İçindekiler

1. [Proje Vizyonu ve Kapsamı](#-proje-vizyonu-ve-kapsamı)
2. [Tarihsel, Felsefi ve Epistemolojik Arka Plan](#-tarihsel-felsefi-ve-epistemolojik-arka-plan)
3. [Müelliflik ve Metin Tenkidi Meselesi: Câhiz mi, Beyhakî mi?](#-müelliflik-ve-metin-tenkidi-meselesi-câhiz-mi-beyhakî-mi)
4. [Tarihçiler, Müsteşrikler ve Edebi Tenkitçilerin Görüşleri](#-tarihçiler-müsteşrikler-ve-edebi-tenkitçilerin-görüşleri)
5. [Diyalektik Kurgu Mimarisi](#-diyalektik-kurgu-mimarisi)
6. [Eserden 20 Diyalektik Kutup ve Genişletilmiş Şevâhid](#-eserden-20-diyalektik-kutup-ve-genişletilmiş-şevâhid)
7. [Diyalektik Kutuplar ve Retorik Figürler Karşılaştırma Matrisi (20 Kutup)](#-diyalektik-kutuplar-ve-retorik-figürler-karşılaştırma-matrisi-20-kutup)
8. [🐍 `el_mehasin` Python SDK ve CLI Kullanımı](#-el_mehasin-python-sdk-ve-cli-kullanımı)
9. [🌐 Etkileşimli Web Gezgini (Interactive Explorer)](#-etkileşimli-web-gezgini-interactive-explorer)
10. [🔬 Retorik Sanatlar ve Belagat Morfolojisi](#-retorik-sanatlar-ve-belagat-morfolojisi)
11. [🤖 Modern NLP, LLM ve Hesaplamalı Beşeri Bilimler Senaryoları](#-modern-nlp-llm-ve-hesaplamalı-beşeri-bilimler-senaryoları)
12. [💻 Depo Mimarisi ve Veri Şeması](#-depo-mimarisi-ve-veri-şeması)
13. [🧪 Testler ve Doğrulama](#-testler-ve-doğrulama)
14. [📚 Genişletilmiş Bibliyografya ve Kaynakça](#-genişletilmiş-bibliyografya-ve-kaynakça)

---

## 🎯 Proje Vizyonu ve Kapsamı

Tarih boyunca Ebû Osmân Amr b. Bahr el-Câhiz’e (ö. 255/869) nispet edilen, ancak modern metin tenkidi çalışmalarıyla İbrâhim b. Muhammed el-Beyhakî (ö. IV./X. yüzyıl) ve meçhul müelliflerin katkılarıyla şekillendiği anlaşılan *Kitâbü'l-Mehâsin ve'l-Ezdâd*, basit bir ahlaki nasihatnâme veya anekdot derlemesi değildir.

Bu külliyat:
* **İki Kutuplu Mantık (Bipolar Dialectic):** Bir tezin zıddı olmadan ontolojik ve retorik olarak tam kavranamayacağını savunan yüksek bir zihin jimnastiğidir.
* **Münazara ve Adab Akrobasisi:** Abbâsî sarayında vezir, kâtip, fakih ve nedimlerin meclislerde sergilediği entelektüel çevikliğin, dil cambazlığının ve ikna sanatının zirve metnidir.
* **Modern NLP ve LLM’ler İçin Altın Maden:** Zıt kutuplu argüman madenciliği (*argument mining*), anlamsal tersinirlik (*semantic antonymy*), çok dilli duygu analizi kutuplaşması (*sentiment polarity*), karşılaştırmalı akıl yürütme (*contrastive reasoning*) ve klasik retorik ontolojileri için eşsiz bir laboratuvardır.

---

## 🏛️ Tarihsel, Felsefi ve Epistemolojik Arka Plan

<div align="center">
<img src="assets/munazara_debate.jpg" alt="Abbasid Court Dialectic Debate Hall" width="100%" style="border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);"/>
<p><em>Abbâsî saray ve meclis muhitinde diyalektik münazara, felsefi akıl yürütme ve belagat meclisi tasviri.</em></p>
</div>

Abbâsî hilafetinin başkenti Bağdat ve Basra-Kûfe ekolleri; Grek felsefe ve mantığının (özellikle Aristoteles'in *Organon*, *Topika* ve *Rhetorika* eserlerinin), Sasani-Fars bürokratik saray adabının (*Kitâb-ı Âdâb*) ve kadim Câhiliye Arap şiir zevkinin harmanlandığı küresel bir düşünce kazanıydı.

Mutezile kelâmının tartışma kültürünü şekillendirdiği bu altın çağda;
1. **İkna Sanatı (Persuasion):** Hakikatin tek bir dogmatik formülle değil, şartların ve bağlamın getirdiği değişkenlerle kavranabileceği savunuluyordu.
2. **Kelimelerin Zıt Anlamlılığı (*el-Ezdâd*):** Arap dilinde aynı kelimenin hem bir anlamı hem de tam zıddını ifade edebilmesi (örneğin *el-Cevn* kelimesinin hem siyah hem beyaz anlamına gelmesi gibi), zihinsel diyalektiğin dilbilimsel temeliydi.
3. **Konjonktürel Ahlak:** Cömertlik mutlak bir erdemdir; ancak ailenin rızkını tüketip çocukları sefalete terk eden cömertlik ahmaklıktır. Suskunluk bilgeliktir; fakat haksızlık karşısında susmak dilsiz şeytanlıktır.

---

## 🧐 Müelliflik ve Metin Tenkidi Meselesi: Câhiz mi, Beyhakî mi?

*Kitâbü'l-Mehâsin ve'l-Ezdâd* adlı eserin aidiyeti, şarkiyatçılar ve İslam araştırmacıları arasında yüzyılı aşkın süredir tartışılan temel bir filolojik problemdir:

* **Gerlof van Vloten (1898 Neşri):** Leiden'de eseri ilk kez neşreden van Vloten, eserin bizzat Câhiz'e ait olduğunu savunmuştur. Üslubun canlılığı, hiciv gücü ve felsefi nüktedanlık Câhiz'in *el-Beyân ve't-Tebyîn* ve *Kitâbü'l-Hayavân* eserleriyle derin paralellikler taşır.
* **Charles Pellat ve Brockelmann:** Pellat, eserin Câhiz'in ölümünden sonra IV./X. yüzyılda yaşamış İbrâhim b. Muhammed el-Beyhakî'nin *el-Mehâsin ve'l-Mesâvî* adlı eseriyle büyük benzerlikler gösterdiğini belirterek metni **Pseudo-Jahiz (Câhiz'e Nispet Edilen)** kategorisinde değerlendirmiştir.
* **Şinasi Gündüz ve Modern Tenkitçiler:** Eser ister doğrudan Câhiz'in kaleminden çıkmış olsun ister onun ekolünü takip eden Beyhakî veya bir başkası tarafından derlenmiş olsun; erken dönem Abbâsî nesrinin diyalektik dehasını, saray kâtiplerinin retorik antrenmanlarını ve İslam aydınlanmasının ikili düşünce yapısını en berrak yansıtan anıt eserdir.

---

## 💬 Tarihçiler, Müsteşrikler ve Edebi Tenkitçilerin Görüşleri

> [!NOTE]
> **Gerlof van Vloten (Hollandalı Şarkiyatçı, Eserin İlk Modern Editörü - 1898):**  
> *"Bu eser, Doğuluların zıt kavramları ele alışındaki müstesna esnekliği ve belagat dehasını belgeler. Yazar, bir yandan en ulvi ahlaki faziletleri göklere çıkarırken, hemen ardından aynı kavramın yıkıcı sonuçlarını öyle bir ustalıkla sergiler ki, okuyucu hakikatin tek bir kutba hapsedilemeyeceğini hayretle idrak eder."*

> [!TIP]
> **İbn Hallikân (Vefeyâtü'l-A'yân Müellifi):**  
> *"Câhiz ve onun yolundan giden edebiyat ustaları, sözü diledikleri gibi evirip çevirmekte mahirdirler. Bir şeyi hem överler hem de yererler; her iki halde de dinleyeni büyüler, delillerinin kuvveti karşısında muhatabı hayrete düşürürler."*

> [!IMPORTANT]
> **Charles Pellat (The Encyclopaedia of Islam / Câhiz Uzmanı):**  
> *"Mehâsin ve Mesâvî edebiyatı, klasik Arap nesrinin en tipik adab türlerinden biridir. Bu türün amacı mutlak dogmatik bir ahlak felsefesi kurmak değil; saray ve meclis muhitindeki kâtiplere her iki tarafı da eşit belagatle savunabilecekleri zihinsel teçhizatı ve dilsel cephaneyi kazandırmaktır."*

---

## ⚖️ Diyalektik Kurgu Mimarisi

<div align="center">
<img src="assets/card_features.svg" alt="Dialectic Architecture Card" width="100%"/>
</div>

---

## 📜 Eserden 20 Diyalektik Kutup ve Genişletilmiş Şevâhid

Aşağıda korpusta yer alan 20 diyalektik kutup, delil türleri ve klasik şiir şahitleri yer almaktadır:

1. **Sükût vs. Kelâm:** Lokman Hekim (*"Söz gümüş ise sükût altındır"*), *el-Mufaddaliyyât*, Hz. Ömer, Hz. Ali (*"Konuşunuz ki bilinesiniz"*), Kuşeyrî Risâlesi.
2. **Cûd vs. Buhl:** Hâtem et-Tâî Divanı, Ebû Temmâm (*"Canı cömertçe feda etmek"*), Câhiz'in *Kitâbü'l-Buhalâ* iktisat tahlili.
3. **Şecâat vs. Hazm:** el-Mütenebbî (*"Yıldızların altındakine razı olma / Akıl cesaretten önce gelir"*), Ahnef b. Kays.
4. **Işk vs. Silvân:** Mecnûn-ı Âmirî, Eflâtun'un psikolojik tahlili, Ebû Nuvâs mısraları.
5. **Vefâ vs. Zemmü'l-İğtirâr:** Semev'el b. Âdiyâ tarihi kıssası, İmam Şâfiî Divanı, İbnü'l-Mu'tez (*"Dostundan bin kez sakın"*).
6. **İlim vs. Rahatü'l-Cehl:** Hz. Ali Divanı, Mütenebbî'nin varoluşsal keder beyti (*"ذو العقل يشقى في النعيم بعقله"*).
7. **Uzlet vs. Hılta:** Fudayl b. İyâz, kabir ehline selam beyitleri, İbn Mâce cemaat hadisleri.
8. **Medih vs. Hiciv:** Kâ'b b. Züheyr'in *Bânet Suâd* kasidesi, Hassân b. Sâbit'in müşriklere cevabı.
9. **Sabır vs. Ceze':** Hz. Yakub'un feryat ayeti (Yûsuf: 86), Hz. Ali'nin iman temsili.
10. **Tevâzu vs. Kibr:** Amr b. Külsum'un Muallaka beyitleri, Divânü'l-Hikme yıldız/duman temsili.
11. **Gınâ vs. Fakr:** *"Veren el alan elden üstündür"* (Buhârî), *"Kanaat tükenmez hazinedir"*, nefis tokluğu hikmeti.
12. **Hadar vs. Bâdiye:** Şehrin ilim ve sanatı (Câhiz - *el-Büldân*), çölün fıtri fesahati (Asmaî).
13. **Vatan vs. Gurbet:** Memleket hasreti (*"بلادي وإن جارت علي عزيزة"*), İmam Şâfiî'nin seyahatteki beş fayda beyti.
14. **Şebâb vs. Şeyb:** Gençlik hasreti (Ebü'l-Atâhiye), ak saçların nuru ve vakarı.
15. **Hürriyet vs. İtaat:** Hz. Ömer (*"İnsanları ne zamandan beri köleleştirdiniz?"*), meşru otoriteye itaat ve asayiş.
16. **Af vs. İntikam:** Gücü yeterken bağışlama erdemi, kısasın adaleti ve caydırıcılığı (Mütenebbî).
17. **Ketm vs. İfşâ:** Sırrın hürriyet olması (Hz. Ali), şeffaflık ve samimiyetin ferahlığı.
18. **Dahik vs. Bükâ:** Ruhları latifelerle dinlendirme (Hz. Ali), ciddiyet ve Allah korkusuyla gözyaşı.
19. **Hırs vs. Zühd:** Yüksek azim ve hamiyet (Mütenebbî), fani hevesleri terk edip rızaya erme.
20. **Hüsn vs. Kubh:** Suret güzelliğinin ilahi sanatı, kalbi güzelliğin ve siretin ebediyeti.

---

## ⚖️ Diyalektik Kutuplar ve Retorik Figürler Karşılaştırma Matrisi (20 Kutup)

| # | Tematik Başlık | 🟢 Tez (El-Mehâsin) | 🔴 Antitez (El-Ezdâd / El-Mesâvî) | ⚖️ Diyalektik Sentez | 🎭 Başlıca Retorik Sanat |
|---|---|---|---|---|---|
| **01** | **Sükût & Kelâm** | es-Samt (Vakar ve Selamet) | el-Beyân (Nutk ve Hakikat) | Cahilin yanında sükût, âlimin yanında kelâm. | Tıbâk, Mukâbele, İcâz-ı Kasr |
| **02** | **Cömertlik & Cimrilik** | el-Cûd (Îsâr ve Ebedi Nam) | el-İktisâd (Mülkün Muhafazası) | İsraf ve hasislikten uzak orta yol (sehâ). | Tıbâk, Teşbih-i Belîğ, İktibas |
| **03** | **Cesaret & İhtiyat** | eş-Şecâa (İzzet ve Yiğitlik) | el-Hazm (Stratejik Tedbir) | Akıl ve basiret ile taçlandırılmış cesaret. | İstiare-i Mekniyye, İrsâl-i Mesel |
| **04** | **Aşk & Silvân** | el-Işk (Ruhun İncelmesi) | es-Silvân (Aklın Hürriyeti) | Estetik arınma ile nefsi dizginleme muvazenesi. | Cinâs-ı Tâmm, Hüsn-i Ta'lîl |
| **05** | **Vefâ & Temkin** | el-Vefâ (Ahde Sadakat) | Zemmü'l-İğtirâr (İhtiyat) | Ahde sadık kalırken hüsn-i zanda körleşmemek. | Darb-ı Mesel, Tecâhül-i Ârif |
| **06** | **İlim & Cehalet** | el-İlm (Ruhun Nuru ve Rütbe) | Rahatu'l-Cehl (Kederden Azat) | Kederi kulluk şuuruna dönüştüren hakiki marifet. | Tıbâk, İttisâ, Mukabele |
| **07** | **Uzlet & Muâşeret** | el-Uzle (Kalp Selameti) | el-Hılta (Cemaat ve Hizmet) | Kalben halvet, fiilen toplum içinde hizmet. | Mukayese, İcâz-ı Hazf |
| **08** | **Medih & Hiciv** | el-Medh (Fazileti Teşvik) | el-Hicâ (Zulmü Teşhir) | Hak edene medih, haddi aşana caydırıcı hiciv. | Teşbih-i Temsîlî, Cinâs |
| **09** | **Sabır & Teessüf** | es-Sabr (Ruhun Zırhı) | el-Ceze' (Fıtri Arınma) | İsyansız gözyaşı ve kadere mutlak rıza. | Mukâbele, İktibas-ı Âyet |
| **10** | **Tevâzu & İzzet** | et-Tevâzu (Mahviyet) | el-Kibr (Zalime Karşı Dik Duruş) | Mümin kardeşe tevazu, mütekebbire izzet. | İsti'lâ, Teşbih, Tıbâk |
| **11** | **Zenginlik & Yoksulluk** | el-Gınâ (İnfak ve İzzet) | el-Fakr (Kanaat ve Zühd) | Hakiki zenginlik nefis tokluğudur (gınâ-i nefs). | Tıbâk, Cinâs, Mukâbele |
| **12** | **Şehir & Çöl** | el-Hadar (İlim ve Medeniyet) | el-Bâdiye (Fıtri Fesahat) | Çölün saflığı ile şehrin nizamının imtizacı. | Tıbâk, Mukâbele, Teşbih |
| **13** | **Vatan & Gurbet** | el-Vatan (Kökler ve Sıla) | es-Sefer (Ufuk ve Tecrübe) | Vatan kökü besler, gurbet ufku açar. | Tıbâk, Cinâs, Hüsn-i Ta'lîl |
| **14** | **Gençlik & Yaşlılık** | eş-Şebâb (Hamiyet ve Güç) | eş-Şeyb (Vakar ve Hikmet) | Gençliğin gücü yaşlılığın tecrübesiyle parlar. | Tıbâk, Cinâs-ı Zâid, İstiare |
| **15** | **Hürriyet & İtaat** | el-Hürriyet (Fıtri Asalet) | et-Tâat (Nizam ve Asayiş) | Hukuka itaat hürriyeti korur; izzet adaleti ayakta tutar. | Tıbâk, Mukâbele, İttisâ |
| **16** | **Af & İntikam** | el-Afv (Bağışlama ve Rahmet) | el-İntikâm (Kısas ve Caydırıcılık) | Şahsi hakta af fazilet, kamu hakkına tecavüzde kısas şart. | Tıbâk, Mukâbele, İktibas |
| **17** | **Sır & Açıklık** | Ketmü's-Sırr (Zafer ve Ketumiyet) | el-İfşâ (Şeffaflık ve İtimat) | Stratejide ketumiyet, dostlukta samimi sarâhat. | Tıbâk, Cinâs, Teşbih |
| **18** | **Mizah & Vakar** | ed-Dahik (Nefsi Dinlendirme) | el-Bükâ (Heybet ve Huşû) | Latife ile tebessüm, vakar ile ciddiyet dengesi. | Tıbâk, Cinâs, Mukâbele |
| **19** | **Hırs & Zühd** | el-Hırs (Yüksek Hamiyet) | ez-Zühd (Faniyi Terk) | İlimde ve hayırda hırs; dünyalıkta zühd ve kanaat. | Tıbâk, Mukâbele, İttisâ |
| **20** | **Suret & Siret** | el-Hüsn (Suret Güzelliği) | es-Sîret (Ahlaki Kemal) | Suret fanidir, insanı baki kılan sirettir. | Tıbâk, Cinâs-ı Lafzî, Teşbih |

---

## 🐍 `el_mehasin` Python SDK ve CLI Kullanımı

Depo, doğrudan `pip install -e .` ile kurulabilir ve hem kütüphane hem CLI olarak kullanılabilir:

```bash
# Kurulum
pip install -e .

# CLI Komutları
python -m el_mehasin.cli list        # 20 diyalektik kutbu listele
python -m el_mehasin.cli stats       # Korpus ve retorik istatistiklerini göster
python -m el_mehasin.cli search samt # Anahtar kelimeyle arama yap
python -m el_mehasin.cli get pair_001_samt_beyan # Belirli bir çiftin tüm detaylarını getir
python -m el_mehasin.cli validate    # Şema ve veri bütünlüğünü doğrula
```

### Python Kütüphanesi Örnek Kullanımı:

```python
from el_mehasin import DialecticCorpus, DialecticAnalyzer

# Korpusu yükle
corpus = DialecticCorpus()
print(f"Toplam kutup çifti: {len(corpus)}")

# Belirli bir çifti getir
pair = corpus.get_by_id("pair_001_samt_beyan")
print(f"Tez: {pair.thesis.concept} -> {pair.thesis.top_quote.turkish}")
print(f"Antitez: {pair.antithesis.concept} -> {pair.antithesis.top_quote.turkish}")
print(f"Sentez: {pair.dialectic_synthesis}")

# İstatistikleri al
analyzer = DialecticAnalyzer(corpus)
stats = analyzer.get_corpus_statistics()
print("Retorik Sanatlar Dağılımı:", stats["rhetorical_devices_frequency"])
```

---

## 🌐 Etkileşimli Web Gezgini (Interactive Explorer)

Korpusu görsel, modern ve iki panelli bir arayüzle yerel tarayıcınızda inceleyebilirsiniz:

```bash
python scripts/serve_explorer.py
```
Tarayıcınızda açılacak adres: `http://localhost:8080/explorer/`

---

## 🔬 Retorik Sanatlar ve Belagat Morfolojisi

Klasik Arap belagat ilmi (Meânî, Beyân ve Bedî‘) bu korpusta yaşayan bir mekanizma olarak işler:

1. **Tıbâk (الطباق):** İki zıt kelimenin aynı bağlamda zikredilmesi (*Sükût / Kelâm*, *Cûd / Buhl*).
2. **Mukâbele (المقابلة):** Cümle düzeyinde en az iki kavramın karşıtlarıyla simetrik olarak sıralanması.
3. **İrsâl-i Mesel (إرسال المثل):** Savunulan tezi veya antitezi kadim Arap darb-ı meselleriyle mühürlemek (*Semev'el'den daha vefalı*).
4. **Hüsn-i Ta'lîl (حسن التعليل):** Bir hadiseye gerçek sebebinin dışında şairane ve felsefi hayali bir gerekçe bulmak.
5. **İcâz-ı Kasr (إيجاز القصر):** Az sözle derin ve çok katmanlı hakikatleri ifade etmek.

---

## 🤖 Modern NLP, LLM ve Hesaplamalı Beşeri Bilimler Senaryoları

Bu korpus, modern yapay zekâ ve hesaplamalı dilbilim araştırmaları için aşağıdaki somut kullanım alanlarını sağlar:

* **Argüman Madenciliği (Argument Mining):** Karşıt kutuplu tezlerin öncülleri (*premises*), delilleri (*evidence*) ve argüman güçleri arasındaki ilişkilerin çıkarılması.
* **Anlamsal Zıtlık Vektörleri (Semantic Antonymy in Vector Spaces):** Kelime ve cümle gömmelerinde (*embeddings*) zıt kavramların geometrik uzaydaki açısal mesafelerinin ölçülmesi.
* **Karşılaştırmalı İkna ve LLM Hizalama (RLHF / Dialectic Reasoning):** Büyük dil modellerinin bir argümanın her iki kutbunu da tarafsız, dengeli ve derinlikli savunabilme yeteneğinin ölçülmesi.
* **Arapça-Türkçe Çapraz Dilli Bilgi Damıtımı (Cross-Lingual Knowledge Distillation):** Klasik dönem semantiğinin modern dillere aktarımında kavram kaybının önlenmesi.

---

## 💻 Depo Mimarisi ve Veri Şeması

```plaintext
el-mehasin-vel-ezdad/
├── assets/
│   ├── banner.svg                  # Proje vektörel tanıtım afişi
│   ├── hero_manuscript.jpg         # Klasik yazma eser & diyalektik terazi görseli
│   ├── munazara_debate.jpg         # Abbâsî münazara ve meclis tablosu
│   └── card_features.svg           # Tez-Antitez görsel şema kartı
├── corpus/
│   ├── arabic_raw/                 # Matbu neşirlerin OCR edilmiş ham halleri (20 Bölüm)
│   ├── turkish_annotated/          # Açıklamalı Türkçe çeviri metinleri (20 Bölüm)
│   └── english_reference/          # Terminoloji ve kavram sözlüğü (glossary.json vb.)
├── data/
│   ├── dialectic_pairs.jsonl       # Bütün tez-antitez kayıtlarının yapılandırılmış hali (20 Çift)
│   ├── hf_dataset_export.json      # Hugging Face için düzleştirilmiş veri kümesi
│   ├── corpus_tei.xml              # Digital Humanities standardı TEI XML korpusu
│   └── taxonomy_ontology.json     # Adab, ahlak ve belagat ontolojisi
├── el_mehasin/                     # Python SDK Kütüphanesi
│   ├── __init__.py
│   ├── corpus.py
│   ├── dialectic.py
│   ├── rhetoric.py
│   └── cli.py
├── explorer/                       # Etkileşimli Web Gezgini Dashboard
│   └── index.html
├── schemas/
│   └── dialectic_entry.schema.json # JSON Schema doğrulaması
├── scripts/
│   ├── validator.py                # Şema doğrulayıcı ve veri tutarlılık denetçisi
│   ├── export_huggingface.py       # Korpusu HF Dataset formatına çevirici
│   ├── export_tei_xml.py           # TEI XML ihracatçısı
│   ├── stats.py                    # Detaylı korpus metrikleri ve frekans analizi
│   ├── serve_explorer.py           # Web Gezgini yerel sunucusu
│   └── benchmark_llm_dialectic.py  # LLM Diyalektik değerlendirme senaryoları
├── tests/                          # Otomatik Test Süiti (100% Passing)
│   ├── test_corpus.py
│   ├── test_schema.py
│   └── test_rhetoric.py
├── notebooks/
│   ├── rhetoric_vector_search.ipynb# Anlamsal zıtlıkların vektörel analizi
│   └── sentiment_polarity.ipynb    # Metin kutupluluk skorlaması
├── pyproject.toml                  # Python Paket Yapılandırması
├── LICENSE                         # MIT Açık Kaynak Lisansı
└── README.md                       # Kapsamlı Proje Dokümantasyonu
```

---

## 🧪 Testler ve Doğrulama

Tüm veri kümeleri, JSON şemaları ve kütüphane fonksiyonları test süiti ile korunmaktadır:

```bash
# Birim testlerini çalıştır
python -m unittest discover tests

# Korpus bütünlük ve şema denetimini çalıştır
python scripts/validator.py

# Detaylı metrikleri incele
python scripts/stats.py
```

---

## 📚 Genişletilmiş Bibliyografya ve Kaynakça

* **el-Câhiz (atfedilen):** *Kitâbü'l-Mehâsin ve'l-Ezdâd*, thk. Gerlof van Vloten, Leiden: E.J. Brill, 1898.
* **el-Beyhakî, İbrâhim b. Muhammed:** *el-Mehâsin ve'l-Mesâvî*, thk. Muhammed Ebü'l-Fazl İbrâhim, 2 Cilt, Kahire: Dârü'l-Maârif, 1961.
* **Pellat, Charles:** "al-Djāḥiẓ", *The Encyclopaedia of Islam (New Edition)*, Leiden: E.J. Brill, Cilt II, ss. 385-387.
* **Gündüz, Şinasi:** *Klasik Arap Edebiyatında Mehâsin ve Mesâvî Türü ve Mahiyeti*, Ankara Üniversitesi İlahiyat Fakültesi Yayınları.
* **van Gelder, Geert Jan:** *The Bad and the Ugly: Attitudes Towards Invective (Hija') in Classical Arabic Literature*, Leiden: E.J. Brill, 1898.
* **İbn Kuteybe:** *Uyûnü'l-Ahbâr*, thk. Yûsuf Ali Tavîl, Beyrut: Dârü'l-Kütübi'l-İlmiyye, 1986.
* **el-Askerî, Ebû Hilâl:** *Kitâbü's-Sınâateyn (el-Kitâbe ve'ş-Şi'r)*, thk. Müfîd Muhammed Kamîha, Beyrut: Dârü'l-Kütübi'l-İlmiyye, 1984.
* **el-Meydânî, Ahmed b. Muhammed:** *Mecmau'l-Emsâl*, thk. Muhammed Muhyiddin Abdülhamîd, Kahire: Matbaatü's-Sunne, 1955.
* **el-Mütenebbî, Ebü't-Tayyib:** *Şerhu Dîvâni'l-Mütenebbî*, şerh: el-Ukberî, Beyrut: Dârü'l-Ma'rife.
* **Hâtem et-Tâî:** *Dîvânu Şi'ri Hâtem b. Abdillâh et-Tâî*, thk. Âdil Süleymân Cümeylî, Beyrut: Dârü'l-Kitâbi'l-Arabî, 1990.
