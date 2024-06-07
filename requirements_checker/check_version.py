from typing import *
from object_info import ObjectInfo
from .check_string import GetattrClassmethod_Meta


# VARIANTS ----------------------------------------------
from packaging import version
ObjectInfo(version.parse(str((1,2,3)))).print()

# result = version.parse("2.3.1") < version.parse("10.1.2")

# ObjectInfo(version.parse("1.2.3")).print()
# print(result)
# print()
#
# from pkg_resources import parse_version         # DEPRECATED!!!
# parse_version("1.9.a.dev") == parse_version("1.9a0dev")
#

# import sys
# print(sys.winver)
# print(sys.version_info)
# print(tuple(sys.version_info))
#
# result = sys.version_info > (2, 7)
# print(result)


def parse_version_into_tuple(source: Any):
    # if iterable list()+joing to str.str
    # else str()
    # del started [v, ver, version]
    # del all brackets
    # split by .,:space into TUPLE
    # drop overLength - keep only same length
    # drop all blanks
    # try convert parts to int OR break to else one TUPLE if have digits!
    # compare all by chanks
    pass


class ReqCheckVer(metaclass=GetattrClassmethod_Meta):
    pass

    def _check(self, source: Any,
        pass
