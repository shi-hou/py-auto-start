import sys

if sys.platform.startswith('win32'):
    from .windows import WinAutoStarter as AutoStarter
elif sys.platform.startswith('linux'):
    from .linux import LinuxAutoStarter as AutoStarter
elif sys.platform.startswith('darwin'):
    from .mac import MacAutoStarter as AutoStarter
else:
    raise Exception('Unsupported platform')

auto_starter = AutoStarter()
