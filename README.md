# AI Kelautan

AI chatbot khusus domain kelautan yang bisa menjawab pertanyaan dan mencari informasi terbaru secara otomatis dari internet.

## Cara Kerja

1. **Chat biasa** — langsung tanya apa saja tentang kelautan
2. **Auto web search** — jika pertanyaan lebih dari 3 kata, AI otomatis mencari data terbaru di internet
3. **Memori percakapan** — AI ingat konteks chat sebelumnya

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
```

Buka file `.env` dan isi API key kamu:

| Variabel | Deskripsi | Cara Dapatkan |
|----------|-----------|---------------|
| `OPENAI_API_KEY` | API key OpenAI | https://platform.openai.com/api-keys |
| `SERPAPI_KEY` | API key untuk pencarian web | https://serpapi.com (gratis 100 search/bulan) |
| `MODEL` | Model AI yang digunakan (default: gpt-4o-mini) | Bisa diganti gpt-4o, gpt-3.5-turbo, dll |

## Menjalankan

```bash
python main.py
```

## Perintah

| Perintah | Fungsi |
|----------|--------|
| `keluar` | Menghentikan aplikasi |
| `bersihkan` | Menghapus histori percakapan |

## Struktur Proyek

```
ai-kelautan/
├── main.py          # Entry point
├── requirements.txt # Dependencies
├── .env.example     # Template konfigurasi
├── data/            # Untuk menyimpan data kelautan (nanti bisa ditambah)
└── src/
    ├── chatbot.py   # Logika chatbot utama
    ├── web_search.py # Pencarian internet via SerpAPI
    ├── prompt.py    # Template sistem prompt
    └── history.py   # Manajemen memori percakapan
```

## Contoh Pertanyaan

- "Apa itu upwelling dan mengapa penting bagi ekosistem laut?"
- "Cara budidaya udang vannamei yang benar?"
- " Apa penyebab pemanasan laut?"
- "Jenis-jenis terumbu karang di Indonesia"
