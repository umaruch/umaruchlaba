from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import Visitor, Usage
from .forms import AddVisitorForm, AddUsageForm


# Create your views here.
def del_usage(request):
    try:
        obj_id = int(request.GET.get('id'))
        Usage.objects.get(id=obj_id).delete()
    except:
        print("Error")
    return HttpResponseRedirect('/usages/')

def sort_usages(sort_settings):
    return Usage.objects.order_by(sort_settings)

def change_usage(request):
    if request.method == "POST":
        obj_id = int(request.POST.get("id"))
        usage = Usage.objects.get(id=obj_id)
        usage.visitor_id = request.POST.get("visitor")
        date_on = request.POST.get("date_on_year")+'-'+request.POST.get("date_on_month").zfill(2)+'-'+request.POST.get("date_on_day").zfill(2)
        usage.date_on = datetime.strptime(date_on, "%Y-%m-%d").date()
        date_of = request.POST.get("date_of_year")+'-'+request.POST.get("date_month").zfill(2)+'-'+request.POST.get("date_of_day").zfill(2)
        usage.date_of = datetime.strptime(date_of, "%Y-%m-%d").date()
        usage.book_name = request.POST.get("book_name")
        usage.book_id = request.POST.get("book_id")
        usage.book_author = request.POST.get("book_author")
        usage.save()
        return HttpResponseRedirect('/usages/')
    else:
        obj_id = request.GET.get('id')
        usage =  Usage.objects.get(id = obj_id);
        form = AddUsageForm(initial={
            'visitor': usage.visitor,
            'date_on': usage.date_on,
            'date_of': usage.date_of,
            'book_name': usage.book_name,
            'book_id': usage.book_id,
            'book_author': usage.book_author
        });
        return render(
            request,
            'form.html',
            {
                'form': form
            }
        )

def UsagesView(request):
    if request.method == "POST":
        form = AddUsageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/usages/')
    else:
        try:
            sort_settings = request.GET.get('sort')
            model = sort_usages(sort_settings)
        except:
            model = Usage.objects.all()
        form = AddUsageForm()
        return render(
            request,
            'usages.html',
            {'form': form , 'model': model}
        )

def HistoryView(request):
        obj_id = int(request.GET.get('id'))
        model = Usage.objects.filter(visitor = obj_id)
        form = AddUsageForm()
        return render(
            request,
            'usages.html',
            {'form': form , 'model': model}
        )


def del_visitor(request):
    try:
        obj_id = int(request.GET.get('id'))
        Visitor.objects.get(id=obj_id).delete()
    except:
        print("Error")
    return HttpResponseRedirect('/visitors/')

def sort_visitors(sort_settings):
    return Visitor.objects.order_by(sort_settings)

def change_visitor(request):
    if request.method == "POST":
        obj_id = int(request.POST.get("id"))
        visitor = Visitor.objects.get(id=obj_id)
        visitor.fio = request.POST.get("fio")
        date = request.POST.get("birthday_year")+'-'+request.POST.get("birthday_month").zfill(2)+'-'+request.POST.get("birthday_day").zfill(2)
        visitor.birthday = datetime.strptime(date, "%Y-%m-%d").date()
        visitor.gender = request.POST.get("gender")
        visitor.save()
        return HttpResponseRedirect('/visitors/')
    else:
        obj_id = request.GET.get('id')
        visitor =  Visitor.objects.get(id = obj_id);
        form = AddVisitorForm(initial={
            'fio': visitor.fio,
            'num': visitor.num,
            'birthday': visitor.birthday,
            'gender': visitor.gender
        });
        return render(
            request,
            'form.html',
            {
                'form': form
            }
        )

def VisitorsView(request):
    if request.method == "POST":
        form = AddVisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/visitors/')
    else:
        try:
            sort_settings = request.GET.get('sort')
            model = sort_visitors(sort_settings)
        except:
            model = Visitor.objects.all()
        form = AddVisitorForm()
        return render(
            request,
            'visitors.html',
            {'form': form , 'model': model}
        )

