from typing import *
import platform


# =====================================================================================================================
# TODO: add Base for version checker (py interpreter for example!)
# TODO: apply check_no with __getattr__


# =====================================================================================================================
class Exx_RequirementCantGetActualValue(Exception):
    """
    """


class Exx_Requirement(Exception):
    """Some of the requirements are not match
    """


# =====================================================================================================================
class ReqCheckStr_Base:
    """Base class for check exact requirement by string value

    VARIANTS for check
    ------------------
    add attributes with bool values (case-insensitive)
        - True - if value is definitely acceptable - Always need at least one True!!!
        - False - if not definitely acceptable
        - None - if requirement is undefined

    SETTINGS
    --------
    :ivar _RAISE: raise in case of inacceptance
    :ivar _CHECK_FULLMATCH:
        True - if need fullmatch (but always case-insensitive)
        False - if partial match by finding mentioned values in value actual

    :ivar _GETTER: function which will get the exact value to check
    :ivar _VALUE_ACTUAL:
    """
    _GETTER: Callable = None
    _RAISE: bool = True
    _CHECK_FULLMATCH: bool = True
    _VALUE_ACTUAL: Optional[str] = None

    def __init__(self):
        self.check()

    def check(self, _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        if _raise is None:
            _raise = self._RAISE

        if not self._GETTER:
            msg = f"[ERROR] incomplete settings [{self._GETTER=}]"
            raise Exx_RequirementCantGetActualValue(msg)

        try:
            value = self.__class__._GETTER()
            self._VALUE_ACTUAL: str = value.lower()
        except Exception as exx:
            raise Exx_RequirementCantGetActualValue(repr(exx))

        msg = "[ERROR] No TRUE variants MET!"
        for name in dir(self):
            if name.startswith("_"):
                continue
            acceptance: Optional[bool] = getattr(self, name)
            name = name.lower()
            if acceptance is True:
                msg = f"[ERROR] requirement not ACCEPTABLE [{self.__class__.__name__}/{self._VALUE_ACTUAL=}/req={name}]"
                if (
                        (self._CHECK_FULLMATCH and name == self._VALUE_ACTUAL)
                        or
                        (not self._CHECK_FULLMATCH and name in self._VALUE_ACTUAL)
                ):
                    return True

        # final
        if _raise:
            raise Exx_Requirement(msg)
        else:
            return False

    def check_no(self, value: Union[str, List[str]], _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        pass

    def __getattr__(self, item):    # todo: apply
        pass


# =====================================================================================================================
class ReqCheckStr_Os(ReqCheckStr_Base):
    _GETTER: Callable = platform.system
    Linux: bool
    Windows: bool


# =====================================================================================================================
class ReqCheckStr_Arch(ReqCheckStr_Base):
    _GETTER: Callable = platform.machine
    AMD64: bool      # standard PC
    x86_64: bool     # wsl standard
    AARCH64: bool    # raspberry    ARM!


# =====================================================================================================================
