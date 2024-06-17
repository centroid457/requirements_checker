from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory
from configparser import ConfigParser
from pytest import mark
from pytest_aux import *

from requirements_checker import *
from pytest_aux import *


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS _SOURCE!!!
# from PRJ_NEW__ import *


# =====================================================================================================================
class Test__VersionBlock:
    Victim: Type[VersionBlock]
    @classmethod
    def setup_class(cls):
        pass
        cls.Victim = VersionBlock

    # @classmethod
    # def teardown_class(cls):
    #     if cls.victim:
    #         cls.victim.disconnect()
    #
    # def setup_method(self, method):
    #     pass
    #
    # def teardown_method(self, method):
    #     pass

    # -----------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (True, "true"),
            (1, "1"),

            ("1", "1"),
            ("hello", "hello"),
            ("HELLO", "hello"),
            ("11rc22", "11rc22"),
            (" 11 rc-2 2", "11rc22"),

            # zeros invaluable
            ("01rc02", "01rc02"),

            # not clean chars
            ("[11:rc.22]", "[11:rc.22]"),

            # iterables
            ([11, "r c---", 22], "11rc22"),

        ]
    )
    def test__convert_to_string(self, args, _EXPECTED):
        func_link = self.Victim._convert_to_string
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (True, False),
            (1, False),

            ("1", True),
            ("hello", True),
            ("HELLO", False),
            ("11rc22", True),
            (" 11 rc-2 2", False),

            # zeros invaluable
            ("01rc02", True),

            # not clean chars
            ("[11:rc.22]", False),

            # iterables
            ([11, "r c---", 22], False),
        ]
    )
    def test__validate_string(self, args, _EXPECTED):
        func_link = self.Victim._validate_string
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)

    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (True, ()),
            (1, ()),

            ("1", (1, )),
            ("hello", ("hello", )),
            ("HELLO", ()),
            ("11rc22", (11, "rc", 22)),
            (" 11 rc-2 2", (11, "rc", 2, 2)),   # FIXME:!!! think what to do with it!!!!

            # zeros invaluable
            ("01rc02", (1, "rc", 2)),

            # not clean chars
            ("[11:rc.22]", (11, "rc", 22)),

            # iterables
            ([11, "r c---", 22], ()),
        ]
    )
    def test__parce_elements(self, args, _EXPECTED):
        func_link = self.Victim._parse_elements
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)

    # INST ------------------------------------------------------------------------------------------------------------
    @pytest.mark.parametrize(
        argnames="args, _EXPECTED",
        argvalues=[
            (True, "true"),
            (1, "1"),

            ("1", "1"),
            ("hello", "hello"),
            ("HELLO", "hello"),
            ("11rc22", "11rc22"),
            (" 11 rc-2 2", "11rc22"),

            # zeros invaluable
            ("01rc02", "01rc02"),

            # not clean chars
            ("[11:rc.22]", Exx_VersionBlockIncompatible),

            # iterables
            ([11, "r c---", 22], "11rc22"),
        ]
    )
    def test__string(self, args, _EXPECTED):
        func_link = lambda source: str(self.Victim(source))
        pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
