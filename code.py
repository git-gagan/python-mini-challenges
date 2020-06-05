# --------------
#Code starts here
'''def palindrome(num):
    while(num):
        num=int(num)+1
        num=str(num)
        if num[::-1]==num:
            return num

res=palindrome(13456)
print(res)'''

#Function to check for palindrome
def palindrome_check(num):
  num=str(num)
  return (num[::-1]==num)

#Function to find the smallest palindrome
def palindrome(num):
    while(1):
        num=num+1
        if palindrome_check(num):
            return num


# --------------
#Code starts here
def a_scramble(str_1,str_2):
    str_1=str_1.lower().replace(" ","")
    print(str_2)
    for i in str_2.lower():
        if i in str_1:
            str_1=str_1.replace(i,"",1)
            print(str_1)
            continue
        else:
            return False
    return True
a=a_scramble("eatcher","teacher")
print(a)


# --------------
#Code starts here
def check_fib(num):
    li=[0,1]
    for i in range(2,int(num/2)):
        li.append(li[i-1]+li[i-2])
    if num in li:
        return True
    return False

res=check_fib(377)
print(res)


# --------------
#Code starts here

#Function to compress string
def compress(word):
    word=word.lower()
    mist=[]
    l=0
    while(l<len(word)):
        m=word[l]
        j=0
        while(l<len(word) and word[l]==m):
                 j=j+1
                 l=l+1    

        mist.append(m)
        mist.append(str(j))
    
    return ''.join(mist)

#Code ends here


# --------------
#Code starts here
def k_distinct(string,k):
    s=''
    for v in string.lower():
        if v not in s:
            s+=v
            if len(s)==k:
                return True
    return False
    
res=k_distinct('Falafel',5)
print(res)


