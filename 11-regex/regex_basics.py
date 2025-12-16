import re

text = "The quick brown fox jumps over the lazy dog"

match = re.search(r"fox", text)
if match:
    print(f"Found 'fox' at position {match.start()}")

matches = re.findall(r"the", text, re.IGNORECASE)
print(f"Found 'the' {len(matches)} times: {matches}")

result = re.sub(r"fox", "cat", text)
print(f"After substitution: {result}")
