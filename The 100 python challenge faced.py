def multi():
    l=[]
    for num in range (2000,3200):
        if num%7==0 and num%5!=0:
            l.append(str(num))
    return ','.join(l)

def factorial(nums):
    l=[]
    for num in nums:
        if num == 1:
            l.append (str(num))
        elif num ==0:
            l.append(str(1))
        elif num != 1:
            fac=1
            while num != 1:
                fac*= num
                num-=1
            l.append(str(fac))
    return ','.join(l)

def square(num):
    l={}
    for i in range (1, num+1):
        l[i]= i*i
    return l

def change_format():
    value=input('Enter the numbers')
    l=value.split(',')
    print (l)
    print (tuple(l))

#failed
class stringer():
    def __init__(self):
        acc=''

    def get_string(acc):
        acc=input('Hey yoo what are you wiating for...')
        return acc
    def print_string(acc):    
        for key in string:
            acc+=key
        print(acc)
def testa():
    test=stringer()
    test.get_string()
    test.print_string(acc)



class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s =input('Yoo enter the string:')

    def printString(self):
        print (self.s.upper())
def test():
    strObj = InputOutString()
    strObj.getString()
    strObj.printString()


def calc():
    import math
    C=50
    H=30
    D=input('enter the numbers:')
    D=D.split(',')
    l=[]
    for num in D:
        Q = math.sqrt((2 * C * int(num))/H)
        l.append(Q)
    return l


def matrix(c,r):
    BiG=[] 
    for i in range(0,c):
        sl=[]
        for v in range (0, r):
            sl.append(v*i)
        BiG.append(sl)
    return BiG

def sorter():
    items=input('Here come the moon:')
    items=items.split(',')
    items.sort()
    print(','.join(items))
    return

def upper_case():
    sentence=input('Dude just enter the facinating sentence:')
    sent=''
    for letter in sentence:
        sent+=(str(letter)).upper()
    print(sent)

def main():
    s = input()
    words = [word for word in s.split(" ")]
    print (" ".join(sorted(list(set(words)))))
    
#Good work for today!!!     
#11 next



def binary():
    binary_nums=input('Enter the binary numbers:')
    lista=binary_nums.split(',')
    ','.join(lista)
    print(lista)
    digital_list=[]
    binary_list=[]
    for num in lista:
        digital_num=0
        i=1
        for digit in num:
            digital_num+=(int(digit))*(2**((len(num))-i))
            i+=1
        digital_list.append(digital_num)
        if digital_num%5==0:
            binary_list.append(num)
    print(digital_list)
    print(binary_list)


def all_even():
    lista=[]
    for num in range(1000,3001):
        i=0
        for j in range(4):
            if (num//(10**j))%2==0:
                i+=1
        if i==4:
            lista.append(num)
    print(lista)

#or you can do it this way
def easy():
    values = []
    for i in range(1000, 3001):
        s = str(i)
        if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
            values.append(s)
    print (",".join(values))



#Oh got no idea for this
def counter():
    s = input('here you go enter your shit:')
    d={"DIGITS":0, "LETTERS":0}
    for c in s:
        if c.isdigit():
            d["DIGITS"]+=1
        elif c.isalpha():
            d["LETTERS"]+=1
        else:
            pass
    print ("LETTERS:", d["LETTERS"])
    print ("DIGITS:", d["DIGITS"])




def case_counter():
    s = raw_input()
    d={"UPPER CASE":0, "LOWER CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER CASE"]+=1
        elif c.islower():
            d["LOWER CASE"]+=1
        else:
            pass
    print ("UPPER CASE:", d["UPPER CASE"])
    print ("LOWER CASE:", d["LOWER CASE"])



def substitution():
    lista=[]
    string=''
    num=input('Enter the size:')
    equation='a'*int(num)
    value=input('Enter your number:')
    for i in equation:
        if  i=='a':
            string+=(value)
            lista.append(int(string))
    print(lista)
    print(sum(lista))
    print(string)


#didnt worked this  time :(

def ans():
    a =input('Enter your number')
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print (n1+n2+n3+n4)

#Guess what I fixed it the next day!


def odd_square():
    values =input('Enter the numbers dummy')
    numbers = [x for x in values.split(",") if int(x)%2!=0]
    print (",".join(numbers))
        
def odd_square2():
    values =input('Enter the numbers smarty')
    string=''
    numbers=values.split(',')
    for num in numbers:
        if int(num)%2!=0:
            string+=num
    print(','.join(string))
            
            

def banker():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation=="D":
            netAmount+=amount
        elif operation=="W":
            netAmount-=amount
        else:
            pass
    print (netAmount)
#used some help :)



def correct_password():
    passwords=input('Enter the bunch of passwords:')
    valid=''
    valid_list=[]
    pasword=passwords.split(',')
    for password in pasword:
        lenght_counter=0
        lowercase_counter=0
        uppercase_counter=0
        char_counter=0
        num_counter=0
        for key in password:
            lenght_counter+=1
            if key.isupper():
                uppercase_counter+=1
            elif key.islower():
                lowercase_counter+=1
            elif key.isdigit():
                num_counter+=1
            elif key in ('@','#','$'):
                char_counter+=1
        if (lowercase_counter,uppercase_counter,char_counter,
            num_counter)>=(1,1,1,1) and (6< lenght_counter <13):
            valid+=password+','
            valid_list.append(password)
    print(valid)
    print(','.join(valid_list))


def correct_password2():
    import re
    value = []
    items=[x for x in raw_input().split(',')]
    for p in items:
        if len(p)<6 or len(p)>12:
            continue
        else:
            pass
        if not re.search("[a-z]",p):
            continue
        elif not re.search("[0-9]",p):
            continue
        elif not re.search("[A-Z]",p):
            continue
        elif not re.search("[$#@]",p):
            continue
        elif re.search("\s",p):
            continue
        else:
            pass
        value.append(p)
    print (",".join(value))
#What is re(re.search)
#I think its searching for it in the given list



def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

    for i in reverse(100):
        print (i)

    
#niether worked nor understood
#my turn


def multiple_7(n):
    lista=[]
    for num in range(0,n):
        if num%7==0:
            lista.append(num)
    return(lista)


def sort_them():
    lista=[]
    while True:
        info=input('')
        if not info:
            break
        lista.append(tuple(info.split(',')))
    print(sorted(lista))
        
        

def where_are_you():
    import math
    hor=0
    ver=0
    while True:
        movement=input('')
        movement=movement.split(' ')
        print(movement)
        if movement[0]=='UP':
            ver+=int(movement[1])
        elif movement[0]=='DOWN':
            ver-=int(movement[1])
        elif movement[0]=='RIGHT':
            hor+=int(movement[1])
        elif movement[0]=='LEFT':
            hor-=int(movement[1])
        else:
            distance= math.sqrt((hor**2)+(ver**2))
            break
    print((distance//0.0001)/10000,',',int(distance))
#With different input method
#fixed works with right module
    



def where_are_you_orig():
    import math
    pos = [0,0]
    while True:
        s = input()
        if not s:
            break
        movement = s.split(" ")
        print(movement)
        direction = movement[0]
        steps = int(movement[1])
        if direction=="UP":
            pos[0]+=steps
        elif direction=="DOWN":
            pos[0]-=steps
        elif direction=="LEFT":
            pos[1]-=steps
        elif direction=="RIGHT":
            pos[1]+=steps
        else:
            pass

    print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))



#Question 22
#Level 3
#no idea
def freq():
    freq = {}   # frequency of words in text
    line = input()
    for word in line.split():
        freq[word] = freq.get(word,0)+1

    words = freq.keys()
    words.sort()

    for w in words:
        print ("%s:%d" % (w,freq[w]))


#have to build the frequency counter on ma own
def freq2():
    sent=input('Enter the thing:')
    lista=sent.split(' ')
    words={} #'keys' are the first elements in a dict
             #and 'values' are second ones
    # keys and values are iterated over in the same order
    
    for i in lista:
        freq=0
        for j in lista:
            if j==i:
                freq+=1
        words[i]=freq
    l=sorted(words)
    print(words)
    for k in l:
        print(k,':',words[k])
        iter(words)
    return '''returns the frequency of a word in any group of words'''



#24            
def doc():
    print(freq2.__doc__)
    print(abs.__doc__)
    print(input.__call__)
    print(input.__doc__)
    print(abs.__class__)
    return '''its great just to write'''



def mesher():
    class Person:
        # Define the class parameter "name"
        name = "Person"
        
        def __init__(self, name = None):
            # self.name is the instance parameter
            self.name = name

    jeffrey = Person("Jeffrey")
    print ("%s name is %s" % (Person.name, jeffrey.name))

    nico = Person()
    nico.name = "Nico"
    print ("%s name is %s" % (Person.name, nico.name))
    print ('%s name is %s' % (jeffrey.name, Person.name))

          
#It didn't workout but I will understand it later
#Guess what it worked
    

def sumoftwo(num1,num2):
    sum= num1+num2
    return sum


def stringer(integer):
    return str(integer)




def conc():
    str1=input('Enter string:')
    str2=input('Enter another string:')
    concat=str1+str2
    return concat


def comp(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(s1)
    elif len1 < len2:
        print(s2)
    else:
        print(s1)
        print(s2)


def printDict():
	d=dict()
	d['one']=1
	d['two']=2**2
	d['three']=3**2
	print (d)


	

def print_only_value():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print (v)
def print_only_key():
	d=dict()
	for i in range(1,21):
		d[i]=i**2
	for (k,v) in d.items():	
		print (k)
	#or
	'''for k in d.keys():	
		print k'''
	


def print_first_List():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[:5])
	#will print the frist five elements
def print_last_List():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[-5:])
	#will print the last five elements





def filter_it():
    li = [1,2,3,4,5,6,7,8,9,10]
    evenNumbers = filter(lambda x: x%2==0, li)
    print (evenNumbers)
#can filter even numbers in a list by using filter function
def map_it():
    li = [1,2,3,4,5,6,7,8,9,10]
    squaredNumbers = map(lambda x: x**2, li)
    print (squaredNumbers)
# can map() to make a list whose elements are square of elements
def map_filt():
    li = [1,2,3,4,5,6,7,8,9,10]
    evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
    print (evenNumbers)
#can map() and filter() to make a list whose elements are square of even number
























            
                
    















































