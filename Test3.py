import pytest
import sys, os
pathname = os.path.dirname(sys.argv[0])      
pytest3_args = [
   '--junitxml=' + os.path.abspath(pathname) + '\\Test3Result.xml', 'prefunc3.py'
]
pytest.main(pytest3_args)
input("press on key 'Enter' to exit")