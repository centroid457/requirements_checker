from typing import *
import pathlib
import re
import sys

from cli_user import CliUser


# =====================================================================================================================
# TYPE__MODULE_NAME = Union[str, list[str]]


# ---------------------------------------------------------------------------------------------------------------------
# TODO: FINISH!!!
# TODO: FINISH!!!
# TODO: FINISH!!!
# TODO: FINISH!!!
# TODO: FINISH!!!
# TODO: FINISH!!!
class PyModule:
    TARGET_NAME: str
    TARGET_VER: str = None

    def __init__(self, name: str):
        # if
        # self.NAME = name
        pass




# =====================================================================================================================
class CmdPattern:
    """
    USAGE
    -----
    cmd = pattern % (PYTHON_PATH, PARAMETER)
    cmd = CmdPattern.INSTALL_UPGRADE__MODULE % (self.PYTHON_PATH, modules)

    """
    INSTALL_UPGRADE__MODULE: str = f"%s -m pip install --upgrade %s"    # (PYTHON_PATH, MODULE)
    INSTALL_UPGRADE__FILE: str = f"%s -m pip install --upgrade -r %s"   # (PYTHON_PATH, FILE)
    SHOW_INFO: str = f"%s -m pip show %s"                               # (PYTHON_PATH, MODULE)
    UNINSTALL: str = f"%s -m pip uninstall -y %s"                       # (PYTHON_PATH, MODULE)


# =====================================================================================================================
class Packages:
    """
    RULE
    ----
    for all module names you could use
    """
    PKGSET__CENTROID_457: list[str] = [
        # =============================
        # CENTROID457 common projects
        # -----------------------------
        "requirements-checker",
        "object-info",
        "singleton-meta",
        "funcs-aux",
        "logger-aux",
        "pytest-aux",
        "classes-aux",

        # =============================
        # CENTROID457 other projects
        # -----------------------------
        "dummy-module",

        "annot-attrs",
        "private-values",
        "alerts-msg",
        "monitor-utils",

        "cli-user",
        "bus-user",

        "threading-manager",
        "pyqt-templates",

        "testplans",
        "server-templates",

        # =============================
        # DISTRIBUTION PyPI
        # -----------------------------
        # new setup
        "build",
        "twine",    # necessary! share project on pypi!

        # old setup (maybe not all)
        "sdist",
        "setuptools",
        "bdist-wheel-name",

    ]

    PYTHON_PATH: str
    cli: CliUser

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
        self.PYTHON_PATH = sys.executable
        self.cli = CliUser()

    # =================================================================================================================
    def upgrade(self, modules: Union[str, List[str]]) -> bool:
        """
        you can use explicit version definitions!
            name==0.0.1

NOT EXISTS
==================================================
[CLI_SEND] [python -m pip install --upgrade singleton-meta]
==================================================
self.counter=1
self.counter_in_list=0
self.last_cmd='python -m pip install --upgrade singleton-meta'
self.last_duration=1.347492
self.last_finished=True
self.last_finished_success=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	|'Collecting singleton-meta'
	|'  Using cached singleton_meta-0.1.1-py3-none-any.whl.metadata (2.8 kB)'
	|'Using cached singleton_meta-0.1.1-py3-none-any.whl (5.4 kB)'
	|'Installing collected packages: singleton-meta'
	|'Successfully installed singleton-meta-0.1.1'
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=None
==================================================



ALREADY OK
==================================================
[CLI_SEND] [python -m pip install --upgrade singleton-meta]
==================================================
self.counter=1
self.counter_in_list=0
self.last_cmd='python -m pip install --upgrade singleton-meta'
self.last_duration=1.39782
self.last_finished=True
self.last_finished_success=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	|'Requirement already satisfied: singleton-meta in c:\\python3.12.0x64\\lib\\site-packages (0.1.1)'
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=None
==================================================



GOOD UPGRADE
==================================================
[CLI_SEND] [python -m pip install --upgrade requirements-checker]
==================================================
self.counter=1
self.counter_in_list=0
self.last_cmd='python -m pip install --upgrade requirements-checker'
self.last_duration=1.367846
self.last_finished=True
self.last_finished_success=True
self.last_retcode=0
--------------------------------------------------
self.last_stdout=
	|'Requirement already satisfied: requirements-checker in c:\\!=starichenko=element\\!=projects\\abc=requirements_checker (0.0.7)'
	|'Collecting requirements-checker'
	|'  Using cached requirements_checker-0.1.0-py3-none-any.whl.metadata (2.2 kB)'
	|'Using cached requirements_checker-0.1.0-py3-none-any.whl (7.8 kB)'
	|'Installing collected packages: requirements-checker'
	|'  Attempting uninstall: requirements-checker'
	|'    Found existing installation: requirements-checker 0.0.7'
	|"    Can't uninstall 'requirements-checker'. No files were found to uninstall."
	|'Successfully installed requirements-checker-0.1.0'
	|''
--------------------------------------------------
self.last_stderr=
--------------------------------------------------
self.last_exx_timeout=None
==================================================



FIXME: sometimes modules have incorrect SHARE!!! maybe need check upgrade after installation!!! and show ERROR!!
ERROR ON DISTRIBUTION
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
            result = all([self.upgrade(module) for module in modules])
            return result

        # ONE -----------------------------------------------
        cmd = CmdPattern.INSTALL_UPGRADE__MODULE % (self.PYTHON_PATH, modules)
        self.cli.send(cmd, timeout=60 * 2, print_all_states=False)

        # RESULTS ===================================================
        result = f"[{modules}]"
        # RESULT EXISTS ---------------------------------------------
        # 'Requirement already satisfied: requirements-checker in c:\\!=starichenko=element\\!=projects\\abc=requirements_checker (0.0.7)'
        match = re.search(r'Requirement already satisfied: .+ \((\d+\.\d+\.\d+)\)', self.cli.last_stdout)
        if len(self.cli.last_stdout.split("\n")) == 2 and match:
            result += f"(already new){match[1]}"

        # result EXISTS OLD ---------------------------------------------
        # 'Found existing installation: requirements-checker 0.0.7'
        match = re.search(r'Found existing installation: \S+ (\d+\.\d+\.\d+)\s', self.cli.last_stdout)
        if match:
            result += f"(existed old){match[1]}"

        # result NEW VERSION! ---------------------------------------------
        # 'Successfully installed singleton-meta-0.1.1'
        match = re.search(r'Successfully installed \S+-(\d+\.\d+\.\d+)\s', self.cli.last_stdout)
        if match:
            result += f"->{match[1]}(upgraded new)"

        # FINISH ===================================================
        print(result)
        return self.cli.last_finished_success

    def upgrade_pip(self) -> bool:
        """
        upgrade PIP module
        """
        return self.upgrade("pip")

    def upgrade_prj(self, project: "PROJECT") -> bool:
        """
        upgrade PROJECT module to last

        CREATED specially for ensure upgrade to last version in active GIT-repo (you need to start in from git-repo!)
        """
        prj_name = project.NAME_INSTALL
        ver_prj = project.VERSION
        while True:
            ver_active = tuple(map(int, self.version_get(prj_name).split(".")))
            print(f"{ver_prj=}/{ver_active=}")
            if ver_active == ver_prj:
                break
            self.upgrade(prj_name)

        return ver_active == ver_prj

    def upgrade__centroid457(self) -> bool:
        """
        upgrade all author modules by one command
        """
        return self.upgrade(self.PKGSET__CENTROID_457)

    # =================================================================================================================
    def upgrade_file(self, filepath: Union[str, pathlib.Path]) -> bool:
        """
        upgrade modules by file requirements.py
        """
        filepath = pathlib.Path(filepath)
        if not filepath.exists():
            msg = f"[ERROR] file not found {filepath}"
            print(msg)
            return False

        cmd = CmdPattern.INSTALL_UPGRADE__FILE % (self.PYTHON_PATH, filepath)
        print("-" *20)
        print(f"{filepath=}")
        print(filepath.read_text(encoding="utf8"))
        print("-" *20)
        return self.cli.send(cmd, timeout=60 * 5)

    def check_file(self, file) -> bool:
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        # TODO: FINISH
        pass

    # =================================================================================================================
    def version_get(self, name: str) -> Optional[str]:
        """
        get version for module if it installed.

        C:\\Users\\a.starichenko>pip show object-info
        Name: object-info
        Version: 0.1.12
        Summary: print info about object (attributes+properties+methods results)
        Home-page: https://github.com/centroid457/
        Author: Andrei Starichenko
        Author-email: centroid@mail.ru
        License:
        Location: C:\\Python3.12.0x64\\Lib\\site-packages
        Requires:
        Required-by:

        C:\\Users\\a.starichenko>pip show object_info
        Name: object-info
        Version: 0.1.12
        Summary: print info about object (attributes+properties+methods results)
        Home-page: https://github.com/centroid457/
        Author: Andrei Starichenko
        Author-email: centroid@mail.ru
        License:
        Location: C:\\Python3.12.0x64\\Lib\\site-packages
        Requires:
        Required-by:

        C:\\Users\\a.starichenko>
        """
        cmd = CmdPattern.SHOW_INFO % (self.PYTHON_PATH, name)
        if self.cli.send(cmd, timeout=1, print_all_states=False) and self.cli.last_stdout:
            match = re.search(r'Version: (\d+\.\d+\.\d+)\s*', self.cli.last_stdout)
            if match:
                return match[1]

    def check_installed(self, modules: Union[str, list[str]]) -> bool:
        # LIST -----------------------------------------------
        if isinstance(modules, (list, tuple, set, )):
            for module in modules:
                if not self.check_installed(module):
                    return False
            return True

        # ONE -----------------------------------------------
        return self.version_get(modules) is not None

    def uninstall(self, modules: Union[str, list[str]]) -> None:
        # LIST -----------------------------------------------
        if isinstance(modules, (list, tuple, set, )):
            for module in modules:
                self.uninstall(module)

        # ONE -----------------------------------------------
        cmd = CmdPattern.UNINSTALL % (self.PYTHON_PATH, modules)
        self.cli.send(cmd, timeout=120)


# =====================================================================================================================
