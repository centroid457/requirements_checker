from typing import *


# =====================================================================================================================
# TODO:


# =====================================================================================================================
class Exx_RequirementCantGetActualValue(Exception):
    """
    """


class Exx_Requirement(Exception):
    """Some of the requirements are not match
    """


# =====================================================================================================================
class ReqCheckStr_Base:
    """Base class for check exact requirement

    VARIANTS for check
    ------------------
    add attributes with bool values (case-insensitive)
        - True - if value is definitely acceptable
        - False - if not definitely acceptable
        - None - if requirement is undefined

    SETTINGS
    --------
    :ivar _RAISE: raise in case of inacceptance
    :ivar _CHECK_FULLMATCH:
        True - if need fullmatch (but always case-insensitive)
        False - if partial match by finding mentioned values in value actual

    :ivar _GETTER: function which will get the exact value to check
    :ivar VALUE_ACTUAL:
    """
    _GETTER: Callable = None
    _RAISE: bool = True
    _CHECK_FULLMATCH: bool = True
    VALUE_ACTUAL: Optional[str] = None

    def __init__(self):
        self.check()

    def check(self) -> Union[bool, NoReturn]:
        if not self._GETTER:
            msg = f"[ERROR] incomplete settings [{self._GETTER=}]"
            raise Exx_RequirementCantGetActualValue(msg)

        try:
            value = self.__class__._GETTER()
            self.VALUE_ACTUAL: str = value.lower()
        except Exception as exx:
            raise Exx_RequirementCantGetActualValue(repr(exx))

        for name in dir(self):
            if name.startswith("_"):
                continue
            acceptance: Optional[bool] = getattr(self, name)
            if isinstance(acceptance, bool):
                msg = f"[ERROR] requirement not ACCEPTABLE [{self.__class__.__name__}/{self.VALUE_ACTUAL=}/req={name}]"
                if (
                        (self._CHECK_FULLMATCH and name == self.VALUE_ACTUAL)
                        or
                        (not self._CHECK_FULLMATCH and name in self.VALUE_ACTUAL)
                ):
                    if self._RAISE:
                        raise Exx_Requirement(msg)
                    else:
                        return acceptance
        # final
        return True


# =====================================================================================================================
class ReqChecStr_Os(ReqCheckStr_Base):
    pass


# =====================================================================================================================
