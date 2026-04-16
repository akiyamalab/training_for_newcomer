

set -ex



test -f ${PREFIX}/lib/libopenblasp-r0.3.31.dylib
python -c "import ctypes; ctypes.cdll['${PREFIX}/lib/libopenblasp-r0.3.31.dylib']"
exit 0
