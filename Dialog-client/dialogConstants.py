# dialogConstants.py - (C) International Business Machines 2016
""" constants and corresponding utility routines for the Watson Dialog Service
@author hkomine@jp.ibm.com
"""

# CREDENTIALS - fill with the "username" and "password" from the "Service Credentials"
USERNAME="{username}"
PASSWORD="{password}"
DIALOG_ID="{dialog_id}"

# SERVICE URL - fill with the "url" from the "Service Credentials"
SERVICE_URL="https://gateway.watsonplatform.net/dialog/api"

# SERVICE VERSION
VERSION="v1"

## ################################################################
def getDialogId():
    """ return dialog_id
    """
    return DIALOG_ID

## ################################################################
def getUsernameAndPW():
    """ returns username and password separated by a colon and preceded by "-u",  used to construct cURL requests.
    
    Yields:
       a str with "-u" followed by the username, followed by a colon, followed by  the password
    """
    userNameAndPw = "-u %s:%s" % (USERNAME, PASSWORD)
    return userNameAndPw

## ################################################################
## @return the url and command

def getUrlAndCommand(dialog_id, cmd):
    """ builds and returns the full URL for the command based on the specific command and the URL of the service.

    Args:
      cmd (str): the actual command, which appears  after the "https://..../VERSION/" in the request,
      e.g.: "solr_clusters"    

    Yields:
       the full URL for the command 
    """
    # override dialog_id if empty
    if dialog_id == '':
        dialog_id = DIALOG_ID

    urlAndCmd="%s/%s/dialogs/%s/%s" % (SERVICE_URL, VERSION, dialog_id, cmd)
    return urlAndCmd

## ################################################################
## @return the url

def getUrl():
    """ builds and returns the full URL for the command based on the specific command and the URL of the service.

    Args:
      cmd (str): the actual command, which appears  after the "https://..../VERSION/" in the request,
      e.g.: "solr_clusters"    

    Yields:
       the full URL for the command 
    """
    urlAndCmd="%s/%s/dialogs" % (SERVICE_URL, VERSION)
    return urlAndCmd