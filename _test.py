import os
import pytest
import pathlib
import platform
from typing import *

from requirements_checker import *


# =====================================================================================================================
class Test_Base:
    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (ReqCheckStr_Base,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__exx_no_getter(self):
        try:
            victim = self.VICTIM()
        except Exx_RequirementCantGetActualValue:
            assert True
        else:
            assert False

    def test__no_reqs(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM._RAISE = False
        victim = self.VICTIM()

        assert victim.check() is False
        assert victim._VALUE_ACTUAL == "hello"

    def test__req_met_true(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM.hello = True
        victim = self.VICTIM()

        assert victim.check() is True

    def test__req_met_true__several_variants(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM.hello1 = False
        self.VICTIM.hello = True
        self.VICTIM.hello2 = False
        victim = self.VICTIM()

        assert victim.check() is True

    def test__req_met_false(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM.hello = False
        try:
            victim = self.VICTIM()
        except Exx_Requirement:
            assert True
        else:
            assert False

    def test__set_raise(self):
        # _RAISE = True
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM._RAISE = True
        self.VICTIM.hello = False
        try:
            victim = self.VICTIM()
        except Exx_Requirement:
            assert True
        else:
            assert False

        # _RAISE = False
        self.VICTIM._RAISE = False
        victim = self.VICTIM()
        assert victim.check() is False

    def test__set_part(self):
        self.VICTIM._RAISE = False
        self.VICTIM._GETTER = lambda: "Hello"

        # _CHECK_FULLMATCH = True
        self.VICTIM._CHECK_FULLMATCH = True
        self.VICTIM.hell = True

        victim = self.VICTIM()
        # victim.hello
        assert victim.check() is False

        # _CHECK_FULLMATCH = False
        self.VICTIM._CHECK_FULLMATCH = False
        assert victim.check() is True

    def test__case_insencitive(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM.HELLO = True
        victim = self.VICTIM()

        assert victim.check() is True


# =====================================================================================================================
