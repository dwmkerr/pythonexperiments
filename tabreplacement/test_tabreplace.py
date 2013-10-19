# Tab Replacement Tests

import unittest
from tabreplacement.parameters import Parameters

class ParametersTestCase(unittest.TestCase):

	def test_default_parameters_set_correctly(self):

		# Create default parameters.
		parameters = Parameters()

		# Check the default values.
		self.assertFalse(parameters.help,
			"Default value for 'help' is wrong.")
		self.assertFalse(parameters.recurse,
			"Default value for 'recurse' is wrong.")
		self.assertFalse(parameters.preview,
			"Default value for 'preview' is wrong.")
		self.assertEqual(parameters.fileType, None,
			"Default value for 'fileType' is wrong.")
		self.assertEqual(parameters.directories, [],
			"Default value for 'directories' is wrong.")

	def test_loads_recurse_flag_correctly(self):

		# Create the input.
		argv = ["-r"]

		# Parse the parameters.
		parameters = Parameters()
		parameters.parse(argv)

		# Check the value.
		self.assertTrue(parameters.recurse, 
			"Parameter 'recurse' is not set correctly.")

	def test_loads_preview_flag_correctly(self):

		# Create the input.
		argv = ["-p"]

		# Parse the parameters.
		parameters = Parameters()
		parameters.parse(argv)

		# Check the value.
		self.assertTrue(parameters.preview, 
			"Parameter 'preview' is not set correctly.")

	def test_loads_help_flag_correctly(self):

		# Create the input.
		argv = ["-h"]

		# Parse the parameters.
		parameters = Parameters()
		parameters.parse(argv)

		# Check the value.
		self.assertTrue(parameters.help, 
			"Parameter 'help' is not set correctly.")

	def test_loads_filetype_argument_correctly(self):

		# Create the input.
		argv = ["-t", "py"]

		# Parse the parameters.
		parameters = Parameters()
		parameters.parse(argv)

		# Check the value.
		self.assertEqual(parameters.fileType, "py", 
			"Parameter 'preview' is not set correctly.")

	def test_loads_directories_correctly(self):

		# Create the input.
		argv = ["dir1", "dir2", "dir3"]

		# Parse the parameters.
		parameters = Parameters()
		parameters.parse(argv)

		# Check the value.
		self.assertEquals(["dir1", "dir2", "dir3"], parameters.directories, 
			"Directories are not set correctly.")