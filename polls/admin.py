from django.contrib import admin
from .models import Question, Choice


# Register your models here.

# class ChoiceInLine(admin.StackedInline):
class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {"fields": ["pub_date"]}),
        # ("Data Informs", {"fields": ["question_text"], "classes": ['collapse']}), #collapse多了一个隐藏选项
        ("Data Informs", {"fields": ["question_text"]}),
    ]
    # inlines = [ChoiceInLine]
    inlines = (ChoiceInLine,)
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date', "question_text")
    search_fields = ('question_text',)


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)
