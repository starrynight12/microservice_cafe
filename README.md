Requesting data: 
-
The microservice contains the data in 3 json categories of categories, items, and modifiers, like so: 
  
	  categories = [
	    {"id": 1, "name": "Hot Coffee", "description": "Our hot coffee selection."},
	    {"id": 2, "name": "cold Coffee", "description": "Our cold coffee selection."}
	  ]
	 items = [ ...

This can be called by importing the requests module, identifying source url, and calling the items from json; using:

		import requests
		ms_url = "http://127.0.0.1:5000" #replace with hosting url	
		response = requests.get(ms_url + "/categories") 	#replace categories with relevant choice
		
Recieving data:
 - 
 Data is stored in the relevant choice (categories in the above example). That stored data can either be printed, or otherwise collected and displayed, like so: 
 
	categories = response.json()	#replace categories with relevant choice	
	print("Categories:", categories)		#prints out requested data, can be just collected as well

UML sequence diagram:
- 


