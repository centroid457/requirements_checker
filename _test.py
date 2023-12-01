import os
import pytest
import pathlib
import platform
from typing import *

from clisender import *


# =====================================================================================================================
class Test:
    def test__ok(self):
        victim = CliSender()

        if "Windows" in platform.system():
            cmd_line = "ping -n 1 localhost"
        else:
            cmd_line = "ping -c 1 localhost"

        assert victim.send(cmd_line, timeout=2)
        assert victim.last_cmd == cmd_line
        assert victim.last_finished is True

        assert victim._last_exx_timeout is None
        assert bool(victim.last_stdout) is True
        assert bool(victim.last_stderr) is False
        assert victim.last_retcode == 0
        assert victim.last_finished_success


# =====================================================================================================================
