## DataQuest_Lessons_ClassifyingMovieReviews_UnfinishedWork_20150331

url = ("https://dataquest.io")

#####################################

# Lesson 2

# Basics: Classifying movie reviews with naive bayes

# Classify movie reviews according to positive or negative sentiment using naive bayes.


#####################################

#### SUMMARY OF USEFUL CODE ####

Before we classify

We have a csv file containing movie reviews. Each row in the dataset contains the text of the review, and whether the tone of the review was classified as positive(1), or negative(-1).

We want to predict whether a review is negative or positive given only the text. In order to do this, we'll train an algorithm using the reviews and classifications in train.csv, and then make predictions on the reviews in test.csv. We'll then be able to calculate our error using the actual classifications in test.csv, and see how good our predictions were.

For our classification algorithm, we're going to use naive bayes. A naive bayes classifier works by figuring out the probability of different attributes of the data being associated with a certain class. This is based on bayes' theorem. The theorem is P(A∣B)=P(B∣A)P(A)P(B). This basically states "the probability of A given that B is true equals the probability of B given that A is true times the probability of A being true, divided by the probability of B being true."

Let's do a quick exercise to understand this rule better.


# Here's a running history for the past week.
# For each day, it contains whether or not the person ran, and whether or not they were tired.
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

# Let's say we want to calculate the odds that someone was tired given that they ran, using bayes' theorem.
# This is P(A).
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B).
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A).
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was tired"])

# Now we can calculate P(A|B).
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran

print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))

# Here's a running history for the past week.
# For each day, it contains whether or not the person ran, and whether or not they were tired.
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was 
not tired"], ["ran", "was not tired"], ["ran", "was tired"]]
# Let's say we want to calculate the odds that someone was tired given that they ran, using bayes' theorem.
# This is P(A).
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B).
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A).
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was 
tired"])
# Now we can calculate P(A|B).
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran
print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))
Run   Reset Code   Forum


Probability of being tired given that you ran: 0.6