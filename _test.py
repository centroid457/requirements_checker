import os
import pytest
import pathlib
import platform
from typing import *
from object_info import ObjectInfo

from requirements_checker import *


# =====================================================================================================================
DUMMY_MODULE_NAME = "dummy-module"


# =====================================================================================================================
class Test_Base:
    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (ReqCheckStr_Base,), {})

    # TRIVIAL CASES ---------------------------------------------------------------------------------------------------
    def test__no_getter(self):
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
        assert victim._sample_actual == "hello"

    def test__inits(self):
        assert self.VICTIM(_getter=lambda: "hello", _raise=False, _meet_true=True).check() is False
        assert self.VICTIM(_getter=lambda: "hello", _raise=False, _meet_true=False).check() is True

        assert self.VICTIM(_getter=lambda: "hello", _raise=False).check_is__("HELLO") is True
        assert self.VICTIM(_getter=lambda: "hello", _raise=False).bool_if__HELLO() is True

        assert self.VICTIM.bool_if__HELLO() is True

    # ACCEPTANCE VARIANTS ---------------------------------------------------------------------------------------------
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

    # SETTINGS ATTRIBUTES ---------------------------------------------------------------------------------------------
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

    def test__set_meet_true(self):
        self.VICTIM._RAISE = False
        self.VICTIM._GETTER = lambda: "Hello"

        # _MEET_TRUE = True
        self.VICTIM._MEET_TRUE = True
        self.VICTIM.hello = True

        victim = self.VICTIM()
        assert victim.check() is True

        victim.hello = False
        assert victim.check() is False
        victim._RAISE = True
        try:
            victim.check()
        except Exx_Requirement:
            assert True
        else:
            assert False

        # _MEET_TRUE = False
        victim._RAISE = False
        victim._MEET_TRUE = False
        victim.hello = True
        assert victim.check() is True

    #  ---------------------------------------------------------------------------------------------
    def test__case_insencitive(self):
        self.VICTIM._GETTER = lambda: "Hello"
        self.VICTIM.HELLO = True
        victim = self.VICTIM()

        assert victim.check() is True

    # PARAMS ----------------------------------------------------------------------------------------------------------
    # def test__param_values(cls):
    #     cls.VICTIM._RAISE = False
    #     cls.VICTIM._GETTER = lambda: "Hello"
    #     cls.VICTIM.HELLO = True
    #     victim = cls.VICTIM()
    #
    #     assert victim.check() is True
    #     assert victim.check("hellO") is True
    #     assert victim.check(["hellO", ]) is True
    #
    #     assert victim.check("hell") is False
    #     assert victim.check(["hell", ]) is False

    # IS/ISNOT -------------------------------------------------------------------------------------------------------
    def test__check_is(self):
        self.VICTIM._RAISE = False
        self.VICTIM._GETTER = lambda: "Hello"
        victim = self.VICTIM()

        assert victim.check_is__("hellO999") is False
        assert victim.check_is__("hellO") is True
        assert victim.check_is__(["hellO", ]) is True
        assert victim.check_is__(["hellO", "hellO999"]) is True

        assert victim.check_is__("hellO999", _reverse=True) is True
        assert victim.check_is__("hellO", _reverse=True) is False
        assert victim.check_is__(["hellO", ], _reverse=True) is False
        assert victim.check_is__(["hellO", "hellO999"], _reverse=True) is False

        # getattr -------
        assert victim.bool_if__HELLO() is True
        assert victim.bool_if__HELLO999() is False
        assert self.VICTIM.bool_if__HELLO() is True
        assert self.VICTIM.bool_if__HELLO999() is False

        assert victim.bool_if_not__HELLO() is False
        assert victim.bool_if_not__HELLO999() is True
        assert self.VICTIM.bool_if_not__HELLO() is False
        assert self.VICTIM.bool_if_not__HELLO999() is True

        try:
            self.VICTIM.raise_if__HELLO()
        except:
            pass
        else:
            assert False

        assert self.VICTIM.raise_if_not__HELLO() is None

        assert self.VICTIM.raise_if__HELLO999() is None

        try:
            self.VICTIM.raise_if_not__HELLO999()
        except:
            pass
        else:
            assert False


# =====================================================================================================================
class Test_Os:
    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (ReqCheckStr_Os,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__bool(self):
        victim = self.VICTIM()

        assert not hasattr(victim, "WINDOWS")

        assert victim.bool_if__WINDOWS() != victim.bool_if__LINUX()
        if victim._sample_actual in ["windows", ]:
            assert victim.bool_if__WINDOWS() is True

    def test__1(self):
        self.VICTIM.LINUX = True
        self.VICTIM.WINDOWS = True

        victim = self.VICTIM()
        assert victim._sample_actual in ["windows", "linux"]
        assert victim.check() is True


# =====================================================================================================================
class Test_Pkg:
    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (Packages,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__all_methods(self):
        victim = self.VICTIM()

        for version in ["0.0.1", "0.0.2", ]:
            assert victim.upgrade(f"{DUMMY_MODULE_NAME}=={version}")
            assert victim.version_get(DUMMY_MODULE_NAME) == version
            assert victim.check_installed(DUMMY_MODULE_NAME) is True

        victim.uninstall(DUMMY_MODULE_NAME)
        assert victim.version_get(DUMMY_MODULE_NAME) is None
        assert victim.check_installed(DUMMY_MODULE_NAME) is False


# =====================================================================================================================
class Test_File:
    def setup_method(self, method):
        self.VICTIM = type("VICTIM", (Packages,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__upgrade(self, tmpdir):
        # print(tmpdir)
        # ObjectInfo(tmpdir).print()

        victim = self.VICTIM()
        victim.uninstall(DUMMY_MODULE_NAME)
        assert victim.check_installed(DUMMY_MODULE_NAME) is False

        filepath = pathlib.Path(tmpdir.strpath).joinpath("requirements.txt")
        filepath.write_text(DUMMY_MODULE_NAME)
        assert victim.upgrade_file(filepath) is True

        assert victim.check_installed(DUMMY_MODULE_NAME) is True

    def test__print(self, tmpdir):
        """just see printed file content"""
        victim = self.VICTIM()

        filepath = pathlib.Path(tmpdir.strpath).joinpath("requirements.txt")
        filepath.write_text(DUMMY_MODULE_NAME)
        victim.upgrade_file(filepath)


# =====================================================================================================================
