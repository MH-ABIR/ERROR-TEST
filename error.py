import os, sys, platform
bit = platform.architecture()[0]
if bit == '64bit':
    os.system(f"mv sec_69.cpython-312.so {sys.path[2]}/sec_69.cpython-312.so")
    import SARKER
else:
    sys.exit("32 bit not work")
