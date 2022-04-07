# -*- coding: utf-8 -*-
import scrapy

class AmazonScraperSpider(scrapy.Spider):
    name = 'amazon_scraper'
    allowed_domains = ['amazon.com']
    # assing a product-review-page url below
    start_urls = ['https://www.amazon.com/Nokia-520-Unlocked-Dual-Core-Smartphone/product-reviews/B00D7OOAHA/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber=1']
    
    def parse(self, response):
        review_texts = response.css('.a-size-base.review-text')
        for i in range(len(review_texts)):
            review_texts[i] = "".join(review_texts[i].css('::text').extract()).strip()

        review_ratings = response.css('[data-hook="review-star-rating"] > span::text').extract()

        for i in range(len(review_texts)):
            review = {
                'text' : review_texts[i],
                'rating': review_ratings[i]
            }
            yield review

        next_page_url = response.css('.a-last > a::attr(href)').extract_first()
        yield response.follow(next_page_url, self.parse)