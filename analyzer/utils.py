import random
from langdetect import detect

# Extended complaint categories with Tamil & English keywords
COMPLAINT_KEYWORDS = {
    "garbage": ["garbage", "trash", "waste", "dump", "unclean", "overflowing bin", "குப்பை", "அழுக்கான", "அகற்றப்படவில்லை"],
    "water": ["water", "leak", "sewage", "drain", "pipe", "tap", "overflow", "நீர்", "கசிவு", "சுழற்சி", "கழிவுநீர்"],
    "road": ["road", "pothole", "hole", "damaged road", "broken street", "traffic", "pathway", "பாதை", "தெரு", "சேதமடைந்த"],
    "electricity": ["power", "electricity", "voltage", "current", "light", "street light", "மின்சாரம்", "வெளிச்சம்", "நிறுத்தம்"],
    "noise": ["noise", "loud", "speaker", "disturbance", "sound pollution", "சத்தம்", "அதிர்வெண்", "கவலை"],
    "stray animals": ["dogs", "stray", "barking", "monkeys", "bitten", "நாய்கள்", "அலைமோசடி", "குரல்", "தாக்குதல்"],
    "pollution": ["pollution", "smoke", "dust", "contamination", "தூசி", "மாசு", "மாசுபாடு"],
    "public toilet": ["toilet", "public toilet", "dirty toilet", "no toilet", "கழிவறை", "தூய்மை இல்லை", "கழிப்பறை"],
    "drainage": ["drainage", "block", "stagnant water", "clog", "overflow", "கழிவுநீர்", "தடை", "நீர் தேங்கி"],
    "waste collection": ["collector not coming", "waste pickup", "no collection", "சேகரிப்பு இல்லை", "குப்பை சேகரிக்க"]
}

# Suggestion keywords (Tamil & English)
SUGGESTION_KEYWORDS = [
    "should", "suggest", "recommend", "can you", "please consider", "better if", "propose",
    "நீங்கள் செய்யலாம்", "பரிந்துரை", "வழுக்கி", "சிறந்தது", "உரிய"
]

# Dynamic explanation generator
def generate_explanation(tweet, result_type, category):
    tweet_lower = tweet.lower()

    if result_type == "Suggestion":
        suggestions = [
            "This tweet proposes a positive change or idea for improvement.",
            "The user is offering a civic suggestion to enhance public service.",
            "A recommendation is being made, indicating a proactive citizen.",
        ]
        return random.choice(suggestions)

    if result_type == "Complaint":
        explanations = {
            "garbage": [
                "The tweet reports uncollected garbage, indicating sanitation issues.",
                "Mentions trash accumulation, possibly affecting cleanliness and health.",
                "The user is highlighting a need for waste removal in their area."
            ],
            "water": [
                "There seems to be a water leak or sewage overflow causing inconvenience.",
                "Mentions drainage or water stagnation — a sign of poor plumbing or maintenance.",
                "Indicates issues related to water supply or sanitation."
            ],
            "road": [
                "Refers to broken roads or potholes that can cause accidents or delays.",
                "Highlights road conditions that need urgent repair.",
                "Points to infrastructure damage, especially affecting transportation."
            ],
            "electricity": [
                "Tweet indicates streetlight or power supply issues affecting safety.",
                "Mentions a power outage or electrical fault that needs fixing.",
                "User complains about lack of lighting or voltage problems."
            ],
            "noise": [
                "Mentions loud sounds or disturbance, suggesting noise pollution.",
                "User is reporting discomfort caused by noise in a residential area.",
                "Possibly a complaint about public or private events being too loud."
            ],
            "stray animals": [
                "Concern raised about safety due to stray dogs or animals.",
                "Refers to uncontrolled stray animals affecting neighborhood safety.",
                "User is disturbed by barking or aggressive strays."
            ],
            "pollution": [
                "Complaint about air quality or environmental cleanliness.",
                "Indicates pollution from smoke or dust impacting health.",
                "Environmental concern raised due to visible contamination."
            ],
            "public toilet": [
                "Mentions lack of cleanliness or access in public toilets.",
                "Sanitation complaint about poorly maintained toilet facilities.",
                "Indicates unhygienic conditions affecting public convenience."
            ],
            "drainage": [
                "User reports stagnant water or blocked drains.",
                "Mentions overflowing or clogged drainage systems.",
                "Drainage issues are causing unsanitary conditions."
            ],
            "waste collection": [
                "Tweet implies that waste collection services are irregular or missing.",
                "The user points out that garbage is not being picked up.",
                "Indicates failure in routine waste management services."
            ],
            "general": [
                "The tweet contains dissatisfaction without matching known categories.",
                "It appears to be a general civic complaint.",
                "User is expressing a problem, but it’s uncategorized."
            ]
        }

        if category in explanations:
            return random.choice(explanations[category])

    return "Unable to classify tweet content with sufficient detail."

# Main classifier
def classify_tweet_ai(tweet):
    tweet_lower = tweet.lower()

    try:
        lang_code = detect(tweet)
        language = "Tamil" if lang_code == "ta" else "English"
    except:
        language = "unknown"

    if "@chennaicorp" not in tweet_lower:
        return language, "Invalid", None, "Tweet does not mention @chennaicorp"

    # Suggestion
    if any(keyword in tweet_lower for keyword in SUGGESTION_KEYWORDS):
        return language, "Suggestion", None, generate_explanation(tweet, "Suggestion", None)

    # Complaint
    for category, keywords in COMPLAINT_KEYWORDS.items():
        if any(keyword in tweet_lower for keyword in keywords):
            return language, "Complaint", category, generate_explanation(tweet, "Complaint", category)

    # General (fallback)
    return language, "General", "uncategorized", generate_explanation(tweet, "Complaint", "general")
