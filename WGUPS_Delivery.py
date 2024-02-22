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


from datetime import timedelta, datetime


WGUPS_Truck_1 = WGUPS_Truck_1
WGUPS_Truck_2 = WGUPS_Truck_2
WGUPS_Truck_3 = WGUPS_Truck_3    

address_list = []

def Total_miles(WGUPS_Path):
     graph_weights = undirected_graph.edge
     total_miles = 0
     for mil in range(0, len(WGUPS_Path) -1):
         total_miles = total_miles + graph_weights[WGUPS_Path[mil], WGUPS_Path[mil+1]]
     return total_miles      

def Total_miles_for_all_Trucks():
    WGUPS_Truck_1_miles = Total_miles(WGUPS_Truck_1.path)
    WGUPS_Truck_2_miles = Total_miles(WGUPS_Truck_2.path)
    WGUPS_Truck_3_miles = Total_miles(WGUPS_Truck_3.path)                        
    Total_distance_traveled =  WGUPS_Truck_1_miles + WGUPS_Truck_2_miles + WGUPS_Truck_3_miles     
    print("Total miles traveled today by the three WGUPS Trucks are : ", round(Total_distance_traveled, 2) ) 
    print("Total miles traveled today by the WGUPS Truck 1 is : ", round(WGUPS_Truck_1_miles, 2)  ) 
    print("Total miles traveled today by the WGUPS Truck 2 is : ", round(WGUPS_Truck_2_miles, 2) ) 
    print("Total miles traveled today by the WGUPS Truck 3 is : ", round(WGUPS_Truck_3_miles, 2) ) 
    
undirected_graph.package_to_dictionary(complete_table)

loading_inventory_on_truck_()
Total_miles_for_all_Trucks()

def conut_s(t, s):
    todays_date = datetime.datetime(100, 1, 1 , t.hour, t.minute, t.second)
    todays_date = todays_date + timedelta(seconds = s)
    return todays_date.t()

# This function delivers all the packages to the correct address
# O(N^2)
def out_for_delivery():
    distance_between_locations = undirected_graph.edge

    # Truck 1 Delivery
    WGUPS_Truck_1_s = datetime(2022, 5, 28, 8, 0, 0)
    WGUPS_Truck_1.st = WGUPS_Truck_1_s
    WGUPS_Truck_1.ct = WGUPS_Truck_1_s
    for p in range(0, len(WGUPS_Truck_1.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_1.path[p], WGUPS_Truck_1.path[p+1]]
        WGUPS_Speed = WGUPS_Truck_1.truck_speed
        m_d = distance/WGUPS_Speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_1.ct, sta)
        WGUPS_Truck_1.ct = datetime(2020, 1, 1, time_delivered.hour, time_delivered.minute, time_delivered.second)
        uds = "DELIVERED AT", str(time_delivered)
        for information in WGUPS_Truck_1.inventory_on_truck:
            if WGUPS_Truck_1.path[p+1] == information[1]:
                information[8] = uds
    WGUPS_Truck_1.ft = WGUPS_Truck_1.ct
    print("Truck 1 Delivery:", *WGUPS_Truck_1.inventory_on_truck, sep="\n")  # prints using new lines instead of a giant line

    # Truck 2 Delivery
    WGUPS_Truck_2_s = datetime(2022, 5, 28, 9, 5, 0)
    WGUPS_Truck_2.st = WGUPS_Truck_2_s
    WGUPS_Truck_2.ct = WGUPS_Truck_2
    for p in range(0, len(WGUPS_Truck_2.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_2.path[p], WGUPS_Truck_2.path[p+1]]
        WGUPS_Speed = WGUPS_Truck_2.truck_speed
        m_d = distance/WGUPS_Speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_2.ct, sta)
        WGUPS_Truck_2.ct = datetime(2022, 5, 28, time_delivered.hour, time_delivered.minute, time_delivered.second)
        uds = "DELIVERED AT", str(time_delivered)
        for information in WGUPS_Truck_2.inventory_on_truck:
            if WGUPS_Truck_2.path[p+1] == information[1]:
                information[8] = uds
    WGUPS_Truck_2.ft = WGUPS_Truck_2.ct
    print("Truck 2 Delivery:", *WGUPS_Truck_2.inventory_on_truck, sep="\n") # prints using new lines instead of a giant line

    # Truck 3 Delivery
    WGUPS_Truck_3_s = datetime(2022, 5, 28, 9, 5, 0)
    WGUPS_Truck_3.st = WGUPS_Truck_3_s
    WGUPS_Truck_3.ct = WGUPS_Truck_3
    for p in range(0, len(WGUPS_Truck_3.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_3.path[p], WGUPS_Truck_3.path[p+1]]
        WGUPS_Speed = WGUPS_Truck_3.truck_speed
        m_d = distance/WGUPS_Speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_3.ct, sta)
        WGUPS_Truck_3.ct = datetime(2022, 5, 28, time_delivered.hour, time_delivered.minute, time_delivered.second)
        uds = "DELIVERED AT", str(time_delivered)
        for information in WGUPS_Truck_3.inventory_on_truck:
            if WGUPS_Truck_3.path[p+1] == information[1]:
                information[8] = uds
    WGUPS_Truck_3.ft = WGUPS_Truck_3.ct
    print("Truck 3 Delivery:", *WGUPS_Truck_3.inventory_on_truck, sep="\n") # prints using new lines instead of a giant line

def current_status(inventory_on_truck):
    for i in inventory_on_truck:
        i[9] = "loaded and out for delievery"
        
        
def view_your_package(h, mins, s):
    distance_between_locations = undirected_graph.edge
    end_time = datetime(2022, 5, 28, h, mins, s)
    
       # Truck 1 Delivery
    WGUPS_Truck_1_s = datetime(2022, 5, 28, 8, 0, 0)
    WGUPS_Truck_1.st = WGUPS_Truck_1_s
    WGUPS_Truck_1.ct = WGUPS_Truck_1_s
    current_status(WGUPS_Truck_1.inventory_on_truck)
    for i in range(0, len(WGUPS_Truck_1.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_1.path[i], WGUPS_Truck_1.path[i + 1]]
        speed = WGUPS_Truck_1.truck_speed
        m_d = distance / speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_1.ct, sta)
        if time_delivered < end_time.time():
            WGUPS_Truck_1.ct = datetime(2022, 5, 28, time_delivered.hour, time_delivered.minute, time_delivered.second)
            uds = "DELIVERED AT", str(time_delivered)
            for inventory in WGUPS_Truck_1.inventory_on_truck:
                if WGUPS_Truck_1.path[i + 1] == inventory[1]:
                    inventory[8] = uds
    WGUPS_Truck_1.ft = WGUPS_Truck_1.ct
    print("Truck 1 Delivery:", *WGUPS_Truck_1.inventory_on_truck, sep="\n")  # prints using new lines instead of a giant line

    # Truck 2 Delivery
    WGUPS_Truck_2_s = datetime(2022, 5, 28, 9, 5, 0)
    WGUPS_Truck_2.st = WGUPS_Truck_2_s
    WGUPS_Truck_2.ct = WGUPS_Truck_2_s
    current_status(WGUPS_Truck_2.inventory_on_truck)
    for i in range(0, len(WGUPS_Truck_2.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_2.path[i], WGUPS_Truck_2.path[i + 1]]
        speed = WGUPS_Truck_2.truck_speed
        m_d = distance / speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_2.ct, sta)
        if time_delivered < end_time.time():
            WGUPS_Truck_2.ct = datetime(2022, 5, 28, time_delivered.hour, time_delivered.minute, time_delivered.second)
            uds = "DELIVERED AT", str(time_delivered)
            for inventory in WGUPS_Truck_2.inventory_on_truck:
                if WGUPS_Truck_2.path[i + 1] == inventory[1]:
                    inventory[8] = uds
    WGUPS_Truck_2.ft = WGUPS_Truck_2.ct
    print("Truck 2 Delivery:", *WGUPS_Truck_2.inventory_on_truck, sep="\n")  # prints using new lines instead of a giant line

    # Truck 3 Delivery
    WGUPS_Truck_3_s = WGUPS_Truck_3.ft
    WGUPS_Truck_3.st = WGUPS_Truck_3_s
    WGUPS_Truck_3.ct = WGUPS_Truck_3_s
    current_status(WGUPS_Truck_3.inventory_on_truck)
    for i in range(0, len(WGUPS_Truck_3.path) - 1):
        distance = distance_between_locations[WGUPS_Truck_3.path[i], WGUPS_Truck_3.path[i + 1]]
        speed = WGUPS_Truck_3.truck_speed
        m_d = distance / speed
        sta = round(m_d * 60, 2)
        time_delivered = conut_s(WGUPS_Truck_3.ct, sta)
        if time_delivered < end_time.time():
            WGUPS_Truck_3.ct = datetime(2022, 5, 28, time_delivered.hour, time_delivered.minute, time_delivered.second)
            uds = "DELIVERED AT", str(time_delivered)
            for inventory in WGUPS_Truck_3.inventory_on_truck:
                if WGUPS_Truck_3.path[i + 1] == inventory[1]:
                    inventory[8] = uds
    WGUPS_Truck_3.ft = WGUPS_Truck_3.ct
    print("Truck 3 Delivery:", *WGUPS_Truck_3.inventory_on_truck, sep="\n")
             