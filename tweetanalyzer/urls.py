from django.contrib import admin
from django.urls import path
from analyzer.views import analyze_tweet, download_csv, history_view
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('analyze')),
    path('analyze/', analyze_tweet, name='analyze'),
    path('history/', history_view, name='history'),
    path('download/', download_csv, name='download_csv'),
]
