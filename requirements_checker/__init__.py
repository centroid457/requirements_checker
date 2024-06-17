# =====================================================================================================================
# VERSION = (0, 0, 1)   # use import EXACT_OBJECTS! not *
#   from .main import *                 # INcorrect
#   from .main import EXACT_OBJECTS     # CORRECT


# =====================================================================================================================
# TEMPLATE
# from .main import (
#     # BASE
#     EXACT_OBJECTS,
#
#     # AUX
#
#     # TYPES
#
#     # EXX
# )
# ---------------------------------------------------------------------------------------------------------------------
from .check_string import (
    # BASE
    ReqCheckStr_Base,
    ReqCheckStr_Os,
    ReqCheckStr_Arch,

    # AUX
    GetattrClassmethod_Meta,

    # TYPES
    TYPE__VALUES,
    TYPE__RESULT_BOOL,
    TYPE__RESULT_RAISE,

    # EXX
    Exx_RequirementCantGetActualValue,
    Exx_Requirement,
)
from .check_pkg import (
    # BASE
    Packages,
    CmdPattern,

    # AUX

    # TYPES

    # EXX
)
from .check_version import (
    # BASE
    Version,

    # AUX

    # TYPES
    TYPE__VERSION_ELEMENT,
    TYPE__VERSION_ELEMENTS,
    TYPE__BLOCK_SOURCE,
    VersionBlock,

    TYPE__VERSION_BLOCKS,

    # EXX
    Exx_VersionIncompatible,
    Exx_VersionBlockIncompatible,
)


# =====================================================================================================================
