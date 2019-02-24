import matplotlib.pyplot as plt
import numpy as np

### shows bar chart for each sentiment for discussed topic
def showBarCharForSentiment(topicWithPotential, pos=True):
    # get average percentage of sentiment for each unique word in all comments
#     allTopics = {k: v[0]/v[1] for k, v in topicWithPotential.items()}
#     from operator import itemgetter
#     dataMap = sorted(topicWithPotential, key=lambda kv: kv[1][1]/kv[1][2],  reverse=True)
#     print(dataMap)
    # this is for plotting purpose
    labels = []
    polarity = []
  
    for each in topicWithPotential[: 20]:
        labels.append(each[0])
        if pos:
            polarity.append(each[1][1])
        else:
            polarity.append(each[1][0])
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

def showPiChart(sortedDict):
    pieLabels = []
    populationShare = []
    localDict = sortedDict[:10]
    for each in localDict:
        pieLabels.append(each[0])
        populationShare.append(each[1][2])
        
    figureObject, axesObject = plt.subplots()
    axesObject.pie(populationShare,
            labels=pieLabels,
            autopct='%1.2f',
            startangle=90)
    axesObject.axis('equal')
    plt.show()
    
    
def showTempBarChart():
    x = ['fund transfer', 'login', 'biometric', 'crash', 'internet', 'dashboard', 'password']
    polarity = [0.85, 0.78, 0.45, 0.40, 0.40, 0.38, 0.3]
#     x = ['interest', 'account', 'friendly', 'wallet', 'secure', 'great', 'easy']
#     polarity = [0.70, 0.60, 0.58, 0.50, 0.40, 0.38, 0.3]

#     x = ['interest', 'account', 'friendly', 'wallet', 'secure', 'great', 'easy']
#     polarity = [0.40, 0.38, 0.35, 0.32, 0.25, 0.22, 0.20]
    plt.figure(figsize=(10, 5)) 
    bars = plt.bar(x, polarity)
    for bar in bars:
        bar.set_color('r')
    plt.xlabel('Topics', fontsize=15)
    plt.ylabel('Polarity', fontsize=15)
    plt.ylim(0.0, 1.0)
    plt.xticks(x, labels, fontsize=12, rotation=70)
    plt.title('People opinion most -ve on digiBank app store')