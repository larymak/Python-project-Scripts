import os
import chimera
import Midas
from chimera import exports
from chimera import runCommand as rc # use 'rc' as shorthand for runCommand
# change to folder with data files
os.chdir("")

# gather the names of .pdb files in the folder
file_names = [fn for fn in os.listdir(".") if fn.endswith(".pdb")]

# loop through the files, opening, processing, and closing each in turn
for fn in file_names:
	rc("open " + fn)
	rc("window")
	rc("ac wb")
	rc("roll")
	rc("freeze")
	rc("ac c2")
	rc("wait 5")
	htmlname = fn[:-3] +'.html'
	exports.doExportCommand("WebGL",htmlname)
	rc("close all")
	
	# save image to a file that ends in .png rather than .pdb
	