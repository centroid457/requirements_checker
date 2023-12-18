from typing import *
import platform


# =====================================================================================================================
# TODO: use samples as DICT with acceptance!!!!?????


# =====================================================================================================================
class Exx_RequirementCantGetActualValue(Exception):
    """
    """


class Exx_Requirement(Exception):
    """Some of the requirements are not match
    """


# =====================================================================================================================
class GetattrClassmethod_Meta(type):
    """ability to apply classmethod for __getattr__

    WHY USE IT
    ==========
    cause of direct __getattr__ usage - is not applicable!

        class Cls:
        @classmethod
        def __getattr__(cls, item):
            print(item)

        Cls.hello()

        # RESULT
            Cls.hello()
            ^^^^^^^^^
        AttributeError: type object 'Cls' has no attribute 'hello'
    """
    _bool_if__MARKER: str = "bool_if__"
    _bool_if_not__MARKER: str = "bool_if_not__"
    _raise_if__MARKER: str = "raise_if__"
    _raise_if_not__MARKER: str = "raise_if_not__"

    def __getattr__(cls, item):
        """if no exists attr/meth
        """
        if item.lower().startswith(cls._bool_if__MARKER.lower()):
            sample = item[len(cls._bool_if__MARKER):]
            return lambda: cls.check_is__(samples=sample, _raise=False, _reverse=False)
        elif item.lower().startswith(cls._bool_if_not__MARKER.lower()):
            sample = item[len(cls._bool_if_not__MARKER):]
            return lambda: cls.check_is__(samples=sample, _raise=False, _reverse=True)

        elif item.lower().startswith(cls._raise_if__MARKER.lower()):
            sample = item[len(cls._raise_if__MARKER):]
            return lambda: not cls.check_is__(samples=sample, _raise=True, _reverse=True) or None
        elif item.lower().startswith(cls._raise_if_not__MARKER.lower()):
            sample = item[len(cls._raise_if_not__MARKER):]
            return lambda: not cls.check_is__(samples=sample, _raise=True, _reverse=False) or None

        else:
            msg = f"META: '{cls.__name__}' CLASS has no attribute '{item}'"
            raise AttributeError(msg)


# =====================================================================================================================
class ReqCheckStr_Base(metaclass=GetattrClassmethod_Meta):
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

    def __getattr__(self, item):
        """
        apply access to not exists methods from instance! in metaclass we have only access as classmethods!
        """
        # return super().__getattr__(item)    # AttributeError: 'super' object has no attribute '__getattr__'. Did you mean: '__setattr__'?
        return GetattrClassmethod_Meta.__getattr__(self.__class__, item)

    @classmethod
    def _sample_actual__get(cls) -> Union[str, NoReturn]:
        if not cls._GETTER:
            msg = f"[ERROR] incomplete settings [{cls._GETTER=}]"
            raise Exx_RequirementCantGetActualValue(msg)

        try:
            cls._sample_actual = cls._GETTER().lower()
        except Exception as exx:
            raise Exx_RequirementCantGetActualValue(repr(exx))

        return cls._sample_actual

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

    @classmethod
    def check_is__(cls, samples: Union[str, List[str]], _raise: Optional[bool] = None, _reverse: Optional[bool] = None) -> Union[bool, NoReturn, None]:
        """
        USAGE
        =====
        1. instance method
            CLASS_NAME().check_is__("NAME", **kwargs)   # GOOD
            CLASS_NAME().check_is__<NAME>()             # GOOD

        2. classmethod without params!
            # CLASS_NAME.check_is__<NAME>(**kwargs)     # ERROR!!!
            CLASS_NAME.check_is__<NAME>()               # GOOD
        """
        # SETTINGS -------------------------------------------------------
        if _raise is None:
            _raise = cls._RAISE
        _reverse = _reverse or False

        # VALUES ---------------------------------------------------------
        if isinstance(samples, str):
            samples = [samples, ]

        # VALUE ACTUAL ---------------------------------------------------
        cls._sample_actual__get()

        # WORK -----------------------------------------------------------
        match = None
        for sample in samples:
            sample = sample.lower()
            match = (
                (cls._CHECK_FULLMATCH and sample == cls._sample_actual)
                or
                (not cls._CHECK_FULLMATCH and sample in cls._sample_actual)
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
            msg = f"[WARN] sample is not [{cls.__name__}/{cls._sample_actual=}/req={samples}]"
            print(msg)
            if _raise:
                raise Exx_Requirement(msg)
            else:
                return False


# =====================================================================================================================
class ReqCheckStr_Os(ReqCheckStr_Base):
    _GETTER: Callable = platform.system

    LINUX: bool
    WINDOWS: bool

    # DERIVATIVES --------
    bool_if__LINUX: Callable[..., bool]
    bool_if__WINDOWS: Callable[..., bool]
    bool_if_not__LINUX: Callable[..., bool]
    bool_if_not__WINDOWS: Callable[..., bool]

    raise_if__LINUX: Callable[..., Optional[NoReturn]]
    raise_if__WINDOWS: Callable[..., Optional[NoReturn]]
    raise_if_not__LINUX: Callable[..., Optional[NoReturn]]
    raise_if_not__WINDOWS: Callable[..., Optional[NoReturn]]


# =====================================================================================================================
class ReqCheckStr_Arch(ReqCheckStr_Base):
    _GETTER: Callable = platform.machine

    AMD64: bool      # standard PC
    x86_64: bool     # wsl standard
    AARCH64: bool    # raspberry=ARM!

    # DERIVATIVES --------
    raise_if_not__AARCH64: Callable[..., Optional[NoReturn]]


# =====================================================================================================================
