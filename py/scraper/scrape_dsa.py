"""
Scrapes DSA problems from CodeChef and LeetCode using Selenium and BeautifulSoup.
"""
import os
import requests




def scrape_leetcode(limit=10):
    url = 'https://leetcode.com/api/problems/all/'
    response = requests.get(url)
    problems = []
    if response.status_code == 200:
        data = response.json()
        for item in data.get('stat_status_pairs', []):
            stat = item.get('stat', {})
            title = stat.get('question__title', '').strip()
            slug = stat.get('question__title_slug', '')
            if title and slug:
                link = f'https://leetcode.com/problems/{slug}/'
                problems.append({'title': title, 'link': link, 'source': 'LeetCode'})
                if len(problems) >= limit:
                    break
    else:
        print(f"Failed to fetch LeetCode problems. Status code: {response.status_code}")
    return problems




def main():
    leetcode_problems = []
    try:
        leetcode_problems = scrape_leetcode(limit=3000)
    except Exception as e:
        print(f"Error during scraping: {e}")
    all_problems = leetcode_problems
    db_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Database'))
    os.makedirs(db_dir, exist_ok=True)
    import re
    def sanitize_filename(name):
        # Remove or replace characters not allowed in filenames
        return re.sub(r'[\\/:*?"<>|]', '_', name)
    for i, prob in enumerate(all_problems, 1):
        safe_title = sanitize_filename(prob["title"])
        fname = os.path.join(db_dir, f'{i}. {safe_title}.txt')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(f"Title: {prob['title']}\nLink: {prob['link']}\nSource: {prob['source']}\n")
    print(f"Scraped and saved {len(all_problems)} problems.")

if __name__ == '__main__':
    main()
