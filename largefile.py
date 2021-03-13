import os
import fnmatch

print("Select option")
print("1.finding by file size")
print("2.finding by file name")
print("Please select : ")
menu_select = int(input())

# folder path input
print("Enter folder path:")
path = os.path.abspath(input())


if menu_select == 1:
	size = 0

	# for storing the size of
	# the largest file
	print("Enter Max file size (GB):")
	max_size = float(input())*1024*1024*1024

	# for storing the path to the
        # largest file
	max_file =""

	for folder, subfolders, files in os.walk(path):
		try:
                        # checking the size of each file
			for file in files:
				size = os.stat(os.path.join( folder, file )).st_size

                                # updating maximum size
				if size>max_size:
                                        #max_size = size
					max_file = os.path.join( folder, file )
					print("The largest file is: "+max_file)
					print('Size: '+str(size/1024/1024/1024)+' GB')
		except :
			print("Can not access!! Skip folder")

if menu_select == 2:
	size = 0

        # for storing the size of
        # the largest file
	print("Enter file name :")
	search_filename = "*"+input()+"*"

        # for storing the path to the
        # largest file
	find_file =""

	for folder, subfolders, files in os.walk(path):
		try:
			for file in files:
				if fnmatch.fnmatch(file, search_filename):
					find_file = os.path.join( folder, file )
					print("The file location is: "+find_file)
		except : 
			pass
