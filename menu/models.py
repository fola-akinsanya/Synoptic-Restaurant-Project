from email.policy import default
from django.db import models

# Create your models here.
class MainMenu(models.Model):
    def ___str___(self):
        return self.title

    MENU_ITEMS = [
        ('Dough Balls', 'Dough Balls'),
        ('Garlic Pizza Bread ', 'Garlic Pizza Bread '),
        ('Garlic Pizza Bread with Mozzarella', 'Garlic Pizza Bread with Mozzarella'),
        ('Garlic Bread with Vegan Mozzarella ', 'Garlic Bread with Vegan Mozzarella '),
        ('Meatballs', 'Meatballs'),
        ('Mozzarella Sticks', 'Mozzarella Sticks'),
        ('Bacon & Cheese Potato Skins', 'Bacon & Cheese Potato Skins'),
        ('Cheese & Chive Fully Loaded Potato Skins ', 'Cheese & Chive Fully Loaded Potato Skins '),
        ('Mozzarella & Tomato Salad ', 'Mozzarella & Tomato Salad '),
        ('BBQ Chicken Wings ', 'BBQ Chicken Wings '),
        ('Southern Fried Chicken wih BBQ Sauce ', 'Southern Fried Chicken wih BBQ Sauce '),
        ('Sticky Hot Chicken Wings ', 'Sticky Hot Chicken Wings '),
        ('Southern Fried Chicken with Hot Sauce ', 'Southern Fried Chicken with Hot Sauce '),
        ('Classic Beef Burger ', 'Classic Beef Burger '),
        ('Double Bacon Cheese Burger ', 'Double Bacon Cheese Burger '),
        ('Classic Cheese Burger ', 'Classic Cheese Burger '),
        ('Chicken BLT Burger ', 'Chicken BLT Burger '),
        ('Vegan Burger', 'Vegan Burger'),
        ('The House Special Burger ', 'The House Special Burger '),
        ('Classic Chicken Burger ', 'Classic Chicken Burger '),
        ('Crispy BBQ Chicken Burger ', 'Crispy BBQ Chicken Burger '),
        ('Beef Lasagne ', 'Beef Lasagne '),
        ('Meatballs with Spaghetti ', 'Meatballs with Spaghetti '),
        ('Spaghetti Carbonara ', 'Spaghetti Carbonara '),
        ("Mac 'N' Cheese", "Mac 'N' Cheese"),
        ("Ultimate Mac 'N' Cheese with Bacon", "Ultimate Mac 'N' Cheese with Bacon"),
        ('Spaghetti Bolognese ', 'Spaghetti Bolognese '),
        ('Spaghetti Arrabbiata ', 'Spaghetti Arrabbiata '),
        ('Chicken & Prawn Alfredo with Spaghetti ', 'Chicken & Prawn Alfredo with Spaghetti '),
        ('10'' Pepperoni Pizza ', '10'' Pepperoni Pizza '),
        ('10'' BBQ Chicken Pizza ', '10'' BBQ Chicken Pizza '),
        ('10'' Hawaiian Pizza', '10'' Hawaiian Pizza'),
        ('10'' Vegan Margherita Pizza ', '10'' Vegan Margherita Pizza '),
        ('10'' Cajun Chicken Pizza ', '10'' Cajun Chicken Pizza '),
        ('10'' Margherita Pizza ', '10'' Margherita Pizza '),
        ('15'' Margherita Pizza ', '15'' Margherita Pizza '),
        ('15'' Cajun Chicken Pizza', '15'' Cajun Chicken Pizza'),
        ('15'' Pepperoni Pizza ', '15'' Pepperoni Pizza '),
        ('15'' BBQ Chicken Pizza ', '15'' BBQ Chicken Pizza '),
        ('15'' Hawaiian Pizza ', '15'' Hawaiian Pizza '),
        ('15'' Vegan Margherita Pizza ', '15'' Vegan Margherita Pizza '),
        ('Sweet Potato Fries ', 'Sweet Potato Fries '),
        ('Onion Rings ', 'Onion Rings '),
        ('Greens ', 'Greens '),
        ('Fries ', 'Fries '),
        ('Corn on the Cob ', 'Corn on the Cob '),
        ('Side Salad ', 'Side Salad '),
        ('Coleslaw ', 'Coleslaw '),
        ('Beans', 'Beans'),
        ('Tea', 'Tea'),
        ('Coffee', 'Coffee'),
        ('Coke', 'Coke'),
        ('Fanta', 'Fanta'),
        ('Sprite', 'Sprite'),
        ('Orange Juice', 'Orange Juice'),
        ('Water', 'Water'),
    ]

    menu_item = models.CharField(max_length=100, choices= MENU_ITEMS)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    
    image_height = models.PositiveIntegerField(default=100)
    image_width = models.PositiveIntegerField(default=100)

    def __str__(self) -> str:
        return self.menu_item

# class Starter(models.Model):

#     STARTERS = [
#         ('Dough Balls', 'Dough Balls'),
#         ('Garlic Pizza Bread ', 'Garlic Pizza Bread '),
#         ('Garlic Pizza Bread with Mozzarella', 'Garlic Pizza Bread with Mozzarella'),
#         ('Garlic Bread with Vegan Mozzarella ', 'Garlic Bread with Vegan Mozzarella '),
#         ('Meatballs', 'Meatballs'),
#         ('Mozzarella Sticks', 'Mozzarella Sticks'),
#         ('Bacon & Cheese Potato Skins', 'Bacon & Cheese Potato Skins'),
#         ('Cheese & Chive Fully Loaded Potato Skins ', 'Cheese & Chive Fully Loaded Potato Skins '),
#         ('Mozzarella & Tomato Salad ', 'Mozzarella & Tomato Salad '),
#         ('BBQ Chicken Wings ', 'BBQ Chicken Wings '),
#         ('Southern Fried Chicken wih BBQ Sauce ', 'Southern Fried Chicken wih BBQ Sauce '),
#         ('Sticky Hot Chicken Wings ', 'Sticky Hot Chicken Wings '),
#         ('Southern Fried Chicken with Hot Sauce ', 'Southern Fried Chicken with Hot Sauce '),
#     ]
#     starter = models.CharField(max_length=100, choices= STARTERS)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, default="bread.jpeg", blank=True, null=True)
#     stock = models.PositiveIntegerField(default=0)

    
#     image_height = models.PositiveIntegerField(default=100)
#     image_width = models.PositiveIntegerField(default=100)

# class Main(models.Model):
#     def ___str___(self):
#         return self.title

#     MAINS = [
#         ('Classic Beef Burger ', 'Classic Beef Burger '),
#         ('Double Bacon Cheese Burger ', 'Double Bacon Cheese Burger '),
#         ('Classic Cheese Burger ', 'Classic Cheese Burger '),
#         ('Chicken BLT Burger ', 'Chicken BLT Burger '),
#         ('Vegan Burger', 'Vegan Burger'),
#         ('The House Special Burger ', 'The House Special Burger '),
#         ('Classic Chicken Burger ', 'Classic Chicken Burger '),
#         ('Crispy BBQ Chicken Burger ', 'Crispy BBQ Chicken Burger '),
#         ('Beef Lasagne ', 'Beef Lasagne '),
#         ('Meatballs with Spaghetti ', 'Meatballs with Spaghetti '),
#         ('Spaghetti Carbonara ', 'Spaghetti Carbonara '),
#         ("Mac 'N' Cheese", "Mac 'N' Cheese"),
#         ("Ultimate Mac 'N' Cheese with Bacon", "Ultimate Mac 'N' Cheese with Bacon"),
#         ('Spaghetti Bolognese ', 'Spaghetti Bolognese '),
#         ('Spaghetti Arrabbiata ', 'Spaghetti Arrabbiata '),
#         ('Chicken & Prawn Alfredo with Spaghetti ', 'Chicken & Prawn Alfredo with Spaghetti '),
#         ('10'' Pepperoni Pizza ', '10'' Pepperoni Pizza '),
#         ('10'' BBQ Chicken Pizza ', '10'' BBQ Chicken Pizza '),
#         ('10'' Hawaiian Pizza', '10'' Hawaiian Pizza'),
#         ('10'' Vegan Margherita Pizza ', '10'' Vegan Margherita Pizza '),
#         ('10'' Cajun Chicken Pizza ', '10'' Cajun Chicken Pizza '),
#         ('10'' Margherita Pizza ', '10'' Margherita Pizza '),
#         ('15'' Margherita Pizza ', '15'' Margherita Pizza '),
#         ('15'' Cajun Chicken Pizza', '15'' Cajun Chicken Pizza'),
#         ('15'' Pepperoni Pizza ', '15'' Pepperoni Pizza '),
#         ('15'' BBQ Chicken Pizza ', '15'' BBQ Chicken Pizza '),
#         ('15'' Hawaiian Pizza ', '15'' Hawaiian Pizza '),
#         ('15'' Vegan Margherita Pizza ', '15'' Vegan Margherita Pizza '),
#     ]

#     main = models.CharField(max_length=100, choices= MAINS)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, default="bread.jpeg", blank=True, null=True)
#     stock = models.PositiveIntegerField(default=0)

    
#     image_height = models.PositiveIntegerField(default=100)
#     image_width = models.PositiveIntegerField(default=100)

#     def __str__(self) -> str:
#         return self.starter

# class DessertMenu(models.Model):
#     def ___str___(self):
#         return self.title

#     DESSERTS = [
#         ('Deep fried banana fritters', 'Deep fried banana fritters'),
#         ('Strawberry cheesecake mochi', 'Strawberry cheesecake mochi'),
#         ('Coconut and mint ice cream', 'Coconut and mint ice cream'),
#         ('Seasonal fruit salad', 'Seasonal fruit salad')
#     ]

#     dessert = models.CharField(max_length=100, choices= DESSERTS)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, default="bread.jpeg", blank=True, null=True)
#     stock = models.PositiveIntegerField(default=0)

    
#     image_height = models.PositiveIntegerField(default=100)
#     image_width = models.PositiveIntegerField(default=100)

#     def __str__(self) -> str:
#         return self.menu_item

# class SidesMenu(models.Model):
#     def ___str___(self):
#         return self.title

#     SIDES = [
#         ('Sweet Potato Fries ', 'Sweet Potato Fries '),
#         ('Onion Rings ', 'Onion Rings '),
#         ('Greens ', 'Greens '),
#         ('Fries ', 'Fries '),
#         ('Corn on the Cob ', 'Corn on the Cob '),
#         ('Side Salad ', 'Side Salad '),
#         ('Coleslaw ', 'Coleslaw '),
#         ('Beans', 'Beans'),
#     ]

#     side = models.CharField(max_length=100, choices= SIDES)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, default="bread.jpeg", blank=True, null=True)
#     stock = models.PositiveIntegerField(default=0)

#     image_height = models.PositiveIntegerField(default=100)
#     image_width = models.PositiveIntegerField(default=100)

#     def __str__(self) -> str:
#         return self.starter

# class DrinksMenu(models.Model):
#     def ___str___(self):
#         return self.title

#     DRINKS = [
#         ('Tea', 'Tea'),
#         ('Coffee', 'Coffee'),
#         ('Coke', 'Coke'),
#         ('Fanta', 'Fanta'),
#         ('Sprite', 'Sprite'),
#         ('Orange Juice', 'Orange Juice'),
#         ('Water', 'Water'),
#     ]

#     drink = models.CharField(max_length=100, choices= DRINKS)
#     price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
#     image = models.ImageField(upload_to="", height_field='image_height', width_field='image_width', max_length=100, default="bread.jpeg", blank=True, null=True)
#     stock = models.PositiveIntegerField(default=0)

#     image_height = models.PositiveIntegerField(default=100)
#     image_width = models.PositiveIntegerField(default=100)

#     def __str__(self) -> str:
#         return self.starter