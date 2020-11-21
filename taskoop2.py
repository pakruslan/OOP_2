# 1) Контактная книжка
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Создайте экземпляр класса all_contacts и передайте список
# ваших контактов:
# all_contacts = ContactList(list_of_your_contacts).
# Используйте метод search_by_name для поиска.

# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList().
# Создайте несколько контактов, используйте метод search_by_name.


# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList().
# Создайте несколько контактов, используйте метод search_by_name.


# class List:

#     def __init__(self):
#         self.all_contacts = []

#     def search_by_name(self, *name):
#         for i in name:
#             self.all_contacts.append(i.title())
#         ss = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
#         sss = set(ss)
#         print("Список совпадений: ")
#         for a in sss:
#             print("\t",a)
# class ContactList(List):

#     def __init__(self):
#         super().__init__()
# my_contacts = ContactList()
# my_contacts.search_by_name("monkey","flowers","donkey","smile","donkey","monkey","books")

# 2) Пользователи
# Создайте класс с именем User. Создайте два атрибута first_name и last_
# name, а затем еще несколько атрибутов, которые обычно хранятся в профиле пользователя.
# Напишите метод describe_user()



# class User:

#     first_name = 'Endy'
#     last_name = "Winston"
#     age = "27"
#     password = "123"
#     img = "bla-bla"
    
#     def describe_user(self):
#         self.first_name
#         self.last_name
#         self.age
#         self.password
#         self.img

#     def greet_user(self):
#         print(f'Hello mister {self.first_name} {self.last_name}')


# class Admin(User):
#     privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

#     def show_privileges(self):
#         print(Admin.dict)



# a1 = User()
# a1.describe_user()
# a1.greet_user()
# admin = Admin()
# admin.show_privileges()
# admin.first_name = 'Admin'
# admin.describe_user()
# admin.greet_user()

# 3.MEbel
# class House:
#     area = 120
#     housholdType = "Full family "
#     print("Total area of apartment " + str(area))
#     print("Type of house: Apartement")

#     def __init__(self,furniture):
#         self.all_furniture = furniture
#         self.bed = all_furniture[0]
#         self.wardrope = all_furniture[1]
#         self.table = all_furniture[2]

#     def count_area(self,b1,b2,wrd):
#         self.total_area = b1 + b2 + wrd 

#     def final_output(self):
#         self.housholdType = "Full family"
#         self.remaining_area = self.area - self.total_area
#         print("Remaining area: " + str(self.remaining_area) , "\nAll furniture: " + str(self.all_furniture))
        

# all_furniture = ["Bed", "Wardrope","Table"]
# house = House(all_furniture)
# house.count_area(2,2,7)
# print(house.final_output())



# 4.
#  def funnyString(s):
    
#     r = s[::-1]
    
#     for i in range(0, len(s)):
#         if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
#             return "Not Funny"
    
#     return "Funny"

# print(funnyString("acxz"))