## 1\. Home page:
### Request:
Request type => GET

url => http://localhost:5000 or http://127.0.0.1:5000
### Response:
localhost:port/users for list of users.

localhost:port/users/id for individual user name.

localhost:port/update\_user/ for user name update
## 2\. Display all users:
### Request:
Request type=> GET

url => <http://127.0.0.1:5000/users/>
### Response:
[

`    `{

`        `"id": 1,

`        `"name": "vinay"

`    `},

`    `{

`        `"id": 2,

`        `"name": "kiran"

`    `}

]

## 3\. Get user name by id:
### Request:
Request type => GET

url => http://127.0.0.1:5000/users/1
### Response:
vinay

## 4\. Add new user
### Request:
Request type => POST

url => http://127.0.0.1:5000/add\_user

Request body – JSON: 

{

`    `"name": "Sachin"

}


### Response:
[

`    `{

`        `"id": 1,

`        `"name": "vinay"

`    `},

`    `{

`        `"id": 2,

`        `"name": "kiran"

`    `},

`    `{

`        `"id": 3,

`        `"name": "Sachin"

`    `}

]

## 5\. Update user’s name
### Request:
Request type => PUT

url => http://127.0.0.1:5000/update\_user

Request body – JSON: 

{

`    `"id": 1,

`    `"name": "Vinay Patil"

}

### Response:
[

`    `{

`        `"id": 1,

`        `"name": "Vinay Patil"

`    `},

`    `{

`        `"id": 2,

`        `"name": "kiran"

`    `}

]

