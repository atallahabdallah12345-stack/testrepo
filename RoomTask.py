#ROOM 1 
student_name = 'abdallah'
print('Student name is  ',student_name.upper())
print('The name have ',len(student_name) ,'Characters' )

#The first code word is 8 


#ROOM 2 
security_number = 29
print( security_number % 4 )
print( security_number * 2 )

#The sec code word is 1


#ROOM 3

guests = ['Ali', 'Sara', 'Lina']
guests.append('Omar')
guests.remove('Sara')
print('Our guests is :',guests)
print('We have ',len(guests) , 'guests')

#The 3rd code word is 3

#ROOM 4

odd_numbers = list(range(1 , 20 ,2))
print('The odd number list is : ',odd_numbers)
print('The first item ',odd_numbers[0])
print('The last item ',odd_numbers[-1])

#The 4th code word is 19

#ROOM 5 

squares = [value**2 for value in range(1,11)]
print('The list of squares numbers between 1 to 10 is ',squares)
print('The largest elemant is  ',max(squares))

#The 5th code word is 100

#ROOM 6
weapons = ['Sword', 'Bow', 'Shield']
weapons_copy = weapons[:]
weapons_copy.append('Axe')
print('The original list is :' , weapons)
print('The copied list is :' ,weapons_copy)
print('The leangth of the original is :' , len(weapons))
print('The leangth of the copied is :' , len(weapons_copy))

#The 6th code word is 3

#ROOM 7
cities = [
 'Gaza','Nablus','Jerusalem','Ramallah','Hebron','Bethlehem'
]
print('The first 3 cities is : ',cities[:3])
print('The middle two cities is : ',cities[2:4])
print('The last 3 cities is : ',cities[-3:])

#The 7th code word is 3 

#ROOM 8 
lock = (17 , 24 , 31)
print('The first value is : ',lock[0])
print('The middle value is : ',lock[1])
print('The last value is : ',lock[-1])

#The 8th code word is 24

#ROOM 9
grades = [88, 72, 95, 61, 78]
update = grades[:]
update.append(100)
update.sort()
print('The coppied list is : ',update)
print('The length of the updated list is : ',len(update))
result = (update[0],update[-1])
print('The tuple is : ',result)

#The 9th code word is 6 



#ROOM 1 --->  8
#ROOM 2 --->  1
#ROOM 3 --->  3
#ROOM 4 --->  19 
#ROOM 5 --->  100 
#ROOM 6 --->  3
#ROOM 7 --->  3
#ROOM 8 --->  24
#ROOM 9 --->  6