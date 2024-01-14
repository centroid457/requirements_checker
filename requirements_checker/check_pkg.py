from typing import *
import pathlib
from cli_user import CliUser

from . import ReqCheckStr_Os


# =====================================================================================================================
class Packages:
    PKGSET__CENTROID_457: List[str] = [
        # =============================
        # CENTROID457 all projects
        # -----------------------------
        "requirements-checker",
        "object-info",
        "singleton-meta",
        "funcs-aux",

        "annot-attrs",
        "private-values",
        "alerts-msg",
        "monitor-utils",

        "cli-user",
        "bus-user",

        "threading-manager",
        "pyqt_templates",

        # =============================
        # DISTRIBUTION PyPI
        # -----------------------------
        "sdist",
        "setuptools",
        "bdist-wheel-name",
    ]

    pip_name: str
    python_name: str

    # FILENAME_457: str = "requirements__centoid457.txt"      # FILE WILL NOT GO WITHING MODULE AS PART!
    # FILEPATH_457: pathlib.Path = pathlib.Path(__file__).parent.joinpath(FILENAME_457)

    # def explore(self):
    #     # print(f"{__file__=}")
    #     # print(f"{pathlib.Path(__file__).parent.joinpath(self.FILENAME_457)=}")
    #     # print(f"{pathlib.Path(__file__).parent.joinpath(self.FILENAME_457).exists()=}")
    #
    #     print(self.FILEPATH_457)
    #     print(f"{self.FILEPATH_457.exists()}")

    def __init__(self):
        if ReqCheckStr_Os().bool_if__WINDOWS():
            self.pip_name = "pip"
            self.python_name = "python"
        else:
            self.pip_name = "pip3"
            self.python_name = "python3"

        self.PYTHON_PIP = f"{self.python_name} -m pip"

    # =================================================================================================================
    def upgrade(self, modules: Union[str, List[str]]) -> bool:
        # LIST -----------------------------------------------
        if isinstance(modules, (list, tuple, set, )):
            result = True
            for module in modules:
                result = result and self.upgrade(module)
            return result

        # ONE -----------------------------------------------
        cmd = f"{self.PYTHON_PIP} install --upgrade {modules}"
        return CliUser().send(cmd, timeout=60 * 2)

    def upgrade_pip(self) -> bool:
        return self.upgrade("pip")

    def upgrade__centroid457(self) -> bool:
        return self.upgrade(self.PKGSET__CENTROID_457)

    # =================================================================================================================
    def upgrade_file(self, filepath: Union[str, pathlib.Path]) -> bool:
        filepath = pathlib.Path(filepath)
        cmd = f"{self.PYTHON_PIP} install --upgrade -r '{filepath}'"
        return CliUser().send(cmd, timeout=60 * 5)

    # =================================================================================================================
    def delete(self, modules: Union[str, List[str]]) -> bool:
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        pass
        # cmd = ""
        # CliUser().send(cmd)

    def check_installed(self, modules: Union[str, List[str]]) -> bool:
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        pass
        # cmd = ""
        # CliUser().send(cmd)

    def check_file(self, file) -> bool:
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        pass
        # cmd = ""
        # CliUser().send(cmd)

    def get_version(self, modules: str) -> str:
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        pass
        # cmd = ""
        # CliUser().send(cmd)


# =====================================================================================================================
