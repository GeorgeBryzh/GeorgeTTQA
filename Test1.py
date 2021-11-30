import pytest



import sys, os

           
pathname = os.path.dirname(sys.argv[0])        

pytest1_args = [
    '--junitxml=' + os.path.abspath(pathname) + '\\Test1Result.xml','prefunc1.py', 
    
]
pytest.main(pytest1_args)

input("press on key 'Enter' to exit")







