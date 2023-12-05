sample_string = "google.com"
character_frequency = {}

for char in sample_string:
    if char in character_frequency:
        character_frequency[char] += 1
    else:
        character_frequency[char] = 1

print(character_frequency)