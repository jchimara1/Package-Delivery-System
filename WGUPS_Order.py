# -*- coding: utf-8 -*-
"""
Created on Thu May 26 01:49:54 2022

@author: jchim
"""

import Graph_Projection
from Graph_Projection import undirected_graph
from Graph_Projection import truck_route_algorithm
from Hash_Function import *
from Hash_Function import complete_table
from WGUPS_Truck import *
from WGUPS_Truck import WGUPS_Truck_1, WGUPS_Truck_2, WGUPS_Truck_3




address_list = []

undirected_graph.package_to_dictionary(complete_table)


    
def loading_inventory_on_truck_():

    # Populates the unvisited_addresses list with the locations from the graph.
     for i in undirected_graph.dictionary:
        address_list.append(i)

    # Priority 1 (see description above)
     for j in address_list:
        for inventory in undirected_graph.dictionary[j]:
            if inventory[5] == "9:00":
                WGUPS_Truck_1.add(inventory)

    # Priority 2 (see description above)
     for k in address_list:
        for inventory in undirected_graph.dictionary[k]:
            if inventory[5] == "10:30" and inventory[7] != "" and inventory[7] != "2" and inventory[7] != "W" and inventory[7] != "9:05":
                WGUPS_Truck_1.add(inventory)
            elif inventory[5] == "10:30" and inventory[7] == "9:05":
                WGUPS_Truck_2.add(inventory)

    # Priority 3 (see description above)
     for k in address_list:
        for inventory in undirected_graph.dictionary[k]:
            if inventory[5] == "10:30" and inventory[7] == "":
                WGUPS_Truck_1.add(inventory)

    # Priority 4 (see description above)
     for k in address_list:
        for inventory in undirected_graph.dictionary[k]:
            if inventory[5] == "17:00" and inventory[7] == "9:05":
                WGUPS_Truck_2.add(inventory)
            if inventory[5] == "17:00" and inventory[7] == "W":
                WGUPS_Truck_2.add(inventory)
            if inventory[5] == "17:00" and inventory[7] == "2":
                WGUPS_Truck_2.add(inventory)

    # Priority 5 (see description above)
     for k in address_list:
        for inventory in undirected_graph.dictionary[k]:
            if inventory[5] == "17:00" and inventory[7] == "":
                if len(WGUPS_Truck_1.inventory_on_truck) < 16:
                    WGUPS_Truck_1.add(inventory)
                elif len(WGUPS_Truck_2.inventory_on_truck) < 16:
                    WGUPS_Truck_2.add(inventory)
                elif len(WGUPS_Truck_3.inventory_on_truck) < 16:
                    WGUPS_Truck_3.add(inventory)
                else:
                    print("package could not be loaded")
   #Truck 1
     WGUPS_Truck_1_Start = WGUPS_Truck_1.path
     WGUPS_Truck_1_Start.append("4001 South 700 East")
     WGUPS_Truck_1.path = truck_route_algorithm(WGUPS_Truck_1.path)
    
    
    #Truck 2
     WGUPS_Truck_2_Start = WGUPS_Truck_2.path
     WGUPS_Truck_2_Start.append("4001 South 700 East")
     WGUPS_Truck_2.path = truck_route_algorithm(WGUPS_Truck_2.path)
    
    # Truck 3
     WGUPS_Truck_3_Start = WGUPS_Truck_3.path
     WGUPS_Truck_3_Start.append("4001 South 700 East")
     WGUPS_Truck_3.path = truck_route_algorithm(WGUPS_Truck_3.path)
    
    
    # End trip 
     WGUPS_Truck_1.path.append("4001 South 700 East")
     WGUPS_Truck_2.path.append("4001 South 700 East")
     WGUPS_Truck_3.path.append("4001 South 700 East")
    
      # Results
     print("WGUPS Truck information: ")
     print("WGUPS Truck 1 is loaded with ", len(WGUPS_Truck_1.inventory_on_truck), "packages")
     print("The inventory on WGUPS Truck 1 is :", *WGUPS_Truck_1.inventory_on_truck, sep="\n")
     print("WGUPS Truck 2 is loaded with", len(WGUPS_Truck_2.inventory_on_truck), "packages")
     print("The inventory on WGUPS Truck 2 is:", *WGUPS_Truck_2.inventory_on_truck, sep="\n")
     print("WGUPS Truck 3 is loaded with ", len(WGUPS_Truck_3.inventory_on_truck), "packages")
     print("The inventory on WGUPS Truck 3 is:", *WGUPS_Truck_3.inventory_on_truck, sep="\n")

    
    
    