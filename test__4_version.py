from typing import *
import pytest

import pathlib
import shutil
from tempfile import TemporaryDirectory
from configparser import ConfigParser
from pytest import mark
from pytest_aux import *

from requirements_checker import *


# =====================================================================================================================
# KEEP FILES IN ROOT! OR IMPORT PRJ_MODULE WOULD FROM SYSTEM! NOT THIS SOURCE!!!
# from PRJ_NEW__ import *


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        # STRINGS --------
        ("12", 12),
        ("1a", (1, "a")),
        ("1a", (1, "a")),
        ("1a2", (1, "a", 2)),
        ("a2", ("a", 2)),
        ("1a2hello", Exx_VersionBlockIncompatible),
        ("a2hello", Exx_VersionBlockIncompatible),
        ("1.2", Exx_VersionBlockIncompatible),
        ("1/2", Exx_VersionBlockIncompatible),

        # INTS --------
        (12, 12),

        # ITEREBLES --------
        (((1, ), ), 1),
        (((1,"rc",3), ), (1,"rc",3)),
        (((1, None, 3), ), Exx_VersionBlockIncompatible),
        (((1,2), ), Exx_VersionBlockIncompatible),
        (((1,2, "rc"), ), Exx_VersionBlockIncompatible),
        ((("r","c"), ), Exx_VersionBlockIncompatible),
        (((),), Exx_VersionBlockIncompatible),

        # ANY --------
        (None, Exx_VersionBlockIncompatible),
        (1.123, Exx_VersionBlockIncompatible),
    ]
)
@pytest.mark.parametrize(argnames="func_link", argvalues=[Version.version_block__ensure_elements, ])
def test__version_block__ensure_elements(func_link, args, _EXPECTED):
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
@pytest.mark.parametrize(
    argnames="args, _EXPECTED",
    argvalues=[
        # INTS --------
        (12, (12,)),

        # CONTAINERS --------
        (((1,2,3,), ), (1,2,3)),
        (([1,2,3,], ), (1,2,3)),
        (([1,"2",3,], ), (1,2,3)),
        (([1,"02",3,], ), (1,2,3)),
        (([1,"21rc22",3,], ), (1, (21, "rc", 22), 3)),
        (([0,"21rc22",3, 0], ), (0, (21, "rc", 22), 3, 0)),

        # STRINGS SIMPLE --------
        ("", Exx_VersionIncompatible),
        ("12", (12, )),
        ("1.2", (1, 2)),
        ("1.2.3", (1, 2, 3)),
        ("1.2.3.4", (1, 2, 3, 4)),
        ("111.222.333.444", (111, 222, 333, 444)),

        # QUOTES --------
        (" 1, '2', '3 ", (1, 2, 3)),
        (" '1, 2', '3 ", (1, 2, 3)),
        (' 1, "2", 3' , (1, 2, 3)),

        # ZEROS --------
        ("0000.0000.0000.0000", (0, 0, 0, 0)),
        ("0.020.00030.00", (0, 20, 30, 0)),

        # START STRING --------
        ("v1.2.3", (1, 2, 3)),
        ("v 1.2.3", (1, 2, 3)),
        ("ver1.2.3", (1, 2, 3)),
        ("ver 1.2.3", (1, 2, 3)),
        ("version1.2.3", (1, 2, 3)),
        ("version 1.2.3", (1, 2, 3)),
        ("VERsion 1.2.3", (1, 2, 3)),

        ("start 1.2.3", (1, 2, 3)),
        ("start123", (123, )),

        # SEPS --------
        ("..1....2...3..", (1, 2, 3)),
        ("1,2,3", (1, 2, 3)),
        (",,...,,1,..,.,,,.,2.,.,.,,,.3.,.,.,.,.,,,...", (1, 2, 3)),
        ("   , ..  ,,1,..  ,,,.,2.  ,. ,. ,,.3.,.,.,.   ,.,,, ...  ", (1, 2, 3)),

        # BRACKETS --------
        ("(1,.,2,..3.,)", (1, 2, 3)),
        ("[1,,.2,,,3,.]", (1, 2, 3)),
        ("start11,23,(1,.,2,..3.,)finish11.22.33", (1, 2, 3)),

        # BLOCKS --------
        ("1.2a.3", (1, (2, "a", ), 3)),
        ("1.2a.3rc2", (1, (2, "a", ), (3, "rc", 2))),
        ("1.2a.3rc2get", Exx_VersionBlockIncompatible),

    ]
)
@pytest.mark.parametrize(argnames="func_link", argvalues=[Version.version__ensure_tuple, ])
def test__version__ensure_tuple(func_link, args, _EXPECTED):
    pytest_func_tester__no_kwargs(func_link, args, _EXPECTED)


# =====================================================================================================================
class Test__Version:
    Victim: Type[Version]
    @classmethod
    def setup_class(cls):
        pass
        cls.Victim = Version

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
    def test__123_str(self):
        source = "1.2.3"
        victim = self.Victim(source)
        assert victim.SOURCE == source
        assert victim.VERSION__TUPLE == (1,2,3)
        assert str(victim) == "1.2.3"
        assert repr(victim) == "Version(1.2.3)"
        assert len(victim) == 3

        assert victim[0] == 1
        assert victim[1] == 2
        assert victim[2] == 3
        assert victim[3] is None

        assert list(victim) == [1,2,3]

        assert victim.major == 1
        assert victim.minor == 2
        assert victim.micro == 3

    def test__123_list(self):
        source = [1, 2, 3]
        victim = self.Victim(source)
        assert victim.SOURCE == source
        assert victim.VERSION__TUPLE == (1,2,3)
        assert str(victim) == "1.2.3"
        assert repr(victim) == "Version(1.2.3)"
        assert len(victim) == 3

        assert victim[0] == 1
        assert victim[1] == 2
        assert victim[2] == 3
        assert victim[3] is None

        assert list(victim) == [1,2,3]

        assert victim.major == 1
        assert victim.minor == 2
        assert victim.micro == 3


# =====================================================================================================================
