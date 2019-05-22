# Tech_Inventory_Final_Project
Final Project
Technology Inventory

This program is designed for IT administrators of small-midsize businesses, schools, & colleges to create an inventory of the devices being used and if any of these need servicing.  This does not track ongoing servicing done or what needs to be serviced.  This would be better addressed with another program.  This program also stores the serial number of the device, along with the room/office currently located.

The two main scripts in this program are:
    • Technology_Inventory_Final.py – This imports the technology_class & 	pickle, sets global constants (LOOK_UP,ADD,CHANGE,DELETE,QUIT) for the
      Menu choice. This also is responsible for running functions,
      opening/pickling/closing the output_file (technology.dat dictionary).
    • technology_class.py – This module is a Technology class (class  
      Technology). The Technology_Inventory_Final.py references this in it’s
      processing and output of data.


Program Interface:

When this program is initialized, the following options are displayed:

1.  Look up an existing device
2.  Add a new device
3.  Update existing device
4.  Delete existing device
5.  Quit the program

-----------------------------------------------------------------------------

1. Look up an existing device
The user would use this option to look up a device already recorded. This would be done by entering the device serial number. When the program has located the device, it displays the matching serial number, what the item is, whether or not it has been noted as needing servicing, and where the device is located.


2. Add a new device
The user would use option 2 to add a new device. When the item, serial number, whether or not servicing is needed, & location is complete the program will report “The Entry has been added”.


3. Update existing device
The user would use option 3 to update an existing device already entered. This option is mainly used when a device status changes between needing and not needing to be serviced. In addition, option 3 could be used if one realizes that the wrong device has been recorded to a serial number. When the information is updated, the program will report “Information updated”.


4. Delete existing device
The user would use option 4 to delete an existing device.  When the device has been deleted, the program will report “Entry deleted”.

 	
5. Quit the program
When the user has finished using Technology Inventory, option 5 (Quit the program) is selected.  If the program has saved data and closed out correctly, it will report “Program Quit”.


-----------------------------------------------------------------------------


Requirements:

    • python (3.4+)


Developer Notes
If there are questions or comments, please feel free to email me at jason.bruss001@my.hennepintech.edu

