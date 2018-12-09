import matplotlib.pyplot as plt
import numpy as np

### shows bar chart for each sentiment for discussed topic
def showBarCharForSentiment(topicWithPotential, pos=True):
    # get average percentage of sentiment for each unique word in all comments
#     allTopics = {k: v[0]/v[1] for k, v in topicWithPotential.items()}
#     from operator import itemgetter
    dataMap = sorted(topicWithPotential, key=lambda kv: kv[1][1]/kv[1][2],  reverse=True)
#     print(dataMap)
    # this is for plotting purpose
    labels = []
    polarity = []
  
    for each in dataMap[: 20]:
        labels.append(each[0])
        polarity.append(each[1][1]/each[1][2])

    plt.figure(figsize=(20, 10)) 
    x = np.arange(len(polarity))
    bars = plt.bar(x, polarity)
    for bar in bars:
        if pos:
            bar.set_color('g')
        else:
            bar.set_color('r')
    plt.xlabel('Topics', fontsize=15)
    plt.ylabel('Polarity', fontsize=15)
    plt.xticks(x, labels, fontsize=12, rotation=70)
    plt.title('People opinion most -ve on digiBank app store')