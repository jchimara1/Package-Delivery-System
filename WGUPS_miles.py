# -*- coding: utf-8 -*-
"""
Created on Fri May 27 03:28:22 2022

@author: jchim
"""


from Graph_Projection import *
from Graph_Projection import undirected_graph
from Hash_Function import *
from Hash_Function import complete_table
from WGUPS_Truck import *
from WGUPS_Truck import WGUPS_Truck_1, WGUPS_Truck_2, WGUPS_Truck_3
from WGUPS_Order import *
from WGUPS_Order import address_list



address_list = []


class miles():
    
  def Total_miles(WGUPS_Path):
     graph_weights = undirected_graph.edge
     total_miles = 0
     for mil in range(0, len(WGUPS_Path) -1):
         total_miles = total_miles + graph_weights[WGUPS_Path[mil], WGUPS_Path[mil+1]]
     return total_miles      

  def Total_miles_for_all_Trucks(WGUPS_Truck_path):
    WGUPS_Truck_1_miles = Total_miles(WGUPS_Truck_1.path)
    WGUPS_Truck_2_miles = Total_miles(WGUPS_Truck_2.path)
    WGUPS_Truck_3_miles = Total_miles(WGUPS_Truck_3.path)                        
    Total_distance_traveled =  WGUPS_Truck_1_miles + WGUPS_Truck_2_miles + WGUPS_Truck_3_miles     
    print("Total miles traveled today by the three WGUPS Trucks are : ", round(Total_distance_traveled, 2) ) 
    print("Total miles traveled today by the WGUPS Truck 1 is : ", round(WGUPS_Truck_1_miles, 2)  ) 
    print("Total miles traveled today by the WGUPS Truck 2 is : ", round(WGUPS_Truck_2_miles, 2) ) 
    print("Total miles traveled today by the WGUPS Truck 3 is : ", round(WGUPS_Truck_3_miles, 2) ) 
             