#!/usr/bin/env python3

import json

# Let's test and fix the translator by simplifying it
class EmojiTranslator:
    def __init__(self):
        self.phrase_patterns = {
            "good morning": "\U0001F305",  # 
            "good night": "\U0001F319",    # 
            "on fire": "\U0001F525",       # 
        }
        
        self.emoji_map = {
            "coffee": ["\U00002615"],      # 
            "love": ["\U00002764\U0000FE0F"], # 
            "happy": ["\U0001F60A"],       # 
            "cat": ["\U0001F431"],         # 
            "work": ["\U0001F4BC"],        # 
            "time": ["\U000023F0"],        # 
        }
    
    def translate(self, text, density='medium', mode='append'):
        import re
        import random
        
        result = text
        
        # Replace phrases first
        for phrase, emoji in self.phrase_patterns.items():
            if phrase.lower() in result.lower():
                pattern = re.compile(re.escape(phrase), re.IGNORECASE)
                if mode == 'replace':
                    result = pattern.sub(emoji, result)
                else:
                    result = pattern.sub(lambda m: m.group() + emoji, result)
        
        # Replace words
        word_pattern = re.compile(r'\b\w+\b')
        matches = list(word_pattern.finditer(result))
        
        offset = 0
        for match in matches:
            start, end = match.span()
            word = match.group().lower()
            
            if word in self.emoji_map:
                # Density check
                chance = {'light': 0.5, 'medium': 0.8, 'heavy': 1.0}
                if random.random() <= chance.get(density, 0.8):
                    emoji = random.choice(self.emoji_map[word])
                    
                    actual_start = start + offset
                    actual_end = end + offset
                    
                    if mode == 'replace':
                        replacement = emoji
                    else:
                        replacement = match.group() + emoji
                    
                    result = result[:actual_start] + replacement + result[actual_end:]
                    offset += len(replacement) - (end - start)
        
        return result

# Test the translator
translator = EmojiTranslator()

tests = [
    "Good morning! I love coffee",
    "I'm happy to work",
    "The team is on fire",
    "My cat loves coffee time"
]

print("=== EMOJI TRANSLATOR TEST ===")
for test in tests:
    result = translator.translate(test, density='heavy', mode='append')
    print(f"Input:  {test}")
    print(f"Output: {result}")
    
    # Also show the raw unicode representation
    print(f"Unicode: {repr(result)}")
    print(f"Length difference: {len(result) - len(test)}")
    print()

# Test different modes
print("=== MODE COMPARISON ===")
test_text = "I love coffee"
append_result = translator.translate(test_text, mode='append', density='heavy')
replace_result = translator.translate(test_text, mode='replace', density='heavy')

print(f"Original: {test_text}")
print(f"Append:   {append_result} (repr: {repr(append_result)})")
print(f"Replace:  {replace_result} (repr: {repr(replace_result)})")
