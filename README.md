# Web studio
  

## How to run

```
* git init
* git clone git@github.com:avamerina/web_studio.git

* python3 -m venv venv
* . venv/bin/activate

* pip install -r requirements.txt

* create .env file in project root
* create authentication/gs_credentials directory and add json file with credentials

* python manage.py migrate
* python manage.py createsuperuser

* or use existing db file


* python manage.py runserver
  
* http://127.0.0.1:8000/ api base url
  
* http://127.0.0.1:8000/admin/ admin url
```

## Run celery

```
* sudo service redis-server start
* celery -A core worker -B -l INFO

```


## APIs

* registration
```
POST /users/ 
body: {"phone": "your_username", "password": "your_password"}
```

* login
```
POST /jwt/create
body: {"phone": "your_username", "password": "your_password"} 
```


* profiles
  
```
GET /profiles
GET /profiles/1
PATCH /profiles/1/
  {
    "birth_date": "1991-11-26"
  }
PATCH /profiles/1/set_photo/
  form-data
  {"image": single_file}

```

* orders
  
```
use Authorization header to request as authorized user

GET /orders/
GET /profiles/1
GET /orders/my_orders
POST /orders/
  body:
  {
      "description": "My order"
  }
```

* files
```
GET /files
GET /files/1
POST /files/
  form-data
  {
      "order": "slug",
      "url": multiple_files
  }

```

## Change orders statuses in admin panel
```
* select orders from list
* select "Send selected orders to process" action
* Go
* Update page in 10 seconds to check orders have been successfully processed
```



  

  

