import os
import pytest
import pathlib
import platform
from typing import *
from object_info import ObjectInfo

from requirements_checker import *


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
