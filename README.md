# 🎙️ Automated Podcast Generator

**Transform industry news into professional podcast episodes automatically**

A complete workflow that scrapes current news, generates engaging podcast scripts using AI, converts to professional audio, and publishes to RSS feeds - all automated.

## 🌟 Features

- **📰 Automated News Collection**: Scrapes Google News RSS feeds with intelligent filtering
- **🎯 Industry-Specific Targeting**: Configurable search terms and company lists
- **🤖 AI Script Generation**: Uses Google Gemini LLM for conversational podcast scripts
- **🎤 Professional Audio**: Eleven Labs text-to-speech with natural pacing
- **📡 RSS Feed Publishing**: Automatic podcast feed generation and hosting
- **🌐 Web Interface**: Clean podcast website with episode management
- **⏰ Scheduling Ready**: Built for weekly automation

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Google Gemini API key
- Eleven Labs API key
- Flask for web hosting

### Installation

```bash
git clone https://github.com/yourusername/automated-podcast-generator
cd automated-podcast-generator
pip install -r requirements.txt
```

### Configuration

1. Copy the example configuration:
```bash
cp config.example.py config.py
```

2. Edit `config.py` with your API keys:
```python
GEMINI_API_KEY = "your_gemini_api_key_here"
ELEVEN_LABS_API_KEY = "your_eleven_labs_api_key_here"
```

3. Customize your industry focus in `config.py`:
```python
INDUSTRY_COMPANIES = [
    "Hal Leonard LLC", "Alfred Music", "Faber Music",
    # Add your target companies
]

SEARCH_PRIORITIES = [
    "Breaking industry news and major deals",
    "Publishing company updates and executive moves",
    # Customize your content priorities
]
```

### Usage

#### Generate a Single Episode

```bash
python generate_episode.py
```

#### Run the Web Interface

```bash
python app.py
```

Then visit `http://localhost:5000` to see your podcast website.

#### Schedule Weekly Episodes

```bash
# Add to crontab for weekly generation
0 9 * * 1 /path/to/python /path/to/generate_episode.py
```

## 📁 Project Structure

```
automated-podcast-generator/
├── src/
│   ├── news_collector.py      # Google News RSS scraping
│   ├── content_generator.py   # AI script generation
│   ├── audio_generator.py     # Text-to-speech conversion
│   ├── rss_generator.py       # Podcast feed creation
│   └── web_app.py            # Flask web interface
├── templates/
│   └── podcast_website.html  # Web interface template
├── static/
│   ├── audio/                # Generated episodes
│   └── images/               # Podcast artwork
├── config.py                 # Configuration settings
├── requirements.txt          # Python dependencies
├── generate_episode.py       # Main episode generator
├── app.py                   # Web application entry point
└── README.md               # This file
```

## 🔧 Configuration Options

### News Collection

```python
# Target time frame for news (days)
NEWS_TIMEFRAME_DAYS = 7

# Number of articles to collect per search
ARTICLES_PER_SEARCH = 50

# Minimum relevance score (0-10)
MIN_RELEVANCE_SCORE = 6
```

### Content Generation

```python
# Target episode duration (minutes)
TARGET_DURATION_MINUTES = 10

# Podcast format and style
PODCAST_STYLE = "executive_briefing"  # or "conversational", "news_report"

# Target audience
TARGET_AUDIENCE = "Music Publishing Executives"
```

### Audio Generation

```python
# Eleven Labs voice settings
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam voice
VOICE_MODEL = "eleven_monolingual_v1"
```

## 🎯 Use Cases

### Industry News Podcasts
- **Music Publishing**: Track industry deals, executive moves, technology developments
- **Tech Industry**: Monitor startup funding, product launches, regulatory changes
- **Finance**: Follow market trends, regulatory updates, executive appointments

### Corporate Communications
- **Internal Updates**: Transform company news into engaging audio briefings
- **Investor Relations**: Convert earnings reports and updates into podcast format
- **Training Content**: Generate educational content from industry developments

### Content Marketing
- **Thought Leadership**: Position your company as an industry expert
- **Client Updates**: Keep clients informed with regular industry insights
- **Lead Generation**: Attract prospects with valuable industry intelligence

## 🛠️ Customization

### Adding New News Sources

```python
# In news_collector.py
def add_custom_source(self, rss_url, source_name):
    """Add a custom RSS feed source"""
    self.custom_sources.append({
        'url': rss_url,
        'name': source_name,
        'weight': 1.0
    })
```

### Custom Script Templates

```python
# In content_generator.py
SCRIPT_TEMPLATES = {
    'executive_briefing': """
    Welcome to {podcast_name}... your essential weekly briefing.
    This week we're covering {num_stories} key developments...
    """,
    'conversational': """
    Hey everyone, welcome back to {podcast_name}!
    I'm excited to dive into this week's biggest stories...
    """
}
```

### Voice Customization

```python
# Multiple voice support
VOICE_OPTIONS = {
    'professional_male': 'pNInz6obpgDQGcFmaJgB',
    'professional_female': '21m00Tcm4TlvDq8ikWAM',
    'conversational': 'AZnzlk1XvdvUeBnXmlld'
}
```

## 📊 Analytics & Monitoring

### Episode Metrics

```python
# Track episode performance
episode_stats = {
    'articles_processed': 25,
    'relevance_score': 8.2,
    'generation_time': '45 seconds',
    'audio_duration': '9:30',
    'file_size': '4.5MB'
}
```

### Content Quality Monitoring

```python
# Automated quality checks
quality_metrics = {
    'script_readability': 8.5,
    'topic_diversity': 7.8,
    'executive_relevance': 9.1,
    'audio_clarity': 8.9
}
```

## 🔒 Security & Privacy

- **API Key Management**: Secure configuration handling
- **Content Filtering**: Automated screening for inappropriate content
- **Data Retention**: Configurable cleanup of temporary files
- **Rate Limiting**: Built-in API usage management

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/automated-podcast-generator
cd automated-podcast-generator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Google Gemini**: For intelligent content generation
- **Eleven Labs**: For professional text-to-speech conversion
- **Flask**: For web application framework
- **BeautifulSoup**: For web scraping capabilities

## 📞 Support

- **Documentation**: [Wiki](https://github.com/yourusername/automated-podcast-generator/wiki)
- **Issues**: [GitHub Issues](https://github.com/yourusername/automated-podcast-generator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/automated-podcast-generator/discussions)

## 🗺️ Roadmap

- [ ] **Multi-language Support**: Generate podcasts in multiple languages
- [ ] **Advanced Analytics**: Detailed episode performance tracking
- [ ] **Plugin System**: Extensible architecture for custom integrations
- [ ] **Cloud Deployment**: One-click deployment to major cloud platforms
- [ ] **Mobile App**: Companion app for episode management
- [ ] **Collaboration Tools**: Multi-user editing and approval workflows

---

**Made with ❤️ for the developer community**

*Transform your industry expertise into engaging audio content automatically*

