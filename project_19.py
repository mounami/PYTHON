import requests
from bs4 import BeautifulSoup
import json

def scrape_url(url):
    """Scrape quotes from quotes.toscrape.com

    Args:
        url : The URL of the page to scrape.

     Returns:
        list: List of dictionaries containing quote data
    """

    print(f"Scraping URL: {url}")

    # Step 1: Send HTTP request to the website
    response = requests.get(url)

    # check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page with status code: {response.status_code}")
        return []
    
    print("✅ Page fetched successfully!")

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 3: Find all quote containers
    quote_elements = soup.find_all('div', class_='quote')

    print(f"📚 Found {len(quote_elements)} quotes on this page\n")

    quotes = []

    # Step 4: Extract data from each quote

    for quote_elem in quote_elements:

        # Extract the quote text
        text = quote_elem.find('span', class_='text').text.strip('“”')

        # Extract the author
        author = quote_elem.find('small', class_='author').text

        # Extract tags (there can be multiple)
        tag_elements = quote_elem.find_all('a', class_='tag')
        tags = [tag_elem.text for tag_elem in tag_elements]

        # Store in dictionary
        quote_data = {
            'quote': text,
            'author': author,
            'tags': tags
        }
        
        quotes.append(quote_data)
    
    return quotes

def display_quotes(quotes):
    """Pretty print the scraped quotes"""
    print("=" * 80)
    print("✨ INSPIRATIONAL QUOTES ✨".center(80))
    print("=" * 80)

    for i, quote in enumerate(quotes, 1):
        print(f"\n📖 Quote #{i}")
        print(f"   \"{quote['quote']}\"")
        print(f"   — {quote['author']}")
        print(f"   🏷️  Tags: {', '.join(quote['tags'])}")
        print("-" * 80)


def save_to_json(quotes, filename='quotes.json'):
    """Save quotes to a JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)
    print(f"\n💾 Saved {len(quotes)} quotes to {filename}")


def scrape_multiple_pages(base_url, num_pages=3):
    """Scrape quotes from multiple pages"""
    all_quotes = []
    
    for page in range(1, num_pages + 1):
        url = f"{base_url}/page/{page}/"
        print(f"\n{'='*60}")
        print(f"📄 Scraping Page {page}")
        print(f"{'='*60}")
        
        quotes = scrape_url(url)
        all_quotes.extend(quotes)
        
        # Be polite - wait a bit between requests
        import time
        time.sleep(1)
    
    return all_quotes

def find_quotes_by_author(quotes, author_name):
    """Filter quotes by a specific author"""
    author_quotes = [q for q in quotes if author_name.lower() in q['author'].lower()]
    return author_quotes


def find_quotes_by_tag(quotes, tag_name):
    """Filter quotes by a specific tag"""
    tagged_quotes = [q for q in quotes if tag_name.lower() in [t.lower() for t in q['tags']]]
    return tagged_quotes

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    # Base URL of the quotes website
    base_url = "http://quotes.toscrape.com"
    
    print("🚀 Starting Quote Scraper!\n")
    
    # Example 1: Scrape first page
    print("📌 EXAMPLE 1: Scraping Single Page")
    quotes = scrape_url(base_url)
    display_quotes(quotes[:3])  # Show first 3 quotes
    
    # Example 2: Scrape multiple pages
    print("\n\n📌 EXAMPLE 2: Scraping Multiple Pages")
    all_quotes = scrape_multiple_pages(base_url, num_pages=2)
    print(f"\n🎉 Total quotes scraped: {len(all_quotes)}")
    
    # Example 3: Filter by author
    print("\n\n📌 EXAMPLE 3: Finding Quotes by Author")
    einstein_quotes = find_quotes_by_author(all_quotes, "Einstein")
    print(f"Found {len(einstein_quotes)} quotes by Einstein:")
    display_quotes(einstein_quotes)
    
    # Example 4: Filter by tag
    print("\n\n📌 EXAMPLE 4: Finding Quotes by Tag")
    love_quotes = find_quotes_by_tag(all_quotes, "love")
    print(f"Found {len(love_quotes)} quotes tagged with 'love':")
    display_quotes(love_quotes[:2])
    
    # Example 5: Save to file
    print("\n\n📌 EXAMPLE 5: Saving to JSON File")
    save_to_json(all_quotes)
    
    print("\n✨ Scraping complete! ✨")