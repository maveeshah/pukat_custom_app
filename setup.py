from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pukat_custom_app/__init__.py
from pukat_custom_app import __version__ as version

setup(
	name="pukat_custom_app",
	version=version,
	description="Customizations in ERPNext/Frappe done by Ameer Muavia",
	author="Ameer Muavia Shah",
	author_email="mavee.shah@hotmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
