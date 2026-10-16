#we have to create a Secreate code language which only can be understand by coder and decoder
#  CODER
#1. input, if input ke each string have <=2 cahr then use reverse kar do 
# 2. if string have >= 3 char then  
#    a. remove first char from st and add it on end
#    b. add 3 random cahr in front and back
# ex:- Shubham is good boy
#   then : - Shubham = srfhubhamSrtg
#        :- is = si
#        :- good = rkuoodgbnf
#        :- boy = ybtoybrec
# final ans = srfhubhamSrtg si rkuoodgbnf ybtoyrec

# DECODER
# spilt each String 
# 1. if string<= 2 char then simply reverse
# 2. else:
#       a. remove 3 char from st and end 
#       b. now take last char and copy or/ append it in front of string


# Code of coder
import random
random_cahr= ["fhy","hrv","ths","pce","acr","hdj", "qki","iev","pev","uiq", "xyz","azx","tce","mon","yvd"]
st = input("enter a massaage:-")
words =st.split(" ")  #Spliting every word from whole string
coding = input("1. for Codeing  or 0. for Decoding:-")
coding = True if (coding=="1") else False
print(coding)
if(coding):#True for coder and False for decoder
    nwords =[]
    for word in words:
        if(len(word)>=3):
            r1= random.choice(random_cahr)
            r2 =random.choice(random_cahr)
            stnew = r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
       

 # DECODER
else:
    nwords=[]
    for word in words:
        if (len(word)>=9):
            stnew = word[3:-3]
            stnew = stnew[-1]+ stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
print(" ".join(nwords))        