import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=True)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://www.surfline.com/surf-reports-forecasts-cams/mexico/estado-de-baja-california/4017700"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["spot_name"] = soup.find("h3", class_="sl-spot-details__name").get_text()
    listings["size"] = soup.find("span", class_="quiver-surf-height").get_text()
    listings["url"] = "https://www.surfline.com" + soup.find("a", class_="sl-cam-list-link", href=True)["href"]

    # browser.visit(listings["url"])

    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")


    return listings

