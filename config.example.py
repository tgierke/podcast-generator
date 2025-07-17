"""
Configuration Template for Automated Podcast Generator
Copy this file to config.py and customize for your industry
"""

# =============================================================================
# API KEYS (Required)
# =============================================================================

# Gemini AI for content generation
# Get your key at: https://makersuite.google.com/app/apikey
GEMINI_API_KEY = "your_gemini_api_key_here"

# ElevenLabs for text-to-speech
# Get your key at: https://elevenlabs.io
ELEVEN_LABS_API_KEY = "your_elevenlabs_api_key_here"

# =============================================================================
# PODCAST CONFIGURATION
# =============================================================================

# Basic podcast information
PODCAST_NAME = "The Music Publishing Beat"
PODCAST_DESCRIPTION = "A weekly roundup of major news in music publishing, relevant for executives in the music publishing industry"
HOST_NAME = "Tom Gierke"
HOST_EMAIL = "tgierke@gmail.com"

# =============================================================================
# INDUSTRY CONFIGURATION
# =============================================================================

# Target industry and companies
INDUSTRY_NAME = "Music Publishing"
TARGET_AUDIENCE = "Music publishing executives and decision-makers"

# Key companies to monitor (add your industry's major players)
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

# =============================================================================
# SEARCH CONFIGURATION
# =============================================================================

# Search priorities (1 = highest priority)
SEARCH_PRIORITIES = {
    1: {
        "name": "Breaking industry news and major deals",
        "terms": [
            f"{INDUSTRY_NAME} acquisition",
            f"{INDUSTRY_NAME} merger", 
            f"{INDUSTRY_NAME} deal",
            "music publishing acquisition",
            "music publishing merger"
        ]
    },
    2: {
        "name": "Publishing company updates and executive moves",
        "terms": [
            "music publishing executive",
            "music publishing CEO",
            "music publishing appointment",
            "music publishing promotion"
        ]
    },
    3: {
        "name": "Technology/AI developments affecting publishing",
        "terms": [
            "AI music publishing",
            "music publishing technology",
            "digital music publishing",
            "music publishing AI"
        ]
    },
    4: {
        "name": "Market trends and financial reports",
        "terms": [
            "music publishing market",
            "music publishing revenue",
            "music publishing trends",
            "music publishing industry report"
        ]
    }
}

# =============================================================================
# CONTENT GENERATION SETTINGS
# =============================================================================

# Content filtering
MAX_ARTICLE_AGE_DAYS = 7  # Only include articles from past 7 days
MIN_RELEVANCE_SCORE = 3   # Minimum relevance score (1-10)
MAX_ARTICLES_PER_EPISODE = 15  # Maximum articles to include

# Episode structure
TARGET_EPISODE_LENGTH_MINUTES = 8  # Target episode length
EPISODE_SEGMENTS = [
    "Breaking News & Major Deals",
    "Executive Moves & Strategic Updates", 
    "Technology & Innovation",
    "Market Intelligence & Trends",
    "Executive Takeaways"
]

# =============================================================================
# AUDIO SETTINGS
# =============================================================================

# ElevenLabs voice settings
VOICE_ID = "male_voice"  # or "female_voice"
VOICE_STABILITY = 0.75
VOICE_CLARITY = 0.75

# Audio processing
TRIM_INTRO_SECONDS = 0.5  # Seconds to trim from beginning
AUDIO_FORMAT = "mp3"
AUDIO_QUALITY = "high"

# =============================================================================
# WEBSITE CONFIGURATION
# =============================================================================

# Website branding
WEBSITE_TITLE = f"{PODCAST_NAME}"
WEBSITE_TAGLINE = "Weekly industry intelligence for music publishing executives"
BRAND_COLOR_PRIMARY = "#fbbf24"  # Golden yellow
BRAND_COLOR_SECONDARY = "#0f172a"  # Dark blue

# RSS feed settings
RSS_CATEGORY_PRIMARY = "Business"
RSS_CATEGORY_SECONDARY = "News"
RSS_LANGUAGE = "en-us"
RSS_COPYRIGHT = f"© 2025 {HOST_NAME}"

# =============================================================================
# DEPLOYMENT SETTINGS
# =============================================================================

# File paths
OUTPUT_DIRECTORY = "output"
STATIC_DIRECTORY = "static"
AUDIO_DIRECTORY = "static/audio"
IMAGES_DIRECTORY = "static/images"

# Deployment
AUTO_DEPLOY = True
DEPLOYMENT_PLATFORM = "manus"  # or your preferred platform

# =============================================================================
# EXAMPLE CONFIGURATIONS FOR OTHER INDUSTRIES
# =============================================================================

# Uncomment and modify for your industry:

# CONSTRUCTION INDUSTRY EXAMPLE
# INDUSTRY_NAME = "Construction"
# INDUSTRY_COMPANIES = ["Caterpillar", "John Deere", "Komatsu", "Volvo Construction"]
# SEARCH_PRIORITIES = {
#     1: {"name": "Construction deals", "terms": ["construction acquisition", "construction merger"]},
#     2: {"name": "Executive moves", "terms": ["construction executive", "construction CEO"]},
#     3: {"name": "Technology", "terms": ["construction technology", "construction AI"]},
#     4: {"name": "Market trends", "terms": ["construction market", "construction trends"]}
# }

# FINANCE INDUSTRY EXAMPLE  
# INDUSTRY_NAME = "Financial Services"
# INDUSTRY_COMPANIES = ["JPMorgan", "Goldman Sachs", "Morgan Stanley", "Bank of America"]
# SEARCH_PRIORITIES = {
#     1: {"name": "Financial deals", "terms": ["bank acquisition", "fintech merger"]},
#     2: {"name": "Executive moves", "terms": ["bank executive", "finance CEO"]},
#     3: {"name": "Technology", "terms": ["fintech", "banking AI", "digital banking"]},
#     4: {"name": "Market trends", "terms": ["banking trends", "finance market"]}
# }

