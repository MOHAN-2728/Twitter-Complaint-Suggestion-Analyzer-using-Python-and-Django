from django.db import models

class AnalysisResult(models.Model):
    tweet_text = models.TextField()
    result_type = models.CharField(max_length=20)  # Complaint/Suggestion/Unclear
    category = models.CharField(max_length=50, null=True, blank=True)  # e.g., road, garbage
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.result_type} - {self.tweet_text[:50]}"
