#!/usr/bin/env python3

# Simple test of emoji functionality
class SimpleEmojiTranslator:
    def __init__(self):
        self.phrases = {
            "good morning": "",
            "good night": ""
        }
        self.words = {
            "coffee": "",
            "love": "",
            "happy": ""
        }
    
    def translate(self, text):
        result = text
        
        # Replace phrases first
        for phrase, emoji in self.phrases.items():
            if phrase.lower() in result.lower():
                import re
                pattern = re.compile(re.escape(phrase), re.IGNORECASE)
                result = pattern.sub(lambda m: m.group() + emoji, result)
        
        # Replace words
        words = result.split()
        new_words = []
        for word in words:
            clean_word = word.lower().strip('.,!?')
            if clean_word in self.words:
                new_words.append(word + self.words[clean_word])
            else:
                new_words.append(word)
        
        return ' '.join(new_words)

# Test it
translator = SimpleEmojiTranslator()
print("Simple translator test:")
print("Input: Good morning! I love coffee")
result = translator.translate("Good morning! I love coffee")
print(f"Output: {result}")
