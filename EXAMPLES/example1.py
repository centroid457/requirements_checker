from requirements_checker import *


ReqCheckStr_Os().bool_if__WINDOWS()
ReqCheckStr_Os().bool_if_not__WINDOWS()
ReqCheckStr_Os().raise_if__LINUX()


class ReqCheckStr_Os_MY(ReqCheckStr_Os):
    LINUX: bool = True
    WINDOWS: bool = False


ReqCheckStr_Os_MY()  # check requirement!
