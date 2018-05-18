import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import poisson
import plotly.plotly as py
import plotly
import plotly.figure_factory as ff
from dataConstants import *


FILE_PATH = './images/{}'
def plotScatter(X_values, Y_values, fileName):
    assert(len(X_values) == len(Y_values))

    plt.scatter(X_values, Y_values)
    
    plt.savefig(FILE_PATH.format(fileName))

def getFipsValues(countyNames, scores):
    fips = []
    values = []
    for i, c in enumerate(countyNames):
        if c in COUNTY_MAP:
            fips.append(COUNTY_MAP[c])
            values.append(scores[i])
        else:
            continue
            
    return values, fips 
        
def plotNY(values, fips, fileName):
    endpts = list(np.mgrid[min(values):max(values):9j])
    colorscale=['#004475', '#1B5884', '#376D93', '#5381A2', '#6F96B1', '#8AAAC0', '#A6BFCF', '#C2D3DE', '#DEE8ED', '#FFFFFF']
    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['NY'], show_state_data=True,
        colorscale=colorscale, binning_endpoints=endpts, round_legend_values=True,
        plot_bgcolor='rgb(229,229,229)',
        paper_bgcolor='rgb(229,229,229)',
        legend_title='Percetange with Health Insurance',
        county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
        exponent_format=False,
    )
    plotly.offline.iplot(fig, filename = '{}'.format(fileName), image='png')
    
def plotHist(values, bins):
    
    plt.hist(values, bins = bins)

def removeExcept(df, column):
    try:
        df.pop(column)
    except:
        pass
    
def checkUnique(df, column):
    counts = corHeartDisease['county_name'].value_counts()
    
def computePScores(values):
    mu = values.mean()
    return [poisson.cdf(x, mu) for x in values]

def check(name, keys):
    print name
    for key in keys:
        if name.lower() == keys.lower():
            return True
    return False

def filterDF(df):
    keys = COUNTY_MAP.keys()
    keys = [x.lower() for x in keys]
    return df[df['county'].isin(keys)]

def reverseMap():
    inverseMap = {}
    for key, value in COUNTY_MAP.iteritems():
        inverseMap[value] = key
        
    return inverseMap
