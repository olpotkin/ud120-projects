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

### My code starts here
print "Dataset length: ", len(enron_data)
print "Number of features: ", len(enron_data.values()[0])


print "First person data: ", enron_data.values()[0]
# Count the number of POI:
# person_name - key
num_of_poi = 0
for person_name in enron_data:
    if (enron_data[person_name]["poi"] == 1):
        num_of_poi += 1
print "Number of POI: ", num_of_poi

# Real POI count:
#poi_names = open("../final_project/poi_names.txt").read().split('\n')
#poi_y = [name for name in poi_names if "(y)" in name]
#print("poi_names_count:", len(poi_y))



