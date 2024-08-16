import scrapy

class JumiaSpider(scrapy.Spider):
    name = "jumia"
    allowed_domains = ["jumia.com", "jumia.com.ng"]  # Updated to include jumia.com.ng
    start_urls = ["https://www.jumia.com.ng/mlp-appliances/",
                  "https://www.jumia.com.ng/phones-tablets/",
                  "https://www.jumia.com.ng/health-beauty/",
                  "https://www.jumia.com.ng/home-office/",
                  "https://www.jumia.com.ng/electronics/",
                  "https://www.jumia.com.ng/category-fashion-by-jumia/",
                  "https://www.jumia.com.ng/groceries/",
                  "https://www.jumia.com.ng/computing/",
                  "https://www.jumia.com.ng/baby-products/",
                  "https://www.jumia.com.ng/video-games/",
                  "https://www.jumia.com.ng/sporting-goods/"                  
                  ]

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy.downloadermiddlewares.offsite.OffsiteMiddleware': None,  # Disable temporarily
        },
        'LOG_LEVEL': 'DEBUG',
        'ROBOTSTXT_OBEY': False,  # Disable robots.txt adherence
    }

    def parse(self, response):
        # Extract product information
        for product in response.css("div.info"):
            yield {
                "name": product.css("h3.name::text").get(),
                "price": product.css("div.prc::text").get(),
            }

        # Extract the current page number from the URL
        if "mlp-appliances" in response.url:    
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/mlp-appliances/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)

        elif "phones-tablets" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/phones-tablets/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)

        elif "health-beauty" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/health-beauty/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url) 

        elif "home-office" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/home-office/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)  

        elif "electronics" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/electronics/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)   

        elif "category-fashion-by-jumia" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/category-fashion-by-jumia/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)   

        elif "groceries" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/groceries/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)  

        elif "computing" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/computing/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url) 

        elif "baby-products" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/baby-products/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)

        elif "video-games" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/video-games/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url) 

        elif "sporting-goods" in response.url:
            current_page = response.url.split("page=")[-1].split("#")[0] if "page=" in response.url else "1"
            next_page_number = int(current_page) + 1

            # Manually generate the next page URL
            next_page_url = f"/sporting-goods/?page={next_page_number}#catalog-listing"
            print("Next page URL:", next_page_url)                         
                            


        # Check if the next page exists (this is optional and can be based on some condition, e.g., a maximum page limit)
        if next_page_number <= 50:  # Assuming you know there's a max of 50 pages
            yield response.follow(next_page_url, callback=self.parse)


