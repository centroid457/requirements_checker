from typing import *


# =====================================================================================================================
class PROJECT:
    # AUX --------------------------------------------------
    _VERSION_TEMPLATE: Tuple[int] = (0, 0, 2)

    # AUTHOR -----------------------------------------------
    AUTHOR_NAME: str = "Andrei Starichenko"
    AUTHOR_EMAIL: str = "centroid@mail.ru"
    AUTHOR_HOMEPAGE: str = "https://github.com/centroid457/"

    # PROJECT ----------------------------------------------
    NAME_INSTALL: str = "requirements-checker"
    NAME_IMPORT: str = "requirements_checker"
    KEYWORDS: List[str] = [
        "check requirements", "check system requirements", "raise/bool if no requirements",
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
        "...see tests for this!"
    ]

    # HISTORY -----------------------------------------------
    VERSION: Tuple[int, int, int] = (0, 1, 1)
    VERSION_STR: str = ".".join(map(str, VERSION))
    TODO: List[str] = [
        "add WARN_if__*/if_not__* (and use message in stderr)",
        "add check_version (py interpreter for example!)",
        "add work with packages",
    ]
    FIXME: List[str] = [
        "sometimes modules have incorrect SHARE!!! maybe need check upgrade after installation!!! and show ERROR!"
    ]
    NEWS: List[str] = [
        "show result for module installation",
        "apply new PRJ version 0.0.2"
    ]


# =====================================================================================================================
if __name__ == '__main__':
    pass


# =====================================================================================================================
