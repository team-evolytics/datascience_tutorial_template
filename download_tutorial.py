"""
The proper way to get this onto your computer is with git. However, 
I want to ensure that people that do not have git installed or are not familiar 
can easily download the tutorial hence the use of built in python.
"""


import os
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

# Replace the below with the github zip file link for your tutorial. 
#zipurl = 'https://github.com/team-evolytics/data_science_party_nlp_tutorial/archive/refs/heads/main.zip'

with urlopen(zipurl) as zipresp:
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        zfile.extractall(os.getcwd())

