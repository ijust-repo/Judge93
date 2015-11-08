ElmosJudge93 v0.1 API DOC
=========================

APIs Usage
==========

> In case url or method does not exist response status code will be **404**.
> In case you send a bad json request status code will be **400**.
> In all resources if response status code is **405** then the request url or method is invalid or you must login to use that resource.


User API
========


View user page
===============

Resource URL
>GET
> **/user/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|NO (must be not authenticated)|


> **NOTE:**
>
>- This url returns a html template.

-------

View user home page
===============

Resource URL
>GET
> **/user/home/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template.

-------

Checking user existance
=======================

Resource URL
>GET
**/user/exists/```string:username```/*

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|NO (must be not authenticated)|

Example Request
```
url: /user/exists/admin/
```

> **NOTE:**
>
>- In case username exists response status code will be **200** otherwise **404**.

-------

Login
=====

Resource URL
>POST
**/user/login/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|NO (must be not authenticated)|

Example Request
```
{
  "username": "admin", 
  "password": "123123"
}
```

> **NOTE:**
>
>- If response status code is **200** then you have successfully logged in.
>- If response status code is **401** then you have errors with login.
>- If there are errors like a required field response status code will be **406**.

--------

Signup
======

Resource URL
>POST
**/user/signup/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|NO (must be not authenticated)|

Example Request
```
{
  "username": "admin", 
  "email": "mdan.hagh@gmail.com",  
  "password": "123123"
}
```

> **NOTE:**
>
>- If response status code is **201** then you have successfully signed in.
>- If response status code is **409** then you have errors with signup like `Username already exists.` or `Email already exists.`.
>- If there are errors like a required field response status code will be **406**.

--------

Logout
======

Resource URL
>GET
> **/user/logout/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|


> **NOTE:**
>
>- If response status code is **200** then you have successfully logged out.

-------



ChangePassword
======

Resource URL
>PUT
> **/user/change_password/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|


Example Request
```
{
  "old_password": "123123",
  "new_password": "1231235"
}
```


> **NOTE:**
>
>- If response status code is **200** then you have successfully changed password.
>- If response status code is **401** then you have errors with changing Password like `Wrong password`.
>- If there are errors like a required field response status code will be **406**.

-------

ChangeProfile
======

Resource URL
>PUT
> **/user/change_profile/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|


Example Request
```
{
  "new_username": "aref",
  "new_email": "arefhosseini@yahoo.com"
}
```


> **NOTE:**
>
>- If response status code is **200** then you have successfully changed password.
>- If response status code is **409** then you have errors with changing Profile like `Username already exist.` or 'Email already exist.' .
>- If there are errors like a required field response status code will be **406**.

-------


Get user profile by username
============================

Resource URL
>GET
> **/user/get_profile/by_username/<string:username>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|

Example Response:
```
{
  "id": "563b9d2857040f1b6c805892", 
  "email": "mdan.hagh@gmail.com"
}
```

> **NOTE:**
>
>- username is the username of the user.
>- If response status code is **200** then username have been successfully found and returned.
>- If response status code is **406** then the username does not exist.

--------


Get logged in user profile
==========================

Resource URL
>GET
> **/user/get_profile/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|

Example Response:
```
{
  "email": "example@gmail.com", 
  "id": "563b9d2857040f1b6c805892", 
  "username": "admin"
}
```

> **NOTE:**
>
>- If response status code is **200** then the logged in user have been successfully found and returned.

-----------


Get user profile by user id
============================

Resource URL
>GET
> **/user/get_profile/by_id/<string:user_id>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|

Example Response:
```
{
  "username": "admin", 
  "email": "mdan.hagh@gmail.com"
}
```

> **NOTE:**
>
>- user_id is the Id of the user in database.
>- If response status code is **200** then user id have been successfully found and returned.
>- If response status code is **406** then the user id does not exist.

--------


Team API
========


View team page
===============

Resource URL
>GET
> **/team/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template.

-------

Creating new team
=================

Resource URL
>POST
**/team/create/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "name": "new_team" ,
  "members": ["member1", "member2"]
}

{
  "name": "new_team"
}
```

> **NOTE:**
>
>- The team creator will be the owner of the team.
>- If response status code is **201** then new team is successfully created.
>- If there are more than two members in the request, response status code will be **406** and you will have errors with creating team like  **'Number of members must be under three!' ** .
>- If owner is found in the members of the request, status code will be **406** and and you will have errors with creating team like  **'Owner can not be added to the team!' ** .
>- If the members in the request are the same, status code will be **406** and and you will have errors with creating team like **'No one can be added twice!' ** .
>- If the requested members do not exist in data base, status code will be **406** and you will have errors with creating team like  **'User does not exist!' ** .
>- If the name of team already exists, status code will be **409** .
>- If there are errors like a required field response status code will be **406** .

--------


Change team name
===============

Resource URL
>PUT
**/team/change_name/```string:team_id```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "new_name": "newTeam" 
}
```

> **Note:**

>- Team_id is the Id of the team in database.
>- If response status code is **200** then the team name successfully changed.
>- If response status code is **406** then the user is not owner of the team or team does not exist.
>- If response status code is **409** then the new name does not exist.
>- If there are errors like a required field response status code will be **406** .

------- 


Contest API
========


Creating new contest
===============

Resource URL
>post
> **/contest/create/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "name": "new_contest" ,
  "starts_on": 1500000000,
  "ends_on": 1800000000
}

```

> **NOTE:**
>
>- Type of "starts_on" is float:timestamp and it must be in UTC.
>- Type of "ends_on" is float:timestamp and ite must be in UTC.
>- If response status code is **201** then new contest is successfully created.
>- If the name of contest already exists, status code will be **409** and you will have errors with creating contest like **'Contest with this name already exists!' ** .
>- If the value of "starts_on" is biger than value of "ends_on" , status code will be **406** and you will have errors with creating contest like **'Start date must be earlier than end date!' ** .
>- If the float form of current time is biger than the value of "starts_on",  status code will be **406** and you will have errors with creating contest like **'Start date must be later than now!' ** .
>- If there are errors like a required field response status code will be **406** .

--------


Add problem to contest
===============

Resource URL
>post
> **/```string:contest_id```/problem/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "title":"problem2",
  "time_limit":1000 ,
  "space_limit":1000 ,
  "header":"header",
  "body":"body",
  "footer":"footer", 
  "testcases": [ {
                  "input":"1" ,
                  "output":"9" 
                 },
                 {
                   "input":"6",
                   "output":"4"
                 } ]
}
```

> **NOTE:**
>
>- If response status code is **201** then new problem is successfully added to contest.
>- The header, footer and tastcases fields are optional (but if there is a test case, both of its fields are required.)
>- Just the owner of contest can add new problems, if the loged in user is not the owner of contest, status code will be **403**.
>- If there are errors like a required field response status code will be **406** .

--------


Contests List
===============

Resource URL
>GET
> **/contest/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|NO (must be authenticated)|

Example Request
```
/contest/?create_from=1200000000&create_to= 1500000000&start_from=1300000000&start_to=1500000550
```
Example Response
```
{
"created_on": "2015-11-07 10:14:00", 
"ends_on": "2015-11-07 15:42:40", 
"id": "563dcee823e3c01d38a73502", 
"name": "maincontest", 
"owner": {"id": "563d03c623e3c01694ee7291","username": "admin24"}
}
```

> **NOTE:**
>- Type of "create_from" and "create_to" and "start_from" and "start_to" is float:timestamp.
>- default value of "start_from" and "create_from" is 0.
>- default value of "start_to" and "create_to" is current time.
>- If response status code is **200** then the ContestsList returned successfully.

--------
