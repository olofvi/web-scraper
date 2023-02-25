from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path
import scrapy
import csv
import re
import pandas as pd
from urllib.parse import urlparse

class CompanyObjects (CrawlSpider):
    name = "companylinks"


    def start_requests(self):
        file = pd.read_csv("../../Downloads/companydata.csv")
        urls = file['Website URL']
        for url in urls:
            if url is not None:
                if not url.startswith("http"):
                    page_url = ("http://" + url)
                    yield scrapy.Request(url=page_url, callback=self.parse)
                else: 
                    yield scrapy.Request(url=url, callback=self.parse)

   

    def parse(self, response):
        links = response.css('a::attr(href)').getall()
        baseURl = urlparse(response.url)
        class Companylink:
                linkedin = str
                facebook = str
                instagram = str
                twitter = str
                youtube = str
                tumblr = str
                reddit = str
                pintrest = str
                tiktok = str
                discord = str
                twitch = str
                snapchat = str
        for link in links:
            if "linkedin" in link:
                Companylink.linkedin = link
            if "facecebook" in link:
                Companylink.facebook = link
            if "instagram" in link:
                Companylink.instagram = link
            if "twitter" in link:
                Companylink.twitter = link
            if "youtube" in link:
                Companylink.youtube = link
            if "tumblr" in link:
                Companylink.tumblr = link
            if "reddit" in link:
                Companylink.reddit = link
            if "pintrest" in link:
                Companylink.pintrest = link
            if "tiktok" in link:
                Companylink.tiktok = link
            if "discord" in link:
                Companylink.discord = link
            if "twitch" in link:
                Companylink.twitch = link
            if "snapchat" in link:
                Companylink.snapchat = link

        yield {
            'baseUrl': baseURl,
            'linkedin': Companylink.linkedin,
            'facebook': Companylink.facebook,
            'instagram': Companylink.instagram,
            'twitter': Companylink.twitter,
            'youtube': Companylink.youtube,
            'reddit': Companylink.reddit,
            'tiktok': Companylink.tiktok,
            'discord': Companylink.discord,
            'twitch': Companylink.twitch,
            'snapchat': Companylink.snapchat
            }


