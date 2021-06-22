# flight-deals-python
This is python program which helps in getting great flight deals to the desired destinations without having us to check for flight ticket prices manually.
This program can be run daily on on the cloud (e.g using python anywhere). 

You need to provide 2 google sheets: 
1. 'Users' sheet: It has 3 columns: First Name, Last Name, Email. 
2. 'Prices' sheet: It has 3 columns: City, IATA Code, Lowest Price 

The flight search api is used to check if there are flights available in next 6 months for the cities and below the prices as given in 'Prices' sheet. 
If available email is sent to all the people in the 'Users' sheet.
