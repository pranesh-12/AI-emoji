#!/usr/bin/env python3
"""
Emoji Translator AI - Core Translation Module
Advanced emoji translation with multiple modes, styles, and context awareness
"""

import re
import json
import argparse
import random
from typing import Dict, List, Tuple, Optional
from pathlib import Path

class EmojiTranslator:
    def __init__(self, custom_emoji_file: Optional[str] = None):
        """Initialize the emoji translator with built-in and custom emoji mappings."""
        self.phrase_patterns = self._get_phrase_patterns()
        self.emoji_map = self._get_emoji_map()
        self.sentiment_emojis = {
            'positive': ['', '', '', '', ''],
            'negative': ['', '', '', '', ''],
            'neutral': ['', '', '', '']
        }
        
        # Load custom emojis if provided
        if custom_emoji_file:
            self.load_custom_emojis(custom_emoji_file)
    
    def _get_phrase_patterns(self) -> Dict[str, str]:
        """Return dictionary of multi-word phrase patterns."""
        return {
            # Time-related phrases
            "good morning": "",
            "good night": "",
            "have a good day": "",
            "see you later": "",
            "see you tomorrow": "",
            
            # Expressions
            "on fire": "",
            "fire station": "",
            "break a leg": "",
            "piece of cake": "",
            "it's raining cats and dogs": "",
            "spill the tea": "",
            "throw shade": "",
            "catch some z's": "",
            "hit the hay": "",
            "burning the midnight oil": "",
            
            # Emotions & States
            "over the moon": "",
            "on cloud nine": "9",
            "feeling blue": "",
            "green with envy": "",
            "tickled pink": "",
            "seeing red": "",
            
            # Food expressions
            "cherry on top": "",
            "cool as a cucumber": "",
            "hot potato": "",
            "full of beans": "",
            
            # Work/Tech
            "touch base": "",
            "circle back": "",
            "low hanging fruit": "",
            "move the needle": "",
            "think outside the box": "",
            
            # General
            "break the ice": "",
            "bite the bullet": "",
            "hit the nail on the head": "",
            "ball is in your court": "",
            "cost an arm and a leg": "",
        }
    
    def _get_emoji_map(self) -> Dict[str, List[str]]:
        """Return comprehensive emoji mapping for individual words."""
        return {
            # Emotions
            "happy": ["", "", "", ""],
            "sad": ["", "", "", ""],
            "angry": ["", "", "", ""],
            "love": ["", "", "", ""],
            "excited": ["", "", "", ""],
            "tired": ["", "", "", ""],
            "confused": ["", "", "", ""],
            "surprised": ["", "", "", ""],
            "laughing": ["", "", "", ""],
            "crying": ["", "", "", ""],
            
            # Food & Drinks
            "coffee": ["", ""],
            "tea": ["", ""],
            "beer": ["", ""],
            "wine": ["", ""],
            "pizza": [""],
            "burger": ["", ""],
            "sushi": ["", ""],
            "cake": ["", ""],
            "ice cream": ["", ""],
            "chocolate": ["", ""],
            "apple": ["", ""],
            "banana": [""],
            "bread": ["", ""],
            "cheese": [""],
            "pasta": ["", ""],
            "soup": ["", ""],
            "salad": ["", ""],
            "sandwich": ["", ""],
            
            # Animals
            "cat": ["", "", ""],
            "dog": ["", "", ""],
            "bird": ["", "", ""],
            "fish": ["", "", ""],
            "lion": [""],
            "tiger": [""],
            "elephant": [""],
            "monkey": ["", ""],
            "bear": ["", ""],
            "rabbit": ["", ""],
            "snake": [""],
            "frog": [""],
            
            # Tech & Work
            "computer": ["", ""],
            "phone": ["", ""],
            "email": ["", ""],
            "internet": ["", ""],
            "code": ["", "", ""],
            "programming": ["", "", ""],
            "data": ["", "", ""],
            "server": ["", ""],
            "bug": ["", ""],
            "meeting": ["", "", ""],
            "presentation": ["", "", ""],
            "deadline": ["", "", ""],
            "project": ["", "", ""],
            
            # Places & Travel
            "home": ["", ""],
            "office": ["", ""],
            "school": ["", ""],
            "hospital": ["", ""],
            "airport": ["", ""],
            "beach": ["", ""],
            "mountain": ["", ""],
            "city": ["", ""],
            "park": ["", ""],
            "restaurant": ["", ""],
            "hotel": ["", ""],
            "car": ["", ""],
            "train": ["", ""],
            "plane": ["", ""],
            
            # Time & Weather
            "morning": ["", ""],
            "afternoon": ["", ""],
            "evening": ["", ""],
            "night": ["", ""],
            "today": ["", ""],
            "tomorrow": ["", ""],
            "yesterday": ["", ""],
            "sun": ["", ""],
            "moon": ["", ""],
            "rain": ["", ""],
            "snow": ["", ""],
            "wind": ["", ""],
            "storm": ["", ""],
            
            # Activities & Sports
            "running": ["", "", ""],
            "swimming": ["", "", ""],
            "cycling": ["", "", ""],
            "football": ["", ""],
            "basketball": [""],
            "tennis": ["", ""],
            "golf": ["", ""],
            "music": ["", "", ""],
            "dancing": ["", "", ""],
            "reading": ["", "", ""],
            "writing": ["", "", ""],
            "cooking": ["", "", ""],
            "shopping": ["", "", ""],
            "gaming": ["", "", ""],
            
            # Nature & Plants
            "tree": ["", ""],
            "flower": ["", "", ""],
            "grass": ["", ""],
            "ocean": ["", ""],
            "fire": ["", ""],
            "water": ["", ""],
            "earth": ["", "", ""],
            "star": ["", "", ""],
            "rainbow": [""],
            
            # Objects & Tools
            "book": ["", "", ""],
            "pen": ["", ""],
            "pencil": ["", ""],
            "clock": ["", "", ""],
            "calendar": ["", ""],
            "money": ["", "", ""],
            "gift": ["", ""],
            "key": ["", ""],
            "lock": ["", ""],
            "camera": ["", ""],
            "light": ["", ""],
            "mirror": [""],
            "scissors": [""],
            "hammer": [""],
            
            # Miscellaneous
            "party": ["", "", ""],
            "birthday": ["", "", ""],
            "wedding": ["", "", ""],
            "graduation": ["", ""],
            "vacation": ["", "", ""],
            "sleep": ["", "", ""],
            "dream": ["", "", ""],
            "magic": ["", "", ""],
            "luck": ["", "", ""],
            "success": ["", "", ""],
            "failure": ["", "", ""],
            "help": ["", "", ""],
            "question": ["", "", ""],
            "answer": ["", "", ""],
        }
    
    def load_custom_emojis(self, file_path: str) -> None:
        """Load custom emoji mappings from a JSON file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                custom_emojis = json.load(f)
                
            # Merge custom emojis with existing mappings
            for word, emojis in custom_emojis.get('words', {}).items():
                if word in self.emoji_map:
                    self.emoji_map[word].extend(emojis)
                else:
                    self.emoji_map[word] = emojis if isinstance(emojis, list) else [emojis]
            
            # Add custom phrases
            if 'phrases' in custom_emojis:
                self.phrase_patterns.update(custom_emojis['phrases'])
                
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Warning: Could not load custom emojis from {file_path}: {e}")
    
    def _detect_sentiment(self, text: str) -> str:
        """Simple sentiment detection based on keywords."""
        positive_words = ['good', 'great', 'awesome', 'amazing', 'wonderful', 'fantastic', 
                         'excellent', 'perfect', 'love', 'happy', 'excited', 'best']
        negative_words = ['bad', 'terrible', 'awful', 'horrible', 'hate', 'sad', 'angry',
                         'frustrated', 'disappointed', 'worst', 'fail', 'problem']
        
        text_lower = text.lower()
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return 'positive'
        elif negative_count > positive_count:
            return 'negative'
        else:
            return 'neutral'
    
    def _get_context_aware_emoji(self, word: str, context: str) -> List[str]:
        """Select emojis based on surrounding context."""
        if word not in self.emoji_map:
            return []
        
        available_emojis = self.emoji_map[word]
        context_lower = context.lower()
        
        # Time-based context
        if any(time_word in context_lower for time_word in ['morning', 'dawn', 'sunrise']):
            if word in ['sun', 'light']:
                return ['', '']
        elif any(time_word in context_lower for time_word in ['night', 'evening', 'dark']):
            if word in ['moon', 'light']:
                return ['', '']
        
        # Fire context awareness
        if word == 'fire':
            if any(term in context_lower for term in ['on fire', 'burning', 'hot', 'flame']):
                return ['']
            elif any(term in context_lower for term in ['station', 'truck', 'department', 'fighter']):
                return ['', '']
        
        # Default to all available emojis
        return available_emojis
    
    def translate(self, text: str, density: str = 'medium', mode: str = 'append', 
                 style: str = 'fun', add_sentiment: bool = False) -> str:
        """
        Translate text to emoji-enhanced version.
        
        Args:
            text: Input text to translate
            density: 'light', 'medium', or 'heavy' - controls emoji frequency
            mode: 'append' (word + emoji) or 'replace' (emoji only)
            style: 'fun', 'professional', or 'meme' - controls emoji selection
            add_sentiment: Whether to add sentiment emojis at the end
        """
        result = text
        
        # Step 1: Replace multi-word phrases first
        result = self._replace_phrases(result, density, mode, style)
        
        # Step 2: Replace individual words
        result = self._replace_words(result, density, mode, style)
        
        # Step 3: Add sentiment emoji if requested
        if add_sentiment:
            sentiment = self._detect_sentiment(text)
            sentiment_emoji = random.choice(self.sentiment_emojis[sentiment])
            result = f"{result} {sentiment_emoji}"
        
        return result
    
    def _replace_phrases(self, text: str, density: str, mode: str, style: str) -> str:
        """Replace multi-word phrases with emojis."""
        result = text
        
        # Sort phrases by length (longest first) to avoid partial matches
        sorted_phrases = sorted(self.phrase_patterns.keys(), key=len, reverse=True)
        
        for phrase in sorted_phrases:
            if phrase.lower() in result.lower():
                emoji = self.phrase_patterns[phrase]
                
                # Apply style modifications
                if style == 'meme':
                    emoji = emoji * random.randint(2, 4)
                elif style == 'professional':
                    # Skip some phrases in professional mode
                    if random.random() < 0.3:
                        continue
                
                # Apply density
                if density == 'light' and random.random() < 0.5:
                    continue
                elif density == 'heavy':
                    emoji = emoji * 2 if style != 'meme' else emoji
                
                # Replace phrase
                pattern = re.compile(re.escape(phrase), re.IGNORECASE)
                if mode == 'replace':
                    result = pattern.sub(emoji, result)
                else:  # append mode
                    result = pattern.sub(f"{phrase}{emoji}", result)
        
        return result
    
    def _replace_words(self, text: str, density: str, mode: str, style: str) -> str:
        """Replace individual words with emojis."""
        words = re.findall(r'\b\w+\b', text)
        result = text
        
        for word in words:
            word_lower = word.lower()
            
            # Skip if word is part of a phrase we already processed
            if self._is_part_of_phrase(word_lower, text):
                continue
            
            # Get context-aware emojis
            available_emojis = self._get_context_aware_emoji(word_lower, text)
            if not available_emojis:
                continue
            
            # Apply density filtering
            density_chance = {'light': 0.3, 'medium': 0.6, 'heavy': 0.9}
            if random.random() > density_chance.get(density, 0.6):
                continue
            
            # Apply style filtering
            if style == 'professional':
                # Only use work/tech related emojis in professional mode
                professional_categories = ['tech', 'work', 'time', 'places']
                if not self._is_professional_word(word_lower):
                    continue
            
            # Select emoji
            emoji = random.choice(available_emojis)
            
            # Apply style modifications
            if style == 'meme':
                emoji = emoji * random.randint(2, 3)
            
            # Replace word
            pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
            if mode == 'replace':
                result = pattern.sub(emoji, result)
            else:  # append mode
                result = pattern.sub(f"{word}{emoji}", result)
        
        return result
    
    def _is_part_of_phrase(self, word: str, text: str) -> bool:
        """Check if word is part of a phrase pattern that was already processed."""
        text_lower = text.lower()
        for phrase in self.phrase_patterns.keys():
            if word in phrase.lower() and phrase.lower() in text_lower:
                return True
        return False
    
    def _is_professional_word(self, word: str) -> bool:
        """Check if word is appropriate for professional style."""
        professional_words = {
            'meeting', 'project', 'deadline', 'presentation', 'data', 'computer',
            'email', 'office', 'work', 'team', 'client', 'report', 'analysis',
            'strategy', 'goal', 'target', 'success', 'growth', 'development'
        }
        return word in professional_words or word in ['today', 'tomorrow', 'time']


def main():
    """CLI interface for the Emoji Translator."""
    parser = argparse.ArgumentParser(description='Emoji Translator AI - Transform text with emojis!')
    parser.add_argument('text', help='Text to translate')
    parser.add_argument('--density', choices=['light', 'medium', 'heavy'], 
                       default='medium', help='Emoji density level')
    parser.add_argument('--mode', choices=['append', 'replace'], 
                       default='append', help='Translation mode')
    parser.add_argument('--style', choices=['fun', 'professional', 'meme'], 
                       default='fun', help='Output style')
    parser.add_argument('--sentiment', action='store_true', 
                       help='Add sentiment emoji at the end')
    parser.add_argument('--custom-emojis', help='Path to custom emoji mappings file')
    parser.add_argument('--save', help='Save translation to file')
    
    args = parser.parse_args()
    
    # Initialize translator
    translator = EmojiTranslator(custom_emoji_file=args.custom_emojis)
    
    # Perform translation
    result = translator.translate(
        text=args.text,
        density=args.density,
        mode=args.mode,
        style=args.style,
        add_sentiment=args.sentiment
    )
    
    # Display result
    print("\n" + "="*50)
    print("EMOJI TRANSLATOR AI")
    print("="*50)
    print(f"Original: {args.text}")
    print(f"Translated: {result}")
    print(f"Settings: {args.density} density, {args.mode} mode, {args.style} style")
    print("="*50)
    
    # Save if requested
    if args.save:
        with open(args.save, 'w', encoding='utf-8') as f:
            f.write(f"Original: {args.text}\n")
            f.write(f"Translated: {result}\n")
            f.write(f"Settings: {args.density} density, {args.mode} mode, {args.style} style\n")
        print(f"Translation saved to {args.save}")


if __name__ == "__main__":
    main()
