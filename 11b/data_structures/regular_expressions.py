import re

# Example 1: Matching Email Addresses
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Example 2: Extracting Phone Numbers
phone_pattern = re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b')
pattern = re.compile(r'\+[0-9]{2}-[0-9]{3}-[0-9]{3}-[0-9]{4}')

# Usage
text = """ Contact us at john.doe@example.com or call 555 123 4567 for assistance.
Contact us at martha_mithcel@test.com or call +38-099-765-5434 for assistance."""

# Find email addresses
emails = email_pattern.findall(text)
print("Email Addresses:", emails)

# Find phone numbers
phones = phone_pattern.findall(text)
print("Phone Numbers:", phones)

p2 = pattern.findall(text)
print(p2)
