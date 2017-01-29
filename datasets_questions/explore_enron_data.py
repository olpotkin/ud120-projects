#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

### My code starts here ###
print "Dataset length: ", len(enron_data)
print "Number of features: ", len(enron_data.values()[0])


print "First person data: ", enron_data.values()[0]
# Count the number of POI:
# person_name - key
num_of_poi = 0
for person_name in enron_data:
    if (enron_data[person_name]['poi'] == 1):
        num_of_poi += 1
print "Number of POI: ", num_of_poi

# QUERY THE DATASET - 1
# Total value of the stock belonging to James Prentice
person_name = 'PRENTICE JAMES'
parameter = 'total_stock_value'
print "James Prentice stock: ", enron_data[person_name][parameter]

# QUERY THE DATASET - 2
# How many email messages do we have from Wesley Colwell to person of interest?
person_name = 'COLWELL WESLEY'
parameter = 'from_this_person_to_poi'
print "Messages from Wesley Colwell to PoI: ", enron_data[person_name][parameter]

# QUERY THE DATASET - 3
# The value of stock options exercised by Jeffrey K Skilling?
person_name = 'SKILLING JEFFREY K'
parameter = 'exercised_stock_options'
print "Value of stock options exercised by Jeffrey K Skilling: ", enron_data[person_name][parameter]

# Who took home the most money?
person_name = 'FASTOW ANDREW S'
parameter = 'total_payments'
print "Andy Fastow: ", enron_data[person_name][parameter]
person_name = 'SKILLING JEFFREY K'
print "Jeffrey Skilling: ", enron_data[person_name][parameter]
person_name = 'LAY KENNETH L'
print "Ken Lay: ", enron_data[person_name][parameter]

# Count valid emails
valid_emails = 0
for p in enron_data:
    if enron_data[p]['email_address'] != 'NaN':
        valid_emails += 1
print "Valid emails: ", valid_emails

# Count quantified salaries
quantified_salaries = 0
for p in enron_data:
    if enron_data[p]['salary'] != 'NaN':
        quantified_salaries += 1
print "Quantified salaries: ", quantified_salaries

# 1. Persons who has a NaN value for their total payments
# 2. Count percentage of people from dataset as a whole
q_total_payments = 0
q_total = 0
for p in enron_data:
    q_total += 1
    if enron_data[p]['total_payments'] == 'NaN':
        q_total_payments += 1
print "NaN for total payments have: ", q_total_payments
print "NaN for total payments have (%): ", (float(q_total_payments)/float(q_total))*100

# 1. POI who has a NaN value for their total payments
# 2. Count percentage of POI from dataset as a whole
num_of_poi = 0
for p in enron_data:
    if enron_data[p]['poi'] == 1:
        if enron_data[p]['total_payments'] == 'NaN':
            num_of_poi += 1
print "Number of POI: ", num_of_poi

