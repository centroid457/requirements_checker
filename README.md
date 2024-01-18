# requirements_checker (v0.1.1)

## DESCRIPTION_SHORT
Check if requirements met

## DESCRIPTION_LONG
designed for check requirements (systemos) and raise/bool if no match


## Features
1. check requirements (systemOs), raise/bool if no match  
2. create fuck(?)/getter and is it for check for settings  
3. ...see tests for this!  


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
See tests and sourcecode for other examples.

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
