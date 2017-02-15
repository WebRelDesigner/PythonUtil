import os,os.path

def genCsvClass(filename):
	fileOpen = open(filename,'r')
	line = fileOpen.readline()
	line = fileOpen.readline().rstrip('\n')
	propArr = line.split(',')
	line = fileOpen.readline().rstrip('\n')
	typeArr = line.split(',')
	csvName = filename.split('.')[0]
	fileOpen.close()

	isExists = os.path.exists('./csv')
	if not isExists:
		os.makedirs('./csv')
	os.chdir('./csv')
	cfName = ''
	for index in range(len(csvName.split('_'))):
		cfName += (csvName.split('_')[index][0:1].upper() + csvName.split('_')[index][1:])
	cfName += 'Cell'
	fileOpen = open(cfName+'.ts', 'w')
	fileOpen.write('class '+cfName+' {' + '\n')
	for index in range(len(propArr)):
		propType = typeArr[index]
		if propType == 'float'or propType == 'int':
			propType = 'number'
		fileOpen.write('\tpublic '+propArr[index]+': ' + propType + ';\n')
	fileOpen.write('}')
	fileOpen.close()
	os.chdir('../')

def main():
	os.chdir('./')
	for path in os.listdir('./'):
		if os.path.isfile(os.path.join('./',path)):
			ext = path.split('.')[-1]
			if ext == 'csv' :
				genCsvClass(path)

if __name__ == '__main__':
	main()
	raw_input('Press Enter to exit...')
