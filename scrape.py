import asyncio
import aiohttp
import bs4

# some subreddits I'm interested in
subreddits = ['/r/Science',
    '/r/AskScience',
    '/r/everythingscience',
    '/r/learnprogramming',
    '/r/compsci',
    '/r/javascript',
    '/r/coding',
    '/r/machinelearning',
    '/r/howtohack',
    '/r/cpp',
    '/r/python',
    '/r/learnpython',
    '/r/engineering',
    '/r/ubuntu',
    '/r/stocks',
    '/r/math',
    '/r/Space',
    '/r/nhl',
    '/r/nutrition',
    '/r/history',
    '/r/lifehacks',
    '/r/ZenHabits',
    '/r/climbing',
    '/r/food']

async def get_top_link(page):
    soup = bs4.BeautifulSoup(page, "lxml")
    try:
        return soup.find('div', id='siteTable').find('div', {"data-rank" : "1"})['data-permalink']
    except:
        return ''

async def scrape(subreddit):
    url = 'https://www.reddit.com'+subreddit
    print('Starting {}'.format(subreddit))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page = await response.text()
            top = await get_top_link(page)
            print('Top post for {}: {}'.format(subreddit, 'https://www.reddit.com'+top)); return

futures = [scrape(subreddit) for subreddit in subreddits]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
