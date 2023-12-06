from typing import *
import platform


# =====================================================================================================================
# TODO: use samples as DICT with acceptance!!!!?????
# TODO: ref into classmethods? seems good!


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
    _MEET_TRUE: bool = False
    _CHECK_FULLMATCH: bool = True

    __check_is__MARKER: str = "check_is__"
    __check_is_not__MARKER: str = "check_is_not__"

    # temporary ------------------------------------------
    _sample_actual: Optional[str] = None

    # TODO: add values as dict??? - it would be direct great!

    def __init__(
            self,
            _getter: Callable[..., str] = None,
            _raise: Optional[bool] = None,
            _meet_true: Optional[bool] = None,
            _check_fullmatch: Optional[bool] = None
    ):
        # INIT SETTINGS ----------------------------------
        if _getter is not None:
            self.__class__._GETTER = _getter
        if _raise is not None:
            self._RAISE = _raise
        if _meet_true is not None:
            self._MEET_TRUE = _meet_true
        if _check_fullmatch is not None:
            self._CHECK_FULLMATCH = _check_fullmatch

        # WORK -------------------------------------------
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

    def check(
            self,
            # samples: Union[None, str, List[str]] = None,
            _raise: Optional[bool] = None
    ) -> Union[bool, NoReturn]:
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
        # if isinstance(samples, str):
        #     samples = [samples, ]
        # if not samples:
        samples = filter(lambda _sample: not _sample.startswith("_"), dir(self))

        # WORK -----------------------------------------------------------
        for sample in samples:
            sample = sample.lower()
            try:
                name_from_obj = list(filter(lambda obj_attr: obj_attr.lower() == sample, dir(self)))[0]
                acceptance: Optional[bool] = getattr(self, name_from_obj)
            except:
                continue

            match = (
                (self._CHECK_FULLMATCH and sample == self._sample_actual)
                or
                (not self._CHECK_FULLMATCH and sample in self._sample_actual)
            )
            if match:
                if acceptance is True:
                    return True
                else:
                    msg = f"[ERROR] requirement not ACCEPTABLE [{self.__class__.__name__}/{self._sample_actual=}/req={sample}]"
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

    def check_is__(self, samples: Union[str, List[str]], _raise: Optional[bool] = None, _reverse: Optional[bool] = None) -> Union[bool, NoReturn]:
        # SETTINGS -------------------------------------------------------
        if _raise is None:
            _raise = self._RAISE
        _reverse = _reverse or False

        # VALUES ---------------------------------------------------------
        if isinstance(samples, str):
            samples = [samples, ]

        # VALUE ACTUAL ---------------------------------------------------
        self._sample_actual__get()

        # WORK -----------------------------------------------------------
        match = None
        for sample in samples:
            sample = sample.lower()
            match = (
                (self._CHECK_FULLMATCH and sample == self._sample_actual)
                or
                (not self._CHECK_FULLMATCH and sample in self._sample_actual)
            )
            if match:
                break

        if match:
            result = not _reverse
        else:
            result = _reverse

        if result:
            return True
        else:
            msg = f"[WARN] sample is not [{self.__class__.__name__}/{self._sample_actual=}/req={samples}]"
            print(msg)
            if _raise:
                raise Exx_Requirement(msg)
            else:
                return False

    def check_is_not__(self, samples: Union[str, List[str]], _raise: Optional[bool] = None) -> Union[bool, NoReturn]:
        return self.check_is__(samples=samples, _raise=_raise, _reverse=True)

    def __getattr__(self, item: str):
        """if no exists attr/meth
        """
        if item.lower().startswith(self.__check_is__MARKER):
            sample = item[len(self.__check_is__MARKER):]
            return lambda: self.check_is__(samples=sample)
        elif item.lower().startswith(self.__check_is_not__MARKER):
            sample = item[len(self.__check_is_not__MARKER):]
            return lambda: self.check_is_not__(samples=sample)
        else:
            msg = f"'{self.__class__.__name__}' object has no attribute '{item}'"
            raise AttributeError(msg)


# =====================================================================================================================
class ReqCheckStr_Os(ReqCheckStr_Base):
    _GETTER: Callable = platform.system

    Linux: bool
    Windows: bool

    # DERIVATIVES --------
    check_is_not__LINUX: Callable[..., bool]
    check_is_not__WINDOWS: Callable[..., bool]


# =====================================================================================================================
class ReqCheckStr_Arch(ReqCheckStr_Base):
    _GETTER: Callable = platform.machine

    AMD64: bool      # standard PC
    x86_64: bool     # wsl standard
    AARCH64: bool    # raspberry=ARM!

    # DERIVATIVES --------
    check_is_not__AARCH64: Callable[..., bool]


# =====================================================================================================================
