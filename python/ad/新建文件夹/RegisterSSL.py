#!/usr/bin/python
import ldap
import sys

if len (sys.argv) != 3:
    print "Usage: RegisterSSL.py course student"
    print "Eg: RegisterSSL.py ant student1"
    sys.exit(1)
ldap.set_option (ldap.OPT_PROTOCOL_VERSION, ldap.VERSION3)
ldap.set_option (ldap.OPT_X_TLS_CACERTFILE, "nldapcacert.pem")
#alternative: TLS_CACERT /etc/certs/nldapcacert.pem 
#in /etc/openldap/ldap.conf 
c = ldap.initialize ("ldaps://www.nldap.com:636")
c.simple_bind_s("cn=admin, ou=subldap, ou=user, o=novell",
  "secret")
c.modify_s ("cn=" + sys.argv[1] + ", " + "ou=200201," +   
   "ou=courses, ou=zoology, ou=subldap, ou=user, o=novell",
   [(ldap.MOD_ADD, "member", "cn=" + sys.argv[2] + "," +
   "ou=students, ou=zoology, ou=subldap, ou=user, o=novell")])
c.unbind_s()
