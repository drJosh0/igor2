import os
import mysql.connector
from datetime import datetime

try:
	db = mysql.connector.connect(
host='localhost',
user='root',
passwd='iNoMJZyCZCSF8d',
database='EDGAR'
)
	print("\n\n******* Connected. ******* \n\n")
except:
	print("Cannot connect to database")

datapath = '~/Downloads/DataSets'
mycursor = db.cursor()
database = 'EDGAR'
tablename = 'EdgarData1'


'''
try:
	mycursor.execute('CREATE TABLE {} (idnum int PRIMARY KEY AUTO_INCREMENT, adsh VARCHAR(50), name VARCHAR(100), filed VARCHAR(10), form VARCHAR(10), date_modified VARCHAR(50))'.format(tablename))
except:
	pass
'''


with open('sub.tsv', 'r') as file:
	for line in file:
		if line.startswith('adsh'):
			keys = line.replace('\n','').split('\t')
			keys = ['company_name' if i=='name' else i for i in keys]
			keys = ['changed_date' if i=='changed' else i for i in keys]
			keys = ['instance_address' if i=='instance' else i for i in keys]
			table_input = ''
			keys_input = ''
			for i in keys:
				keys_input += i+','
				abc = i+' VARCHAR(100), '
				table_input += abc
			
			try:
				#print('CREATE TABLE {} (idnum int PRIMARY KEY AUTO_INCREMENT, {} date_modifies VARCHAR(50) )'.format(tablename, table_input) )				
				mycursor.execute('CREATE TABLE {}.{} (idnum int PRIMARY KEY AUTO_INCREMENT, {} date_modified VARCHAR(50) )'.format(database, tablename, table_input) )
			except:
				pass
		else:
			row = line.replace('\n','').replace('\'','').split('\t')
			val_input = ''
			for i in row:
				if i == '':
					i = 'NA'
				val_input += '\''+i+'\''+', '
			date_string = '\''+str(datetime.now())+'\''
			print('\n\n')
			print('INSERT INTO {}.{} ({} date_modified) VALUES ({}{});'.format(database, tablename, keys_input, val_input, date_string ) )
			print('\n\n')			
			
			mycursor.execute('INSERT INTO {}.{} ({} date_modified) VALUES ({}{});'.format(database, tablename, keys_input, val_input, date_string))
			db.commit()


			#mycursor.execute('INSERT INTO {} (name) VALUES (The Josh Company)'.format(tablename) )
			#db.commit()
			#mycursor.execute('INSERT INTO {} (adsh, name, filed, form, date_modified) VALUES {}'.format(tablename, (adsh, name, filed, form, str(datetime.now()) ) ))
			#db.commit()



