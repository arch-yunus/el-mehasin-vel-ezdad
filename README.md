<div align="center">

![el-mehasin-vel-ezdad Banner](assets/banner.svg)

# el-mehasin-vel-ezdad (كِتَابُ المَحَاسِنِ وَالأَضْدَادِ)

[![Validator](https://img.shields.io/badge/Validator-Passing-10b981?style=for-the-badge&logo=checkmarx)](scripts/validator.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](LICENSE)
[![Corpus](https://img.shields.io/badge/Dialectic_Pairs-10_Pairs-6366f1?style=for-the-badge)](#-eserden-metin-içi-seçkiler-ve-diyalektik-kutuplar)
[![Format](https://img.shields.io/badge/Data_Format-JSONL%20%7C%20HuggingFace-ec4899?style=for-the-badge)](data/)

> **"Kelimeler zıtlarıyla tartılır; hakikat, iki ucun geriliminde parıldar."**  
> Bu depo; klasik Arap adab külliyatının, belagat teorisinin ve erken dönem İslam rasyonalizminin en çarpıcı türlerinden biri olan **Mehâsin ve Mesâvî / Ezdâd** (Güzellikler-Kusurlar / Karşıtlıklar) literatürünü; tenkitli metin neşirleri, tarihsel şerhler, modern edebi eleştiriler ve yapılandırılmış diyalektik veri modelleriyle dijital çağa aktaran kapsamlı bir beşeri bilimler (Digital Humanities) ve hesaplamalı retorik korpusudur.

</div>

---

## 📖 İçindekiler

1. [Proje Vizyonu ve Kapsamı](#-proje-vizyonu-ve-kapsamı)
2. [Tarihsel ve Felsefi Arka Plan](#-tarihsel-ve-felsefi-arka-plan)
3. [Tarihçiler, Müsteşrikler ve Edebi Tenkitçiler Ne Dedi?](#-tarihçiler-müsteşrikler-ve-edebi-tenkitçiler-ne-dedi)
4. [Eserden Metin İçi Seçkiler ve Diyalektik Kutuplar](#-eserden-metin-içi-seçkiler-ve-diyalektik-kutuplar)
   * [1. Sükût (Susmak) vs. Kelâm (Konuşmak/Beyân)](#1-sükût-susmak-vs-kelâm-konuşmakbeyân)
   * [2. Cûd (Cömertlik) vs. Buhl (Cimrilik/Tasarruf)](#2-cûd-cömertlik-vs-buhl-cimriliktasarruf)
   * [3. Şecâat (Cesaret) vs. Cübn/Hazm (Korkaklık/İhtiyat)](#3-şecâat-cesaret-vs-cübnhazm-korkaklıkihtiyat)
   * [4. Işk (Tutkulu Aşk) vs. Silvân (Unutuş/Akılcılık)](#4-ışk-tutkulu-aşk-vs-silvân-unutuşakılcılık)
   * [5. Vefâ (Bağlılık) vs. Gadîze (Hıyanet/Mesafe)](#5-vefâ-bağlılık-vs-gadîze-hıyanetmesafe)
   * [6. İlim (Hikmet) vs. Rahatü'l-Cehl (Cehaletin Konforu)](#6-ilim-hikmet-vs-rahatül-cehl-cehaletin-konforu)
   * [7. Uzlet (İnzivâ) vs. Hılta (Toplumsallık/Muâşeret)](#7-uzlet-inzivâ-vs-hılta-toplumsallıkmuâşeret)
   * [8. Medih (Övgü) vs. Hiciv (Yergi/Teşhir)](#8-medih-övgü-vs-hiciv-yergiteşhir)
   * [9. Sabır (Metanet) vs. Ceze' (Kederin İfşası)](#9-sabır-metanet-vs-ceze-kederin-ifşası)
   * [10. Tevâzu (Mahviyet) vs. Kibr ale'l-Mütekebbirîn (İzzet)](#10-tevâzu-mahviyet-vs-kibr-alel-mütekebbirîn-izzet)
5. [Diyalektik Kutuplar Karşılaştırma Matrisi](#-diyalektik-kutuplar-karşılaştırma-matrisi)
6. [Edebi Tür Olarak "Mehâsin ve Mesâvî"nin Morfolojisi](#-edebi-tür-olarak-mehâsin-ve-mesâvînin-morfolojisi)
7. [Depo Mimarisi ve Veri Şeması](#-depo-mimarisi-ve-veri-şeması)
8. [Katkı Sağlama ve İnceleme Süreci](#-katkı-sağlama-ve-inceleme-süreci)
9. [Bibliyografya ve Kaynakça](#-bibliyografya-ve-kaynakça)

---

## 🎯 Proje Vizyonu ve Kapsamı

Tarih boyunca Ebû Osmân Amr b. Bahr el-Câhiz’e (ö. 255/869) nispet edilen, ancak metin tenkidi çalışmalarıyla İbrâhim b. Muhammed el-Beyhakî (ö. IV./X. yüzyıl) ve meçhul müelliflerin katkılarıyla şekillendiği anlaşılan *Kitâbü'l-Mehâsin ve'l-Ezdâd*, basit bir nasihatnâme veya fıkra derlemesi değildir. 

Bu külliyat:
* **İki Kutuplu Mantık (Bipolar Dialectic):** Bir tezin zıddı olmadan tam olarak kavranamayacağını savunan bir zihin jimnastiğidir.
* **Retorik Akrobasisi:** Dönemin vezir, kâtip ve nedimlerinin meclislerde sergilediği münazara çevikliğinin yazılı belgesidir.
* **Modern NLP İçin Altın Maden:** Zıt kutuplu argüman madenciliği (argument mining), anlamsal tersinirlik (semantic antonymy), duygu analizi kutuplaşması ve retorik figürlerin formel ontolojisi için eşsiz bir laboratuvardır.

Bu deponun amacı, eserin orijinal Arapça nüsahını, satır arası Türkçe ve İngilizce akademik çevirileriyle eşlemek; ardından her bir tematik başlığı tez, antitez, delil türü ve retorik ağırlık bağlamında JSONL/YAML formatında makinece işlenebilir kılmaktır.

---

## 🏛️ Tarihsel ve Felsefi Arka Plan

Abbâsî hilafetinin başkenti Bağdat, sadece askeri ve idari bir merkez değil; Grek mantığının, Fars bürokratik *adab* geleneğinin ve Arap şiir zevkinin çarpıştığı küresel bir düşünce kazanıydı. Mutezile kelâmının tartışma kültürünü şekillendirdiği bu çağda, bir fikrin savunulması kadar, onun tam zıddının da meşru delillerle (kıyas, ayet, rivayet, şiir) temellendirilebilmesi bir entelektüel erdem sayılıyordu.

*el-Mehâsin ve'l-Ezdâd*, tam olarak bu iklimin mahsulüdür. Eser, tek boyutlu bir ahlak vaaz etmek yerine; insan tabiatının, toplumsal şartların ve bağlamın getirdiği değişkenliği gözler önüne serer. Cömertlik kural olarak övülür; ancak yerinde yapılmayan cömertlik ahmaklık ve mülkün ziyanı olarak yerilir. Suskunluk bilgelik olarak yüceltilir; fakat hakkı haykırmayan suskunluk cehalet ve dilsizlik olarak mahkûm edilir.

---

## 💬 Tarihçiler, Müsteşrikler ve Edebi Tenkitçiler Ne Dedi?

Eser ve temsil ettiği gelenek hakkında Doğu ve Batı ilim dünyasının önde gelen isimlerinin değerlendirmeleri:

> **Gerlof van Vloten (Hollandalı Şarkiyatçı, Eserin İlk Modern Editörü - 1898):**  
> *"Bu eser, Doğuluların zıt kavramları ele alışındaki müstesna esnekliği ve belagat dehasını belgeler. Yazar, bir yandan en ulvi ahlaki faziletleri göklere çıkarırken, hemen ardından aynı kavramın yıkıcı sonuçlarını öyle bir ustalıkla sergiler ki, okuyucu hakikatin tek bir kutba hapsedilemeyeceğini hayretle idrak eder."*

> **İbn Hallikân (Vefeyâtü'l-A'yân Müellifi):**  
> *"Câhiz ve onun yolundan giden edebiyat ustaları, sözü diledikleri gibi evirip çevirmekte mahirdirler. Bir şeyi hem överler hem de yererler; her iki halde de dinleyeni büyüler, delillerinin kuvveti karşısında muhatabı hayrete düşürürler."*

> **Charles Pellat (The Encyclopaedia of Islam / Câhiz Uzmanı):**  
> *"Mehâsin ve Mesâvî edebiyatı, klasik Arap nesrinin en tipik adab türlerinden biridir. Bu türün amacı mutlak bir ahlak felsefesi kurmak değil; saray ve meclis muhitindeki kâtiplere her iki tarafı da eşit belagatle savunabilecekleri zihinsel teçhizatı ve dilsel cephaneyi kazandırmaktır."*

> **Prof. Dr. Şinasi Gündüz / Klasik Edebiyat Araştırmacıları:**  
> *"Câhiz’e atfedilen Mehâsin ve'l-Ezdâd, zıtların birliğinden ziyade zıtların çatışmasındaki estetiği hedefler. Arapça'daki zıt anlamlı kelimeler (ezdâd) mantığı ile insanın ahlaki eylemleri arasındaki paralellik bu eserde somutlaşır. İnsan tek bir erdemle tanımlanamaz; şartların doğurduğu karşıtlıklar bütünüdür."*

> **Regis Blachère (Arap Edebiyatı Tarihçisi):**  
> *"Bu metinler, ortaçağ İslam dünyasında diyalektiğin ve sofistike münazaranın bir oyuna, yüksek bir sanat formuna dönüşmüş halidir. Burada ahlak, dilin ve zekânın emrine girmiştir."*

---

## 📜 Eserden Metin İçi Seçkiler ve Diyalektik Kutuplar

Aşağıda, eserde yer alan 10 temel kavramsal ikiliğin orijinal metin mantığına, şiir şahitlerine (*şevâhid*) ve klasik nakillere sadık kalınarak derlenmiş örnek dökümleri yer almaktadır.

---

### 1. Sükût (Susmak) vs. Kelâm (Konuşmak/Beyân)

#### 🟢 Mehâsinü's-Samt (Susmanın Güzellikleri ve Erdemleri)
> **Metinden İktibas:**  
> *"Bil ki suskunluk, emniyet libasıdır ve vakar süsüdür. İnsana pişmanlık getirmeyen tek şey, söylemediği sözdür. Lokman Hekim oğluna şöyle demiştir: 'Ey oğul! Söz gümüş ise, sükût altındır. Konuştuğum zaman defalarca pişman oldum, fakat sustuğum için bir kez bile nedamet getirmedim.'  
> Şairin dediği gibi:  
> *يموت الفتى من عثرة بلسانه *** وليس يموت المرء من عثرة الرِّجلِ*  
> *(Yiğit ayağı sürçtüğü için değil, dili sürçtüğü için helak olur!)*  
> Susmak, cahil için perde, âlim için zinet ve heybettir."*

#### 🔴 Mehâsinü'l-Kelâm / Zemmü's-Samt (Konuşmanın Fazileti ve Susmanın Yergisi)
> **Metinden İktibas:**  
> *"Fakat bir topluluk çıkıp suskunluğu mutlak fazilet sandı da yanıldı. Kelâm olmasaydı hikmet nereden bilinir, hak batıldan nasıl ayrılırdı? Allah Teâlâ insanı 'nutk' (konuşma ve akletme) ile şereflendirmiş, 'İnsanı yarattı ve ona beyânı öğretti' buyurmuştur. Dilsizlik ve acizlik bir erdem sayılamaz.  
> Hz. Ali (k.v.) şöyle buyurmuştur:  
> *تكلموا تُعرفوا، فإن المرء مخبوء تحت طي لسانه لا طيلسانه*  
> *(Konuşunuz ki bilinesiniz; zira insan sarığının değil, dilinin kıvrımları altında gizlidir.)*  
> Hakkı açıklamaktan kaçınarak susan kimse dilsiz şeytandır. Konuşmak nurdur; suskunluk ise o nurun üzerini örten karanlık bir örtüdür."*

---

### 2. Cûd (Cömertlik) vs. Buhl (Cimrilik/Tasarruf)

#### 🟢 Mehâsinü'l-Cûd ve's-Sehâ (Cömertliğin Övgüsü)
> **Metinden İktibas:**  
> *"Cömertlik öyle bir erdemdir ki, sahibinin diğer bütün ayıplarını ve kusurlarını örter. Hâtem et-Tâî malını mülkünü dağıtıp aç yattığında ona sitem eden karısına şöyle demiştir:  
> *أماويّ إن المال غادٍ ورائحٌ *** ويبقى من المال الأحاديث والذكرُ*  
> *(Beni kınama ey kadın! Zira zenginlik gelir ve gider; fakat arkada bırakılan güzel övgü ve asil nam baki kalır.)*  
> Kerem sahibi insanın malı tükense de şerefi artar. Cömert kimse Allah’a yakın, insanlara yakın, cennete yakın ve cehennemden uzaktır."*

#### 🔴 Mehâsinü'l-Buhl ve'l-İktisâd (Tasarrufun/Cimriliğin Müdafaası)
> **Metinden İktibas:**  
> *"İnsanlar bönce bir cömertliği övüp dururlar; oysa ceplerini boşaltıp çocuklarını muhtaç bırakan kimsenin sonu zillet ve pişmanlıktır. Akıllı kişi odur ki, varlık zamanında yokluk gününü hesaba katar.  
> Câhiz'in aktardığına göre:  
> *'Mal senin asaletindir, şerefindir ve hürriyetindir. Malın tükendiğinde dostların düşman, hürmet edenlerin alaycı olur.'*  
> Hadis-i şerifte buyrulmuştur: *'Tasarruf eden darlığa düşmez.'* Ziyan edilen her dirhem, insanın boynuna vurulacak bir kölelik zinciridir."*

---

### 3. Şecâat (Cesaret) vs. Cübn/Hazm (Korkaklık/İhtiyat)

#### 🟢 Mehâsinü'ş-Şecâa (Cesaretin Fazileti)
> **Metinden İktibas:**  
> *"Cesaret, ruhun izzeti ve nefsin ölüm korkusuna galebe çalmasıdır. Korkak kimse günde bin defa ölür; cesur insan ise eceli geldiğinde ancak bir kez ölümü tadar.  
> Şair el-Mütenebbî ne güzel haykırır:  
> *إذا غامَرْتَ في شَرَفٍ مَرُومِ *** فَلا تَقنَعْ بما دونَ النّجُومِ*  
> *فطَعْمُ المَوْتِ في أمْرٍ حَقِيرٍ *** كطَعْمِ المَوْتِ في أمْرٍ عَظِيمِ*  
> *(Eğer yüce bir şerefe talip olduysan, yıldızların altındaki hiçbir bayağılığa razı olma! Zira küçük bir iş uğruna ölmenin tadı ne ise, büyük bir gaye uğruna ölmenin tadı da birdir.)*"*

#### 🔴 Mehâsinü'l-Hazm / Zemmü't-Tehevvür (Tedbir ve Canı Muhafaza Etmenin Övgüsü)
> **Metinden İktibas:**  
> *"Cesaret ile körü körüne helake koşmak (tehevvür) arasında ince bir çizgi vardır. Kendini boş yere ateşe atan adam yiğit değil, delidir. İhtiyat (hazm), aklın kalkanıdır.  
> Ahnef b. Kays der ki: *'İhtiyat, rehavete kapılmayıp tedbiri elden bırakmamaktır.'*  
> Mütenebbî de bu hakikati ikrar eder:  
> *الرأي قبل شجاعة الشجعان *** هو أول وهي المحل الثاني*  
> *(Stratejik akıl ve basiret, yiğitlerin cesaretinden önce gelir; akıl başta, cesaret ikinci sıradadır.)*"*

---

### 4. Işk (Tutkulu Aşk) vs. Silvân (Unutuş/Akılcılık)

#### 🟢 Mehâsinü'l-Işk (Aşkın Ruhu Yüceltmesi)
> **Metinden İktibas:**  
> *"Aşk, kaba ruhları incelten, cimriyi cömert kılan, korkağa cesaret aşılayan ilahi bir iksirdir. Âşık olmayan insan, taşlaşmış bir kalbe ve hissiz bir bedene mahkûmdur.  
> Eserde nakledilir ki:  
> *'Aşk öyle bir ateştir ki, nefsin kirlerini yakar; geriye saf ve latif bir cevher bırakır. Seven insan, sevdiğinin aynasında kemale erer.'*  
> Mecnûn-ı Âmirî haykırır: *'Benim saadetim ancak onun aşkıyla çektiğim çilededir!'*"*

#### 🔴 Mesâvîü'l-Işk ve Mehâsinü's-Silvân (Aşkın Helaki ve Aklın Kurtuluşu)
> **Metinden İktibas:**  
> *"Aşk bir hastalıktır, aklın felcidir ve kalbin zindan edilmesidir. Aşk batağına saplanan kimse; iradesini bir fani hevese teslim eder, izzetini kaybeder, melankoli ve keder içinde helak olur.  
> Eflâtun şöyle demiştir: *'Aşk, boş kalan ve gayesi olmayan nefislerin marazıdır.'*  
> Kurtuluş ise 'silvân'da (unutuş, teselli ve metanet) ve aklın dizginlerini yeniden ele alıp nefsi özgürleştirmektedir."*

---

### 5. Vefâ (Bağlılık) vs. Gadîze (Hıyanet/Mesafe)

#### 🟢 Mehâsinü'l-Vefâ (Dostluk ve Ahde Vefa)
> **Metinden İktibas:**  
> *"Vefa, asil ruhların alametidir. Ahdine sadık kalmayan kimsenin dini de mürüvveti de eksiktir. Semev’el b. Âdiyâ’nın, emanet edilen zırhları korumak uğruna kendi evladının gözleri önünde katledilmesine razı olması darb-ı mesel olmuştur: 'Semev'el'den daha vefalı.'  
> İmam Şâfiî uyarır: *'Rüzgar nereden eserse oraya meyleden dalkavuğun dostluğunda hiçbir hayır yoktur.'*"*

#### 🔴 Zemmü'l-İğtirâr bi'n-Nâs (İnsanlara Aşırı Güvenin Yergisi ve Tedbir)
> **Metinden İktibas:**  
> *"Lakin bu zamanda vefa beklemek, çölde serap aramaya benzer. İnsanların ahdine güvenip zırhını çıkaran kimse, ilk fırsatta sırtından hançerlenir.  
> İbnü'l-Mu'tez şöyle ihtar eder:  
> *احذر عدوك مرة واحذر صديقك ألف مرة *** فلربما انقلب الصديق فكان أعلم بالمضرة*  
> *(Düşmanından bir kez sakın, fakat dostundan bin kez sakın! Zira dostun düşmana dönerse sana nereden vuracağını en iyi o bilir.)*"*

---

### 6. İlim (Hikmet) vs. Rahatü'l-Cehl (Cehaletin Konforu)

#### 🟢 Mehâsinü'l-İlm (İlmin Yüceliği)
> **Metinden İktibas:**  
> *"İlim, insanın yeryüzündeki hilafet tacı ve iki cihan saadetinin anahtarıdır.  
> Hz. Ali (k.v.) şöyle buyurur:  
> *العلم يرفع بيتاً لا عماد له *** والجهل يهدم بيت العز والشرف*  
> *(İlim, direksiz haneleri göklere yükseltir; cehalet ise şeref ve asalet köşklerini yıkar.)*"*

#### 🔴 Rahatü'l-Cehl ve Âfâtü'l-İlm (Cehaletin Rahatlığı ve İlmin Hüznü)
> **Metinden İktibas:**  
> *"Fakat ilim, sahibine derin bir varoluşsal sancı, ağır bir mesuliyet ve dinmeyen bir keder yükler.  
> Şair el-Mütenebbî ne acı söyler:  
> *ذو العقل يشقى في النعيم بعقله *** وأخو الجهالة في الشقاوة ينعم*  
> *(Akıl sahibi, nimetler içinde dahi aklının getirdiği kederle kıvranır; cahil kimse ise sefaletin ortasında gamsızca keyif sürer.)*"*

---

### 7. Uzlet (İnzivâ) vs. Hılta (Toplumsallık/Muâşeret)

#### 🟢 Mehâsinü'l-Uzle (Yalnızlığın Fazileti)
> **Metinden İktibas:**  
> *"Uzlet, dedikodudan, riyadan ve insanların şerrinden korunma kalesidir. Fudayl b. İyâz der ki: 'Yalnızlık, kötü arkadaşların eziyetinden kurtuluş ve dinin zırhıdır.' İnsanın kalbi ancak halvette sükun bulur."*

#### 🔴 Mehâsinü'l-Hılta (Toplumun ve Cemaatin Fazileti)
> **Metinden İktibas:**  
> *"İnsan tek başına eksiktir; hayır, cihad ve ilim ancak toplumla kaimdir. Hadis-i şerifte teyit edildiği üzere: 'İnsanların arasına karışıp eziyetlerine sabreden mümin, köşesine çekilenden katbekat hayırlıdır.' Kişi dostlarıyla çoğalır."*

---

### 8. Medih (Övgü) vs. Hiciv (Yergi/Teşhir)

#### 🟢 Mehâsinü'l-Medh (Övgünün Fazileti)
> **Metinden İktibas:**  
> *"Hak edilmiş övgü, fazilet tohumlarını yeşerten bir bahar yağmurudur. Kâ'b b. Züheyr'in Resûlullah'ı (s.a.v.) övdüğü 'Bânet Suâd' kasidesi, adaletin ve hakkın teslimiyet belgesidir. İyiliği övmek, toplumu iyiliğe sevk eder."*

#### 🔴 Mehâsinü'l-Hicâ (Hicvin Caydırıcılığı)
> **Metinden İktibas:**  
> *"Zalimleri ve hasisleri dizginleyen yegane kamçı hicivdir. Hassân b. Sâbit'in dili, müşriklere kılıç darbelerinden daha ağır gelmiştir. Şairin dediği gibi: 'Asil kimseye ikram edersen kazanırsın, alçak kimseye ikram edersen azar!' Alçağın hakkı hicivdir."*

---

### 9. Sabır (Metanet) vs. Ceze' (Kederin İfşası)

#### 🟢 Mehâsinü's-Sabr (Sabrın Fazileti)
> **Metinden İktibas:**  
> *"Sabır imanın başıdır. Kur'an-ı Kerim'de müjdelenmiştir: 'Sabredenlere ecirleri hesapsız ödenecektir.' Hz. Ali (r.a.) der ki: 'Sabır, imanın bedenindeki baş gibidir; başı kopanın imanı kalmaz.'"*

#### 🔴 Mehâsinü'l-Ceze' ve't-Teessüf (Hüznü Dışa Vurmanın Rahatlığı)
> **Metinden İktibas:**  
> *"Acıyı içine gömmek kalbi zehirler. Hz. Yakub (a.s.) 'Ben hüznümü ancak Allah'a arz ederim' diyerek ağlamıştır. Gözyaşı rahmettir; fıtri bir arınma ve kalpteki keder volkanını söndürme vesilesidir."*

---

### 10. Tevâzu (Mahviyet) vs. Kibr ale'l-Mütekebbirîn (İzzet)

#### 🟢 Mehâsinü't-Tevâzu (Tevazuun Güzelliği)
> **Metinden İktibas:**  
> *"Tevazu büyüklüğün ziynetidir. 'Kim Allah için tevazu gösterirse Allah onu yüceltir.'  
> *تواضع تكن كالنجم لاح لناظرٍ *** على صفحات الماء وهو رفيعُ*  
> *(Tevazu göster ki, suyun yüzeyinde parıldayan fakat göğün zirvesinde duran yıldız gibi olasın!)*"*

#### 🔴 Mehâsinü'l-Kibr ale'l-Mütekebbirîn (Kibirlilere Karşı İzzet)
> **Metinden İktibas:**  
> *"Zalimlere ve kibirlilere tevazu göstermek zillet ve ahmaklıktır. 'Kibirlenene kibir göstermek sadakadır.' Amr b. Külsum'un haykırdığı gibi: 'Kimse bize cahillik taslamasın; yoksa cahillerin cehaletini katbekat aşarız!'"*

---

## ⚖️ Diyalektik Kutuplar Karşılaştırma Matrisi

| # | Tematik Başlık | 🟢 Tez (El-Mehâsin) | 🔴 Antitez (El-Ezdâd / El-Mesâvî) | ⚖️ Diyalektik Sentez |
|---|---|---|---|---|
| **01** | Sükût & Kelâm | es-Samt (Vakar ve Selamet) | el-Beyân (Nutk ve Hakikat) | Cahilin yanında sükût, âlimin yanında kelâm. |
| **02** | Cömertlik & Cimrilik | el-Cûd (Îsâr ve Ebedi Nam) | el-İktisâd (Mülkün Muhafazası) | İsraf ve hasislikten uzak orta yol (sehâ). |
| **03** | Cesaret & İhtiyat | eş-Şecâa (İzzet ve Yiğitlik) | el-Hazm (Stratejik Tedbir) | Akıl ve basiret ile taçlandırılmış cesaret. |
| **04** | Aşk & Silvân | el-Işk (Ruhun İncelmesi) | es-Silvân (Aklın Hürriyeti) | Estetik arınma ile nefsi dizginleme muvazenesi. |
| **05** | Vefâ & Temkin | el-Vefâ (Ahde Sadakat) | Zemmü'l-İğtirâr (İhtiyat) | Ahde sadık kalırken hüsn-i zanda körleşmemek. |
| **06** | İlim & Cehalet | el-İlm (Ruhun Nuru ve Rütbe) | Rahatu'l-Cehl (Kederden Azat) | Kederi kulluk şuuruna dönüştüren hakiki marifet. |
| **07** | Uzlet & Muâşeret | el-Uzle (Kalp Selameti) | el-Hılta (Cemaat ve Hizmet) | Kalben halvet, fiilen toplum içinde hizmet. |
| **08** | Medih & Hiciv | el-Medh (Fazileti Teşvik) | el-Hicâ (Zulmü Teşhir) | Hak edene medih, haddi aşana caydırıcı hiciv. |
| **09** | Sabır & Teessüf | es-Sabr (Ruhun Zırhı) | el-Ceze' (Fıtri Arınma) | İsyansız gözyaşı ve kadere mutlak rıza. |
| **10** | Tevâzu & İzzet | et-Tevâzu (Mahviyet) | el-Kibr (Zalime Karşı Dik Duruş) | Mümin kardeşe tevazu, mütekebbire izzet. |

---

## 🔬 Edebi Tür Olarak "Mehâsin ve Mesâvî"nin Morfolojisi

Bir bölümün kurgusu, klasik retorik mimarisine göre şu dört kademeli döngüyü takip eder:

```text
[Kavram: X]
   │
   ├── 1. KUTUP: EL-MEHÂSİN (Övgü & Teşvik)
   │     ├── Kur'an ve Hadis Delilleri / Sahabe Sözleri
   │     ├── Tarihsel Örnek Olaylar (Abbâsî/Emevî Anekdotları)
   │     ├── Şiir Şahitleri (Şevâhid) ve İkna Edici Meseller
   │     └── Felsefi/Ahlaki Çıkarım
   │
   └── 2. KUTUP: EL-MESÂVÎ / EL-EZDÂD (Yergi & İtiraz)
         ├── Karşı-Ayet ve Rivayet Yorumları (Bağlamsal Kısıtlama)
         ├── Felaketle Biten Tarihi Vakalar ve İbretlik Kıssalar
         ├── Hiciv ve Realist Şiirler
         └── Realist/Pragmatik Çıkarım
```

---

## 💻 Depo Mimarisi ve Veri Şeması

```plaintext
el-mehasin-vel-ezdad/
├── assets/
│   └── banner.svg                  # Proje vektörel tanıtım görseli
├── corpus/
│   ├── arabic_raw/                 # Matbu neşirlerin OCR edilmiş ham halleri (10 Bölüm)
│   ├── turkish_annotated/          # Açıklamalı Türkçe çeviri metinleri (10 Bölüm)
│   └── english_reference/          # Terminoloji ve kavram sözlüğü
├── data/
│   ├── dialectic_pairs.jsonl       # Bütün tez-antitez kayıtlarının yapılandırılmış hali (10 Çift)
│   ├── hf_dataset_export.json      # Hugging Face için düzleştirilmiş veri
│   └── taxonomy_ontology.json     # Adab, ahlak ve belagat kavramlar hiyerarşisi
├── schemas/
│   └── dialectic_entry.schema.json # JSON Schema doğrulaması
├── scripts/
│   ├── validator.py                # Şema doğrulayıcı ve veri tutarlılık denetçisi
│   └── export_huggingface.py       # Korpusu HF Dataset formatına çevirici
├── notebooks/
│   ├── rhetoric_vector_search.ipynb# Anlamsal zıtlıkların vektörel analizi
│   └── sentiment_polarity.ipynb    # Metin kutupluluk skorlaması
├── LICENSE
└── README.md
```

---

## 🛠️ Katkı Sağlama ve İnceleme Süreci

1. Depoyu forklayın (fork).
2. Yeni bir dal açın: `git checkout -b feature/yeni-kutup-eklemesi`.
3. Eserden seçtiğiniz metin çiftini `corpus/` altına ekleyin ve `data/dialectic_pairs.jsonl` dosyasına şemaya uygun biçimde işleyin.
4. Doğrulama testini çalıştırın:
   ```bash
   python scripts/validator.py
   ```
5. Dalınızı gönderin (push) ve bir Pull Request oluşturun.

---

## 📚 Bibliyografya ve Kaynakça

* **el-Câhiz (atfedilen):** *Kitâbü'l-Mehâsin ve'l-Ezdâd*, thk. Gerlof van Vloten, Leiden: E.J. Brill, 1898.
* **el-Beyhakî, İbrâhim b. Muhammed:** *el-Mehâsin ve'l-Mesâvî*, thk. Muhammed Ebü'l-Fazl İbrâhim, Kahire: Dârü'l-Maârif, 1961.
* **Pellat, Charles:** "al-Djāḥiẓ", *The Encyclopaedia of Islam (New Edition)*, Leiden: E.J. Brill.
* **Gündüz, Şinasi:** *Klasik Arap Edebiyatında Mehâsin ve Mesâvî Türü ve Mahiyeti*, Ankara Üniversitesi İlahiyat Fakültesi Yayınları.
* **van Gelder, Geert Jan:** *The Bad and the Ugly: Attitudes Towards Invective (Hija') in Classical Arabic Literature*, E.J. Brill, 1988.
