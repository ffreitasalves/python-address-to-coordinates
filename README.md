python-address-to-coordinates
=============================

Python script to convert addresses to coordinates using google maps


Simple Usage
=============

    from script import coordinates
    test = coordinates('first avenue, new york, usa')
    >>> print test['lat']
    40.763368
    >>> print test['lng']
    -73.95924

Coordinates for each row in an excel file
=========================================

    #The third argument of this function is the column that contains the address.
    #It wil read the input.xlsx file, read the 'Plan1' sheet, looking for coordinates to addresses('0' column)
    #And create another file 'output.xlsx' with two more columns lat and lng for each row.    
    from script import xlsx_coordinates
    xlsx_coordinates('input.xlsx','Plan1',0,'output.xlsx')

Create a kml file from a xlsx
==============================

    from script import create_kml
    create_kml('input.xlsx','sheet_name','output.kml')
