import requests
#import MySQLdb
import mysql.connector
import json

# data pulled from https://data.cdc.gov/Vaccinations/COVID-19-Vaccinations-in-the-United-States-Jurisdi/unsk-b7fc

# connect to vaccine database
mydb = mysql.connector.connect(user = 'api', password = 'csci4830', host = 'ec2-52-14-14-132.us-east-2.compute.amazonaws.com', database = 'vaccineData')


# drops table if it exists
mycursor = mydb.cursor()
sql = "DROP TABLE IF EXISTS total_vaccinations"
mycursor.execute(sql)

# create table
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE total_vaccinations (date VARCHAR(255) NOT NULL, location VARCHAR(255) NOT NULL, distributed INT, distributed_Janssen INT, distributed_Moderna INT, distributed_Pfizer INT, distributed_per_100k INT, distributed_per_100k_12Plus INT, distributed_per_100k_18Plus INT, distributed_per_100k_65Plus INT, administered INT DEFAULT null, administered_12Plus INT, administered_18Plus INT, administered_65Plus INT, administered_Janssen INT, administered_Moderna INT, administered_Pfizer INT, PRIMARY KEY (date, location))")


# HTTP request to CDC website (str object)
requests = requests.get("https://data.cdc.gov/resource/unsk-b7fc.json").text
# record is now a dictionary

# list object
record = json.loads(requests)


# the loop iterates through the json string, matching each attribute key with
# its value

x = 0
while x != len(record):

	date = record[x]['date']
	date = date.split("T")[0]

	location = record[x]['location']
	distributed = record[x]['distributed']
	distributed_janssen = record[x]['distributed_janssen']
	distributed_moderna = record[x]['distributed_moderna']
	distributed_pfizer = record[x]['distributed_pfizer']


	dist_per_100k = record[x]['dist_per_100k']

	if  'distributed_per_100k_12plus' in record[x].keys():
		distributed_per_100k_12plus = record[x]['distributed_per_100k_12plus']
	else:
		distributed_per_100k_12plus = None

	distributed_per_100k_18plus = record[x]['distributed_per_100k_18plus']
	distributed_per_100k_65plus = record[x]['distributed_per_100k_65plus']
	administered = record[x]['administered']


	if 'administered_12plus' in record[x].keys():
		administered_12plus = record[x]['administered_12plus']
	else:
		administered_12plus = None
	administered_18plus = record[x]['administered_18plus']
	administered_65plus = record[x]['administered_65plus']
	administered_moderna = record[x]['administered_moderna']
	administered_janssen = record[x]['administered_janssen']
	administered_pfizer = record[x]['administered_pfizer']

	x = x + 1


	# instert CDC data into database
	sql = "INSERT INTO total_vaccinations VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

	val = (date, location, distributed, distributed_janssen, distributed_moderna, distributed_pfizer, dist_per_100k, distributed_per_100k_12plus, distributed_per_100k_18plus, distributed_per_100k_65plus, administered, administered_12plus, administered_18plus, administered_65plus, administered_moderna, administered_janssen, administered_pfizer)
	mycursor.execute(sql, val)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")






#INSERT INTO total_vaccinations VALUES




