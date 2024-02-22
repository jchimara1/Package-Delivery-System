# -*- coding: utf-8 -*-
"""
Created on Wed May 11 05:14:54 2022

@author: jchim
"""

import csv


csv_file = "WGUPS_packages.csv"



class Hashtable_function:
    
    def __init__(self, table_size=40):
        self.Chaining_Table = []
        for i in range(table_size):
            self.Chaining_Table.append([])
    
    def add(self, value, mail):
        mail[0]= int(mail[0])
        slots = value % len(self.Chaining_Table)
        self.Chaining_Table[slots].append(mail)
        if mail[7] != "9:05":
            mail.append("Currently at the hub")
        if mail[7] == "9:05":
            mail.append("stuck on Flight")
            
            
            
    def kv(self, value, mail):
        key_hash = self.hashing(value)
        value_mail = [value, mail]

        if self.Chaining_Table[key_hash] is None:
            self.Chaining_Table[key_hash] = list([value_mail])
            return True
        else:
            for pair in self.Chaining_Table[key_hash]:
                if pair[0] == value:
                    pair[1] = value_mail
                    return True
            self.Chaining_Table[key_hash].append(value_mail)
            return True        
            
    def Find(self, value):

        Slot = value % len(self.Chaining_Table)
        list_of_Slots = self.Chaining_Table[Slot]
        
        for mail in list_of_Slots:
            if mail[0] == value:
                return mail
            return None
        
        
    def hashing(self, key):
        bucket = int(key) % len(self.Chaining_Table)
        return bucket
        
    def Delete(self, value):
        Slot = hash(value) %len(self.Chaining_Table)
        list_of_Slots =self.Chaining_Table[Slot]
        
        for mail in list_of_Slots:
            if mail[0] == value:
                list_of_Slots.Delete(value)
                
                
def Deliver(csv_name):
           stored_mail = Hashtable_function()
           with open(csv_name) as hash_table:
               fake_pandas = csv.reader(hash_table)
               next(fake_pandas, None)
               for line in fake_pandas:
                   stored_mail.add(int(line[0]), line)
           return stored_mail        


Hash_package = Hashtable_function(40)

class Hash_table_package:
     
    def __init__(self, p_ID, Street, City, State, ZIP, Deadline, Weight, Notes, Delivery_status):
        self.p_ID = p_ID
        self.Street = Street
        self.City = City
        self.State = State
        self.ZIP = ZIP
        self.Deadline = Deadline
        self.Weight = Weight
        self.Notes = Notes
        self.Delivery_status = Delivery_status
        
        
    def create_package(csv_file):
        with open(csv_file) as csv_package:
            Data = csv.reader(csv_package, delimiter=',',)
            next(Data)
            for i in csv_package:
             package_number = int(i[0])      
             package_Street = i[1]
             package_City = i[2]
             package_State = i[3]
             package_ZIP = i[4]
             package_Deadline = i[5]
             package_Weight = i[6]
             package_Notes = i[7]
             package_Delivery_status = i[8]
             package_Delivery_status = 'currently at Hub'
             
             package_list = Hash_table_package(package_number, package_Street, package_City,
                                               package_State, package_ZIP, package_Deadline, package_Weight, package_Notes, package_Delivery_status)
             Hash_package.kv(package_number, package_list)
                     
       
        
complete_table = Deliver("WGUPS_packages.csv")
#print(Hash_table_package.create_package(csv_file))
    
def show_deliveries(number):
       display = complete_table.Find(number)
       print(display)
       
       
       
#show_deliveries(1)      
       
       
       
       
       
