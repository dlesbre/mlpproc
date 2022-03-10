"""
setup file. run 'python3 setup.py install' to install.
"""
from setuptools import setup  # type: ignore

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setup(
	name = "preproc",
	version = "1.0.0",
	author = "Dorian Lesbre",
	url = "https://github.com/Lesbre/preprocessor/",
	description = "Preprocessor for text files (code/html/tex/...) inspired by the C preprocessor",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	packages = ["preproc"],
	scripts = ["pproc"],
	install_requires = [],
	extras_require = {
		"dev": ["pytest", "mypy", "pre-commit"],
	},
	python_requires = ">=3.6",
	license = "MIT",
	platforms=["any"],
	keywords=['preprocessor preprocess markup language python terminal'],
	classifiers = [
		# How mature is this project? Common values are
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 5 - Production/Stable',

		# Indicate who your project is intended for
		'Intended Audience :: Developers',
		'Environment :: Console',
		'Natural Language :: English',

		# Pick your license as you wish (should match "license" above)
		"License :: OSI Approved :: MIT License",

		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",

		"Operating System :: OS Independent",
		"Topic :: Utilities",
	],
	data_files=[('', ['LICENSE'])],
)
