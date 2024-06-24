from typing import *
from _aux__release_files import release_files_update


# =====================================================================================================================
# VERSION = (0, 0, 3)   # 1/deprecate _VERSION_TEMPLATE from PRJ object +2/place update_prj here in __main__ +3/separate finalize attrs
VERSION = (0, 0, 4)     # add AUTHOR_NICKNAME_GITHUB for badges


# =====================================================================================================================
class PROJECT:
    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"
    AUTHOR_NICKNAME_GITHUB: str = "centroid457"

    # PROJECT ----------------------------------------------
    NAME_IMPORT: str = "requirements_checker"
    KEYWORDS: List[str] = [
        "check requirements", "raise/bool if no requirements",
        "check system requirements",
        "python packages/modules aux (upgrade/delete/version get)",
        "version parse", "version check", "version compare",
    ]
    CLASSIFIERS_TOPICS_ADD: List[str] = [
        # "Topic :: Communications",
        # "Topic :: Communications :: Email",
    ]

    # README -----------------------------------------------
    # add DOUBLE SPACE at the end of all lines! for correct representation in MD-viewers
    DESCRIPTION_SHORT: str = "check if requirements met"
    DESCRIPTION_LONG: str = """
designed for check requirements (systemOs) and raise/bool if no match
    """
    FEATURES: List[str] = [
        # "feat1",
        # ["feat2", "block1", "block2"],

        "check requirements (systemOs), raise/bool if no match",
        "create fuck(?)/getter and is it for check for settings",
        ["[python PACKAGES/MODULES]", "upgrade", "delete", "version_get", "check_installed)", "upgrade pip"],
        ["[VERSION]",
            "parse",
            "check",
            "compare",
        ],
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 2, 4)
    TODO: List[str] = [
        "add WARN_if__*/if_not__* (and use message in stderr)",
        "add check_file"
    ]
    FIXME: List[str] = [
        "sometimes modules have incorrect SHARE!!! maybe need check upgrade after installation!!! and show ERROR!",
        "FIX TESTS!"
    ]
    NEWS: List[str] = [
        "[TESTS] move into separated folder",
    ]

    # FINALIZE -----------------------------------------------
    VERSION_STR: str = ".".join(map(str, VERSION))
    NAME_INSTALL: str = NAME_IMPORT.replace("_", "-")


# =====================================================================================================================
if __name__ == '__main__':
    release_files_update(PROJECT)


# =====================================================================================================================
