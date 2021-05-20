""" 
    This script scrapes benchmark data from the official geekbench website.
    Right now only the top twenty single core scores are gathered from the
    PC, Mac and android sections. However, this script can be easily extended
    to gather both single and multi-core scores from all available sections.
    In addition, speed can be drastically improved through threads or async processing,
    as the script is highly I/O bound at the moment.
 """

import aiohttp
import asyncio
import cchardet
from array import array
from enum import Enum
from bs4 import BeautifulSoup, SoupStrainer
from typing import Dict

# CONSTANTS
BASE_URL = 'https://browser.geekbench.com/'

class SCRAPE_URLS(Enum):
    PROCESSOR_URL = BASE_URL + 'processor-benchmarks'
    ANDROID_URL = BASE_URL + 'android-benchmarks'
    IOS_URL = BASE_URL + 'ios-benchmarks'
    MAC_URL = BASE_URL + 'mac-benchmarks'

STRAINER = SoupStrainer("td",{"class":["name", "score"]})
ENTRIES_PER_LIST = 20



async def get_scores(url, sorted_scores_array) -> Dict:
    # get html file
    session = aiohttp.ClientSession()
    try:
        print(f"gathering data from: {url}")
        response = await session.get(url)
        html_str = await response.read()
        
        # pass html file into beautiful soup for parsing
        # we only need the data from the tables
        soup = BeautifulSoup(html_str, 'lxml', parse_only=STRAINER)
    except Exception(aiohttp.ClientPayloadError) as e:
        print(f"invalid response payload from: {url}")
        print(e)
    except Exception(aiohttp.InvalidURL) as e:
        print(f"the url: {url} is invalid")
        print(e)
    except Exception(aiohttp.ClientConnectionError) as e:
        print(f"error encountered while connecting to: {url}")

    # close the connection
    await session.close()

    entry_names = []
    entry_scores = []

    # scrape data from soup object
    # and then store data 
    for entry in soup.select('.name', limit=ENTRIES_PER_LIST):
        entry_str = entry.get_text(" ", strip=True)
        entry_names.append(entry_str)
    
    for entry in soup.select('.score', limit=ENTRIES_PER_LIST):
        entry_str = entry.get_text(strip=True)
        entry_number = int(entry_str)
        entry_scores.append(entry_number)
        sorted_scores_array.append(entry_number)
    
    # store the entry name and coressponding score in dictionary
    # the entry score is used as the key here
    return dict(zip(entry_scores, entry_names))


async def main():
    sorted_scores = array('H')
    entries_dict = {}
    
    pc_results = await get_scores(SCRAPE_URLS.PROCESSOR_URL.value, sorted_scores)
    mac_results = await get_scores(SCRAPE_URLS.MAC_URL.value, sorted_scores)
    android_results = await get_scores(SCRAPE_URLS.ANDROID_URL.value, sorted_scores)
    
    # sort the scores in descending order
    sorted_scores = array(sorted_scores.typecode, sorted(sorted_scores, reverse=True))
    
    # combine dictionaries together
    # this method only works for python >= 3.9.0
    entries_dict = entries_dict | pc_results | mac_results | android_results

    # finally print the results
    for score in sorted_scores:
        print(f'{entries_dict[score]} : {score}')

if __name__=='__main__':
    
    asyncio.get_event_loop().run_until_complete(main())







