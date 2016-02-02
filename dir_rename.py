# Author: catmes
# Created: 2nd February 2016
# Copyright: © 2011 catmes
# License for Use: https://github.com/catmes/Box-o-Code/blob/master/LICENSE
# Source: https://github.com/catmes/Box-o-Code.git

# Description: dir_rename.py is a script that, when placed inside the current working 
# directory, will systematically rename all the files located in the cwd via console.

import os 


list_of_files = os.listdir(os.getcwd())

def name_file(src):
	'''Returns name.'''
	dst = raw_input('What would you like to name file %s ? ' % src)
	return dst
				
for file in list_of_files: # For files in working directory.

	if file == __file__:
		None
		
	elif file == '.DS_Store':
		None
		
	else:
		os.rename(file, name_file(file))
		
	
	
	
	
