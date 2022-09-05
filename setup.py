from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in antoryum_gayrimenkul/__init__.py
from antoryum_gayrimenkul import __version__ as version

setup(
	name="antoryum_gayrimenkul",
	version=version,
	description="Antoryum Website & Uygulama",
	author="Harpiya Software Technologies",
	author_email="info@harpiya.cloud",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
