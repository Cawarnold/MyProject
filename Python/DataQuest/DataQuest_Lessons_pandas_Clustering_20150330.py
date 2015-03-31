## DataQuest_Lessons_pandas_Clustering_20150330

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

# Python front-end for data -- Flask (simple) or Django (hard)   (http://insightdataengineering.com/blog/pipeline_map.html)

#####################################

# Chapter 16

# Basics: Clustering in Python

# Learn about clustering from the 114th Senate votes.

#####################################

#### SUMMARY OF USEFUL CODE ####

## Dimensions of a Pandas DataFrame
print(votes.shape)

## Counts types of votes, Yes, No, Abstain
print(pd.value_counts(votes.iloc[:,3:].values.ravel()))



########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#### Loading in the data ####

# We have a csv file that contains all the votes from the 114th Senate.

# Each row contains the votes of an individual senator. 
# Votes are coded as 0 for "No", 1 for "Yes", and 0.5 for "Abstain".
# Here are the first three rows of the data:

# name,party,state,00001,00004,00005,00006,00007,00008,00009,00010,00020,00026,00032,00038,00039,00044,00047
# Alexander,R,TN,0,1,1,1,1,0,0,1,1,1,0,0,0,0,0
# Ayotte,R,NH,0,1,1,1,1,0,0,1,0,1,0,1,0,1,0

# Instructions
# Feel free to write code and analyze the data however you want.
# You can hit "Run" to run your own code.
# When you're done, press "Next" to move forward.

import pandas as pd
# Read in the csv file
votes = pd.read_csv("114_congress.csv")

# As you can see, there are 100 senators, and they voted on 15 bills (we subtract 3 because the first 3 columns aren't bills).
print(votes.shape)

# To get the first three rows.
print(votes.loc[0:2]) 

# We have more "Yes" votes than "No" votes overall
print(pd.value_counts(votes.iloc[:,3:].values.ravel()))

# ravel returns a flattened (1D) array
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
>>>[[1 2 3
>>> 4 5 6]]
print(np.ravel(x))
>>>[1 2 3 4 5 6]

# values returns just the values (in condensed format) of the dataframe. ie, no column headers.

#### Initial clustering ####

# k-means clustering will try to make clusters out of the senators.
# Each cluster will contain senators whose votes are as similar to each other as possible.
# We'll need to specify the number of clusters we want upfront.
# Let's try 2 to see how that looks.

# Instructions
# Press "Next" to move forward.

import pandas as pd
# The kmeans algorithm is implemented in the scikits-learn library
from sklearn.cluster import KMeans
# Create a kmeans model on our data, using 2 clusters.  
# random_state helps ensure that the algorithm returns the same results each time.
kmeans_model = KMeans(n_clusters=2, random_state=1).fit(votes.iloc[:, 3:])
# These are our fitted labels for clusters -- the first cluster has label 0, and the second has label 1.
labels = kmeans_model.labels_
# The clustering looks pretty good!
# It's separated everyone into parties just based on voting history
print(pd.crosstab(labels, votes["party"]))

>party D   I   R
>row_0
>0    41   2   0
>1     3   0  54


#### Exploring people in the wrong cluster ####

# We can now find out which senators are in the "wrong" cluster.
# These senators are in the cluster associated with the opposite party.

# Let's call these types of voters "oddballs" (why not?)
# There aren't any republican oddballs
democratic_oddballs = votes[(votes["label"] == 1) & (votes["party"] == "D")]
# It looks like Reid has abstained a lot, which changed his cluster.
# Manchin seems like a genuine oddball voter.
print(democratic_oddballs["name"])

> 42 Heikamp
> 56 Manchin
> 74 Reid

#### Plotting out the clusters ####

# Let's explore our clusters a little more by plotting them out.
# Each column of data is a dimension on a plot, and we can't visualize 15 dimensions.
# We'll use principal component analysis to compress the vote columns into two.
# Then, we can plot out all of our senators according to their votes, and shade them by their cluster.

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
pca_2 = PCA(2)
# Turn the vote data into two columns with PCA
plot_columns = pca_2.fit_transform(votes.iloc[:,3:18])
print(plot_columns)
# Plot senators based on the two dimensions, and shade by cluster label
# You can see the plot by clicking "plots" to the bottom right
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=votes["label"])
plt.show()
plt.clf()

## plot_columns is just a list of points for a graph. 

#### Trying even more clusters ####

# While two clusters is interesting, it didn't tell us anything we don't already know.
# More clusters could show wings of each party, or cross-party groups.
# Let's try using 5 clusters to see what happens.

import pandas as pd
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=5, random_state=1).fit(votes.iloc[:, 3:])
labels = kmeans_model.labels_
# The republicans are still pretty solid, but it looks like there are two democratic "factions"
print(pd.crosstab(labels, votes["party"]))

