![Ver/TestedPython](https://img.shields.io/pypi/pyversions/requirements_checker)
![Ver/Os](https://img.shields.io/badge/os_development-Windows-blue)  
![repo/Created](https://img.shields.io/github/created-at/centroid457/requirements_checker)
![Commit/Last](https://img.shields.io/github/last-commit/centroid457/requirements_checker)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/requirements_checker/actions/workflows/test_linux.yml/badge.svg)
![Tests/GitHubWorkflowStatus](https://github.com/centroid457/requirements_checker/actions/workflows/test_windows.yml/badge.svg)  
![repo/Size](https://img.shields.io/github/repo-size/centroid457/requirements_checker)
![Commit/Count/t](https://img.shields.io/github/commit-activity/t/centroid457/requirements_checker)
![Commit/Count/y](https://img.shields.io/github/commit-activity/y/centroid457/requirements_checker)
![Commit/Count/m](https://img.shields.io/github/commit-activity/m/centroid457/requirements_checker)

# requirements_checker (current v0.2.10/![Ver/Pypi Latest](https://img.shields.io/pypi/v/requirements_checker?label=pypi%20latest))

## DESCRIPTION_SHORT
check if requirements met

## DESCRIPTION_LONG
designed for check requirements (systemOs) and raise/bool if no match


## Features
1. check requirements (systemOs), raise/bool if no match  
2. create fuck(?)/getter and is it for check for settings  
3. [python PACKAGES/MODULES]:  
	- upgrade  
	- delete  
	- version_get  
	- check_installed)  
	- upgrade pip  
4. [VERSION]:  
	- parse  
	- check  
	- compare  


********************************************************************************
## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history
See the [HISTORY.md](HISTORY.md) file for release history.


## Installation
```commandline
pip install requirements-checker
```


## Import
```python
from requirements_checker import *
```


********************************************************************************
## USAGE EXAMPLES
See tests, sourcecode and docstrings for other examples.  

------------------------------
### 1. example1.py
```python
from requirements_checker import *


ReqCheckStr_Os().bool_if__WINDOWS()
ReqCheckStr_Os().bool_if_not__WINDOWS()
ReqCheckStr_Os().raise_if__LINUX()


class ReqCheckStr_Os_MY(ReqCheckStr_Os):
    LINUX: bool = True
    WINDOWS: bool = False


ReqCheckStr_Os_MY()  # check requirement!
```

********************************************************************************
