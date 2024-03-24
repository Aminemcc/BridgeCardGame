import asyncio
from pyppeteer import launch
import requests
import os

chromium_path = "C:\Program Files\Chromium\Application\chrome.exe"
# url = "https://www.bridgebase.com/myhands/hands.php?tourney=69844-1710510084-&username=the+camel"
username = "Aminemc"
password = "Aminemc236"

def download_all_lin(links, save_path):
    with open(save_path, "wb") as f:
        for link in links:
            if "fetchlin" in link:
                print(link)
                response = requests.get(link)
                if response.status_code == 200:
                    f.write(b"st||")
                    f.write(response.content)
                    # f.write(b"\n")

async def scrape_links(url):
    # browser = await launch(headless=True)
    browser = await launch(headless=True, executablePath=chromium_path)
    page = await browser.newPage()
    await page.goto(url)
    await page.waitForSelector('a')
    await page.screenshot({'path': 'screenshot 1.png'})
    await page.type('#username', username)
    await page.type('#password', password)
    await page.click('input[type="submit"][value="Login"]')
    await page.waitForNavigation()
    await page.screenshot({'path': 'screenshot 2.png'})
    links = await page.evaluate('''() => {
        return Array.from(document.querySelectorAll('a'), a => a.href);
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

async def main():
    url = input("URL >> ")
    # filename = input("File Name : ")
    filename, links = await scrape_links(url)
    download_all_lin(links, f"{filename}.txt")

asyncio.get_event_loop().run_until_complete(main())
