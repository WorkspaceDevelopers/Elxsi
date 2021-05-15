from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='elxsi',
      version='1.0.3',
      description='Python package for advanced mathematical operations, distributions and visualizations',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url="https://github.com/WorkspaceDevelopers/elxsi",
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
      packages=['elxsi'],
      author= 'Ashwin Raj',
      license='GNU General Public License v3.0',
      author_email= 'rajashwin733@gmail.com',
      zip_safe=False)
