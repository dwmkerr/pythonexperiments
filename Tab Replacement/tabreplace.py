# Tab Replacement
#
# This script can be used to replace tabs in files with spaces.
# 
# Usage:
# tabreplacement [folder]

# Core imports
import sys, getopt, os

def main(argv):

	# Create the default settings.
	recurse = False
	directories = None

	# Get the arguments.
	try:
		options, arguments = getopt.getopt(argv, "hr")
	except getopt.GetoptError:
		show_help(True)

	# Go through the options.
	for opt, arg in options:
		if opt == '-h':
			show_help(True)
		elif opt == '-r':
			recurse = False
		
	# The directory list is now the arguments.
	directories = arguments
	if(len(directories) == 0):
		show_help(True)

	# Handle each directory.
	for directory in directories:
		process_directory(directory, recurse)

def process_directory(directory, recurse):

	# Write some info to the user.
	print("Checking " + directory)

	# Get the files and directories in the given directory.
	for root, dirs, files in os.walk(directory):

		# Process each file.
		for file in files:
			process_file(file)

		# Process directories if we're recursing.
		if recurse:
			for dir in dirs:
				process_directory(dir, recurse)

def process_file(file):

	# The count of tabs.
	tabCount = 0

	# If we don't have write access to the file then skip it.
	if(os.access(file, os.W_OK) == False): 
		print(file + ": No write access.")
		return

	# TODO: We could improve on the above. If we can read the file,
	# we can check to see if it has tabs. If it doesn't we don't care
	# and don't need to warn.

	# Open a temporary file to write to.
	tempFile = file + "~"
	with open(tempFile, "w") as outputfile:

		# Open the file, go though each line.
		with open(file, "r") as inputfile:
			
			# Go through each line.
			for line in inputfile:

				# Count tabs.
				tabCount += line.count("\t")

				# Replace tabs.
				newLine = line.replace("\t", "    ")

				# Write the newline to the new file.
				outputfile.write(newLine)

			# Output info on the file.
			print(file + ": Replaced " + str(tabCount) + " tabs")

	# Now delete the existing file and replace it with the new one.
	#os.remote(file)
	#os.rename(temoFile, file)

def show_help(exitAfter):

	# Print the help text.
	print("tabplace - Replace tabs with four spaces")
	print("Usage: tabreplace -r <directory> <directory> <directory>")
	print(" -r: Recurse in <directory>")
	print(" <directory>: The directory to search for files")

	# If we've been told to exit, do so.
	if(exitAfter):
		sys.exit()

if __name__ == "__main__":
	main(sys.argv[1:])