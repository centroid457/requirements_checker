from requirements_checker import *


class ReqCheckStr_Base(ReqCheckStr_Base):
    _GETTER = lambda: "hello"
    _MEET_TRUE = False

victim = ReqCheckStr_Base()
# victim.check_()
victim.check_no_HELLO()
