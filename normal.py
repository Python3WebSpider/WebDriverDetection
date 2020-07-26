import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto('http://localhost:8000/detect.html')
    await page.waitFor('.el-card')
    await asyncio.sleep(1)
    content = await page.content()
    doc = pq(content)
    items = doc('.item').items()
    for item in items:
        key = item.find('.key').text()
        value = item.find('.value').text()
        print(f'{key}: {value}')
    await page.close()
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
