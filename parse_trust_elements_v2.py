#!/usr/bin/env python3
"""
Parse Trust Elements document and convert to Excel - Improved Version
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
entry_num = 0

for entry in entries:
    entry = entry.strip()
    if not entry or len(entry) < 10:
        continue
    
    entry_num += 1
    lines = [line.strip() for line in entry.split('\n') if line.strip()]
    
    if not lines:
        continue
    
    # Initialize variables
    name = ""
    instagram_handle = ""
    category = ""
    website = ""
    followers = ""
    location = ""
    instagram_links = []
    notes = []
    testimonial = ""
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Skip separator lines
        if '—-------' in line or '-------------' in line:
            i += 1
            continue
        
        # Extract Instagram links
        if 'instagram.com' in line:
            instagram_links.append(line)
            i += 1
            continue
        
        # Extract website (non-Instagram)
        if line.startswith('http') and 'instagram.com' not in line:
            if not website:
                website = line
            i += 1
            continue
        
        # Extract follower count (e.g., "126k", "472K")
        follower_match = re.search(r'(\d+\.?\d*)\s*[kK]', line)
        if follower_match and not followers:
            followers = follower_match.group(0)
            # Remove follower count from line and use rest as name
            name_part = re.sub(r'\d+\.?\d*\s*[kK]', '', line).strip()
            if name_part and not name:
                name = name_part
            i += 1
            continue
        
        # Detect categories
        category_keywords = [
            'interior design', 'design studio', 'architect', 'home decor',
            'digital creator', 'artist', 'hotel', 'airbnb', 'vacation',
            'renovations', 'custom builds', 'plumbing', 'photographer',
            'stylist', 'collector', 'personal blog', 'family', 'enthusiast'
        ]
        
        if any(keyword in line.lower() for keyword in category_keywords):
            if not category:
                category = line
            elif category and category != line:
                # Multiple categories, append
                category = category + " | " + line
            i += 1
            continue
        
        # Detect location
        location_keywords = [
            'france', 'italy', 'italia', 'canada', 'costa rica', 'costarica',
            'portugal', 'california', 'new york', 'london', 'vermont', 'arkansas'
        ]
        
        if any(keyword in line.lower() for keyword in location_keywords):
            if not location:
                location = line
            i += 1
            continue
        
        # Detect testimonials (usually longer text, mentions product/brand)
        if len(line) > 100 or '@insideastdesigns' in line or 'brass' in line.lower():
            testimonial += line + " "
            i += 1
            continue
        
        # If it's the first meaningful line and no name yet, it's probably the name
        if not name and i == 0:
            name = line
            i += 1
            continue
        
        # Everything else goes to notes
        notes.append(line)
        i += 1
    
    # Clean up extracted data
    if testimonial:
        testimonial = testimonial.strip()[:1000]  # Limit length
    
    notes_text = ' | '.join(notes)[:500] if notes else ""
    
    # Create entry
    data.append({
        'Name/Handle': name if name else (lines[0] if lines else ""),
        'Category': category,
        'Followers': followers,
        'Location': location,
        'Website': website,
        'Instagram Posts': '\n'.join(instagram_links[:10]),
        'Total Posts': len(instagram_links),
        'Testimonial/Notes': testimonial if testimonial else notes_text
    })

# Create DataFrame
df = pd.DataFrame(data)

# Clean up - remove empty rows
df = df[df['Name/Handle'].str.len() > 0]

# Remove duplicates based on name
df = df.drop_duplicates(subset=['Name/Handle'], keep='first')

# Sort by followers (extract numeric value for sorting)
def extract_follower_number(val):
    if pd.isna(val) or val == '':
        return 0
    match = re.search(r'(\d+\.?\d*)', str(val))
    if match:
        num = float(match.group(1))
        if 'k' in str(val).lower():
            return num * 1000
        return num
    return 0

df['follower_sort'] = df['Followers'].apply(extract_follower_number)
df = df.sort_values('follower_sort', ascending=False)
df = df.drop('follower_sort', axis=1)

# Save to Excel with better formatting
output_file = '/Users/redadrissielbouzaidi/Downloads/insideast/Trust_Elements.xlsx'

with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Influencers & Customers')
    
    # Get the worksheet
    worksheet = writer.sheets['Influencers & Customers']
    
    # Set column widths
    worksheet.column_dimensions['A'].width = 40  # Name
    worksheet.column_dimensions['B'].width = 30  # Category
    worksheet.column_dimensions['C'].width = 12  # Followers
    worksheet.column_dimensions['D'].width = 20  # Location
    worksheet.column_dimensions['E'].width = 40  # Website
    worksheet.column_dimensions['F'].width = 50  # Instagram Posts
    worksheet.column_dimensions['G'].width = 12  # Total Posts
    worksheet.column_dimensions['H'].width = 60  # Testimonial

print(f"✅ Excel file created: {output_file}")
print(f"📊 Total entries: {len(df)}")
print(f"\n📈 Top 10 by followers:")
print(df[['Name/Handle', 'Followers', 'Category']].head(10).to_string(index=False))
