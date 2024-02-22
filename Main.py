# -*- coding: utf-8 -*-
"""
Created on Mon May 30 16:25:51 2022

@author: jchim
"""
from Hash_Function import Hashtable_function, show_deliveries
from Graph_Projection import truck_route_algorithm
from WGUPS_Delivery import Total_miles, Total_miles_for_all_Trucks, WGUPS_Truck_1, WGUPS_Truck_2, WGUPS_Truck_3
from WGUPS_Delivery import conut_s, out_for_delivery, current_status, view_your_package
from WGUPS_Order import loading_inventory_on_truck_

def graphical_user_interface():
    
    start = input("Good Morning The time is 8:00 AM /n"
                  "To start your day and Load your inventory type 1 /n"
                  "to check the status of a particular package type 2 /n"
    
                  "type 0 to leave the program /n")
    
    
    
    
    if start == "1":
        loading_inventory_on_truck_
        print("package are being loaded into their perspective trucks")
        t_s = input("\n to view the location and status of packages that are set to be delievered between the times of 8:35 AM and 9:25 AM /n "
                    "type 0 to leave the program /n")    
        
        if t_s == "0":
            print("You have selected to leave the program. Thank you come again")
            SystemExit
            
        if t_s == "1":
            view_your_package(9,25,0)
    
    
    
    
    
    if start == "0":
        print("You have selected to leave the program. Thank you come again")
        SystemExit
graphical_user_interface()