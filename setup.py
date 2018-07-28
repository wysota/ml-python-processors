from setuptools import setup

setup(name='mlpythonprocessors',
      version='0.1',
      description='MountainLab python processors',
      url='https://github.com/wysota/ml-python-processors',
      author='Witold Wysota',
      packages=setuptools.find_packages(),
      package_data={ 
        '': ['*.mp']
      },
      zip_safe=False)

