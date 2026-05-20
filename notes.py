from datetime import datetime

print("📝 Kiber Kundalik Tizimi Yoqildi")
nota = input("Bugungi muhim qaydingizni yozing: ")

vaqt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("my_diary.txt", "a", encoding="utf-8") as f:
    f.write(f"📅 [{vaqt}]\n✍️ Qayd: {nota}\n" + "="*40 + "\n")

print("\n✅ Qaydingiz 'my_diary.txt' fayliga muvaffaqiyatli saqlandi!")