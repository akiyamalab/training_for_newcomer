

set -ex



f2py -h
python -c "import numpy; numpy.show_config()"
export OPENBLAS_NUM_THREADS=1
pytest -ra -vv -n auto --pyargs numpy -k "not slow and not (_not_a_real_test or test_configtool_pkgconfigdir)" --durations=50 --durations-min=1.0
exit 0
