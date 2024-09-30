import sys
import re
import pandas as pd

def extract_info(data):
    # Define the patterns to search for, including the new pattern
    patterns = [
        r"(user-plane predefined-rules predefined-rule[\s\S]*?(?<!\s)!(?=\n))",
        r"(user-plane packet-detection predefined-pdrs predefined-pdr[\s\S]*?(?<!\s)!(?=\n))",
        r"(user-plane packet-detection applications application[\s\S]*?(?<!\s)!(?=\n))",
        r"(user-plane packet-detection filters filter[\s\S]*?(?<!\s)!(?=\n))"
    ]

    extracted_data = []

    # Iterate over each pattern and find matching text
    for pattern in patterns:
        matches = re.findall(pattern, data, re.MULTILINE)
        extracted_data.extend(matches)

    return extracted_data

# Read from standard input
data = sys.stdin.read()

# Run the extraction process
extracted_data = extract_info(data)

# Save the extracted information to an intermediate text file (optional, for verification)
with open('source_upf.txt', 'w', encoding='utf-8') as file:
    for item in extracted_data:
        file.write(item)
        file.write('\n')
