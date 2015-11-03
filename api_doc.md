#ElmosJudge93 v0.1 API DOC

# APIs Usage

> In all resources if response status code is **405** then you must login to use that resource.


User API
========


View login page
===============

Resource URL
>GET
> **/user/login/**

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
**/user/exists/```string:username```**

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
**/user/do_login/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|NO (must be not authenticated)|

Example Request
```
{"username": "admin", "password": "123123"}
```

> **NOTE:**
>
>- If response status code is **200** then you have successfully logged in.
>- If response status code is **401** then you have errors with login.
>- If there are errors like a required field response status code will be **406**.

--------

View signup page
================

Resource URL
>GET
> **/user/signup/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|NO (must be not authenticated)|


> **NOTE:**
>
>- This url returns a html template.

-------

Signup
======

Resource URL
>POST
**/user/do_signup/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|NO (must be not authenticated)|

Example Request
```
{"username": "admin", "password": "123123"}
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
