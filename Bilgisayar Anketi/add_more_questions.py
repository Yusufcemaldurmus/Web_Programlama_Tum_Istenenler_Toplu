import os
import django
from django.utils import timezone
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from polls.models import Category, Question, Choice

def add_questions():
    now = timezone.now()
    cat_pc, _ = Category.objects.get_or_create(
        name='Donanım & Yazılım', 
        defaults={'description':'Bilgisayar dünyası hakkında sorular', 'icon':'bi-pc-display-horizontal'}
    )
    cat_gaming, _ = Category.objects.get_or_create(
        name='Oyun & Eğlence', 
        defaults={'description':'Oyun dünyası soruları', 'icon':'bi-controller'}
    )

    new_questions = [
        {
            "text": "Oyun oynarken en çok hangi türü tercih edersiniz?",
            "category": cat_gaming,
            "choices": ["FPS", "RPG", "Strateji", "MOBA"]
        },
        {
            "text": "Yeni bir bilgisayar alırken en çok neye önem verirsiniz?",
            "category": cat_pc,
            "choices": ["İşlemci (CPU)", "Ekran Kartı (GPU)", "RAM", "Depolama Alanı"]
        },
        {
            "text": "Sizce bir oyun bilgisayarı için ideal RAM boyutu nedir?",
            "category": cat_pc,
            "choices": ["8 GB", "16 GB", "32 GB", "64 GB ve üzeri"]
        },
        {
            "text": "Klavye tercihiniz nedir?",
            "category": cat_pc,
            "choices": ["Mekanik Klavye", "Membran Klavye", "Farketmez"]
        },
        {
            "text": "Bulut oyun platformları (GeForce Now, xCloud vb.) kullanıyor musunuz?",
            "category": cat_gaming,
            "choices": ["Sürekli kullanıyorum", "Arada bir", "Hiç kullanmadım"]
        }
    ]

    print("5 yeni soru ekleniyor...")
    for idx, q_data in enumerate(new_questions):
        pub_date = now - datetime.timedelta(minutes=idx)
        q = Question.objects.create(
            question_text=q_data["text"],
            pub_date=pub_date,
            category=q_data["category"],
            views=0
        )
        for c_text in q_data["choices"]:
            Choice.objects.create(question=q, choice_text=c_text, votes=0)

    print("Sorular eklendi!")

if __name__ == '__main__':
    add_questions()
