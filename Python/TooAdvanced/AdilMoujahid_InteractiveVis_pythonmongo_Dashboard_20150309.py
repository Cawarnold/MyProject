## AdilMoujahid_InteractiveVis_pythonmongo_Dashboard_20150309

# You can also use ctrl+alt+r to run code. Click on the instructions panel, then type ? to see all the hotkeys.

#####################################

# DonorChoose.org is a US based Nonprofit organisation.

# Basics: Interactive Data Visualisation

# The building blocks for creating a meaningful interactive data visualization.
# Using: 
# MongoDB 	for storing and querying the data
# Python 	for building a web server that interacts with MongoDB and serving html pages
# Javascript libraries d3.js, dc.js and crossfilter.js for building interative charts.

# http://adilmoujahid.com/posts/2015/01/interactive-data-visualization-d3-dc-python-mongodb/


########################################################################################################################
########################################################################################################################
########################################################################################################################

#### The case study ####

# We will use a dataset from DonorsChoose.org to build a data visualization 
# that represents school donations broken down by different attributes

# DonorsChoose.org is a US based nonprofit organization that allows individuals to donate money directly to 
# public school classroom projects. Public school teachers post classroom project requests on the platform, 
# and individuals have the option to donate money directly to fund these projects. 
# The classroom projects range from pencils and books to computers and other expensive equipments for classrooms. 
# In more than 10 years of existence, this platform helped teachers in all US states to 
# post more than 7700,000 classroom project requests and raise more than $280,000,000. 
# DonorsChoose.org is making the platform data open and available for making discoveries and building applications. 
# In this tutorial we will be using one of the available datasets for building an interactive data visualization that 
# represents school donations broken down by different attributes.

#### Getting and understanding the data ####

# We will get a file called opendata_projects.csv
# The data is represented in csv format. csv files are used for storing tabular data and its metadata. 

# This file contains 771,929 records along 44 attributes. 
# In this tutorial, we will be using only 5 attributes, 

# Attribute: example
# school_state: NY
# resource_type: Technology
# poverty_level: highest poverty
# date_posted: 2002-11-11
# total_donations: 329.00


#### Storing and querying the data: A crash course in MongoDB ####

# Now that we have our dataset, we will store the data into a database called MongoDB. 
# MongoDB is the most popular non-relational database. 
# Relational databases represent data in rows and columns (similar to a spreadsheet). 
# In relational databases, we have to specify the data schema in advance. 
# Furthermore, relational database don’t scale very well. 
# In contrast, MongoDB is a schemaless database, 
# which provides more flexibly in storing records of different formats in the same database. 
# mongoDB scales very well. 
# However, it doesn’t support joins and transactions that relational databases provide. 
# MongoDB stores data in BSON format (similar to JSON), which stands for Binary JSON. 
# JSON stands for JavaScript Object Notation. This format makes it easy to humans to read the data, and for machines to parse it.

# MongoDB can be used with all major operating systems. The installation guides can be found in this page.






