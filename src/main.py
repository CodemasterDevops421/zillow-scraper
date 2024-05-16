"""
This module defines the `main()` coroutine for the Apify Actor, executed from the `__main__.py` file.

Feel free to modify this file to suit your specific needs.

To build Apify Actors, utilize the Apify SDK toolkit, read more at the official documentation:
https://docs.apify.com/sdk/python
"""
import random
from typing import Any

from apify import Actor
from playwright.async_api import async_playwright


# To run this Actor locally, you need to have the Playwright browsers installed.
# Run `playwright install --with-deps` in the Actor's virtual environment to install them.
# When running on the Apify platform, they are already included in the Actor's Docker image.


async def main() -> None:
    """
    The main coroutine is being executed using `asyncio.run()`, so do not attempt to make a normal function
    out of it, it will not work. Asynchronous execution is required for communication with Apify platform,
    and it also enhances performance in the field of web scraping significantly.

    Scrapes Zillow real estate website and returns a list of dictionaries containing scraped data.
    """

    async with Actor:

        # Structure of input is defined in input_schema.json
        actor_input = await Actor.get_input() or {}
        url = actor_input.get('url')
        homepage = actor_input.get('homepage')

        if not homepage:
            Actor.log.info('Homepage not specified, using default value...')
            homepage = "https://zillow.com"

        if not url:
            Actor.log.info('No URL specified in actor input, exiting...')
            await Actor.exit()

        data: list[dict[str, str | Any]] = []  # Define an empty list

        user_agent_strings = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.2227.0 '
            'Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
            'Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/109.0.3497.92 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
            'Safari/537.36',
        ]

        async with async_playwright() as p:

            # Launch Chromium browser instance
            browser = await p.chromium.launch(headless=False)

            # Create a new browser context with a randomly selected user agent string
            context = await browser.new_context(
                user_agent=user_agent_strings[random.randint(0, len(user_agent_strings) - 1)])

            page = await context.new_page()
            await page.goto(url)

            # Wait for all cards to load
            await page.wait_for_selector(".photo-cards")

            # Extract data from each card
            card_elements = await page.query_selector_all(".property-card")
            for card in card_elements:
                image_url = await card.query_selector("img")
                price_size = await card.query_selector("span[data-test=property-card-price]")
                link = await card.query_selector("a.property-card-link")
                address = await card.query_selector("address[data-test=property-card-addr]")

                card_details = {
                    "imageUrl": await image_url.evaluate("el => el.src"),
                    "price": await price_size.inner_text(),
                    "link": homepage + await link.get_attribute("href"),  # Get full URL
                    "address": await address.inner_text()
                }

                # Append card_details to data
                data.append(card_details)
                Actor.log.info(f"Extracted details: {card_details}")

        # Save jobs data to Apify Dataset
        await Actor.push_data(data)
