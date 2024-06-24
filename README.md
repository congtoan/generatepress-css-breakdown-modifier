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
    
    **Explaination**
   
    | Original Media Query                                         | Updated Media Query                                 |
    |--------------------------------------------------------------|-----------------------------------------------------|
    | `@media (min-width: 769px) and (max-width: 1024px)`           | `@media (min-width: 902px) and (max-width: 1280px)` |
    | `@media (min-width: 1025px)`                                  | `@media (min-width: 1281px)`                        |
    | `@media (max-width: 768px)`                                   | `@media (max-width: 901px)`                         |

    **Explanation of Changes:**
    The table above illustrates the adjustments made to the original media queries to enhance responsiveness across different device sizes:
    
    - **First Row:** The original media query targeting a range from 769px to 1024px is updated to now apply styles from 902px to 1280px. This change ensures smoother transitions and layout adjustments for devices within this range, improving visual consistency.
    
    - **Second Row:** Media queries originally set for a minimum width of 1025px are modified to begin applying styles from 1281px onwards, accommodating larger screens effectively.
    
    - **Third Row:** Queries specifying a maximum width of 768px are revised to cater to devices up to 901px wide, refining the presentation on smaller screens.
    
    These adjustments aim to provide a more refined and adaptable user experience across desktop, tablet, and mobile devices, aligning with modern responsive design practices.


3. **Edit `directories` Path Pattern**
    
    Ensure that the `directories` variable matches the directory path for the GeneratePress theme.

    The example `directories` path provided will match GeneratePress theme directories across all domains on your server.
    
    ```python
    directories = glob.glob("/path/to/your/server/*/public_html/wp-content/themes/generatepress")
    ```

   If your server has a different directory structure, adjust the `directories` variable in the script accordingly.

5. **Run the script:**
    ```bash
    python generatepress_css_modifier.py
    ```
    or
    ```bash
    python3 generatepress_css_modifier.py
    ```   
