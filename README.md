# 🐉 Discord Pokéball Bot

Bu proje, kullanıcıların Discord üzerinden Pokémon toplamasını, beslemesini ve birbirleriyle savaştırmasını sağlayan etkileşimli bir bottur.  
Pokémon verileri, [PokeAPI](https://pokeapi.co/) üzerinden gerçek verilerle çekilmektedir.

---

## 🚀 Özellikler

- 🎮 Her kullanıcı kendi Pokémon’unu oluşturabilir.  
- 🧩 Farklı türler: **Normal**, **Fighter** ve **Wizard** Pokémon türleri.  
- ⚔️ Pokémon’lar birbirleriyle savaşabilir.  
- 🍎 Pokémon’unuzu besleyerek canını artırabilirsiniz.  
- 🖼️ Pokémon’un resmi otomatik olarak API’den çekilir.

---

## 🧠 Proje Yapısı

```bash
.
├── logic.py   # Pokémon sınıfları, saldırı ve besleme mekanikleri
├── main.py    # Discord botunun komutları ve olayları
└── config.py  # Discord token'ının tutulduğu dosya (oluşturulmalı)
```

## 🧩 Kullanılan Teknolojiler

Python 3.10+

Discord.py (discord.ext.commands)

aiohttp (asenkron HTTP istekleri için)

PokeAPI (Pokémon verilerini almak için)


## ⚙️ Kurulum

Depoyu klonla:

git clone https://github.com/kullaniciadi/discord-pokemon-bot.git
cd discord-pokemon-bot


Gerekli kütüphaneleri yükle:
```bash


pip install discord aiohttp
```

config.py dosyasını oluştur:
```bash
# config.py
token = "DISCORD_BOT_TOKENINIZ"
```

Botu çalıştır:
```bash
python main.py
```


## 🕹️ Komutlar
| Komut                | Açıklama                                         |
| -------------------- | ------------------------------------------------ |
| `!go`                | Yeni bir Pokémon oluşturur.                      |
| `!feed`              | Pokémon’unuzu besler ve canını yeniler.          |
| `!attack @kullanıcı` | Belirtilen kullanıcıyla Pokémon savaşı başlatır. |
| `!sil`               | Mevcut Pokémon’unuzu siler.                      |



## ⚔️ Pokémon Türleri
| Tür                  | Özellik                                                       |
| -------------------- | ------------------------------------------------------------- |
| **Normal (Pokemon)** | Temel saldırı ve savunma istatistiklerine sahip.              |
| **Fighter**          | Saldırı sırasında ekstra güç kazanır.                         |
| **Wizard**           | Beslenme süresi daha kısa, savaşta kalkan kullanma şansı var. |


## 📸 Örnek Görsel
Her Pokémon’un resmi PokeAPI’den çekilir ve Discord mesajına gömülü olarak gönderilir:


## 🧾 Lisans

Bu proje MIT lisansı altında paylaşılmıştır.
Detaylar için LICENSE
dosyasına bakabilirsiniz.


