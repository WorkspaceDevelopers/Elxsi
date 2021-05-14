# Elxsi - Python Package
Elxsi is a python package for performing advanced mathematical operations, distributions and visualizations and is licensed under the GNU General Public License v3.0. It includes modules for calculating mean, standard deviation and probability distribution function of various statistical distributions. The latest released stable version of elxsi is 1.0.3.

The project was started in 2021 by [Ashwin Raj](https://www.github.com/ashwinraj-in) as an academic project. The resources for the package and the pull requests are maintained and reviewed by a team of volunteers. Learn more about elxsi [here](https://pypi.org/project/elxsi/)

# Subdirectories and Constraints
### Dependencies
- Python (>= 3.9.0)
- NumPy (>=1.20.3)

### Files and Folders
The files and folders used in the package are as follows:
- [dist](https://github.com/WorkspaceDevelopers/elxsi/tree/main/dist): This subdirectory contains the source distribution for the package that needs to be uploaded to Pypi.
- [elxsi.egg-info](https://github.com/WorkspaceDevelopers/elxsi/tree/main/elxsi.egg-info): This subdirectory contains the package's metadata including PKG-INGFO and the sources.
- [elxsi](https://github.com/WorkspaceDevelopers/elxsi/tree/main/elxsi): This folder contains the source code for performing operations and visualizing statistical distributions.

**Note:**
Elxsi runs on all operating systems, is quick to install and is available for free use. No version of elxsi support Python 2.7 and Python 3.4. Elxsi plotting capabiliies requires matplotlib (>= 2.1.1) and seaborn (>= 0.9.0) packages.

# User Installation and Source Code
The latest stable release of elxsi can be installed from Pypi, using the code:
```
pip install elxsi
```
Once the package is succesfully installed, various statistical distribution instances can be imported by specifying their name with the first letter of each word in UpperCase.

### Package Development
Elxsi development takes place on [GitHub](https://github.com/WorkspaceDevelopers/elxsi). Please submit bugs that you encounter to the issue tracker with a reproducible example demonstrating the problem, as per the issue template in /.github

# Contribution
New contributors of all experience levels are welcomed to contribute to this project. Some basic information about the project has been included in this README. For major changes, it is recommended that you open an issue first to discuss what you would like to change.

### Clone the repository
To contribute to this project you have to first clone the repository and then send a pull request with proposed changes.
```
git clone https://github.com/ashwinraj-in/Workspace/tree/main/PandoraNLPWebApp
```
### Installing Required Libraries
The web application requires some requirements that are present in the requirements.txt file. These can be installed by running:
```
sudo pip3 install -r requirements.txt
```
### Testing the Package
After installation, you can launch the test suite from outside the source directory (requires pytest >= 3.3.0)
```
pytest elxsi
```
View statistics for elxsi via [Libraries.io](https://libraries.io/pypi/elxsi), or by using the [public dataset on Google BigQuery](https://packaging.python.org/guides/analyzing-pypi-package-downloads/).

### Submitting a Pull Request
Before opening a Pull Request, have a look at the full Contributing page to make sure your code complies with our guidelines.

# License and Project Status
The package and other resources are distributed under GNU General Public License v3.0. The latest stable version of elxsi is 1.0.3 and is available to be installed for general use through pip install from [Pypi](https://pypi.org/project/elxsi/) (and other indexes) using requirement specifiers.
