#from google.colab import output, drive, files # specific to Google Colab
import pandas as pd
import numpy as np
#import plotly.express as px
import requests
import warnings

# settings
warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)

def get_listings(api_key, listing_url):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/listing"

    querystring = {
        "api_key": api_key,
        "url":listing_url
    }

    return requests.request("GET", url, params=querystring)

def get_property_detail(api_key, zpid):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/property"

    querystring = {
        "api_key": api_key,
        "zpid":zpid
    }

    return requests.request("GET", url, params=querystring)

def get_zpid(api_key, street, city, state, zip_code=None):
    url = "https://app.scrapeak.com/v1/scrapers/zillow/zpidByAddress"

    querystring = {
        "api_key": api_key,
        "street": street,
        "city": city,
        "state": state,
        "zip_code":zip_code
    }

    return requests.request("GET", url, params=querystring)

# read in api key file
#df_api_keys = pd.read_csv(file_dir + "api_keys.csv")

# get keys
api_key = "62311a02-e186-4ff1-9a3c-40902a58afe3" #df_api_keys.loc[df_api_keys["API"] == "scrapeak"]["KEY"].iloc[0] # replace this with your own key
#api_key = "62311a02-e186-4ff1-9a3c-40902a58afe3"

# zillow search url
# 385 -> listing_url = "https://www.zillow.com/toronto-on/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-79.87900901171875%2C%22east%22%3A-78.87375998828125%2C%22south%22%3A43.422999454929105%2C%22north%22%3A43.99182230287438%7D%2C%22usersSearchTerm%22%3A%22Toronto%20ON%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3A50000%2C%22max%22%3A1000000%7D%2C%22mp%22%3A%7B%22min%22%3A254%2C%22max%22%3A5089%7D%7D%2C%22isListVisible%22%3Atrue%7D"
#listing_url = "https://www.realtor.ca/map#ZoomLevel=11&Center=45.549164%2C-73.597026&LatitudeMax=45.67789&LongitudeMax=-73.21388&LatitudeMin=45.42015&LongitudeMin=-73.98017&Sort=6-D&PGeoIds=g30_f25dfkk6&GeoName=Montreal%2C%20QC&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=0&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"
listing_url = "https://www.zillow.com/toronto-on/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-79.87900901171875%2C%22east%22%3A-78.87375998828125%2C%22south%22%3A43.422999454929105%2C%22north%22%3A43.99182230287438%7D%2C%22usersSearchTerm%22%3A%22Toronto%20ON%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A792680%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22listPriceActive%22%3Atrue%7D"
# get listings
listing_response = get_listings(api_key, listing_url)

# view all keys
listing_response.json().keys()

# check if request is successful
listing_response.json()["is_success"]

# view count of properies returned in request
num_of_properties = listing_response.json()["data"]["categoryTotals"]["cat1"]["totalResultCount"]
print("Count of properties:", num_of_properties)

# view all listings
df_listings = pd.json_normalize(listing_response.json()["data"]["cat1"]["searchResults"]["mapResults"])
print("Number of rows:", len(df_listings))
print("Number of columns:", len(df_listings.columns))
df_listings
#print(df_listings.columns)
#df_listings.to_excel("output.xlsx", sheet_name="Toronto_listings", index=True)
