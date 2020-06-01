import os,re

path = r"C:\Users\raghu\Desktop\testing"
res=[]
fres=[]

for rootdir, subdir, files  in os.walk(path, topdown=True):   
	for file in files:
		
		with open(os.path.join(rootdir, file), 'r') as ipf: 
			ipfread = ipf.read()
			pattern = re.compile('(?:[0-9]{1,3}\.){3}[0-9]{1,3}')
			matches = pattern.findall(ipfread)
			for i in matches:
				res.append(i)
				
def validIPAddress(IP):
      def isIPv4(s):
         try: return str(int(s)) == s and 0 <= int(s) <= 255
         except: return False
      if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
	      fres.append(IP)
		 
		 
      
res.sort()
for x in res:
	validIPAddress(x)

	
for y in fres:
    print(y)


