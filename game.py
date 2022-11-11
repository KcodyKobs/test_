import random 
computervalue= random.randrange(1,10)
num_of_tries=0
playervalue = int(input('guess a number between 1 and 10: '))
while playervalue!=computervalue:
    num_of_tries+=1

    if num_of_tries==3:
        print ('out of tries')
    else:
        print ('try again')




#for  x in range(2):
    # if playervalue!=computervalue:
    #  playervalue = int(input('wrong guess, try again: '))
    # else:
    #     print ('You won')

#print ('you have no more tries left')