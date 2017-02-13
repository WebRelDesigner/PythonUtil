import os,time,os.path
import hashlib

def scandir(rootPath,filePath,fsOpen):
	check_ext = ["txt","swf","png","jpg","jpeg","xml","astar","data"]
	os.chdir(filePath)
	
	for obj in os.listdir(os.curdir) :
	    if os.path.isdir(obj) :
	    	scandir(rootPath + obj + '/',obj,fsOpen)
	        os.chdir(os.pardir)
	    else :
	    	ext = obj.split('.')[-1]
	    	if ext in check_ext :
	    		curFilePath = os.path.abspath('') + '\\' + obj
		    	xmlStr = '	<item url=\"%s\" key=\"%s\" type=\"%s\" changeTime=\"%i\"/>\n'
		    	
		    	changeTime = os.path.getmtime(obj)

		    	m = hashlib.md5()
		    	curFile = open(obj,'r')
		    	curFilebytes = curFile.read(1024) 
		        while(curFilebytes != b''):
		            m.update(curFilebytes)
		            curFilebytes = curFile.read(1024)   
		        curFile.close() 
		        md5value = m.hexdigest()

		        print(rootPath + obj)
		    	fsOpen.write(xmlStr %(rootPath + obj,md5value,ext,changeTime))

	

if __name__ == '__main__':
	md5XmlFile = open('./md5.xml','w')
	md5XmlFile.write('<?xml version=\'1.0\' encoding=\'utf-8\'?>\n')
	md5XmlFile.write('<items>\n')

	scandir('','./',md5XmlFile)

	md5XmlFile.write('</items>')
	md5XmlFile.close()