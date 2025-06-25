def classify_tweet(tweet):
    tweet = tweet.lower()
    if '@chennaicorp' not in tweet:
        return "Invalid", None

    suggestion_keywords = ['should', 'suggest', 'recommend', 'can you']
    complaint_keywords = {
        'garbage': ['garbage', 'trash', 'waste'],
        'road': ['pothole', 'road', 'street'],
        'water': ['sewage', 'water', 'drain']
    }

    if any(k in tweet for k in suggestion_keywords):
        return "Suggestion", None

    for category, keywords in complaint_keywords.items():
        if any(k in tweet for k in keywords):
            return "Complaint", category

    return "Complaint", "general"
