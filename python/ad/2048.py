#!/usr/bin/python
# -*- coding:UTF-8 -*-


EAST='0'
SOUTH='1'
WEST='2'
NORTH='3'

#list  = [0,0,0,0]
#list  = [2,0,0,0]
#list  = [0,0,0,2]
#list  = [0,2,2,2]
#list  = [2,0,0,2]
#list  = [0,2,0,2]
#list  = [2,2,2,2]
list  = [[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]

#list  = [[2,2,4,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#list  = [[2,0,0,0],[2,0,0,0],[2,0,0,0],[2,0,0,0]]

#list  = [[2,2,2,2],[0,0,0,0],[2,2,2,2],[0,0,0,0]]


#print list


def moveAll(list1):
	list2 = []
	i=len(list1)
	for e in list1:
		if e!=0:
			list2.append(e)
			i-=1
	for j in range(0,i):
		list2.append(0)
	return list2

def addAll(list1):
	list1[0]+=list1[1]
	list1[1]=0
	list1[2]+=list1[3]
	list1[3]=0
	return list1
	
def act(l):
        ll = moveAll(l)
        ll = addAll(ll)
        ll = moveAll(ll)
        return ll

def row2col(copyList):
        
        tempRow=[]
        tempList=[]
        for j in range(0,len(copyList[0])):
                for i in range(0,len(copyList)):
                        tempRow.append(copyList[i][j])
                tempList.append(tempRow)
                #print tempList
                tempRow = []
        return tempList


def showPanel(copyList):
        for row in copyList:
                print row


showPanel(list)

direction=raw_input("input(0,1,2,3,q):")

while(direction!='q'):
        if direction == EAST:
                sortedList = []
                for row in list:
                        r=act(row)
                        r.reverse()
                        sortedList.append(r)
                list = sortedList
        elif direction == WEST:
                sortedList = []
                for row in list:
                        r=act(row)
                        sortedList.append(r)
                list = sortedList            
        elif direction == SOUTH:
                orgList=[]
                sortedList=[]
                changedList=row2col(list)
                for row in changedList:
                        r=act(row)
                        r.reverse()
                        sortedList.append(r)
                orgList=row2col(sortedList)
                list = orgList
        elif direction == NORTH:
                orgList=[]
                sortedList=[]
                changedList=row2col(list)
                for row in changedList:
                        r=act(row)
                        sortedList.append(r)
                orgList=row2col(sortedList)
                list = orgList

        showPanel(list)
        direction=raw_input("input(0,1,2,3,q):")

        


#when the direction is WEST, nothing to do 

#print list
#for row in list:
 #       r=act(row)


#l = act(list)
#print l

