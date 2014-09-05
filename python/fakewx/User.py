#!/usr/bin/python
#coding:utf-8

class User:
    uid=None
    name=None
    email=None
    def __init__(self):
        #self.uid,self.name,self.email=uid,name,email
        pass


if __name__ == "__main__":
    #usr=User('1','admin',None)
    usr=User()
    print usr.uid
    print usr.name
    print usr.email

