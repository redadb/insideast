#!/usr/bin/env python3
"""
Parse Trust Elements document and convert to Excel
"""
import re
import pandas as pd

# Read the text file
with open('/tmp/trust_elements.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Split by the separator line
entries = content.split('—---------------------------------------')

# Parse each entry
data = []
for entry in entries:
    entry = entry.strip()
    if not entry:
        continue
    
    lines = [line.strip() for line in entry.split('\n') if line.strip()]
    
    if not lines:
        continue
    
    # Extract information
    name = ""
    instagram_handle = ""
    category = ""
    website = ""
    followers = ""
    location = ""
    instagram_links = []
    notes = ""
    
    # First line usually contains name/handle or category
    first_line = lines[0]
    
    # Check for Instagram handle patterns
    if first_line.startswith('@') or '|' in first_line or 'https' not in first_line:
        name = first_line
    
    for line in lines:
        # Extract Instagram links
        if 'instagram.com' in line:
            instagram_links.append(line)
        # Extract website (non-Instagram)
        elif line.startswith('http') and 'instagram.com' not in line:
            website = line
        # Extract category/type
        elif any(keyword in line.lower() for keyword in ['interior', 'design', 'hotel', 'airbnb', 'artist', 'digital creator', 'home decor', 'architect']):
            if not category:
                category = line
        # Extract follower count
        elif re.search(r'\d+[kK]', line) and not instagram_links:
            followers = line
        # Extract location
        elif any(country in line.lower() for country in ['france', 'italy', 'canada', 'costarica', 'portugal', 'california', 'new york', 'london', 'vermont']):
            location = line
        # Everything else is notes
        elif 'http' not in line and line not in [name, category, followers]:
            notes += line + " "
    
    # If name is empty but we have lines, use first non-URL line
    if not name and lines:
        for line in lines:
            if 'http' not in line and line:
                name = line
                break
    
    data.append({
        'Name/Handle': name,
        'Category': category,
        'Followers': followers,
        'Location': location,
        'Website': website,
        'Instagram Links': '\n'.join(instagram_links[:5]),  # Limit to first 5
        'Notes': notes.strip()[:500]  # Limit notes length
    })

# Create DataFrame
df = pd.DataFrame(data)

# Remove duplicate entries
df = df.drop_duplicates(subset=['Name/Handle'], keep='first')

# Save to Excel
output_file = '/Users/redadrissielbouzaidi/Downloads/insideast/Trust_Elements.xlsx'
df.to_excel(output_file, index=False, sheet_name='Trust Elements')

print(f"Excel file created: {output_file}")
print(f"Total entries: {len(df)}")
