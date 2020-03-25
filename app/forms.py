from django import forms
from .models import Visitor, Usage



YEARS = [ x for x in range(1940, 2045)]

class AddVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('fio','num','birthday','gender')
        labels = {
            'fio': 'ФИО',
            'num': 'Номер билета',
            'birthday': 'День рождения',
            'gender': 'Пол'
        }
        widgets = {
            'birthday': forms.SelectDateWidget(years=YEARS)
        }

class AddUsageForm(forms.ModelForm):
    class Meta:
        model = Usage
        fields = ('visitor','date_on','date_of','book_name','book_id','book_author')
        labels = {
            'visitor': "Посетитель",
            'date_on': "Дата обращения",
            'date_of': "Дата возврата",
            'book_name': 'Название книги',
            'book_id': "Номер книги",
            'book_author': "Автор книги"
        }
        widgets = {
            'date_on': forms.SelectDateWidget(years=YEARS),
            'date_of': forms.SelectDateWidget(years=YEARS)
        }