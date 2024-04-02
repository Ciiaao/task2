import keyword
import random
import turtle
from threading import Timer
import time
import string 

#first mission
def decrypt_clue(txt):
    
    key_words_counter=[0]*35
    key_words_list=keyword.kwlist
    for x in txt:
        for i in range(len(key_words_list)):
            if key_words_list[i] in x:
                cnt = x.count(key_words_list[i])
                key_words_counter[i]=key_words_counter[i]+cnt
    for i in range(len(key_words_list)):
        if key_words_counter[i]!=0:
            print(f'{key_words_list[i]}:{key_words_counter[i]}')


file_object=open(r"mysterious.txt","r")
decrypt_clue(file_object)

#second mission
def solve_puzzles(puzzles):
    bool_values=[]
    for x in puzzles:
        if x==0 or x==False:
            bool_values.append(False)
        else:
            try:
                if len(x)==0:
                    bool_values.append(False)
                else:
                    bool_values.append(True)
            except:
                bool_values.append(True)
    print(bool_values)


#third mission
def calculate_magic_numbers(start,end):
    cnt=end-start
    magic_num_count=random.randint(1,cnt)
    magic_nums=[]
    for i in range(magic_num_count):
        x=random.randint(0,100)
        x=x/100
        magic_number=x*(end-start)+ start
        magic_nums.append(magic_number)
    print(magic_nums)




def exam_numbers():
    
    time_out=20
    t=Timer(time_out,lambda:print("your time is over! ")) #setting timer for 20 seconds
    t.start()
    answer_list={'True':0,'False':0}
    print("You have 20 seconds to answer the decimal values:\n")
    start_time= time.time() 
    while time.time()<start_time+time_out: #setting the loop to run while timer is not finished
        binary_num=[]
        decimal_num=0
        for i in range(4): #creating binary number
            random_num=random.randint(0,1)
            binary_num.append(random_num)
        i=len(binary_num)-1 #turning binary number into decimal
        for j in binary_num:
            if j==1:
                decimal_num=decimal_num+2**i
            i=i-1
        binary_num=''.join(map(str,binary_num)) #converting binary number from a list to a string
        print(binary_num)
        answer=input()
        decimal_num=str(decimal_num) #as answer is a string,decimal value shold be converted into string too
        if answer==decimal_num:
            answer_list['True']+=1
        elif len(answer)==0: # if input is nothing or user presses enter key the answer list should not change
            pass
        else:
            answer_list['False']+=1
    t.cancel()
    print(answer_list)



def check_pass(user_pass):
    punctuation_list=list(string.punctuation)
    for x in user_pass:
        if len(x[1])>= 8: 
            for y in punctuation_list:
                if y in x[1]:
                    if x[1].isupper()==False and x[1].islower()==False:
                        print(x[0])


user_pass=[]

while 1:
    # listing usernames and passwords 
    print("enter username and password as many time as you want(enter end to stop)")
    username=input()
    if username=='end':
        break
    password=input()
    user_info=(username,password)
    user_pass.append(user_info)
check_pass(user_pass)



#forth mission
def move_turtle(obj,f,b,r,l):
    obj.forward(f)
    obj.right(r)
    obj.left(l)
    obj.backward(b)


CIAO=turtle.Turtle()
CIAO.pensize(3)
CIAO.speed(10)
CIAO.shape('turtle')
CIAO.penup()
move_turtle(CIAO,200,200,90,0)
CIAO.pendown()
move_turtle(CIAO,200,100,0,90)
move_turtle(CIAO,0,200,90,0)
CIAO.penup()
move_turtle(CIAO,0,50,0,90)
move_turtle(CIAO,0,150,0,90)
CIAO.pendown()
CIAO.right(180)
move_turtle(CIAO,50,100,0,90)
move_turtle(CIAO,0,100,0,70)
move_turtle(CIAO,0,100,25,0)
CIAO.penup()
move_turtle(CIAO,0,250,135,0)
move_turtle(CIAO,0,150,90,0)
CIAO.pendown()
CIAO.circle(10)
CIAO.penup()
CIAO.backward(20)
CIAO.pendown()
CIAO.circle(10)
CIAO.penup()
move_turtle(CIAO,200,50,120,0)
CIAO.pendown()
move_turtle(CIAO,50,110,0,70)
move_turtle(CIAO,0,150,130,0)
move_turtle(CIAO,0,150,0,90)
CIAO.left(90)
move_turtle(CIAO,100,150,0,90)
CIAO.penup()
move_turtle(CIAO,0,180,90,0)
move_turtle(CIAO,0,50,90,0)
CIAO.pendown()
CIAO.circle(10)
turtle.done()