from django.contrib import admin
from django.urls import path
from .views import UsagesView, VisitorsView, del_visitor, del_usage, HistoryView, change_visitor, change_usage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UsagesView),
    path('usages/', UsagesView, name="usages"),
    path('delusage/', del_usage, name="delusage"),
    path('visitors/', VisitorsView, name="visitors"),
    path('delvisitor/', del_visitor, name="delvisitor"),
    path('history/', HistoryView, name="history"),
    path('changevisitor/', change_visitor, name="changevisitor"),
    path('changeusage/', change_usage, name="changeusage"),
]
