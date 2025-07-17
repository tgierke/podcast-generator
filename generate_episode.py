#!/usr/bin/env python3
"""
Main Episode Generator
Orchestrates the complete podcast generation workflow
"""

import os
import sys
import logging
from datetime import datetime
from pathlib import Path

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from news_collector import NewsCollector
from content_generator import ContentGenerator
from audio_generator import AudioGenerator
from rss_generator import RSSGenerator
import config

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )

def create_directories():
    """Create necessary output directories"""
    directories = [
        config.AUDIO_OUTPUT_DIR,
        config.IMAGES_OUTPUT_DIR,
        config.SCRIPTS_OUTPUT_DIR,
        'logs'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

def generate_search_terms():
    """Generate search terms based on configuration"""
    search_terms = []
    
    # Add company-specific searches
    for company in config.INDUSTRY_COMPANIES[:10]:  # Limit to avoid too many requests
        search_terms.append(f'"{company}"')
    
    # Add priority-based searches
    for priority in config.SEARCH_PRIORITIES:
        for keyword in priority['keywords'][:3]:  # Limit keywords per priority
            search_terms.append(f"{keyword} music publishing")
    
    # Add general industry terms
    search_terms.extend([
        "music publishing industry",
        "music publishing deals",
        "music publishing executives",
        "music publishing technology"
    ])
    
    return search_terms

def main():
    """Main episode generation workflow"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("Starting podcast episode generation")
    
    try:
        # Create output directories
        create_directories()
        
        # Initialize components
        news_collector = NewsCollector()
        content_generator = ContentGenerator()
        audio_generator = AudioGenerator()
        rss_generator = RSSGenerator()
        
        # Step 1: Collect news articles
        logger.info("Collecting news articles...")
        search_terms = generate_search_terms()
        articles = news_collector.collect_articles(search_terms, config.NEWS_TIMEFRAME_DAYS)
        
        if not articles:
            logger.error("No articles collected. Exiting.")
            return False
        
        # Step 2: Filter and select top articles
        top_articles = news_collector.get_top_articles(articles, config.MAX_ARTICLES_PER_EPISODE)
        logger.info(f"Selected {len(top_articles)} top articles for episode")
        
        # Step 3: Generate podcast script
        logger.info("Generating podcast script...")
        episode_number = rss_generator.get_next_episode_number()
        script = content_generator.generate_script(top_articles, episode_number)
        
        # Validate script quality
        validation = content_generator.validate_script(script)
        logger.info(f"Script validation: {validation}")
        
        if validation['overall_quality'] < 0.7:
            logger.warning("Script quality below threshold, but proceeding...")
        
        # Step 4: Save script
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        script_filename = f"{config.SCRIPTS_OUTPUT_DIR}/episode_{episode_number:03d}_{timestamp}.md"
        
        with open(script_filename, 'w', encoding='utf-8') as f:
            f.write(f"# {config.PODCAST_NAME} - Episode {episode_number}\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Articles Processed:** {len(top_articles)}\n")
            f.write(f"**Estimated Duration:** {validation['estimated_duration']:.1f} minutes\n\n")
            f.write("---\n\n")
            f.write(script)
        
        logger.info(f"Script saved to: {script_filename}")
        
        # Step 5: Generate audio
        logger.info("Generating audio...")
        audio_filename = f"{config.AUDIO_OUTPUT_DIR}/episode_{episode_number:03d}_{timestamp}.mp3"
        audio_generator.generate_audio(script, audio_filename)
        
        if not os.path.exists(audio_filename):
            logger.error("Audio generation failed")
            return False
        
        # Step 6: Update RSS feed
        logger.info("Updating RSS feed...")
        episode_data = {
            'number': episode_number,
            'title': f"Episode {episode_number}: Weekly Industry Update",
            'description': f"This week's top stories in {config.TARGET_AUDIENCE.lower()}",
            'audio_file': audio_filename,
            'script_file': script_filename,
            'pub_date': datetime.now(),
            'duration': validation['estimated_duration'] * 60,  # Convert to seconds
            'articles': top_articles
        }
        
        rss_generator.add_episode(episode_data)
        
        # Step 7: Generate summary report
        generate_summary_report(episode_data, validation, top_articles)
        
        logger.info(f"Episode {episode_number} generated successfully!")
        logger.info(f"Audio: {audio_filename}")
        logger.info(f"Script: {script_filename}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error generating episode: {e}")
        return False

def generate_summary_report(episode_data, validation, articles):
    """Generate a summary report of the episode generation"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_filename = f"logs/episode_report_{timestamp}.md"
    
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(f"# Episode Generation Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Episode Number:** {episode_data['number']}\n")
        f.write(f"**Duration:** {episode_data['duration']/60:.1f} minutes\n\n")
        
        f.write("## Script Quality Metrics\n\n")
        for metric, value in validation.items():
            f.write(f"- **{metric.replace('_', ' ').title()}:** {value}\n")
        
        f.write("\n## Top Articles Used\n\n")
        for i, article in enumerate(articles, 1):
            f.write(f"{i}. **{article['title']}**\n")
            f.write(f"   - Source: {article['source']}\n")
            f.write(f"   - Relevance: {article['relevance_score']}/10\n")
            f.write(f"   - Date: {article['pub_date'].strftime('%Y-%m-%d') if article['pub_date'] else 'Unknown'}\n\n")

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

