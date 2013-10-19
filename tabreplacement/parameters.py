# Parameters
# 
# The Paramters module contains the Parameters class, which is used
# to parse input parameters to the program.

import getopt

class Parameters:

    # If true, we should show help.
    help = False

    # If true, we should recurse.
    recurse = False

    # If true, we should preview only.
    preview = False

    # If not None, only files with this extension are processed.
    fileType = None

    # The directories to process.
    directories = []

    def parse(self, argv):

        # If we have no input we have a problem.
        if(argv is None):
            raise ValueError("The input must have a value.")

        # Get the arguments.
        try:
            options, arguments = getopt.getopt(argv, "hrpt:")
        except getopt.GetoptError:
            raise ValueError("The input value is incorrectly formatted.")

        # Go through the options.
        for opt, arg in options:
            if opt == "-h":
                self.help = True
            elif opt == "-r":
                self.recurse = True
            elif opt == "-p":
                self.preview = True
            elif opt == "-t":
                self.fileType = arg
        
        # The directory list is now the arguments.
        self.directories = arguments

