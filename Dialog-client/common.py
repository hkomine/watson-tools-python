#!/usr/bin/env/python
""" common.py - (C) International Business Machines 2016
 --------------------------------------------------------------
 utilities in support of multiple services
 --------------------------------------------------------------
 @author hkomine@jp.ibm.com
"""
import json
import subprocess

#
VERBOSE=True 
CURL_OPTIONS="-k"


## ###############################################################
def issueCmd(cmd):
    """ issues a command
    Args:
        cmd (str): the command to be issued 
    Yields:
        the possibly empty json object with the result
    """
    a = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = a.communicate();
    
    try:
        res = json.loads(out)
        return res
    except Exception:
        print "common.issueCmd eror:"
        print "\tcommand: %s" % cmd
        print "\toutput: %s" % out
        print "\terror: %s" % err
        res = json.loads("{\"status\":\"FAILED\"}")
        return res

################################################################
def getCurlCommand(curl_verbose):
    if curl_verbose:
        curl_command = "curl %s %s" % (CURL_OPTIONS, "-v")
    else:
        curl_command = "curl %s" % (CURL_OPTIONS)

    return curl_command

################################################################
def addCurlOption(option):
    curOption = CURL_OPTIONS
    CURL_OPTIONS = '%s %s' & (curOption, option)
