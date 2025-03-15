import requests
from multiprocessing import Pool
from bs4 import BeautifulSoup
import time

# Define a list of urls to be scraped
urls = [
    "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_and_their_capitals_in_native_languages",
    "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)",
    "https://en.wikipedia.org/wiki/List_of_countries_by_area",
    "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)",
    "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)",
    "https://en.wikipedia.org/wiki/List_of_countries_by_Human_Development_Index",
    "https://en.wikipedia.org/wiki/List_of_countries_by_life_expectancy",
    "http://books.toscrape.com/",
    "https://quotes.toscrape.com/",
    "https://www.scrapethissite.com/pages/simple/",
    "https://www.scrapethissite.com/pages/forms/",
    "https://www.scrapethissite.com/pages/ajax-javascript",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2015",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2014",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2013",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2012",
    "https://www.scrapethissite.com/pages/ajax-javascript/#2011",
    "https://www.scrapethissite.com/pages/frames/",
    ]

def scrape(url):
    # Send a GET request to the url
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all the links in the page
        links = [link.get('href') for link in soup.find_all('a')]
        # Find all the images in the page
        images = [img.get('src') for img in soup.find_all('img')]
        # Print the title of the page
        title = soup.find('title').text
        return {
            'url': url,
            'links': links,
            'images': images,
            'title': title,
        }
    else:
        return None
    
if __name__ == '__main__':
    # Print the number of urls to be scraped
    print(f"Number of urls to be scraped: {len(urls)}")

    # Start the timer
    start_time = time.time()

    # Create a Pool object with the number of processes to be used
    with Pool(processes=4) as pool:
        # Map the scrape function to the urls
        results = pool.map(scrape, urls)
        # Print the results
        for result in results:
            if result:
                print(f"Title: {result['title']}")
                print(f"Links: {len(result['links'])}")
                print(f"Images: {len(result['images'])}")
                print(f"URL: {result['url']}\n")
            else:
                print("Failed to retrieve data from url")
    
    # Stop the timer
    end_time = time.time()
    # Print the start time
    print(f"Started scraping at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")
    # Print the end time
    print(f"Finished scraping at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
    # Print the total time taken
    print(f"Total time taken: {end_time - start_time} seconds")