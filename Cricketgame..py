title='''
        - : : Cricket India vs Australia : : -
'''
'''import random

score_list=[0,1,2,3,4,6,"wicket"]

ind=0
aus=0

for ball in range(1,7):
    print("enter to bowl...",ball)
    score=random.choice(score_list)
    
    if score=="wicket":
        print("Wicket")
        break    
    else:
        print("score",score)
        ind+=score
print("Ind",ind)
'''


import random

score_list=[0,1,2,3,4,6,"wicket"]

ind=0
aus=0

'''
                     - : India : - 
'''

for iball in range(1,7):
    print("bowl to ind :",iball)
    score_i=random.choice(score_list)

    if score_i=="wicket":
        print("Wicket :")
        break
    else:
        print("iball",score_i)
        ind += score_i
print("India scored:",ind)

'''
                    - : Australia : - 
'''

for aball in range(1,7):
    print("bowl  to aus: ",aball)
    score_a=random.choice(score_list)

    if score_a=="wicket":
        print("wicket")
        break
    else:
        print("aball",score_a)
        aus += score_a
print("Aus scored :",aus)

if ind>aus:
    print("India Won")
else:
    print("Australia Won")

