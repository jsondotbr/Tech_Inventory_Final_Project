#This module is a Technology class

class Technology:
    #Initializing the data attributes
    def __init__(self,item,serial_number,needs_servicing,room_location):
        self.__item = item
        self.__serial_number = serial_number
        self.__needs_servicing = needs_servicing
        self.__room_location = room_location
        
    def set_item(self,item):
        self.__item = item
        
    def set_serial_number(self,serial_number):
        self.__serial_number = serial_number

    def set_needs_servicing(self,needs_servicing):
        self.__needs_servicing = needs_servicing

    def set_room_location(self,room_location):
        self.__room_location = room_location
    def get_item(self):
        return self.__item

    def get_serial_number(self):
        return self.__serial_number

    def get_needs_servicing(self):
        return self.__needs_servicing

    def get_room_location(self):
        return self.__room_location

    def __str__(self):
        return 'The item is: ' + self.__item +\
               '\nThe serial number is: ' + self.__serial_number +\
               '\nDoes this device need servicing? ' + self.__needs_servicing +\
               '\nThis device is located in: ' + self.__room_location
    
