## tfolkman_BayesPrimer_CoinFlips_WhatisBayesTheorem_20150305

url = ("https://dataquest.io")

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# Bayes Theorem

# Basics: The Coin Flip

# Bayes theorem is what allows us to go from a sampling distribution and a prior distribution to a posterior distribution.


#####################################

Overview of Useful code:



#####################################

#### SUMMARY OF USEFUL CODE ####


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### FULL SET OF INSTRUCTIONS ####

#### What is Bayes Theorem? ####

# Bayes theorem is what allows us to go from a sampling (or likelihood) distribution and a prior distribution 
# to a posterior distribution.

### What is a Sampling Distribution 

# A sampling distribution is the probability of seeing our data (X) given our parameters (θ). This is written as p(X|θ).

# For example, we might have data on 1,000 coin flips. Where 1 indicates a head. This can be represented in python as

import numpy as np
data_coin_flips = np.random.randint(2, size=1000)
# numpy.random.randint(low, high=None, size=None)
# Return random integers from the “discrete uniform” distribution
np.mean(data_coin_flips)

## 0.47899999999999998

# A sampling distribution allows us to specify how we think these data were generated. 
# For our coin flips, we can think of our data as being generated from a Bernoulli Distribution. 
# This distribution takes one parameter p which is the probability of getting a 1 (or a head for a coin flip). 
# It then returns a value of 1 with probablility p and a value of 0 with probablility (1-p).

#You can see how this is perfect for a coin flip. 
# With a fair coin we know our p = .5 because we are equally likely to get a 1 (head) or 0 (tail). 
# We can create samples from this distribution like this:

bernoulli_flips = np.random.binomial(n=1, p=.5, size=1000)
# Samples are drawn from a Binomial distribution with specified parameters, 
# n trials and p probability of success where n an integer >= 0 and p is in the interval [0,1]
np.mean(bernoulli_flips)






