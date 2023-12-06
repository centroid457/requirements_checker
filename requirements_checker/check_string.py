from typing import *
import platform


# =====================================================================================================================
# TODO: finish check_not__ with __getattr__
# TODO: add check__ with __getattr__
# TODO: use samples as DICT with acceptance!


# =====================================================================================================================
class Exx_RequirementCantGetActualValue(Exception):
    """
    """


class Exx_Requirement(Exception):
    """Some of the requirements are not match
    """


# =====================================================================================================================
class ReqCheckStr_Base:
    """Base class for check exact requirement by string sample

    VARIANTS for check
    ------------------
    add attributes with bool samples (case-insensitive)
        - True - if sample is definitely acceptable - Always need at least one True!!!
        - False - if not definitely acceptable
        - None - if requirement is undefined

    SETTINGS
    --------
    :ivar _RAISE: raise in case of inacceptance
    :ivar _MEET_TRUE: you can use requirement class for check only false variant
    :ivar _CHECK_FULLMATCH:
        True - if need fullmatch (but always case-insensitive)
        False - if partial match by finding mentioned samples in _sample_actual

    :ivar _GETTER: function which will get the exact sample to check
    :ivar _sample_actual:
    """
    # settings vital -------------------------------------
    _GETTER: Callable[..., str] = None

    # settings aux ---------------------------------------
    _RAISE: bool = True
    _MEET_TRUE: bool = True
    _CHECK_FULLMATCH: bool = True

    _check_is__MARKER: str = "check_is__"
    _check_is_not__MARKER: str = "check_is_not__"

    # temporary ------------------------------------------
    _sample_actual: Optional[str] = None

    def __init__(self):
        self.check()

    def _sample_actual__get(self) -> Union[str, NoReturn]:
        if not self._GETTER:
            msg = f"[ERROR] incomplete settings [{self._GETTER=}]"
            raise Exx_RequirementCantGetActualValue(msg)

        try:
            self._sample_actual: str = self.__class__._GETTER().lower()
        except Exception as exx:
            raise Exx_RequirementCantGetActualValue(repr(exx))

        return self._sample_actual

    def check(self, samples: Union[None, str, List[str]] = None, _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        """
        :param samples: if not passed - used class settings
            if passed - used only passed values!
        """
        # SETTINGS -------------------------------------------------------
        if _raise is None:
            _raise = self._RAISE

        # VALUE ACTUAL ---------------------------------------------------
        self._sample_actual__get()

        # VALUES ---------------------------------------------------------
        if isinstance(samples, str):
            samples = [samples, ]
        if not samples:
            samples = filter(lambda name: not name.startswith("_"), dir(self))

        # WORK -----------------------------------------------------------
        for name in samples:
            try:
                name_from_obj = list(filter(lambda obj_attr: obj_attr.lower() == name.lower(), dir(self)))[0]
            except:
                continue

            acceptance: Optional[bool] = getattr(self, name_from_obj)
            name = name_from_obj.lower()
            match = (
                (self._CHECK_FULLMATCH and name == self._sample_actual)
                or
                (not self._CHECK_FULLMATCH and name in self._sample_actual)
            )
            if match:
                if acceptance is True:
                    return True
                else:
                    msg = f"[ERROR] requirement not ACCEPTABLE [{self.__class__.__name__}/{self._sample_actual=}/req={name}]"
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

    def check_is__(self, samples: Union[str, List[str]], _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        # TODO: finish!!!
        pass

    def check_is_not__(self, samples: Union[str, List[str]], _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        # TODO: finish!!! dont understand what i need here
        result = self.check(samples=samples, _raise=_raise)
        if result is True:
            return False

    def __getattr__(self, item: str):
        """if no exists attr/meth
        """
        if item.lower().startswith(self._check_is_not__MARKER):
            param_name = item[len(self._check_is_not__MARKER):]
            print(param_name)
            return lambda: self.check_is_not__(samples=param_name)
        else:
            msg = f"'{self.__class__.__name__}' object has no attribute '{item}'"
            raise AttributeError(msg)


# =====================================================================================================================
class ReqCheckStr_Os(ReqCheckStr_Base):
    _GETTER: Callable = platform.system

    check_not__LINUX: Callable
    check_not__WINDOWS: Callable
    Linux: bool
    Windows: bool


# =====================================================================================================================
class ReqCheckStr_Arch(ReqCheckStr_Base):
    _GETTER: Callable = platform.machine
    AMD64: bool      # standard PC
    x86_64: bool     # wsl standard
    AARCH64: bool    # raspberry=ARM!


# =====================================================================================================================
