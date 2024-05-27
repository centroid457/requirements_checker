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
class Test_Pkg:
    def setup_method(self, method):
        self.Victim = type("Victim", (Packages,), {})

    # -----------------------------------------------------------------------------------------------------------------
    def test__all_methods(self):
        victim = self.Victim()

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
        self.VICTIM = type("Victim", (Packages,), {})

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
