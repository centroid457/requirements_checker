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
    @pytest.mark.parametrize(argnames="source", argvalues=[
        "1.2.3",
        [1, 2, 3],
    ])
    def test__123(self, source: Any):
        victim = self.Victim(source)
        assert victim._SOURCE == source


# =====================================================================================================================
