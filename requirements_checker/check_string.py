from typing import *
import platform


# =====================================================================================================================
# TODO: finish check_no with __getattr__


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
    :ivar _MEET_TRUE: you can use requirement class for check only false variant
    :ivar _CHECK_FULLMATCH:
        True - if need fullmatch (but always case-insensitive)
        False - if partial match by finding mentioned values in value actual

    :ivar _GETTER: function which will get the exact value to check
    :ivar _value_actual:
    """
    # settings vital -------------------------------------
    _GETTER: Callable = None

    # settings aux ---------------------------------------
    _RAISE: bool = True
    _MEET_TRUE: bool = True
    _CHECK_FULLMATCH: bool = True

    # temporary ------------------------------------------
    _value_actual: Optional[str] = None

    def __init__(self):
        self.check()

    def check(self, values: Union[None, str, List[str]] = None, _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        # SETTINGS -------------------------------------------------------
        if _raise is None:
            _raise = self._RAISE

        # VALUE ACTUAL ---------------------------------------------------
        if not self._GETTER:
            msg = f"[ERROR] incomplete settings [{self._GETTER=}]"
            raise Exx_RequirementCantGetActualValue(msg)

        try:
            self._value_actual: str = self.__class__._GETTER().lower()
        except Exception as exx:
            raise Exx_RequirementCantGetActualValue(repr(exx))

        # VALUES ---------------------------------------------------------
        if isinstance(values, str):
            values = [values, ]
        if not values:
            values = filter(lambda name: not name.startswith("_"), dir(self))

        # WORK -----------------------------------------------------------
        for name in values:
            try:
                name_from_obj = list(filter(lambda obj_attr: obj_attr.lower() == name.lower(), dir(self)))[0]
            except:
                continue

            acceptance: Optional[bool] = getattr(self, name_from_obj)
            name = name_from_obj.lower()
            match = (
                (self._CHECK_FULLMATCH and name == self._value_actual)
                or
                (not self._CHECK_FULLMATCH and name in self._value_actual)
            )
            if match:
                if acceptance is True:
                    return True
                else:
                    msg = f"[ERROR] requirement not ACCEPTABLE [{self.__class__.__name__}/{self._value_actual=}/req={name}]"
                    print(msg)
                    if _raise:
                        raise Exx_Requirement(msg)
                    else:
                        return False

        # RESULT -----------------------------------------------------------
        if self._MEET_TRUE:
            msg = "[ERROR] No TRUE variants MET!"
            print(msg)
            if _raise:
                raise Exx_Requirement(msg)
            else:
                return False
        else:
            return True

    def check_not(self, value: Union[str, List[str]], _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        # TODO: finish!!! dont anderstand what i need here
        result = self.check(values=value)
        if result is True:
            return False

    def __getattr__(self, item: str):
        """if no exists attr/meth
        """
        startswith_marker = "check_not_"
        if item.lower().startswith(startswith_marker):
            param_name = item[len(startswith_marker):]
            print(param_name)
            return lambda: self.check_not(value=param_name)
        else:
            msg = f"'{self.__class__.__name__}' object has no attribute '{item}' "
            raise AttributeError(msg)


# =====================================================================================================================
class ReqCheckStr_Os(ReqCheckStr_Base):
    _GETTER: Callable = platform.system

    check_not_LINUX: Callable
    check_not_WINDOWS: Callable
    Linux: bool
    Windows: bool


# =====================================================================================================================
class ReqCheckStr_Arch(ReqCheckStr_Base):
    _GETTER: Callable = platform.machine
    AMD64: bool      # standard PC
    x86_64: bool     # wsl standard
    AARCH64: bool    # raspberry=ARM!


# =====================================================================================================================
