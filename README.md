# PharmiPlus

- A website which caters all the medicines for you online. 
- Medicines are sorted according to the category. 
- User Registration and Login functionality is provided.
- User can add any number of items in the cart.
- Checkout functionality is provided in which user can use home address/new address to place order.
- User Queries can also be dealt using Contact Us form.
- Admin Replies to each query of the logged in user is also provided.

Website Link: https://gunjan3103.pythonanywhere.com/shop/

## Technology Stack

***Languages->*** HTML, CSS, JavaScript, Python

***Tools and Frameworks->*** Django

***Database->*** SQLite

## How to Run the project

### Setup and Activate Virtual Environment

- For Windows
```sh
pip install virtualenv 
virtualenv myenv
myenv\Scripts\activate
```

- For Linux
```sh
pip install virtualenv
virtualenv virtualenv_name
source virtualenv_name/bin/activate
```

### Intall all requirements
```sh
pip install -r requirements.txt 
```
### Then Run Following Commands
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### To create a super user to access the django admin:
```sh
python manage.py createsuperuser   
```

## Author

👤 **Kirti Kunj Bajpai**

Interests-> Development and Data Structures and Algorithm

If you have any queries/doubts regarding the project, mail me at kkbajpai.kk@gmail.com

If you liked the repo then please support it by giving it a star ⭐!
