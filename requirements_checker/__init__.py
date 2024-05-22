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

    # EXX
    Exx_RequirementCantGetActualValue,
    Exx_Requirement,
)
from .check_pkg import (
    # BASE
    Packages,

    # AUX

    # TYPES

    # EXX
)
# from .check_version import (      # TODO: create it!
#     # BASE
#     Packages,
#
#     # AUX
#
#     # TYPES
#
#     # EXX
# )

# =====================================================================================================================
