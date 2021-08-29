import pandas as pd
import statistics as stt
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import random
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
pMean = stt.mean(data)
standard_deviatiion = stt.stdev(data)
fig = pff.create_distplot([data], ["reading_time"], show_hist=False)
fig.add_trace(pgo.Scatter(x = [pMean, pMean], y =[0,1], mode="lines", name = "MEAN"))
fig.show()

print(pMean)
print(standard_deviatiion)


def randomSet(counter):
    dataSet = []
    for i in range( 0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    samplemean = stt.mean(dataSet)
    return(samplemean)
def show_Fig(meanlist):
    data = meanlist
    fig = pff.create_distplot([data], ["reading_time"], show_hist=False)
    fig.add_trace(pgo.Scatter(x = [pMean, pMean], y =[0,1], mode="lines", name = "MEAN"))
    fig.show()

    
def main():
    meanLIST = []
    for i in range(0,1000):
        setofmean = randomSet(100)
        meanLIST.append(setofmean)
    show_Fig(meanLIST)

main()
