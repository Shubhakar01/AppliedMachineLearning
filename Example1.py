import datetime as dt
import time as tm

def Dictionary_Example():
    x={'Tom':'tom.m@gmu.org','Bill Gates':'billg@microsoft.com'}
    print(x['Bill Gates'])
    x['Thompson']='mit@ua.edu'

    dept_stores={'Store 1':'Bangalore','Store 2':'Mangalore','Store 3':'Udupi'}
    dept_stores['Store 4']='Mysore'
    # print(dept_stores)
    for store in dept_stores:
        print(store,dept_stores[store])

    for store in dept_stores.items():
        print(store)
    for store,location in dept_stores.items():
            print(f'{store}: {location}')

def Unpacking_Example():
    x=('Tom','Michel','tom.m@gmu.org','USA')
    first_name,last_name,email,country=x
    print(country)

def String_Format_Example():
    sales_record={
        'price':3.24,
        'num_items':4,
        'person':'Tom',
        'email':'tom.m@gmu.org'}
    sales_statement='{} bought {} item(s) at a price of INR {} each for a total of {}'
    print(sales_statement.format(sales_record['person'],
                                 sales_record['num_items'],
                                 sales_record['price'],
                                 sales_record['num_items']*sales_record['price']))

    movie_record={
        'title':'Oppenheimer',
        'director':'Christopher Nolan',
        'year':2023 ,
        'star':'Cillian Murphy'}

    movie_statement='{} was directed by {} and was released in {} starring {}'
    print(movie_statement.format(movie_record['title'], movie_record['director'], movie_record['year'], movie_record['star']))

def Time_Example():
    print(tm.time())
    print("Today's Date is ",dt.date.today())
    delta=dt.timedelta(days=100)

    today=dt.date.today()
    print(today-delta)

def Set_Example():
    set1={34,'one',89,'six','y'}
    set2={1,'x','two','y','a'}
    print(set1,set2)
    set1.add('one')
    set2.remove('a')
    print(set1) 
    print(set2)

def calculateSquare(n):
    return n*n

def Mapping_Function():
     store1=[10.00,11.00,12.34,5.34]
     store2=[19.00,10.10,12.34,5.01]
     store3=[15.00,12.00,11.00,6.00]

     cheapest = map(min,store1,store2,store3)
     costly = map(max,store1,store2,store3)
     print(cheapest)

     for item in cheapest:
         print(item)

     numbers = (1,2,3,4)
     result = map(calculateSquare,numbers)
     print(result)
     list_view = list(result)
     print(list_view)

def Lambda_Function():
    numbers = (1,2,3,4)
    result = map(lambda x:x*x,numbers)
    print(result)
    list_view = list(result)
    print(list_view)

    num1= [4,5,6]
    num2=[5,6,7]
    new_result = map(lambda n1,n2:n1+n2,num1,num2)
    print(list(new_result))
    
people=['Python Programming Language','Computer Lab Test','Vinod scored A','Kumar scored']
def Split_title_and_name(person):
    title = person.split()[0]
    lastname=person.split()[-1]
    return '{} {}'.format(title,lastname)
list(map(Split_title_and_name,people))    
dx = lambda x:x*2
print(dx(5))



# Dictionary_Example()
# Unpacking_Example()
# String_Format_Example()
# Time_Example()
# Set_Example()
# Mapping_Function()
# Lambda_Function()