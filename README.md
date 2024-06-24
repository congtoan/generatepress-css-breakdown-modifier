# GeneratePress CSS Breakdown Modifier

This repository contains a Python script designed to modify media query breakpoints in CSS files within the GeneratePress theme directory. The script recursively searches for all CSS files and updates the media queries according to predefined patterns.

## Features

- Recursively searches for all `.css` files in the specified directory and its subdirectories.
- Modifies media query breakpoints to new specified values.
- Prints a message indicating which files were updated.

## Usage

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/generatepress-css-breakdown-modifier.git
    cd generatepress-css-breakdown-modifier
    ```

2. **Edit the `search_patterns` list in the script if necessary:**

    ```python
    search_patterns = [
        (r"@media\s*\(\s*min-width\s*:\s*769px\s*\)\s*and\s*\(\s*max-width\s*:\s*1024px\s*\)",
        r"@media (min-width:902px) and (max-width:1280px)"),
        (r"@media\s*\(\s*min-width\s*:\s*1025px\s*\)", r"@media (min-width:1281px)"),
        (r"@media\s*\(\s*max-width\s*:\s*768px\s*\)", r"@media (max-width:901px)")
    ]
    ```

3. **Run the script:**
    ```bash
    python generatepress_css_modifier.py
    ```
