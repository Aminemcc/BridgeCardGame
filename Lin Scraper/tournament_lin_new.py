import asyncio
from pyppeteer import launch
import requests
import os
from urllib.parse import unquote
import re

# Fix the path - use raw string or double backslashes
chromium_path = r"C:\Program Files\Chromium\Application\chrome.exe"
# Or: chromium_path = "C:\\Program Files\\Chromium\\Application\\chrome.exe"

username = "Aminemc"
password = "Aminemc236"

def download_all_lin(links, save_path):
    with open(save_path, "w") as f:
        i = 1
        for link in links:
            if i % 2:
                lin_match = re.search(r'lin=([^&]+)', link)
                lin_content = ""
                if lin_match:lin_content = unquote(lin_match.group(1))
                else: lin_content = unquote(link)
                lin_content = lin_content.replace("https://www.bridgebase.com/tools/handviewer.html?bbo=y&lin=","")
                f.write("st||")
                f.write(lin_content)
                f.write("\n")
            i += 1

async def scrape_links(url):
    try:
        # Try with executablePath first, fall back to default if it fails
        try:
            browser = await launch(headless=True, executablePath=chromium_path)
        except:
            browser = await launch(headless=True)
            
        page = await browser.newPage()
        await page.goto(url)
        await page.waitForSelector('a')
        await page.screenshot({'path': 'screenshot_1.png'})
        
        # Check if we need to login
        if await page.querySelector('#username'):
            await page.type('#username', username)
            await page.type('#password', password)
            await page.click('input[type="submit"][value="Login"]')
            await page.waitForNavigation()
        
        await page.screenshot({'path': 'screenshot_2.png'})
        
        links = await page.evaluate('''() => {
            const allLinks = Array.from(document.querySelectorAll('a'));
            return allLinks
                .map(a => a.href)
                .filter(href => href.includes('handviewer.html') && href.includes('lin='));
        }''')
        
        tourneyName = await page.evaluate('''
        () => {
            let linkTexts = [];
            document.querySelectorAll('td.tourneyName a').forEach(a => {
                linkTexts.push(a.textContent.trim());
            });
            return linkTexts;
        }''')
        
        await browser.close()
        return (tourneyName, links)
    
    except Exception as e:
        print(f"Error during scraping: {e}")
        if 'browser' in locals():
            await browser.close()
        return ([], [])

async def main():
    url = input("URL >> ")
    tourneyNames, links = await scrape_links(url)
    
    # Use the first tourney name as filename, or default if none found
    filename = tourneyNames[0] if tourneyNames else "tournament"
    
    # Clean filename for filesystem
    filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()
    
    download_all_lin(links, f"{filename}.txt")
    print(f"Downloaded to {filename}.txt")

# Use modern asyncio run method
if __name__ == "__main__":
    asyncio.run(main())