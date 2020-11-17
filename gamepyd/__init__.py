from ctypes import *
import os
import platform

if platform.architecture()[0] == '32bit':
    arc = '86'
else:
    arc = '64'

_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    'vXboxInterface-x{}'.format(arc),
    'vXboxInterface.dll'
))
_xinput = WinDLL(_path)


class MissingDependancyError(Exception):
    def __init__(self, message):
        self.message = message


if not _xinput.isVBusExists():
    raise MissingDependancyError(
        '''Unable to find VBus Controller.

For more information, refer to https://github.com/shauleiz/vXboxInterface/releases.
For a quick-fix, install ScpVBus from the PreRequisites folder (or grab a release directly
from the original repo at https://github.com/nefarius/ScpVBus/releases/tag/v1.7.1.1)

from .writePad import vController
from .readPad import rController
from ..writePad import main as test_virtual
from .readPad import main as test_read
