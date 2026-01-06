import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class WebScraper:
    """Interactive web scraping program"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape_quotes(self):
        """Scrape quotes from quotes.toscrape.com"""
        print("\n🔍 Scraping quotes...")
        
        try:
            url = "http://quotes.toscrape.com/"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            data = []
            for quote in quotes[:10]:  # Get first 10 quotes
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                tags = [tag.text for tag in quote.find_all('a', class_='tag')]
                
                data.append({
                    'quote': text,
                    'author': author,
                    'tags': tags
                })
            
            self.display_quotes(data)
            return data
            
        except requests.RequestException as e:
            print(f"❌ Error fetching data: {e}")
            return []
    
    def scrape_news_headlines(self):
        """Scrape news headlines from example news site"""
        print("\n🔍 Scraping news headlines...")
        
        try:
            # Using a simple example site
            url = "https://news.ycombinator.com/"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            stories = soup.find_all('span', class_='titleline')
            
            data = []
            for i, story in enumerate(stories[:15], 1):  # Get first 15 headlines
                link = story.find('a')
                if link:
                    data.append({
                        'rank': i,
                        'title': link.text,
                        'url': link.get('href', 'N/A')
                    })
            
            self.display_news(data)
            return data
            
        except requests.RequestException as e:
            print(f"❌ Error fetching data: {e}")
            return []
    
    def scrape_books(self):
        """Scrape book information from books.toscrape.com"""
        print("\n🔍 Scraping book information...")
        
        try:
            url = "http://books.toscrape.com/"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            books = soup.find_all('article', class_='product_pod')
            
            data = []
            for book in books[:10]:  # Get first 10 books
                title = book.find('h3').find('a')['title']
                price = book.find('p', class_='price_color').text
                rating = book.find('p', class_='star-rating')['class'][1]
                availability = book.find('p', class_='instock availability').text.strip()
                
                data.append({
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'availability': availability
                })
            
            self.display_books(data)
            return data
            
        except requests.RequestException as e:
            print(f"❌ Error fetching data: {e}")
            return []
    
    def display_quotes(self, quotes):
        """Display quotes in a user-friendly format"""
        print("\n" + "=" * 80)
        print("INSPIRATIONAL QUOTES")
        print("=" * 80)
        
        for i, quote in enumerate(quotes, 1):
            print(f"\n{i}. {quote['quote']}")
            print(f"   — {quote['author']}")
            print(f"   Tags: {', '.join(quote['tags'])}")
        
        print("\n" + "=" * 80)
    
    def display_news(self, news):
        """Display news headlines in a user-friendly format"""
        print("\n" + "=" * 80)
        print("TOP NEWS HEADLINES")
        print("=" * 80)
        
        for item in news:
            print(f"\n{item['rank']}. {item['title']}")
            print(f"   URL: {item['url']}")
        
        print("\n" + "=" * 80)
    
    def display_books(self, books):
        """Display book information in a user-friendly format"""
        print("\n" + "=" * 80)
        print("FEATURED BOOKS")
        print("=" * 80)
        
        for i, book in enumerate(books, 1):
            print(f"\n{i}. {book['title']}")
            print(f"   Price: {book['price']}")
            print(f"   Rating: {book['rating']} stars")
            print(f"   {book['availability']}")
        
        print("\n" + "=" * 80)
    
    def save_data(self, data, filename):
        """Save scraped data to JSON file"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename}_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"\n💾 Data saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

def main():
    """Main function for web scraping program"""
    scraper = WebScraper()
    
    print("=" * 80)
    print("Interactive Web Scraping Program")
    print("=" * 80)
    
    while True:
        print("\n--- Select Website to Scrape ---")
        print("1. Quotes (quotes.toscrape.com)")
        print("2. News Headlines (Hacker News)")
        print("3. Books (books.toscrape.com)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("\nThank you for using Web Scraper! 👋")
            break
        
        data = []
        filename = ""
        
        if choice == '1':
            data = scraper.scrape_quotes()
            filename = "quotes_data"
        elif choice == '2':
            data = scraper.scrape_news_headlines()
            filename = "news_data"
        elif choice == '3':
            data = scraper.scrape_books()
            filename = "books_data"
        else:
            print("\n❌ Invalid choice! Please try again.")
            continue
        
        if data:
            save = input("\nWould you like to save this data? (yes/no): ")
            if save.lower() in ['yes', 'y']:
                scraper.save_data(data, filename)

if __name__ == "__main__":
    # Install required packages first:
    # pip install requests beautifulsoup4
    main()
