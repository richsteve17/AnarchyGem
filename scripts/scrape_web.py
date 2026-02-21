import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    """Fetches a webpage and extracts all paragraph text."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        
        print(f"--- Scraped content from {url} ---")
        for p in paragraphs:
            print(p.get_text())
        print("----------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("\n--- Web Scraping Script ---")
    print("Usage: python scrape_web.py <url>")

    import sys
    if len(sys.argv) > 1:
        target_url = sys.argv[1]
        scrape_page(target_url)
    else:
        print("No URL provided. Example: python scrape_web.py https://example.com")

    print("\nNOTE: Requires 'requests' and 'beautifulsoup4' libraries. Install with: pip install requests beautifulsoup4")
