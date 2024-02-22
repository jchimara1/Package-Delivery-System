# -*- coding: utf-8 -*-
"""
Created on Fri May 27 02:24:28 2022

@author: jchim
"""


class WGUPS_Truck:
    
    def __init__(self):
        self.path = []
        self.inventory_on_truck = []
        self.truck_speed = 0.5 #30 miles per hour 
        self.st = None
        self.ct = None
        self.ft = None
   
    def add(self, value):
        self.inventory_on_truck.append(value)
        self.path.append(value[1])
        
        
    def Leave_hub(self, t):
        self.st = t
        
    def end(self, t):
        self.ft = t
        return t
    
    def now(self, t):
        self.ct = t
        return t
    
    def delete(self, value):
        self.inventory_on_truck.Delete(value)
        self.path.Delete(value[1])
        
        
WGUPS_Truck_1 = WGUPS_Truck()     
WGUPS_Truck_2 = WGUPS_Truck()    
WGUPS_Truck_3 = WGUPS_Truck()       