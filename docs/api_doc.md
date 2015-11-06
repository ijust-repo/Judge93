ElmosJudge93 v0.1 API DOC
=========================

APIs Usage
==========

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
  "password": "123123"
}
```

> **NOTE:**
>
>- If response status code is **201** then you have successfully signed in.
>- If response status code is **409** then you have errors with signup like `user already exists`.
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
