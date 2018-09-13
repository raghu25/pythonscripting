'''
this script generates 4 text files for when the text file "inp.txt" is given as an input. Each files content is divided at the delimiter '******' of the original file 'inp.txt'.
'''
# opening the file
with open('inp.txt') as fo:
# reading the file
	fs=fo.read().split("\n") # output is list with number of rows as elements and every element in the list is data in a specific row
	op=''
	start=0
	counter=1 # to name the files generated seperately
	for x in fs:
		if (x=='******'):
			if start == 1:
				with open(str(counter)+'.txt','w') as opf:
					opf.write(op)
					opf.close()
					op='' # clear the op to make it ready for next section
					counter+=1
			else:
				start=1
		else:
			if op=='' : # handling the very first line to avoid blank space at the start of each generated file.
				op = x
			else:
				op=op+'\n'+x
	fo.close()
