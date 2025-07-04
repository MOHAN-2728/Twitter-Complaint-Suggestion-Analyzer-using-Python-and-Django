from django.shortcuts import render
from django.http import HttpResponse
from .forms import TweetForm
from .models import AnalysisResult
from .utils import classify_tweet_ai
import csv

def analyze_tweet(request):
    result_type = category = language = explanation = None

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.cleaned_data['tweet']
            language, result_type, category, explanation = classify_tweet_ai(tweet)

            AnalysisResult.objects.create(
                tweet_text=tweet,
                language=language,
                result_type=result_type,
                category=category,
                explanation=explanation
            )
    else:
        form = TweetForm()

    recent_results = AnalysisResult.objects.order_by('-analyzed_at')[:5]

    return render(request, 'analyzer/form.html', {
        'form': form,
        'result_type': result_type,
        'category': category,
        'language': language,
        'explanation': explanation,
        'recent_results': recent_results
    })

def history_view(request):
    history = AnalysisResult.objects.order_by('-analyzed_at')[:20]
    return render(request, 'analyzer/history.html', {'history': history})

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="analysis_results.csv"'

    writer = csv.writer(response)
    writer.writerow(['Tweet', 'Language', 'Result Type', 'Category', 'Explanation', 'Analyzed At'])

    for result in AnalysisResult.objects.all():
        writer.writerow([
            result.tweet_text, result.language, result.result_type,
            result.category, result.explanation, result.analyzed_at
        ])

    return response
