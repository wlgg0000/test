
import random
secret=random.randint(1,10) #1~10之间的随机数
print('--------------------------leigege-------------------')
temp=input("caicai")
guss=int(temp)
while guss!=secret:      
        temp=input("chongxinshuru")
        guss=int(temp)
        if guss==secret:
            print("woxao")
        else:
            if(guss>secret):
                print("dale")
            else:
                print("xiaole")
print("youxijieshu")        
                    

    

