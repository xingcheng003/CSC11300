#Final project by Xingcheng Zhang
#Date: 12/24/17
#Prof.Yuksel

#Question 1:
class soldier():
    def setKey(self):# To determine the how many soldiers
        k = int(input("The Josephus Problem for n = "))
        global key
        if k > 0 and k<=1000:#soldiers range
            key = k
        else:
            print("Maximum soldiers are 1000, minimum soldier is 1")
            return self.setKey()
        return key
    def initialPosition(self):#find the position to start with a specific soldier
        ip = int(input("initial position i =  "))
        if ip > key:
            print("There is not exist such soldier, try again! ")
            return self.initialPosition()
        return ip

    def NewList(self):#re-arrange the cycle, make the soldier I choose to be the first index
        list1 = []
        newIP = self.initialPosition()
        for i in range(newIP,key+1):
            list1.append(i)
        for j in range(1,newIP):
            list1.append(j)
        return list1


    def TheLongestCount(self):#base on the formula, it is 2^biggestPower + restNumber. the soldier who survive
        count=0                #will be 2 * restNumber + 1
        key1 = key
        while(key1>1):
            key1= key1/2.0
            count=count+1
            if key1 < 2:
                break
        return count

    def costFor2toThePowerOfCount(self):# find the biggest number for 2**count in order to find restNumber
        cost = 2**self.TheLongestCount()
        return cost

    def theRemainSoldier(self): # find the restNumber
        c = self.costFor2toThePowerOfCount()
        remainNumber = key - c
        return remainNumber

    def SurviveSoldier(self):# find the index of soldier who survive
        R = self.theRemainSoldier()
        survive = 2*R+1
        return survive

    def safePosition(self):# after re-arrange the list, find the index of the soldier, and find the soldier
        safe = self.NewList()
        luckyperson = self.SurviveSoldier()
        sp = safe[luckyperson-1]
        return sp

surviveSoldier = soldier()
who = surviveSoldier.setKey()
soldierName = surviveSoldier.safePosition()
print("The surviveSoldier is the number",soldierName,"soldier")




