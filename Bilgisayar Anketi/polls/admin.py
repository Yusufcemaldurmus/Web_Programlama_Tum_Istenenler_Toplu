from django.contrib import admin

from .models import Choice, Question, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "icon"]
    search_fields = ["name"]


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text", "category"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
        ("Statistics", {"fields": ["views"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "category", "pub_date", "views", "was_published_recently"]
    list_filter = ["pub_date", "category"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
