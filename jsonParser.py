# Python program to convert 
# JSON file to CSV   
  
import json 
import csv 
  

## need to open all files into var - might need loop 
  
# Opening JSON file and loading the data 
# into the variable data 
with open('items-0.json') as json_file: 
    data = json.load(json_file) 
  
item_data = data['Items'] 


  
# now we will open a file for writing 
data_file = open('tblItems.csv', 'w', newline='') 
  
# create the csv writer object 
csv_writer = csv.writer(data_file) 
  
# Counter variable used for writing  
# headers to the CSV file 
count = 0


for items in item_data: 
    if count == 0: 
  
        # Writing headers of CSV file 
        header = items.keys() 
        csv_writer.writerow(header) 
        count += 1
        


    for x in items["Category"]:
        category_file = open('tblCategories.csv', 'w', newline='')
        csv_writer_cat = csv.writer(category_file)
        csv_writer_cat.writerow(x)

    
    if items["Bids"] is not None:
        for x in items["Bids"]:
            bids_file = open('tblBids.csv', 'w', newline='')
            csv_writer_bid = csv.writer(bids_file)
            csv_writer_bid.writerow(x)
            bids = items["Bids"]
    else:
        bids = None

    if items["Seller"] is not None:
        usrs_file = open('tblUsers.csv', 'w', newline='')
        csv_writer_usr = csv.writer(usrs_file)
        csv_writer_usr.writerow(items["Seller"].values())
        user = items["Seller"]["UserID"]
        
    else:
        user = None


    # Writing data of CSV file 
    csv_writer.writerow([items['ItemID'], items['Name'], items['Category'], items['Currently'],
     items['First_Bid'], items['Number_of_Bids'], bids,
    items['Location'], items['Country'], items['Started'], items['Ends'],
    user, items['Description'] ]) 
    
 


data_file.close() 
category_file.close()
bids_file.close()
usrs_file.close()