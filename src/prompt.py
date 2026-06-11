def build_prompt(question, search_results):
    if not search_results.strip():
        return question

    return f"""Kamu adalah AI ahli kelautan yang menjawab berdasarkan informasi terpercaya.

Berikut adalah hasil pencarian dari internet tentang pertanyaan pengguna,
Gunakan informasi ini untuk menjawab:

---
{search_results}
---

Pertanyaan pengguna: {question}

Jawab dalam bahasa Indonesia yang jelas dan informatif. Jika informasi di atas tidak cukup, katakan bahwa kamu belum menemukan data yang akurat."""
