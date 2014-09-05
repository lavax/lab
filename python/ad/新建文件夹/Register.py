#!/usr/bin/python

import ldap
import sys

if len (sys.argv) != 3:
    print "Usage: Register.py course student"
    print "Eg: Register.py ant student1"
    sys.exit(1)

ldap.set_option (ldap.OPT_PROTOCOL_VERSION, ldap.VERSION3)
c = ldap.initialize ("ldap://www.nldap.com:389")
c.simple_bind_s("cn=admin, ou=subldap, ou=user, o=novell","secret")
c.modify_s ("cn=" + sys.argv[1] + ", " + "ou=200201, ou=courses, " 
   + "ou=zoology, ou=subldap, ou=user, o=novell", 
   [(ldap.MOD_ADD, "member", "cn=" + sys.argv[2] + "," + 
   "ou=students, ou=zoology, ou=subldap, ou=user, o=novell")])
c.unbind_s()

