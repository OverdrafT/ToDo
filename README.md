# ToDo service
This is backend REST service for CRUD operations for TODO.
## Here is a live demo of the app
[Django ToDo app](http://95.217.158.152:8000/api/)
## Prerequisites
Python 3.8.6 \
Django 3.1.5
## Getting started
- Clone repository
- `python manage.py runserver`
- open http://localhost:8000/api/ in browser
### API description
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

## Future improvements
- Return http codes in response
- Add virtualenv support
- Field validation
- Change primary key to UID
- Switch to the same url for each CRUD operation
https://dev.to/enether/managing-restful-urls-in-django-rest-framework