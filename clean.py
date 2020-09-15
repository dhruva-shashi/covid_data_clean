f = open('covid.csv', 'r')
a = f.read().split('\n')
f.close()

f = open('another.csv', 'w')
n = len(a)

id = 'P000000'

f.write('ID,Age,Gender,Patient_type,ICU,Ventilator,Death,Asthma,COPD,Heart,Diabetes,Hypertension,Kidney,Obesity,Other_Disease,Pregnant,Smoker\n')

print('Writing...')

for i in range(1, n):
	s = a[i].split(',')

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

	f.write(id)
	f.write(',')

	f.write(s[8])
	f.write(',')

	if s[1] == '1':
		f.write('1,')
	else:
		f.write('-1,')

	if s[2] == '2':
		f.write('1,')
	else:
		f.write('0,')

	if s[22] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[6] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[5] == '9999-99-99':
		f.write('0,')
	else:
		f.write('1,')

	if s[12] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[11] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[16] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[10] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[14] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[18] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[17] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[15] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[9] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[19] == '1':
		f.write('1,')
	else:
		f.write('0,')

	if s[2] == '2' or s[22] == '1' or s[6] == '1' or s[5] != '9999-99-99' or s[9] == '1':
		f.write('1\n')
	else:
		f.write('0\n')

f.close()
print('\nSuccessfully Written\n')
