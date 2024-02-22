# -*- coding: utf-8 -*-
"""
Created on Thu May 19 20:25:21 2022

@author: jchim
"""

import csv
# import Hash_Function
from Hash_Function import Deliver



# initial hash for distances, excludes vertices (miles) for all locations at each node
hashtable_distances = []
# distance graph for algorithm, includes vertices (miles) for all locations at each node
raw_distances = []
# address hash, list of lists, each sublist = [location_id, street_address, zipcode]
hashtable_addresses = []

def read_csv_data(distance_data):
    data = []
    with open(distance_data) as raw_csv:
     filtered = (line.replace('\n', '') for line in raw_csv)
     csv_data = csv.reader(filtered)
     next(csv_data, None)
     for row in csv_data:
        data.append(row)
    return(data)
        
f = read_csv_data('WGUPS_distances.csv')  
      
class create_graph:        
        
 def __init__(self):
     self.dictionary = {}
     self.edge = {}
     self.hashtable_addresses = hashtable_addresses

 def create_edges_(self, vertex, node, miles = 1.0):
     self.edge[(vertex, node)] = miles
     
     
 def create_vertexs(self, name):
        self.dictionary[name] = []
        
 def package_to_dictionary(self, ht):
        for bucket in ht.Chaining_Table:
            for item in bucket:
                self.dictionary[item[1]].append(item)
                

             
def csv_to_graph(csv):
    information= read_csv_data(csv)
    miles2 = create_graph()
    for i in information:
        miles2.create_vertexs(i[1])
    for i in information:
            for j in range(3, len(i)):
                miles2.create_edges_(i[1], information[j-3][1], float(i[j]))
    return miles2
    
def adjacency_list(csv_to_graph):
    csv_to_graph.edge
    return csv_to_graph.edge

def graph_x(csv_to_graph):
    csv_to_graph.dictionary
    return(csv_to_graph.dictionary)


undirected_graph = csv_to_graph('WGUPS_distances.csv')

def truck_route_algorithm(path):
     start = "4001 South 700 East"  # all trucks start their deliveries at the hub
     distance_between_Nodes =  undirected_graph.edge # get the edge weights from the graph
     sorted_truck_route = path  # this is the route created initially as packages were loaded to the truck
     determined_route = [start]
     
     while len(sorted_truck_route) != 0:
        min = [0, start]  # "0" is the edge weight and "start" is the address, which will change throughout the loop
        for location in sorted_truck_route:
            distance = distance_between_Nodes[determined_route[-1], location]  # get the edge weights between each location
            if min[0] == 0:  # helps establish starting location as well as self-loops to the same location
                min = [distance, location]
            if distance < min[0] and distance != 0:
                min = [distance, location]
        if min[1] not in determined_route:  # eliminates double visits to the same place
            determined_route.append(min[1])
        sorted_truck_route.remove(min[1])  # removes the location and repeat the while loop until empty

    # This is the better route for the truck to take
     return determined_route

    
    
    
    
    
    
    
    
    




