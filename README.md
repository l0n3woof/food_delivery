# Command Line food delivery application
This is my first command line app with Django so please bear with me.

## Install requriements
```
pip -r install requirements.txt
```

## Running the App

### Commands for Hotel

#### For adding a food 
```
python manage.py add_food -f "food_name" -d "Food description"
```
Description is optional here and remember to put them in double quotes ("").

#### To view the menu
```
python manage.py menu
```

#### For deleting a food item
Using the menu you can get the food serial number and then use it to delete the food
```
python manage.py delete_food -i 1
```
Here 1 can be replaced by any id you want to delete
 
#### Checking the order that needs to be delivered 
```
python manage.py deliver_order
```
#### To mark an order as delivered
```
python manage.py delivered -i 1
```
You must have got the trend by now.
 
### Commands for Customer
 
#### To view the menu
```
python manage.py menu
```

#### To view description of a food
```
python manage.py description -i 4
```

#### To add items to your cart 
```
python manage.py cart -o "2,4"
```
or 
```
python manage.py cart -o "2"
```
if you are entering more than 1 item than please seperate it by comma (,).
You will get a order id that you need to remember to check your order and do payments.

#### To check items in your cart
```
python manage.py view_cart -i 1
```

#### To checkout and pay for your order 
```
python manage.py checkout -i 2
```

#### To check your order details
```
python manage.py order_details -i 2
```
