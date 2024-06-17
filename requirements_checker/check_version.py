from typing import *
import re
from object_info import ObjectInfo


# =====================================================================================================================
# TODO: make BIG REF!
# TODO: add class VersionBlock and compare inside + use Schema + validate
# TODO: in Version add parceMethod


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
TYPE__VERSION_ELEMENTS = tuple[TYPE__VERSION_ELEMENT, ...]
TYPE__SOURCE = Union[str, int, list, tuple, Any, 'VersionBlock']


class VersionBlock:
    """
    this is exact block in version string separated by dots!!!

    PATTERN for blocks
    ------------------
        block1.block2.block3

    EXAMPLES for block
    ------------------
        1rc2
        1-rc2
        1 rc 2

    RULES
    -----
    1.
    """
    _SOURCE: Any
    ELEMENTS: TYPE__VERSION_ELEMENTS

    PATTERN_CLEAR = r"[\"' -]*"
    PATTERN_VALIDATE_SOURCE_NEGATIVE = r"\d+[^a-z]+\d+"
    PATTERN_VALIDATE_CLEANED = r"(\d|[a-z])+"
    PATTERN_ITERATE = r"\d+|[a-z]+"

    def __init__(self, source: TYPE__SOURCE):
        self._SOURCE = source
        if not self._validate_source(self._SOURCE):
            raise Exx_VersionBlockIncompatible()

        string = self._convert_to_string(self._SOURCE)
        if not self._validate_string(string):
            raise Exx_VersionBlockIncompatible()

        self.ELEMENTS = self._parse_elements(string)

    @classmethod
    def _validate_source(cls, source: TYPE__SOURCE) -> bool:
        source = str(source).lower()
        match = re.search(cls.PATTERN_VALIDATE_SOURCE_NEGATIVE, source)
        return not bool(match)

    @classmethod
    def _convert_to_string(cls, source: TYPE__SOURCE) -> str:
        if isinstance(source, (list, tuple)):
            result = "".join([str(item) for item in source])
        else:
            result = str(source)

        # FINISH -------------------------------
        result = re.sub(cls.PATTERN_CLEAR, "", result)
        result = result.lower()
        result = result.strip()
        return result

    @classmethod
    def _validate_string(cls, string: str) -> bool:
        if not isinstance(string, str):
            return False
        match = re.fullmatch(cls.PATTERN_VALIDATE_CLEANED, string)
        return bool(match)

    @classmethod
    def _parse_elements(cls, string: str) -> TYPE__VERSION_ELEMENTS:
        if not isinstance(string, str):
            return ()

        result_list = []
        for element in re.findall(cls.PATTERN_ITERATE, string):
            try:
                element = int(element)
            except:
                pass
            result_list.append(element)

        return tuple(result_list)

    def __iter__(self):
        yield from self.ELEMENTS

    def __len__(self) -> int:
        return len(self.ELEMENTS)

    def __str__(self) -> str:
        return "".join(str(item) for item in self.ELEMENTS)

    @property
    def STRING(self) -> str:
        return str(self)

    # CMP -------------------------------------------------------------------------------------------------------------
    def __cmp(self, other: TYPE__SOURCE) -> int | NoReturn:
        other = VersionBlock(other)

        # equel ----------------------
        if str(self) == str(other):
            return 0

        # by elements ----------------
        for elem_1, elem_2 in zip(self, other):
            if elem_1 == elem_2:
                continue

            if isinstance(elem_1, int):
                if isinstance(elem_2, int):
                    return elem_1 - elem_2
                else:
                    return 1
            else:
                if isinstance(elem_2, int):
                    return -1
                else:
                    return int(elem_1 > elem_2) or -1

        # final - longest ------------
        return int(len(self) > len(other)) or -1

    def __eq__(self, other):
        return self.__cmp(other) == 0

    def __ne__(self, other):
        return self.__cmp(other) != 0

    def __lt__(self, other):
        return self.__cmp(other) < 0

    def __gt__(self, other):
        return self.__cmp(other) > 0

    def __le__(self, other):
        return self.__cmp(other) <= 0

    def __ge__(self, other):
        return self.__cmp(other) >= 0


# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================
# TYPE__VERSION_PARSED = tuple[TYPE__VERSION_PARSED__BLOCK, ...]
#
#
# class PatternsVer:
#     VERSION_TUPLE = r"\((\d+\.+(\w+\.?)+)\)"
#     VERSION_LIST = r"\[(\d+\.+(\w+\.?)+)\]"
#     VERSION_BLOCK = r"(\d*)([a-zA-Z]*)(\d*)"
#
#
# # =====================================================================================================================
# class Version:
#     _SOURCE: Any
#     PARSED: TYPE__VERSION_PARSED
#
#     # -----------------------------------------------------------------------------------------------------------------
#     @staticmethod
#     def version_block__ensure_elements(source: Union[str, int]) -> TYPE__VERSION_PARSED__BLOCK | NoReturn:
#         """
#         BLOCK could consists of only pattern like D*S*D* no more else!
#         """
#         result = []
#
#         if isinstance(source, int):
#             return source
#
#         if isinstance(source, str):
#             match = re.fullmatch(PatternsVer.VERSION_BLOCK, source)
#             if match:
#                 for match in (match[1], match[2], match[3]):
#                     if match:
#                         try:
#                             match = int(match)
#                         except:
#                             pass
#                         result.append(match)
#                 if len(result) == 1:
#                     return result[0]
#                 else:
#                     return tuple(result)
#
#         # ITERABLES ----------------
#         if isinstance(source, (list, tuple)):
#             if len(source) > 3:
#                 msg = f"block is too large {len(source)=}"
#                 raise Exx_VersionBlockIncompatible(msg)
#
#             elif len(source) == 3:
#                 if not all(
#                         [
#                             isinstance(source[0], int),
#                             isinstance(source[1], str),
#                             isinstance(source[2], int),
#                         ]
#                 ):
#                     msg = f"incorrect pattern D*S*D* {source=}"
#                     raise Exx_VersionBlockIncompatible(msg)
#
#             elif len(source) == 2:
#                 if not any(
#                         [
#                             isinstance(source[0], int) and isinstance(source[1], str),
#                             isinstance(source[0], str) and isinstance(source[1], int),
#                 ]):
#                     msg = f"incorrect pattern D*S*D* {source=}"
#                     raise Exx_VersionBlockIncompatible(msg)
#
#             elif len(source) == 1:
#                 if not isinstance(source[0], (int, str)) :
#                     msg = f"incorrect pattern D*S*D* {source=}"
#                     raise Exx_VersionBlockIncompatible(msg)
#                 else:
#                     return source[0]
#
#             elif len(source) == 0:
#                 msg = f"incorrect pattern D*S*D* {source=}"
#                 raise Exx_VersionBlockIncompatible(msg)
#
#             return tuple(source)
#
#         # FINAL RAISE
#         raise Exx_VersionBlockIncompatible()
#
#     @staticmethod
#     def version__ensure_tuple(source: Union[str, TYPE__VERSION_PARSED, list[str, int], Any]) -> TYPE__VERSION_PARSED | NoReturn:
#         if isinstance(source, list):
#             pass
#
#         source = str(source)
#
#         source = re.sub(r"\s+", "", source)
#         source = re.sub(r"\'+", "", source)
#         source = re.sub(r"\"+", "", source)
#         source = re.sub(r",+", ".", source)
#         source = re.sub(r"\.+", ".", source)
#
#         for pattern in [PatternsVer.VERSION_TUPLE, PatternsVer.VERSION_LIST]:
#             match = re.search(pattern, source, flags=re.IGNORECASE)
#             if match:
#                 source = match[1]
#                 break
#
#         source = re.sub(r"\A\D+", "", string=source, flags=re.IGNORECASE)
#         source = re.sub(r"\.+\Z", "", source)
#
#         if not source:
#             raise Exx_VersionIncompatible()
#
#         source_list = source.split(".")
#
#         # RESULT -----------
#         for index, item in enumerate(source_list):
#             try:
#                 item = int(item)
#                 source_list[index] = item
#             except:
#                 pass
#
#             item = Version.version_block__ensure_elements(item)
#             source_list[index] = item
#
#         return tuple(source_list)
#
#     # -----------------------------------------------------------------------------------------------------------------
#     def __init__(self, source: Any):
#         self._SOURCE = source
#         self.PARSED = self.version__ensure_tuple(source)
#
#     def __cmp__(self, other: Union[Any, Self]) -> bool | NoReturn:
#         # TODO: FINISH!!!
#         # TODO: FINISH!!!
#         # TODO: FINISH!!!
#         # TODO: FINISH!!!
#         # TODO: FINISH!!!
#         # TODO: FINISH!!!
#         # if elements in same length is equel - longest is higher!
#         pass
#
#     # -------------------
#     def __str__(self):
#         result = ""
#         for block in self.PARSED:
#             if isinstance(block, tuple):
#                 elements = "".join(block)
#                 result += f"{elements}."
#             else:
#                 result += f"{block}."
#
#         result = result[:-1]
#         return result
#
#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}({self})"
#
#     def __len__(self) -> int:
#         return len(self.PARSED)
#
#     def __getitem__(self, item: int) -> TYPE__VERSION_PARSED__BLOCK | None:
#         try:
#             return self.PARSED[item]
#         except:
#             return
#
#     def __iter__(self):
#         yield from self.PARSED
#
#     # -----------------------------------------------------------------------------------------------------------------
#     @property
#     def major(self) -> TYPE__VERSION_PARSED__BLOCK | None:
#         return self[0]
#
#     @property
#     def minor(self) -> TYPE__VERSION_PARSED__BLOCK | None:
#         return self[1]
#
#     @property
#     def micro(self) -> TYPE__VERSION_PARSED__BLOCK | None:
#         return self[2]
#
#
# # =====================================================================================================================
# # class ReqCheckVer(metaclass=GetattrClassmethod_Meta):
# #     pass
# #
# #     def _check(self, source: Any, ):
# #         pass
#
#
# # =====================================================================================================================
