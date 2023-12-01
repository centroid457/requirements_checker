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
class ReqCheckStrBase:
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
        self.check_requirement()

    def check_requirement(self) -> Union[bool, NoReturn]:
        try:
            self.VALUE_ACTUAL: str = self._GETTER().lower()
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


# =====================================================================================================================
class ReqChecStrkOs(ReqCheckStrBase):
    pass


# =====================================================================================================================
