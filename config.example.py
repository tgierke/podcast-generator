"""
Configuration file for Automated Podcast Generator
Copy this file to config.py and fill in your API keys and settings
"""

# API Keys (Required)
GEMINI_API_KEY = "your_gemini_api_key_here"
ELEVEN_LABS_API_KEY = "your_eleven_labs_api_key_here"

# Podcast Settings
PODCAST_NAME = "The Music Publishing Beat"
PODCAST_DESCRIPTION = "A weekly roundup of major news in music publishing, relevant for executives in the music publishing industry"
PODCAST_AUTHOR = "The Music Publishing Beat"
PODCAST_CATEGORY = "Business"
PODCAST_LANGUAGE = "en-us"

# Target Audience
TARGET_AUDIENCE = "Music Publishing Executives"
AUDIENCE_LEVEL = "executive"  # executive, professional, general

# Content Settings
NEWS_TIMEFRAME_DAYS = 7
ARTICLES_PER_SEARCH = 50
MIN_RELEVANCE_SCORE = 6
TARGET_DURATION_MINUTES = 10
MAX_ARTICLES_PER_EPISODE = 15

# Industry Focus - Customize for your industry
INDUSTRY_COMPANIES = [
    "Hal Leonard LLC",
    "Alfred Music", 
    "Faber Music",
    "Carl Fischer Music",
    "Theodore Presser Company",
    "Schott Music",
    "Breitkopf & Härtel",
    "Wise Music Group",
    "Music Sales Group",
    "Bärenreiter Verlag",
    "Edition Peters",
    "JW Pepper",
    "G. Schirmer",
    "Kjos Music Company",
    "Belwin-Mills",
    "Boosey & Hawkes",
    "Oxford University Press",
    "Warner Chappell Music",
    "Universal Music Publishing",
    "Sheet Music Plus",
    "Yousician"
]

# Search Priorities (in order of importance)
SEARCH_PRIORITIES = [
    {
        "name": "Breaking industry news and major deals",
        "keywords": ["acquisition", "merger", "deal", "partnership", "investment"],
        "weight": 10
    },
    {
        "name": "Publishing company updates and executive moves", 
        "keywords": ["CEO", "executive", "appointment", "promotion", "hire"],
        "weight": 8
    },
    {
        "name": "Technology/AI developments affecting publishing",
        "keywords": ["AI", "artificial intelligence", "technology", "digital", "platform"],
        "weight": 7
    },
    {
        "name": "Market trends and financial reports",
        "keywords": ["revenue", "earnings", "market", "growth", "financial"],
        "weight": 6
    }
]

# Audio Settings
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Eleven Labs voice ID (Adam)
VOICE_MODEL = "eleven_monolingual_v1"
AUDIO_FORMAT = "mp3"

# Web Settings
WEB_HOST = "0.0.0.0"
WEB_PORT = 5000
DEBUG_MODE = False

# File Paths
AUDIO_OUTPUT_DIR = "static/audio"
IMAGES_OUTPUT_DIR = "static/images"
SCRIPTS_OUTPUT_DIR = "generated_scripts"

# RSS Feed Settings
RSS_FEED_URL = "/rss"
WEBSITE_BASE_URL = "https://yourpodcast.com"  # Update with your domain

# Content Generation Settings
SCRIPT_STYLE = "executive_briefing"  # executive_briefing, conversational, news_report
TTS_OPTIMIZED = True  # Optimize script for text-to-speech
INCLUDE_TIMESTAMPS = True
INCLUDE_EXECUTIVE_TAKEAWAYS = True

# Quality Control
ENABLE_CONTENT_FILTERING = True
MIN_ARTICLE_LENGTH = 100  # characters
MAX_ARTICLE_AGE_HOURS = 168  # 7 days
DUPLICATE_THRESHOLD = 0.8  # similarity threshold for duplicate detection

# Logging
LOG_LEVEL = "INFO"
LOG_FILE = "podcast_generator.log"
ENABLE_ANALYTICS = True

