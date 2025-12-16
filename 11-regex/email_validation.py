import re

emails = ["user@example.com", "invalid.email", "test@domain.org"]

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

for email in emails:
    if re.match(pattern, email):
        print(f"Valid email: {email}")
    else:
        print(f"Invalid email: {email}")
