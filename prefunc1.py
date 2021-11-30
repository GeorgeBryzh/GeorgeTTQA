
import requests

from pybase64 import b64encode as enc64

import sys, os

           
pathname = os.path.dirname(sys.argv[0])        

os.path.abspath(pathname) 

def testTask1():
 link = f"http://apimeme.com/meme?meme=Alarm-Clock&top=Top+text&bottom=Bottom+text"
 responce = requests.get(link).content
 binary1 = enc64(responce)


 with open(os.path.abspath(pathname) +f'/ForImageList/example.jpeg', 'rb') as file:
        
    binary2 = enc64(file.read())     
 
 assert binary1==binary2
 






 
    
