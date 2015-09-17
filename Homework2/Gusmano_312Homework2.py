import csv
import datetime
import time
import collections
from collections import Counter
#####################Data Import Process#############################

def import_graffiti_data(file_name):
  f = open(file_name)
  csv_f = csv.reader(f)
  headers = csv_f.next()
  before_date = datetime.datetime(2015,1,1) #before_date is of type date

  graf_address_list = []
  for row in csv_f:
    address_row = []
    row_date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
    if (row_date > before_date):
      address_row.append(row[0])  ###Date
      address_row.append(row[1])  ###Status
      address_row.append(row[2])  ###Completion Date
      address_row.append(row[7])  ###Street Adress
      address_row.append(row[8])  ### Zip Code
      address_row.append(row[17]) ### Location Coordinates
      graf_address_list.append(address_row)

  print ('Graffiti Removal Requests Data Loaded')
  return graf_address_list

def import_graffiti_cleanup_perf(file_name):
  p = open(file_name)
  csv_p = csv.reader(p)
  headers = csv_p.next()

  performance_metrics_list = []
  for row in csv_p:
    perf_row = []
    perf_date = datetime.datetime.strptime(row[0], '%m/%d/%Y')
    perf_row.append(row[0]) ### Date: 'Week of'
    perf_row.append(row[1]) ### Average Days to Complete Graffiti Removal
    perf_row.append(row[2]) ### Total Completed Requests
    perf_row.append(row[3]) ### Median Days to Complete Graffiti Removal Request
    perf_row.append(row[4]) ### Target Response Time (Days)
    performance_metrics_list.append(perf_row)
    
  print ('Clean up Performace Data Loaded')
  return performance_metrics_list
  
#############End of Data Import Process################################
def main():
  graffiti_file_name = '311_Service_Requests_-_Graffiti_Removal.csv'
  performance_metrics_file_name = 'Performance_Metrics_-_Streets___Sanitation_-_Graffiti_Removal.csv'


  graf_address_list = import_graffiti_data(graffiti_file_name)
  performance_metrics_list = import_graffiti_cleanup_perf(performance_metrics_file_name)

  print
  print ("The total number of Removal Requests in 2015: ")
  print len(graf_address_list) ### Prints Total number of rows in 2015
  print 
  print ("The average # of Graffiti Removal Requests per Zipcode is: ") 
  print len(graf_address_list)/85
  ### 85 is the total number of chicago Zip codes
  ### For the year of 2015
  print
  
  data = Counter(graf_address_list)
  data.most_common()   # Returns all unique items and their counts
  data.most_common(1)  # Returns the highest occurring item
  
main()



###My goals are to find: ###
###1. If there are different est. times of removal depending if the area is residential or commercial.###
###2. The average "life time" of a graffiti painting (street art).###
###3. If there is a relationship between neighborhoods and requests for graffiti removal.###
###4. Property value vs. graffiti removal requests.####

