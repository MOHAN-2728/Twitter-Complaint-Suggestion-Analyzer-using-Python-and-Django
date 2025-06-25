from django.shortcuts import render
from .forms import TweetForm
from .models import AnalysisResult
from django.http import HttpResponse
import csv


COMPLAINT_KEYWORDS = ['bad', 'worst', 'problem', 'issue', 'not working', 'dirty', 'garbage', 'leak', 'pothole']
SUGGESTION_KEYWORDS = ['should', 'suggest', 'recommend', 'better if', 'could be better']
COMPLAINT_CATEGORIES = {
    'garbage': ['garbage', 'dirty', 'waste'],
    'road': ['road', 'pothole', 'traffic'],
    'water': ['water', 'leak', 'supply']
}

def classify_tweet(tweet):
    tweet = tweet.lower()
    if any(word in tweet for word in COMPLAINT_KEYWORDS):
        category = 'general'
        for key, keywords in COMPLAINT_CATEGORIES.items():
            if any(word in tweet for word in keywords):
                category = key
                break
        return 'Complaint', category
    elif any(word in tweet for word in SUGGESTION_KEYWORDS):
        return 'Suggestion', None
    return 'General', None

def analyze_tweet(request):
    result_type, category = None, None
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['tweet']
            result_type, category = classify_tweet(tweet)

            AnalysisResult.objects.create(
                tweet_text=tweet,
                result_type=result_type,
                category=category
            )
    else:
        form = TweetForm()

    recent_results = AnalysisResult.objects.order_by('-analyzed_at')[:5]

    return render(request, 'analyzer/form.html', {
        'form': form,
        'result_type': result_type,
        'category': category,
        'recent_results': recent_results
    })

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="analysis_results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tweet', 'Result Type', 'Category', 'Analyzed At'])

    results = AnalysisResult.objects.all()

    for result in results:
        writer.writerow([result.tweet_text, result.result_type, result.category, result.analyzed_at])

    return response