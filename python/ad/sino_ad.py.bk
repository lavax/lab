#!/usr/bin/python
# -*- coding:utf-8 -*

import sys 
import os
import logging
import time
import ldap
import ldap.sasl

'''
    测试ldap
'''

reload(sys)
sys.setdefaultencoding('gbk')

class ADService:
    LDAP_USER = "xiongyuehua@sldev.com"
    LDAP_PASSWORD = "Sinolife2008"
    LDAP_URL = "ldap://192.168.0.163"
    LDAP_SSL_URL = "ldaps://192.168.0.163:636"
    LDAP_BASE_DN = "DC=sldev,DC=com"

    ACCOUNTDISABLE=2
    PASSWD_NOTREQD=32
    NORMAL_ACCOUNT=512
    DONT_EXPIRE_PASSWORD=65536
    PASSWORD_EXPIRED=8388608

    def __init__(self,ldapUrl=LDAP_SSL_URL,ldapUser=LDAP_USER,ldapPassword=LDAP_PASSWORD,ldapBaseDN=LDAP_BASE_DN):
        self.ldapUrl=ldapUrl
        self.ldapUser=ldapUser
        self.ldapPassword=ldapPassword
        self.ldapBaseDN=ldapBaseDN
        if os.path.isfile("D:\\workspace\\python\\163.cer"):
            print "cer file is ok!!!"
        ldap.set_option (ldap.OPT_PROTOCOL_VERSION, ldap.VERSION3)
        # 如果是ldaps, 需要指定CA cert file
        ldap.set_option(ldap.OPT_X_TLS_CACERTFILE, "D:\\workspace\\python\\1632.cer")
        # 如果是self-signed cert, 加上这行
        ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
        self.conn = ldap.initialize(ldapUrl)
        self.conn.protocol_version = ldap.VERSION3
        try:
            #self.conn.start_tls_s()
            #self.conn.bind_s(ldapUser,ldapPassword)
            self.conn.simple_bind_s(ldapUser,ldapPassword)
            #auth_tokens = ldap.sasl.digest_md5(ldapUser,ldapPassword)
            #self.conn.sasl_interactive_bind_s( "", auth_tokens )
            logging.info(ldapUrl+" connected.")
        except ldap.LDAPError, e:
            logging.critical("ADService init failed.")
            if type(e.message) == dict and e.message.has_key('desc'):
                logging.critical("Error message=%s" % e.message['desc'])
            logging.critical(e)
            exit()


    def __del__(self):
         self.conn.unbind_s()
         del self.conn 
         print (self.ldapUrl+" connection released.") 

    def validateUser(self,uid,pwd):
        user=uid[:uid.find('@')]
        print "user=%s" % user
        l = ldap.initialize(ADService.LDAP_URL)
        try:
            l.protocol_version = ldap.VERSION3
            print uid,pwd
            l.simple_bind_s(uid,pwd)
 
            searchScope  = ldap.SCOPE_SUBTREE
            searchFiltername = "sAMAccountName"
            retrieveAttributes = None
            
            searchFilter = '(' + searchFiltername + "=" + user +')'
 
            ldap_result_id = l.search(self.LDAP_BASE_DN, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = l.result(ldap_result_id,1)
            print result_data
        except ldap.LDAPError, e:
            print e
            return 0, ''
        finally:
            l.unbind()
            del l

    def changePassword(self,uid, newpwd):
        # 要修改密码的dn
        dn = 'cn=%s,cn=Users,dc=sldev,dc=com' % uid
        try:
            mod_attrs = [(ldap.MOD_REPLACE, "unicodePwd",newpwd)]  
            print newpwd
            print repr(newpwd)
            #mod_attrs = [(ldap.MOD_REPLACE, "sn","xxxxxxx")]  
            self.conn.modify_s(dn, mod_attrs)  
            ##p=newpwd. 
            ## Some place-holders for old and new values
            #old = {'unicode':'User object for replication using slurpd'}
            #new = {'description':'Bind object used for replication using slurpd'}
            #
            ## Convert place-holders for modify-operation using modlist-module
            #ldif = modlist.modifyModlist(old,new)
            #
            ## Do the actual modification 
            #l.modify_s(dn,ldif)
            #self.conn.passwd_s(dn, oldpwd, newpwd)
            logging.info("Change password successfully! %s" % uid)
        except ldap.LDAPError, error_message:
            logging.error("Change password failed. %s" % dn)
            logging.error(error_message)


    def searchUserByAccountName(self,userName):
        baseDN = self.ldapBaseDN    
        searchScope  = ldap.SCOPE_SUBTREE
        searchFiltername = "sAMAccountName"
        retrieveAttributes = None
        searchFilter = '(' + searchFiltername + "=" + userName +')'
        try:    
            ldap_result_id = self.conn.search(baseDN, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = self.conn.result(ldap_result_id,1)
        except ldap.LDAPError, e:
            logging.error(e)
            raise e
        logging.debug("searchByAccountName.result_type=%d" % result_type)
        logging.debug("searchByAccountName.result_data=%s" % result_data)
        return result_type,result_data


    def addUser(self,dn,attrs):
        x=self.conn.add_s(dn, attrs) 
        print x
        logging.info("%s added." % dn)
        return x

    def disableUser(self,user):
        pass

    def deleteUser(self,dn):
        x=self.conn.delete_s(dn) 
        print x
        logging.info("%s has deleted." % dn)
        return x

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARNING)
    ad = ADService()
    '''
    stime=time.time()
    logging.debug("start="+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(stime)))
    #ad.searchByAccountName()
    #t,rs=ad.searchUserByAccountName("liuhaidong")
    etime=time.time()
    logging.debug("end="+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(etime)))
    runTime = etime-stime
    logging.debug("run time=%d" % runTime)
    #if rs == []:
    #    print "ok"
    uid='gaozhihao'
    userMail=uid+'@sino-life.com'
    dn='CN=%s,CN=Users,DC=sldev,DC=com' % name
    attrs={'objectClass': ['top','person','organizationalPerson','user'],
    'cn': [name],
    'displayName': [name],
    'memberOf': ['CN=uat-users,CN=Users,DC=sldev,DC=com','CN=confluence-users,CN=Users,DC=sldev,DC=com','CN=jira-users,CN=Users,DC=sldev,DC=com'] ,
    'name': [name],
    'primaryGroupID': ['513'] ,
    'sAMAccountName': [uid] ,
    'sAMAccountType': ['805306368'] ,
    'userPrincipalName': [userMail] ,
    'objectCategory': ['CN=Person,CN=Schema,CN=Configuration,DC=sldev,DC=com'] ,
    'mail': [userMail]} 
    '''
    uid='gaozhihao'
    sAMAccountName=uid
    userAccountControl=ADService.ACCOUNTDISABLE+ADService.PASSWD_NOTREQD+ADService.NORMAL_ACCOUNT+ADService.DONT_EXPIRE_PASSWORD
    userPassword='Sinolife2008'.encode('utf-8')
    print userPassword
    userPrincipalName='%s@sldev.com' % uid
    name=uid
    sn='gao' #first name
    givenName='zhihao'
    displayName='高志皓'.encode('utf-8')
    
    print displayName
    mail='%s@sino-life.com' % name
    title='title'   #职务
    userPassword='123'
    postalCode='518000'
    postalAddress='postalAddress'
    homePostalAddress='homePostalAddres'
    pager='pager'
    homePhone='homePhone'
    telephoneNumber='telephoneNumber'
    mobile='mobile'
    l='l'   #city
    o='o'
    st='st' #province
    ou='ou'
    destinationIndicator='destinationIndicator'
    dn='CN=%s,CN=Users,DC=sldev,DC=com' % name
    attrs = [('cn', [name]), 
             ('userPrincipalName', [userPrincipalName]),
             ('sAMAccountName', [sAMAccountName]),
             #('userPassword', [userPassword]),
             ('userAccountControl', [str(userAccountControl)]),
             #('unicodePwd', [userPassword]),
             ('sn', [sn]),
             ('givenName', [givenName]),
             ('displayName',[displayName]),
             ('objectClass', ['top', 'person','organizationalPerson', 'user']),
             ('uid', [uid]),
             ('title', [title]),
             ('facsimileTelephoneNumber', [telephoneNumber]),
             ('userPassword', [userPassword]),
             ('postalCode', [postalCode]),
             ('mail', [mail]),
             ('postalAddress',  [postalAddress]),
             ('homePostalAddress', [homePostalAddress]),
             ('pager', [pager]),
             ('homePhone', [homePhone]),
             ('telephoneNumber', [telephoneNumber]),
             ('mobile', [mobile]),
             ('l', [l]),
             ('o', [o]),
             ('st', [st]),
             ('ou', [ou]),
             ('destinationIndicator', [destinationIndicator]),
             #('active',['TRUE']) 
            ]
    #print dn,attrs
    if sys.argv<2:
        ad.addUser(dn,attrs)
        ad.deleteUser(dn)
    elif sys.argv[1] == 'vad':
        ad.validateUser('gaozhihao@sldev.com','Sinolife2008')
    elif sys.argv[1] == 'add':
        ad.addUser(dn,attrs)
    elif sys.argv[1] == 'del':
        ad.deleteUser(dn)
    elif sys.argv[1] == 'pwd':
        ad.changePassword("gaozhihao","\"Sinolife2008\"".encode('UTF-16-LE'))
    elif sys.argv[1] == 'qry':
        t,result_data=ad.searchUserByAccountName("gaozhihao")
        #print result_data[0][0]
        #print type(result_data[0][1])
        #print result_data[0][1]['sn']
        for r in result_data[0][1].items():
            print r
        for x in result_data[0][1]['sn']:
            print x.decode('utf8')
        #\xe6\xb5\xb7\xe4\xb8\x9c 
        #for key,value in result_data[1].items():
        #    print 'key=%s,value=%s' % (key,value)
