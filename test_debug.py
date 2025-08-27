from translator import EmojiTranslator

t = EmojiTranslator()
print("Testing phrase patterns:")
print("Phrases available:", len(t.phrase_patterns))
print("Words available:", len(t.emoji_map))
print()

print("Test 1 - Phrase detection:")
result = t.translate("Good morning", density="heavy", mode="append")
print(f"Good morning -> {result}")
print()

print("Test 2 - Word detection:")
result = t.translate("coffee", density="heavy", mode="append") 
print(f"coffee -> {result}")
print()

print("Test 3 - Love detection:")
result = t.translate("love", density="heavy", mode="append")
print(f"love -> {result}")
print()

print("Direct emoji map check:")
print("coffee in map:", "coffee" in t.emoji_map)
print("love in map:", "love" in t.emoji_map)
print("good morning in phrases:", "good morning" in t.phrase_patterns)

# Test multiple times due to randomness
print("\nTesting randomness (5 attempts):")
for i in range(5):
    result = t.translate("I love coffee", density="heavy", mode="append")
    print(f"Attempt {i+1}: {result}")
