import os
import re
import glob


# Define the search and replace patterns
search_patterns = [
    (r"@media\s*\(\s*min-width\s*:\s*769px\s*\)\s*and\s*\(\s*max-width\s*:\s*1024px\s*\)",
     r"@media (min-width:902px) and (max-width:1280px)"),
    (r"@media\s*\(\s*min-width\s*:\s*1025px\s*\)", r"@media (min-width:1281px)"),
    (r"@media\s*\(\s*max-width\s*:\s*768px\s*\)", r"@media (max-width:901px)")
]

# Function to replace text in a file and print the file name if changed
def replace_in_file(file_path, search_patterns, directory):
    with open(file_path, 'r') as file:
        file_content = file.read()
        updated_content = file_content

    for search_pattern, replace_pattern in search_patterns:
        # Perform the replacement
        updated_content = re.sub(search_pattern, replace_pattern, updated_content)

    if file_content != updated_content:
        with open(file_path, 'w') as file:
            file.write(updated_content)
            
        relative_path = os.path.relpath(file_path, directory)
        print(f"{relative_path} UPDATED.")


# Use glob to find all directories matching the base pattern
directories = glob.glob("/home/*/*/public_html/wp-content/themes/generatepress")

# Iterate through each found directory and process the CSS files using glob for recursion
for directory in directories:
    print(directory)
    css_files = glob.glob(os.path.join(directory, '**', '*.css'), recursive=True)
    for file_path in css_files:
        replace_in_file(file_path, search_patterns, directory)
    print("----") #Split each directory

print("All is done!")
