from typing import *
import re
from object_info import ObjectInfo


# =====================================================================================================================
# EXPLORE VARIANTS ----------------------------------------------
# from packaging import version
# ObjectInfo(version.parse(str((1,2,3)))).print()

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


# =====================================================================================================================
class Exx_VersionBlockIncompatible(Exception):
    """
    """


class Exx_VersionIncompatible(Exception):
    """
    """


# =====================================================================================================================
TYPE__VERSION_ELEMENT = Union[str, int]
TYPE__VERSION_BLOCK = Union[TYPE__VERSION_ELEMENT, tuple[TYPE__VERSION_ELEMENT, ...]]
TYPE__VERSION = tuple[TYPE__VERSION_BLOCK, ...]

PATTERN__VERSION_TUPLE = r"\((\d+\.+(\w+\.?)+)\)"
PATTERN__VERSION_LIST = r"\[(\d+\.+(\w+\.?)+)\]"
PATTERN__VERSION_BLOCK = r"(\d*)([a-zA-Z]*)(\d*)"


# =====================================================================================================================
class Version:
    SOURCE: Any
    VERSION__TUPLE: TYPE__VERSION

    # -----------------------------------------------------------------------------------------------------------------
    @staticmethod
    def version_block__ensure_elements(source: Union[str, int]) -> TYPE__VERSION_BLOCK | NoReturn:
        result = []

        if isinstance(source, int):
            return source

        if isinstance(source, str):
            match = re.fullmatch(PATTERN__VERSION_BLOCK, source)
            if match:
                for match in (match[1], match[2], match[3]):
                    if match:
                        try:
                            match = int(match)
                        except:
                            pass
                        result.append(match)
                return tuple(result)

        raise Exx_VersionBlockIncompatible()

    @staticmethod
    def version__ensure_tuple(source: Union[str, TYPE__VERSION, list[str, int], Any]) -> TYPE__VERSION | NoReturn:
        source = str(source)

        source = re.sub(r"\s+", "", source)
        source = re.sub(r"\'+", "", source)
        source = re.sub(r"\"+", "", source)
        source = re.sub(r",+", ".", source)
        source = re.sub(r"\.+", ".", source)

        for pattern in [PATTERN__VERSION_TUPLE, PATTERN__VERSION_LIST]:
            match = re.search(pattern, source, flags=re.IGNORECASE)
            if match:
                source = match[1]
                break

        source = re.sub(r"\A\D+", "", string=source, flags=re.IGNORECASE)
        source = re.sub(r"\.+\Z", "", source)

        if not source:
            raise Exx_VersionIncompatible()

        source_list = source.split(".")

        # RESULT -----------
        for index, item in enumerate(source_list):
            try:
                item = int(item)
                source_list[index] = item
            except:
                pass

            item = Version.version_block__ensure_elements(item)
            source_list[index] = item

        return tuple(source_list)

    # -----------------------------------------------------------------------------------------------------------------
    def __init__(self, source: Any):
        self.SOURCE = source
        self.VERSION__TUPLE = self.version__ensure_tuple(source)

    def __cmp__(self, other) -> bool | NoReturn:
        # TODO: FINISH!!!
        # TODO: FINISH!!!
        # TODO: FINISH!!!
        # TODO: FINISH!!!
        # TODO: FINISH!!!
        # TODO: FINISH!!!
        # if elements in same length is equel - longest is higher!
        pass

    # -------------------
    def __str__(self):
        result = ""
        for block in self.VERSION__TUPLE:
            if isinstance(block, tuple):
                elements = "".join(block)
                result += f"{elements}."
            else:
                result += f"{block}."

        result = result[:-1]
        return result

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"

    def __iter__(self):
        yield from self.VERSION__TUPLE

    def __len__(self) -> int:
        return len(self.VERSION__TUPLE)

    def __getitem__(self, item: int) -> TYPE__VERSION_BLOCK | None:
        try:
            return self.VERSION__TUPLE[item]
        except:
            return

    # -----------------------------------------------------------------------------------------------------------------
    @property
    def major(self) -> TYPE__VERSION_BLOCK | None:
        return self[0]

    @property
    def minor(self) -> TYPE__VERSION_BLOCK | None:
        return self[1]

    @property
    def micro(self) -> TYPE__VERSION_BLOCK | None:
        return self[2]


# =====================================================================================================================
# class ReqCheckVer(metaclass=GetattrClassmethod_Meta):
#     pass
#
#     def _check(self, source: Any, ):
#         pass


# =====================================================================================================================
