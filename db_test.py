import os
import mysql.connector
import matplotlib.pyplot as plt

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
	raise SystemError



if input('start ingesting new data? (y/n): ') == 'y':

	mycursor = db.cursor()
	database = 'EDGAR'


	datapath = '/home/hjk/Downloads/DataSets/Edgar'
	tablename = 'Numbers'
	for folder in os.listdir(datapath): #not necessarily going in alphabetical order
		os.chdir(datapath+'/'+folder)

		with open('num.txt', 'r') as file:
			for line in file:
				if line.startswith('adsh'):
					keys = line.replace('\n','').split('\t')
					keys = ['company_name' if i=='name' else i for i in keys]  #protected variable names in SQL
					keys = ['changed_date' if i=='changed' else i for i in keys]
					keys = ['instance_address' if i=='instance' else i for i in keys]
					table_input = ''
					keys_input = ''
					for i in keys:
						if i == 'tag': #UNTESTED
							abc = i+' VARCHAR(200), '
						keys_input += i+','
						abc = i+' VARCHAR(100), '
						table_input += abc

					try:
						#print('CREATE TABLE {} (idnum int PRIMARY KEY AUTO_INCREMENT, {} date_modifies VARCHAR(50) )'.format(tablename, table_input) )
						mycursor.execute('CREATE TABLE {}.{} (idnum int PRIMARY KEY AUTO_INCREMENT, {} date_modified VARCHAR(50) )'.format(database, tablename, table_input) )
					except:
						pass
				else:
					row = line.replace('\n','').replace('\'','*').replace('\\','*').split('\t') #removing characters that throw SQL syntax errors
					val_input = ''
					for i in row:
						if i == '':
							i = 'NA'
						elif len(i) > 99:
							i = 'ENTRY TOO LONG'
						val_input += '\''+i+'\''+', '  #SQL syntax requires ' ' around the values
					date_string = '\''+str(datetime.now())+'\''

					try:
						mycursor.execute('INSERT INTO {}.{} ({} date_modified) VALUES ({}{});'.format(database, tablename, keys_input, val_input, date_string))
						db.commit()

					except:
						print('FUCKING SQL SYNTAX ERRORS... \n')
						print(folder + ':   ' + val_input)
						raise ValueError

	print('\n\n<<< Data Ingestion COMPLETE >>>\n\n')

if input('Select from database? (y/n): ') == 'y':
	mycursor = db.cursor()
	database = 'EDGAR'

	COMPANY_SEARCH_TERM = 'FACEBOOK'
	#COMPANY_SEARCH_TERM = 'TESLA'
	SQL_COMMAND = "SELECT adsh,company_name,form,filed FROM EDGAR.Submissions WHERE company_name regexp '^{}*';".format(COMPANY_SEARCH_TERM)
	mycursor.execute(SQL_COMMAND)
	records = mycursor.fetchall()

	assets, assets_current, other_assets_noncurrent = [], [], []
	for r in records:

		print(r)
		SQL_COMMAND2 = "SELECT adsh, tag, ddate, qtrs, cValue, date_modified FROM EDGAR.Numbers WHERE adsh='{}';".format(r[0])
		mycursor.execute(SQL_COMMAND2)
		records2 = mycursor.fetchall()
		print('First Level Finished...')


		for r2 in records2:
			print('Entering Second Level...')

			if r2[1] == 'Assets':
				assets.append((r2[2], r2[4]))
			elif r2[1] == 'AssetsCurrent':
				assets_current.append((r2[2], r2[4]))
			elif r2[1] == 'OtherAssetsNoncurrent':
				other_assets_noncurrent.append((r2[2], r2[4]))
			print(r2)


print('Assets : ',assets)
print('AssetsCurrent : ',assets_current)
print('Other :',other_assets_noncurrent)

for i in assets:
	plt.plot( int(i[0]), float(i[1]), 'or')

plt.xlabel('Year')
plt.xticks(rotation=-45)
plt.ylabel('\$\$ USD \$\$')
plt.title(COMPANY_SEARCH_TERM + ' Assets')
plt.show()