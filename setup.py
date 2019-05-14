import setuptools

from distutils.core import setup

setup(
  name = 'ecco_v4_py',
  packages = ['ecco_v4_py'], # this must be the same as the name above
  version = '1.0.7',
  description = 'Estimating the Circulation and Climate of the Ocean (ECCO) Version 4 Python Package',
  author = 'Ian Fenty',
  author_email = 'ian.fenty@jpl.nasa.gov',
  url = 'https://github.com/ECCO-GROUP/ECCOv4-py',
  keywords = ['ecco','climate','mitgcm','estimate','circulation','climate'],
  install_requires=[
	'cython',
	'shapely',
	'proj',
	'six',
	'dask[complete]',
	'datetime',
	'python-dateutil',
	'matplotlib',
	'numpy',
	'pyresample',
	'xarray',
	'xmitgcm',
	'pyyaml',
	'pyproj',
	'pykdtree',
	'cartopy'],
  classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research', 
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2.7',
      'Topic :: Scientific/Engineering :: Physics'
  ]
)
