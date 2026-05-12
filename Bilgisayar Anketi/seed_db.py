import os
import django
from django.utils import timezone
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Category, Question, Choice
from django.contrib.auth.models import User

def seed_db():
    print("Veritabanı temizleniyor...")
    Question.objects.all().delete()
    Category.objects.all().delete()
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='kullanici').exists():
        print("Sistem kullanıcısı oluşturuluyor...")
        User.objects.create_superuser('kullanici', 'test@test.com', 'sifre123')
    
    # Create PC category
    print("Kategori oluşturuluyor...")
    cat_pc = Category.objects.create(name='Donanım & Yazılım', description='Bilgisayar dünyası hakkında sorular', icon='bi-pc-display-horizontal')
    cat_gaming = Category.objects.create(name='Oyun & Eğlence', description='Oyun dünyası soruları', icon='bi-controller')

    now = timezone.now()

    questions_data = [
        {
            "text": "Bilgisayar kullanmayı seviyor musun?",
            "category": cat_pc,
            "choices": ["Evet", "Hayır", "Biraz"]
        },
        {
            "text": "Hangi işletim sistemini daha çok tercih edersin?",
            "category": cat_pc,
            "choices": ["Windows", "macOS", "Linux"]
        },
        {
            "text": "Günde ortalama kaç saat bilgisayar başındasın?",
            "category": cat_pc,
            "choices": ["1-3 saat", "4-6 saat", "7+ saat"]
        },
        {
            "text": "Bilgisayarında en çok ne yaparsın?",
            "category": cat_gaming,
            "choices": ["Oyun oynamak", "Çalışma / Ders çalışma", "Film / Dizi izleme"]
        },
        {
            "text": "Kendi bilgisayarını toplayabilir misin?",
            "category": cat_pc,
            "choices": ["Evet, kendim toplarım", "Hayır, hazır alırım"]
        }
    ]

    print("Sorular ve şıklar ekleniyor...")
    for idx, q_data in enumerate(questions_data):
        pub_date = now - datetime.timedelta(minutes=idx)
        q = Question.objects.create(
            question_text=q_data["text"],
            pub_date=pub_date,
            category=q_data["category"],
            views=0
        )
        for c_text in q_data["choices"]:
            Choice.objects.create(question=q, choice_text=c_text, votes=0)

    print("Tebrikler! Veritabanı başarıyla tohumlandı (seeded).")
    print("Kullanıcı Adı: kullanici")
    print("Şifre: sifre123")

if __name__ == '__main__':
    seed_db()
