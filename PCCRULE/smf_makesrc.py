import sys
import re
import pandas as pd

def extract_info(data):
    # Define the patterns to search for, including the new pattern
    patterns = [
        r"(epg pgw policy-control rule-scope[\s\S]*?!(?=\n[^ ])\n)",
        r"(epg pgw packet-enforcement traffic-redirection rule[\s\S]*?!(?=\n[^ ])\n)",
        r"(epg pgw qos-control service-profile[\s\S]*?!(?=\n[^ ])\n)",
        r"(epg pgw user-plane predefined-rule profile[\s\S]*?!(?=\n[^ ])\n)"  # New pattern added
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
with open('smf_source.txt', 'w', encoding='utf-8') as file:
    for item in extracted_data:
        file.write(item)
        file.write('\n')
