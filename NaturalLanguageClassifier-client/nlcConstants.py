R'''
constants and corresponding utility routines for the Watson Natural Language Classifier Service
Created on 2016/05/17

@author: hkomine
'''

# CREDENTIALS - fill with the "username" and "password" from the "Service Credentials"
URL="https://gateway.watsonplatform.net/retrieve-and-rank/api"
USERNAME="<USERNAE for NLC service instance>"
PASSWORD="<PASSWORD for NLC service instance>"

def getUsername():
    return USERNAME

def getPassword():
    return PASSWORD

def getUrl():
    return URL
