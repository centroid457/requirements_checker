from typing import *
import pathlib
from cli_user import CliUser

from . import ReqCheckStr_Os


# =====================================================================================================================
class Requirements:
    PIP_NAME: str
    PYTHON_NAME: str
    FILENAME_457: str = "requirements__centoid457.txt"
    FILEPATH_457: pathlib.Path = pathlib.Path(__file__).parent.joinpath(FILENAME_457)

    def explore(self):
        # print(f"{__file__=}")
        # print(f"{pathlib.Path(__file__).parent.joinpath(self.FILENAME_457)=}")
        # print(f"{pathlib.Path(__file__).parent.joinpath(self.FILENAME_457).exists()=}")

        print(self.FILEPATH_457)
        print(f"{self.FILEPATH_457.exists()}")

    def filepath_ge(self) -> pathlib.Path:
        pass

    def __init__(self):
        if ReqCheckStr_Os().bool_if__WINDOWS():
            self.PIP_NAME = "pip"
            self.PYTHON_NAME = "python"
        else:
            self.PIP_NAME = "pip3"
            self.PYTHON_NAME = "python3"

        self.PYTHON_PIP = f"{self.PYTHON_NAME} -m pip"

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
        return CliUser().send(cmd, timeout=60 * 1)

    def upgrade_pip(self) -> bool:
        return self.upgrade("pip")

    # =================================================================================================================
    def upgrade_file(self, filepath: pathlib.Path) -> bool:
        cmd = f"{self.PYTHON_PIP} install --upgrade -r '{filepath}'"
        return CliUser().send(cmd, timeout=60 * 5)

    def upgrade_file__centroid457(self) -> bool:
        return self.upgrade_file(self.FILEPATH_457)

    # =================================================================================================================
    def delete(self, modules: Union[str, List[str]]) -> bool:
        pass
        # cmd = ""
        # CliUser().send(cmd)


# =====================================================================================================================
