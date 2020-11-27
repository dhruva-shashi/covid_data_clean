# Open the file "covid.csv", to read the data related to covid patients
f = open('covid.csv', 'r')
a = f.read().split('\n')
f.close()

# Open the file "another.csv", to write the data related to covid patients
f = open('another.csv', 'w')
n = len(a)

# Assign 'P000000', to id
id = 'P000000'

# Write the field names onto the file
f.write('ID,Age,Gender,Patient_type,ICU,Ventilator,Death,Asthma,COPD,Heart,Diabetes,Hypertension,Kidney,Obesity,Other_Disease,Pregnant,Smoker,Decision\n')

print('Writing...')

# Write the each patients details line by line onto the file
for i in range(1, n-1):
	s = a[i].split(',')

	# The ID is incremented by 1 for each patient
	temp = ''
	flag = True
	for j in range(6, -1, -1):
		if flag and id[j] != '9':
			temp += chr(ord(id[j])+1)
			flag = False
		elif flag:
			temp += '0'
		else:
			temp += id[j]

	id = ''

	for j in range(6, -1, -1):
		id += temp[j]

	# Write the ID to the file to uniquely identify each patient
	f.write(id)
	f.write(',')

	# Write the age of the patient onto the file
	f.write(s[8])
	f.write(',')

	# Write the gender of the patient onto the file
	if s[1] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write the patient_type onto the file
	if s[2] == '2':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient was admitted to ICU or not
	if s[22] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient was on ventilator or not
	if s[6] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient died or not
	if s[5] == '9999-99-99':
		f.write('0,')
	else:
		f.write('1,')

	# Write whether the patient had asthma or not
	if s[12] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had COPD or not
	if s[11] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had cardiovascular diseases or not
	if s[16] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient has diabetes or not
	if s[10] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had hypertension or not
	if s[14] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had kidney disorders or not
	if s[18] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had obesity or not
	if s[17] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient had other_diseases or not
	if s[15] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient was pregnant or not
	if s[9] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write whether the patient was a consumer of tobacco or not
	if s[19] == '1':
		f.write('1,')
	else:
		f.write('0,')

	# Write the result, as to whether the patient requiered a bed or not if any of the following conditions pass
	# If the patient type was inpatient
	# If the patient type was admitted to ICU
	# If the patient was on ventilator support
	# If the patient died
	# If the patient is pregnant
	if s[2] == '2' or s[22] == '1' or s[6] == '1' or s[5] != '9999-99-99' or s[9] == '1':
		f.write('1\n')
	else:
		f.write('0\n')

f.close()
print('\nSuccessfully Written\n')
