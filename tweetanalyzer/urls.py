from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from analyzer.views import analyze_tweet
from analyzer.views import analyze_tweet, download_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze/', analyze_tweet, name='analyze'),
    path('', lambda request: redirect('analyze')),  
    path('download/', download_csv, name='download_csv'),
]
