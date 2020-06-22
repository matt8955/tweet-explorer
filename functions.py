import pandas as pd
import numpy as np
import nest_asyncio
import twint


def scrape_tweets(username,filename):
    c = twint.Config()
    c.Username = username
    c.Output = filename
    c.Hide_output = True
    c.Store_csv = True
    twint.run.Search(c)