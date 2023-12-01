import os
import pytest
import pathlib
import platform
from typing import *

from requirements_checker import *


# =====================================================================================================================
class Test_Base:
    def test__exx_value(self):
        class Victim(ReqCheckStr_Base):
            _GETTER = lambda: "Hello"
            _RAISE = True
            _CHECK_FULLMATCH = True

        victim = Victim()

        assert victim.check() is True
        assert victim.VALUE_ACTUAL == "hello"

        # victim.


# =====================================================================================================================
