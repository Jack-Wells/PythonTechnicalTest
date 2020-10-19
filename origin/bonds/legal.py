from rest_framework.exceptions import ValidationError
import requests
import os

def get_Legal_Name(lei):
    try:
        url = "https://leilookup.gleif.org/api/v2/leirecords/?lei="+lei
        name = requests.get(url).json()

        return name[0]["Entity"]["LegalName"]["$"]
    except:
        return None