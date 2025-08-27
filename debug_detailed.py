from translator import EmojiTranslator

# Create translator and test step by step
t = EmojiTranslator()

print("=== DEBUGGING STEP BY STEP ===")

# Test 1: Check if phrase exists
text = "Good morning"
print(f"\n1. Testing phrase: '{text}'")
print(f"   Phrase in patterns: {'good morning' in t.phrase_patterns}")
print(f"   Pattern value: {t.phrase_patterns.get('good morning', 'NOT FOUND')}")

# Test the phrase replacement function directly
result = t._replace_phrases(text, 'heavy', 'append', 'fun')
print(f"   After phrase replacement: '{result}'")

# Test 2: Check individual word
text2 = "coffee"
print(f"\n2. Testing word: '{text2}'")
print(f"   Word in emoji_map: {'coffee' in t.emoji_map}")
print(f"   Emoji options: {t.emoji_map.get('coffee', 'NOT FOUND')}")

# Test the word replacement function directly
result2 = t._replace_words(text2, 'heavy', 'append', 'fun')
print(f"   After word replacement: '{result2}'")

# Test 3: Check the _is_part_of_phrase function
print(f"\n3. Testing phrase detection logic:")
print(f"   'morning' part of phrase in 'Good morning': {t._is_part_of_phrase('morning', 'Good morning')}")
print(f"   'good' part of phrase in 'Good morning': {t._is_part_of_phrase('good', 'Good morning')}")

# Test 4: Force a replacement by setting random seed
import random
print(f"\n4. Testing with fixed random seed:")
random.seed(42)  # Set seed for reproducible results
result4 = t.translate("I love coffee", density='heavy', mode='append')
print(f"   Result with seed 42: '{result4}'")

random.seed(1)
result5 = t.translate("I love coffee", density='heavy', mode='append')  
print(f"   Result with seed 1: '{result5}'")

# Test 5: Check regex matching
import re
print(f"\n5. Testing regex matching:")
pattern = re.compile(re.escape("good morning"), re.IGNORECASE)
matches = list(pattern.finditer("Good morning"))
print(f"   Regex matches for 'good morning' in 'Good morning': {[m.span() for m in matches]}")
