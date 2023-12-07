# requirements_checker
Designed to raise if no requirements met

## Features
1. check requirements (system), raise if no match 

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


## GUIDE

### USAGE

```python
from requirements_checker import *


class ReqCheckStr_Os_MY(ReqCheckStr_Os):
    LINUX: bool = True
    WINDOWS: bool = False


ReqCheckStr_Os_MY()  # check requirement!  
```
