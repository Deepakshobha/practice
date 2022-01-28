#shopping cart
# class shoppingcart:
#     def __init__(self):
#         self.cart =[]
#
#     def add_item(self,name,quantity,price):
#         self.cart.append({"name":name,"quantity":quantity,"price":price})
#
#     def total_cost(self):
#         total = sum([item['quantity'] * item['price'] for item in self.cart]) # 1st method
#         return total
#         # total = 0.0                                                      #2nd method
#         # for item in self.cart:
#         #     total = total+ (item['quantity']*item['price'])
#         # return total
#     def remove_item(self,name):
#         for item in self.cart:
#             if item['name'] == name:
#                 if item['quantity'] > 1:
#                     item['quantity'] -= 1
#                 else:
#                     self.cart.remove(item)
#
# c1=shoppingcart()
# c2=shoppingcart()
# c3=shoppingcart()
# # print(c1)
# # # print(c2)
# # # print(c3)
# # print(c1.__dict__)
# # # print(c2.__dict__)
# # # print(c3.__dict__)
# print(c1.add_item('iphone',3,800))
# # print(c1.cart)
# # print(c1.__dict__)
# print(c1.add_item('imac',1,900))
# print(c1.__dict__)
# # print(c2.add_item('iwatch',2,3000))
# # print(c2.__dict__)
# print(c1.total_cost())
# print(c1.remove_item('iphone'))
# print(c1.__dict__)




#shopping cart
class shoppingcart:
    products = {'iphone':5,'imac':3, 'pad':2}
    price = {'iphone':100,'imac':200, 'pad':300}
    def __init__(self):
        self.cart =[]

    def add_item(self,name,quantity):
        if name not in self.__class__.products:
            raise Exception('invalid product')
        elif quantity <= self.__class__.products[name]:
            self.cart.append({"name":name,"quantity":quantity,"price":self.__class__.price[name]})
            self.__class__.products[name] -= quantity
        else:
            raise ValueError("product is out of stock")

    def total_cost(self):
        total = sum([item['quantity'] * item['price'] for item in self.cart]) # 1st method
        return total
        # total = 0.0                                                      #2nd method
        # for item in self.cart:
        #     total = total+ (item['quantity']*item['price'])
        # return total
    def remove_item(self,name):
        for item in self.cart:
            if item['name'] == name:
                if item['quantity'] > 1:
                    item['quantity'] -= 1
                else:
                    self.cart.remove(item)

c1=shoppingcart()
c2=shoppingcart()
c3=shoppingcart()
# print(c1)
# # print(c2)
# # print(c3)
# print(c1.__dict__)
# # print(c2.__dict__)
# # print(c3.__dict__)
print(c1.add_item('iphone',3))
# print(c1.cart)
# print(c1.__dict__)
print(c1.add_item('imac',1))
print(c1.__dict__)
# print(c2.add_item('iwatch',2,3000))
# print(c2.__dict__)
print(c1.total_cost())
print(c1.remove_item('iphone'))
print(c1.__dict__)
print(shoppingcart.products)
print(c2.add_item('iphone',1))
print(shoppingcart.products)
print(c2.add_item('samsung',1))
print(shoppingcart.products)