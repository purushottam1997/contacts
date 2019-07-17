print("CONTACTS LIST")
print('1.Add a contact\n2.Delete a contact\n3.Search a contact\n4.Display the contact list\n5.update the contact list\n6.size\n7.exit')
print("Enter your choice")
choice=int(input())
my_contacts={"pro":9038,"nihu":9033}
def add():
  n=print("Enter the number of contacts to be added")
  n=int(input())
  for i in range(n):
      contact_name=input()
      contact_number=int(input())
      my_contacts[contact_name]=contact_number
  print(my_contacts)
def delete():
  print("Enter the contact name to be deleted\n")
  contact_name=input()
  if contact_name in my_contacts:
    my_contacts.pop(contact_name)
  else:
    print("No such name in the contacts list")
  print(my_contacts)
def search():
  print("Enter the name to be searched")
  contact_name=input()
  if contact_name in my_contacts:
    print(my_contacts[contact_name])
  else:
    print("No such name in the contacts list")
def display():
  print(my_contacts)
def update():
  print("Enter the contact name to be updated")
  contact_name=input()
  if contact_name in my_contacts:
    contact_number=int(input("Enter the new contact number"))
  else:
    print("No such name in the contacts list")
  my_contacts[contact_name]=contact_number
  print(my_contacts)
def size():
    print("size of contacts")
    x=len(my_contacts)
    print(x)
if choice==1:
  add()
elif choice==2:
  delete()
elif choice==3:
  search()
elif choice==4:
  display()
elif choice==5:
  update()
elif choice==6:
  size()
else:
  exit(0)
