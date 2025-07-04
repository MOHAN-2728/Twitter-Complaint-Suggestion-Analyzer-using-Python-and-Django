from django.db import models

class AnalysisResult(models.Model):
    tweet_text = models.TextField()
    language = models.CharField(max_length=10, default='unknown')
    result_type = models.CharField(max_length=20)
    category = models.CharField(max_length=50, null=True, blank=True)
    explanation = models.TextField(null=True, blank=True)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result_type} ({self.language}) - {self.tweet_text[:50]}"
