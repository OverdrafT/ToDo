# ToDo service
This is backend REST service for CRUD operations for TODO.
## Prerequisites
Python 3.8.6 \
Django 3.1.5
## Getting started
- Git clone
- python manage.py runserver
- open http://localhost:8000/api/ un browser
### API description
- Create\
POST creates a new resource of the specified resource type. 
- Read\
To read resources in a REST environment, we use the GET method.
- Update\
PUT is the HTTP method used for the CRUD operation, Update.
- Delete\
The CRUD operation Delete corresponds to the HTTP method DELETE. It is used to remove a resource from the system.
### Create todo item:
```
curl -X POST http://localhost:8000/api/task-create/ -d '{ "title" : "<your title>"}' -H "Content-Type: application/json"
```
### Retrieve toto list:
```
curl -X GET http://localhost:8000/api/task-list/ | json_pp
```
### Retrieve todo item:
```
curl -X GET http://localhost:8000/api/task-detail/<id> | json_pp

```
### Update todo item:
```
curl -X PUT http://localhost:8000/api/task-update/<id> -d '{"title": "Pay the bill", "comleted": false}' -H "Content-Type: application/json"

```
### Delete todo item:
```
curl -X DELETE http://localhost:8000/api/task-delete/<id>

```
Enjoy!

### Future improvements
- Field validation
- Return http codes in response
- Change primary key to UID
- Switch to the same url for each CRUD operation
https://dev.to/enether/managing-restful-urls-in-django-rest-framework