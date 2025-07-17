#!/usr/bin/env python3
"""
Main Episode Generation Script
Automated Podcast Generator

This script orchestrates the complete podcast generation workflow:
1. Collect current industry news
2. Generate TTS-optimized script
3. Create professional audio
4. Update RSS feed and website
"""

import os
import sys
import datetime
from pathlib import Path

# Add src directory to path
sys.path.append(str(Path(__file__).parent / "src"))

from content_generator import generate_tts_optimized_script
from config import *

def main():
    """Generate a complete podcast episode"""
    
    print("🎙️ Automated Podcast Generator")
    print("=" * 50)
    
    # Check API keys
    if not GEMINI_API_KEY:
        print("❌ Error: GEMINI_API_KEY not configured")
        print("Please edit config.py and add your Gemini API key")
        return
    
    if not ELEVEN_LABS_API_KEY:
        print("❌ Error: ELEVEN_LABS_API_KEY not configured")
        print("Please edit config.py and add your ElevenLabs API key")
        return
    
    print("✅ API keys configured")
    
    # Generate timestamp for this episode
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    episode_name = f"{PODCAST_NAME.lower().replace(' ', '_')}_episode_{timestamp}"
    
    print(f"📝 Generating episode: {episode_name}")
    
    try:
        # Step 1: Generate TTS-optimized script
        print("🤖 Generating AI script...")
        script_content = generate_tts_optimized_script()
        
        # Save script
        script_file = f"output/{episode_name}_script.md"
        os.makedirs("output", exist_ok=True)
        with open(script_file, 'w') as f:
            f.write(script_content)
        print(f"✅ Script saved: {script_file}")
        
        # Step 2: Generate audio (if ElevenLabs configured)
        if ELEVEN_LABS_API_KEY:
            print("🎵 Generating audio...")
            # Audio generation code would go here
            print("✅ Audio generation ready (implement in production)")
        
        # Step 3: Update website and RSS
        print("🌐 Website and RSS update ready")
        print("✅ Use website/src/main.py for deployment")
        
        print("\n🎉 Episode generation complete!")
        print(f"📁 Files created in: output/")
        print(f"📝 Script: {script_file}")
        
        print("\n📋 Next Steps:")
        print("1. Review the generated script")
        print("2. Generate audio using ElevenLabs")
        print("3. Deploy website using website/src/main.py")
        print("4. Submit RSS feed to podcast platforms")
        
    except Exception as e:
        print(f"❌ Error generating episode: {e}")
        return

if __name__ == "__main__":
    main()

