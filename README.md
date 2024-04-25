## Zillow Search Scraper

This Zillow Search Scraper is a tool that helps you collect real estate data from [Zillow.com](https://www.zillow.com/). You can search for properties anywhere and extract a wide range of details, including full addresses, pricing, descriptions, and photos.

##  What can this Zillow Scraper do?

The [Zillow Search Scraper](https://apify.com/eunit/zillow-scraper) is a powerful tool that goes beyond Zillow's API limitations. It extracts various data points like price, address, and photos for properties listed for sale, rent, or already sold. You can use it to gather market trends, get basic listing details, or even scrape agent information. It allows for large-scale data collection and offers downloads in Excel, CSV, JSON, and other formats for your convenience.


###  How do I get started?

Even if you're new to web scraping, this Zillow scraper is user-friendly. To get started collecting real estate data, follow the steps below:

1. Create a [free Apify account](https://console.apify.com/sign-up),
2. Choose the [Zillow Scraper](https://apify.com/eunit/zillow-scraper), and provide the [search URL](https://apify.com/eunit/zillow-scraper) you want to scrape.
3. Click "**Start**" and wait for the data to be extracted.
4. Download data in JSON, XML, CSV, Excel, or HTML formats.

**Detailed instructions can be found in [our tutorial](https://blog.apify.com/scraping-real-estate-data).**

### Capabilities

This scraper extracts various Zillow data points, including:

* Full Address
* Price
* Bedrooms & Bathrooms
* Photos

### Input

* Use specific search URLs from Zillow.com containing necessary filters (URLs can contain `?searchQueryState=` fragment).
* See the dedicated Input page for detailed descriptions and examples.

**Example Input:**

```json
{
    "url": "https://www.zillow.com/baltimore-md/rentals/",
    "homepage": "https://zillow.com"
}
```

### Output Example

Scraped properties are shown as a dataset in the Output and Storage tabs.

* The output is initially organized as a table for viewing convenience.
* You can preview all fields and choose the download format (JSON, CSV, Excel, HTML, XML).

**Example Output (JSON):**

```json
[
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/91513d3ae89d7bb92391e4ddca49ed49-p_e.jpg",
    "price": "$1,325+ 1 bd",
    "link": "https://www.zillow.com/apartments/baltimore-md/st.-james-place-apartments/5Xt4b5/",
    "address": "St. James Place Apartments | 301 W Franklin St, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/67b6c2a973fbd06af24067f83f5b6fde-p_e.jpg",
    "price": "$1,564+ 1 bd",
    "link": "https://www.zillow.com/apartments/baltimore-md/the-brixton/BpkRWN/",
    "address": "The Brixton | 421 S Broadway, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/2fd2c6ef3934ad3781592043ceb2056a-p_e.jpg",
    "price": "$1,665+ 2 bds",
    "link": "https://www.zillow.com/apartments/baltimore-md/symphony-center-apartments/5XjDKv/",
    "address": "Symphony Center Apartments | 1020 Park Ave, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/bd5752310e46c377355e042bdf8400ce-p_e.jpg",
    "price": "$1,472+ 1 bd",
    "link": "https://www.zillow.com/b/building/39.294807,-76.61341_ll/",
    "address": "The Courtland | 415 Saint Paul Pl, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/4944c97ead4f910291e2064476797f10-p_e.jpg",
    "price": "$1,495+ Studio",
    "link": "https://www.zillow.com/apartments/baltimore-md/redwood-campus-center/ByN4cS/",
    "address": "Redwood Campus Center | 300 W Redwood St, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/e0cc225fa3ffe00df7f2c712557a7179-p_e.jpg",
    "price": "$1,410+ 1 bd",
    "link": "https://www.zillow.com/apartments/baltimore-md/the-renaissance-club/5Xt3yT/",
    "address": "The Renaissance Club | 1712 Waverly Way, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/5de26fa8ef57d9392d0ce05d3e303e89-p_e.jpg",
    "price": "$1,251+ Studio",
    "link": "https://www.zillow.com/apartments/baltimore-md/centerpoint/5Xhv8L/",
    "address": "Centerpoint | 8 N Howard St, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/d823f941e817e822fa5a6cbd6758f436-p_e.jpg",
    "price": "$1,795+ Studio",
    "link": "https://www.zillow.com/apartments/baltimore-md/elms-fells-point/5YYqRv/",
    "address": "Elms Fells Point | 2001 Aliceanna St, Baltimore, MD"
  },
  {
    "imageUrl": "https://photos.zillowstatic.com/fp/865417275d044e611bdca9dc9b067cf8-p_e.jpg",
    "price": "$1,300+ 1 bd",
    "link": "https://www.zillow.com/apartments/baltimore-md/green-acres-apartments/5XkgnX/",
    "address": "Green Acres Apartments | 3607 Labyrinth Rd, Baltimore, MD"
  }
]
```

**Example Output (Table):**

![Example Output (Table)](https://i.postimg.cc/Ghx3dWDY/image.png)


## Is it legal to scrape Zillow data?

While scraping publicly available Zillow data like prices and addresses is legal, be cautious as it might also include personal information. Regulations like [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) protect this data. Avoid scraping personal details unless you have a valid reason and consult a lawyer if unsure. Read our blog post on the [legality of web scraping](https://blog.apify.com/is-web-scraping-legal/).
