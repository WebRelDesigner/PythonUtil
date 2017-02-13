import os,os.path
import zipfile
import chardet

def convert( filename, in_enc = 'GBK', out_enc='UTF8' ) :
	fileOpen = open(filename,'r')
	content = fileOpen.read()
	fileOpen.close()
	det = chardet.detect(content)
	print 'convert ' + filename + ' ' + det['encoding']
	if det['encoding'] != 'utf-8' :
		fileOpen = open(filename,'w')
		outPut = content.decode(in_enc).encode(out_enc)
		fileOpen.write(outPut)
		fileOpen.close()
	print 'done'

def main():
	os.chdir('./')
	z = zipfile.ZipFile('data.zip', 'w', zipfile.ZIP_DEFLATED)
	for path in os.listdir('./'):
		if os.path.isfile(os.path.join('./',path)):
			ext = path.split('.')[-1]
			if ext == 'csv' :
				convert(path)
				z_path = os.path.join('./',path)
				z.write(z_path)
				print z_path
	# for dirpath,dirs,files in os.listdir('./') :
	# 	for path in files :
	# 		ext = path.split('.')[-1]
	# 		if ext == 'csv' :
	# 			convert(path)
	# 			z_path = os.path.join(dirpath,path)
	# 			z.write(z_path)
	# 			print z_path
	z.close()

if __name__ == '__main__':
	main()
	raw_input('Press Enter to exit...')