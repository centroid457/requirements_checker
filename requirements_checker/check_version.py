from typing import *
import re
from object_info import ObjectInfo


# =====================================================================================================================
# TODO:



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
TYPE__SOURCE_BLOCKS = Union[str, int, list, tuple, Any, 'VersionBlock']


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
    PATTERN_VALIDATE_SOURCE_NEGATIVE = r"\d+[^0-9a-z]+\d+"
    PATTERN_VALIDATE_CLEANED = r"(\d|[a-z])+"
    PATTERN_ITERATE = r"\d+|[a-z]+"

    def __init__(self, source: TYPE__SOURCE_BLOCKS):
        self._SOURCE = source
        if not self._validate_source(source):
            raise Exx_VersionBlockIncompatible()

        string = self._prepare_string(source)
        if not self._validate_string(string):
            raise Exx_VersionBlockIncompatible()

        self.ELEMENTS = self._parse_elements(string)

    @classmethod
    def _validate_source(cls, source: TYPE__SOURCE_BLOCKS) -> bool:
        source = str(source).lower()
        match = re.search(cls.PATTERN_VALIDATE_SOURCE_NEGATIVE, source)
        return not bool(match)

    @classmethod
    def _prepare_string(cls, source: TYPE__SOURCE_BLOCKS) -> str:
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

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"

    def __str__(self) -> str:
        return "".join(str(item) for item in self.ELEMENTS)

    @property
    def STRING(self) -> str:
        return str(self)

    # CMP -------------------------------------------------------------------------------------------------------------
    def __cmp(self, other: TYPE__SOURCE_BLOCKS) -> int | NoReturn:
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
TYPE__VERSION_BLOCKS = tuple[TYPE__SOURCE_BLOCKS, ...]
TYPE__SOURCE_VERSION = Union[VersionBlock, tuple[VersionBlock], Any]


class PatternsVer:
    # VERSION_TUPLE = r"\((\d+\.+(\w+\.?)+)\)"
    # VERSION_LIST = r"\[(\d+\.+(\w+\.?)+)\]"
    VERSION_IN_BRACKETS: list = [r"\((.*)\)", r"\[(.*)\]"]  # get first bracket!!!
    VALIDATE_BRACKETS_NEGATIVE: list = [r"[^\[].*\]", r"\[.*[^\]]",   r"[^\(].*\)", r"\(.*[^\)]"]


# =====================================================================================================================
class Version:
    _SOURCE: Any
    BLOCKS: TYPE__VERSION_BLOCKS

    def __init__(self, source: Any):
        self._SOURCE = source
        string = self._prepare_string(source)
        self.BLOCKS = self._parse_blocks(string)

    # -----------------------------------------------------------------------------------------------------------------
    @classmethod
    def _prepare_string(cls, source: Any) -> str | NoReturn:
        """
        ONLY PREPARE STRING FOR CORRECT SPLITTING BLOCKS - parsing blocks would inside VersionBlock
        """
        if isinstance(source, (list, tuple)):
            result = ".".join([str(item) for item in source])
        else:
            result = str(source)

        result = result.lower()

        # CUT ---------
        for pattern in PatternsVer.VERSION_IN_BRACKETS:
            match = re.search(pattern, result)
            if match:
                result = match[1]
                break

        if "," in result and "." in result:
            raise Exx_VersionIncompatible()

        for pattern in PatternsVer.VALIDATE_BRACKETS_NEGATIVE:
            if re.search(pattern, result):
                raise Exx_VersionIncompatible()

        result = re.sub(r"\A\D+", "", result)   # ver/version
        result = re.sub(r",+", ".", result)
        result = re.sub(r"\.+", ".", result)
        result = result.strip(".")

        if not result:
            raise Exx_VersionIncompatible()

        return result

    @staticmethod
    def _parse_blocks(source: str) -> TYPE__VERSION_BLOCKS | NoReturn:
        blocks_list__str = source.split(".")

        # RESULT -----------
        result = []
        for item in blocks_list__str:
            if not item:
                continue

            block = VersionBlock(item)
            result.append(block)

        return tuple(result)

    # -----------------------------------------------------------------------------------------------------------------
    def __len__(self) -> int:
        return len(self.BLOCKS)

    def __getitem__(self, item: int) -> VersionBlock | None:
        try:
            return self.BLOCKS[item]
        except:
            return

    def __iter__(self):
        yield from self.BLOCKS

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"

    def __str__(self):
        return ".".join([str(block) for block in self.BLOCKS])

    @property
    def STRING(self) -> str:
        return str(self)

    # -----------------------------------------------------------------------------------------------------------------
    @property
    def major(self) -> TYPE__SOURCE_BLOCKS | None:
        return self[0]

    @property
    def minor(self) -> TYPE__SOURCE_BLOCKS | None:
        return self[1]

    @property
    def micro(self) -> TYPE__SOURCE_BLOCKS | None:
        return self[2]

    # CMP -------------------------------------------------------------------------------------------------------------
    def __cmp(self, other: TYPE__SOURCE_VERSION) -> int | NoReturn:
        other = Version(other)

        # equel ----------------------
        if str(self) == str(other):
            return 0

        # by elements ----------------
        for block_1, block_2 in zip(self, other):
            if block_1 == block_2:
                continue
            else:
                return int(block_1 > block_2) or -1

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
# class ReqCheckVer(metaclass=GetattrClassmethod_Meta):
#     pass
#
#     def _check(self, source: Any, ):
#         pass


# =====================================================================================================================
