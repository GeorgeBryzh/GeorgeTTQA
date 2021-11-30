import pytest
import sys, os
pathname = os.path.dirname(sys.argv[0])

pytest2_args = [
    '--junitxml=' + os.path.abspath(pathname) + '\\Test2Result.xml', 'prefunc2.py',
]
pytest.main(pytest2_args)
input("press on key 'Enter' to exit")