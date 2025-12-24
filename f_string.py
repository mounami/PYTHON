name = "Mario"
lives = 3
score = 1250

# Old way (boring)
print(name, "has", lives, "lives and", score, "points")

# New way (cool!) - put f before the quote
print(f"{name} has {lives} lives and {score} points")

# You can do math inside f-strings!
print(f"Double score would be {score * 2}")

print(f"Next level in {5000 - score} points for {name} with {lives} lives.")