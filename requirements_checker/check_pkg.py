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
        """
FIXME: sometimes modules have incorrect SHARE!!! maybe need check upgrade after installation!!! and show ERROR!!
==================================================
[#####################ERROR#####################]
self.counter=1
self.counter_in_list=0
self.last_cmd='python -m pip install --upgrade private_values'
self.last_duration=1.392156
self.last_finished=True
self.last_finished_success=False
self.last_retcode=1
--------------------------------------------------
self.last_stdout=
        |'Collecting private_values'
        |'  Using cached private_values-0.5.4.tar.gz (8.8 kB)'
        |'  Preparing metadata (setup.py): started'
        |"  Preparing metadata (setup.py): finished with status 'error'"
        |''
--------------------------------------------------
self.last_stderr=
        |'  error: subprocess-exited-with-error'
        |'  '
        |'  python setup.py egg_info did not run successfully.'
        |'  exit code: 1'
        |'  '
        |'  [6 lines of output]'
        |'  Traceback (most recent call last):'
        |'    File "<string>", line 2, in <module>'
        |'    File "<pip-setuptools-caller>", line 34, in <module>'
        |'    File "C:\\Users\\a.starichenko\\AppData\\Local\\Temp\\pip-install-u6219r9f\\private-values_f5cf3965eb014632a70ff97372b73571\\setup.py", line 2, in <module>'
        |'      from PROJECT import PROJECT'
        |"  ModuleNotFoundError: No module named 'PROJECT'"
        |'  [end of output]'
        |'  '
        |'  note: This error originates from a subprocess, and is likely not a problem with pip.'
        |'error: metadata-generation-failed'
        |''
        |'Encountered error while generating package metadata.'
        |''
        |'See above for output.'
        |''
        |'note: This is an issue with the package mentioned above, not pip.'
        |'hint: See above for details.'
        |''
--------------------------------------------------
self.last_exx_timeout=None
==================================================
"""
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
