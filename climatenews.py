#sources:
#https://newsapi.org/docs
#https://www.youtube.com/watch?v=TOHnGTYCuII
#https://www.educative.io/answers/how-to-set-font-properties-for-title-and-labels-in-matplotlib
#https://stackoverflow.com/questions/44688019/yticklabels-cut-off-in-pandas-plot
#https://dataindependent.com/pandas/pandas-bar-plot-dataframe-plot-bar/

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from newskey import api_key

# fixing the formatting for matplotlib graph labels
rcParams.update({'figure.autolayout': True})

# getting all articles in the science category that are climate-related
endpoint = 'everything'
category = 'science'
query = 'climate'

url = f'https://newsapi.org/v2/{endpoint}?q={query}&language=en&apiKey={api_key}'

# getting API response with the requests module
response = requests.get(url)

# formatting the API response into a json format
data = response.json()
articles = data.get('articles')

# getting the needed information from within the json
title = articles[2]['title']
description = articles[2]['description']

# putting the article sources into a list
article_sources = []
for title in articles:
    article_sources.append(title['source']['name'])

# counting how many times each source appears from the 100 articles that were pulled by the API
article_counts_df  = pd.value_counts(np.array(article_sources))

# making a bar plot to visualize the article source counts
article_counts_df.plot.bar(x='source', y='# of articles',)

font1 = {'family':'fantasy','color':'darkgreen','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Which news sources are the most relevant to finding climate news?", fontdict = font1)
plt.xlabel("Times Source Appears", fontdict = font2)
plt.ylabel("News Source Names", fontdict = font2)

plt.show()
    

    

