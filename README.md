# Paginated Web Scraper

This Python script scrapes emails (or other content) from paginated websites using Selenium. It automates clicking through paginated content, extracting email addresses, and printing unique emails from each page.

## Features
- **Automated Pagination**: The scraper automatically navigates through paginated websites by clicking the "Next" button.
- **Email Extraction**: Extracts emails from each page and stores them in a set to ensure no duplicates.
- **Configurable for Any Website**: The script is flexible and can be easily adapted to scrape any paginated website by changing the initial URL and the pagination button's CSS selector.

## Requirements
- Python 3.x
- Selenium
- Webdriver Manager (to handle browser drivers automatically)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Paginated-Web-Scraper.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Paginated-Web-Scraper
   ```

3. Install the required Python packages:

   ```bash
   pip install selenium webdriver-manager
   ```

4. Install the appropriate browser driver (e.g., ChromeDriver) if not using WebDriverManager.

## Usage

1. **Modify the Script**: Update the `start_url` and `next_button_css_selector` to match the website you want to scrape.

   - `start_url`: The URL of the first page to scrape.
   - `next_button_css_selector`: The CSS selector for the "Next" button or link.

   Example:

   ```python
   scraper = PaginatedScraper(
       start_url="https://example.com/paginated-page",  # Replace with the actual URL
       next_button_css_selector='a.nextpostslink[rel="next"]'  # Replace with the actual CSS selector
   )
   ```

2. **Run the Script**:

   ```bash
   python paginated_scraper.py
   ```

   The script will scrape emails from the pages and print them once scraping is complete.

## Example

```python
scraper = PaginatedScraper(
    start_url="https://example.com/faculty-directory",
    next_button_css_selector="a.nextpostslink[rel='next']"
)
scraper.run()
```

## Customize the Scraper

You can further customize the scraper by modifying the regular expression for extracting emails or changing the content you're extracting from the page.

### Default Email Pattern

The script uses the following regex to match email addresses:

```regex
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
```

You can change this pattern in the `PaginatedScraper` class to scrape other types of data.

