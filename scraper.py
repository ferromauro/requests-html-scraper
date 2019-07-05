from requests_html import HTMLSession
import argparse

parser = argparse.ArgumentParser(description="Simple Yellow Pages data scraper")
parser.add_argument("search_term", type=str, help="Search Term")
parser.add_argument("location_term", type=str, help="Geo Location Term")
args = parser.parse_args() 

def scrape(search_term, location_term):
    session = HTMLSession()
    pages = session.get('https://www.yellowpages.com/search?search_terms='+search_term+'&geo_location_terms='+location_term)
    for page in pages.html:
        try: 
            organic_results = page.find('.organic', first=True)
            results = organic_results.find('.result')
            for result in results:
                business_name = result.find('.business-name')
                address = result.find('.adr')
                print(f'Business Name: {business_name[0].text}')
                print(f'Street Address: {address[0].text}')
                print(f'\n')
        except:
            print('No more results.')
            return

    
      
if __name__ == "__main__":
    scrape(args.search_term, args.location_term)
        