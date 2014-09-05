#!/usr/bin/python
# -*- coding:UTF-8 -*

import time
import ldap

'''
    Need install python-ldap module from:
      http://www.python-ldap.org/
    For windows OS, you can get the module from:
      http://pypi.python.org/pypi/python-ldap/
'''

ldapuser = "xiongyuehua@sldev.com";
#ldapuser = "CN=yourusername,OU=XXX,OU=XXX,DC=XXX,DC=XXXXX,DC=com"
ldappass = "Sinolife2011";
ldappath = "ldap://192.168.0.163:389";

baseDN = "DC=sldev,DC=com"

FoundResult_ServerBusy = "Server is busy"
FoundResult_NotFound = "Not Found"
FoundResult_Found = "Found"


def _validateLDAPUser(user):
    try:
        l = ldap.initialize(ldappath)
        l.protocol_version = ldap.VERSION3
        l.simple_bind(ldapuser,ldappass)

        searchScope  = ldap.SCOPE_SUBTREE
        searchFiltername = "sAMAccountName"
        retrieveAttributes = None
        searchFilter = '(' + searchFiltername + "=" + user +')'

        ldap_result_id = l.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_type, result_data = l.result(ldap_result_id,1)
        if(not len(result_data) == 0):
          print result_data
          return 1, FoundResult_Found
        else:
          return 0, FoundResult_NotFound
    except ldap.LDAPError, e:
        print e
        return 0, FoundResult_ServerBusy
    finally:
        l.unbind()
        del l

def validateLDAPUser(user, trynum =1):
    i = 0
    isfound = 0
    foundResult = ""
    while(i < trynum):
        #print "try: " + str(i)
        isfound, foundResult = _validateLDAPUser(user)
        if(isfound):
          break
        #time.sleep(60)
        i+=1
    print "-------------------------------"
    print "user is :" + user
    print "isfound :" + str(isfound)
    print "FoundResult : " + foundResult
    return isfound, foundResult

validateLDAPUser("xiongyuehua")

