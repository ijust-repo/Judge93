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
> **/user/```string:Username```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template and the id of the user in database.
>- Username is the username of the user.

-------


View user team page
===================

Resource URL
>GET
> **'/user/```string:Username```/team/'**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template and the id of the user in database as user_id.
>- Username is the username of the user.

-------

View user contest page
===================

Resource URL
>GET
> **'/user/```string:Username```/contest/'**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template and the id of the user in database as user_id.
>- Username is the username of the user.

-------



Checking user existance
=======================

Resource URL
>GET
**/user/exists/```string:username```/**

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

ForgotPassword
======

Resource URL
>POST
> **/user/forgot_password/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|


Example Request
```
{
  "username": "admin",
  "email": "n.abdollahi@gmail.com"
}
```


> **NOTE:**
>
>- If response status code is **200** then you have successfully changed password.
>- If response status code is **406** then you have errors with changing Profile like `Username does not exists.` or 'Email does not exists' .

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


Get user's team
===============

Resource URL
>GET
> **/user/<string:user_id>/teams/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Response:
```
 {
  "teams": [
            {
              "contests": [
                            {
                              "name": "new_contest3",
                              "status": "pending"
                            },
                            {
                              "name": "new_contest",
                              "status": "rejected"
                            }
                          ],
              "id": "567cbe2823e3c00ba43affa1",
              "members": [
                          {
                            "id": "567cbce123e3c00ba43aff99",
                            "username": "admin4"
                          },
                          {
                            "id": "567cbcf223e3c00ba43aff9a",
                            "username": "admin3"
                          }
                         ],
              "name": "new_team",
              "owner": {
                        "id": "567cbcf923e3c00ba43aff9b",
                        "username": "admin2"
                       }
            }
          ]
}
```

> **NOTE**
>
>- user_id is the Id of the user in database.
>- If response status code is **200** then user id have been successfully found and information have been returned.
>- If response status code is **406** then the user id does not exist.


Get team by contest id
===============

Resource URL
>GET
> **/user/<string: user_id>/contest/<string:contest_id>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Response:
```
{
  "id": "5662ba0823e3c01da4c9e2b1",
  "name": "new_team9",
  "owner": {
            "id": "566179cb23e3c01f40fc6431",
            "username": "admin2"
           }
}
```

> **NOTE**
>- If response status code is **200** then team have been successfully found and information have been returned.
>- If response status code is **406** then the user or contest does not exist and you will have errors like **'user or contest does not exists!' **, or user is not in contest and you will have errors like **'user is not in contest!' **.

-------




Team API
========


View team page
==============

Resource URL
>GET > 
> **/team/```string:team_name```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template and the id of the team in database as team_id.
>- team_name is the name of the team.
>- If response status code is **406** then the team does not exists.

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
>- If you have created two teams before, status code will be **406** and you will have errors with creating team like  **'You cannot create more teams!' ** .
>- If owner is found in the members of the request, status code will be **406** and and you will have errors with creating team like  **'Owner can not be added to the team!' ** .
>- If the members in the request are the same, status code will be **406** and you will have errors with creating team like **'No one can be added twice!' ** .
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
>- If response status code is **403** then team has running contest and you will have errors like  **'you are in a running contest' ** .
>- If response status code is **409** then the new name does not exist.
>- If there are errors like a required field response status code will be **406** .

------- 


Add members to existing team
===============

Resource URL
>POST
**/team/members/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "name": "Team's name",
  "members" : ["new members"] 
}
```

> **Note:**

>- Team_id is the Id of the team in database.
>- If response status code is **200** then members added to the team successfully.
>- If response status code is **406** then team does not exists or the team owner are in the members list or someone in members list are repeated twice or sum of the team members be greater than 3 or the username in the members list does not exists. 
>- If there are errors like a required field response status code will be **406**.
>- If response status code is **403** then team has running contest and you will have errors like  **'you are in a running contest' ** .
>- If response status code is **403** the user is not owner of the team.


-------

Remove members from team
===============

Resource URL
>DELETE
**/team/```string:team_id```/member/```string:member_id```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|

Example Request
```
team/5662c01a7431e90c36c8bd26/member/56s2bf4e743sd90b4ecc985e/
```

> **Note:**

>- `team_id` is the Id of the team in database.
>- `member_id` is the Id of the member in database.
>- If response status code is **200** then member removed from team successfully.
>- If response status code is **403** then the user is not owner of the team or team has running contest and you will have errors like  **'you are in a running contest' ** .
>- If response status code is **406** then team does not exists.

-------


GetMembers
===============

Resource URL
>GET
> **/team/members/```string:team_id```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|


Example Result
```
{
   "members": [
    {
      "id": "user_id", 
      "username": "member1"
    }, 
    {
      "id": "user_id", 
      "username": "member2"
    }, 
    {
      "id": "user_id", 
      "username": "member3"
    }
  ]
}
```


> **NOTE:**

>- Team_id is the Id of the team in database.
>- If response status code is **200** then the team name successfully changed.
>- If response status code is **406** then the user is not owner of the team or team does not exist.

------- 


Get full info
===============

Resource URL
>GET
> **/team/```string:team_id```/info/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|NULL|YES (must be authenticated)|


Example Result
```
{
  "name": "new_team",
  "contests": [
                {
                  "name": "new_contest3",
                  "status": "accepted"
                },
                {
                  "name": "new_contest",
                  "status": "rejected"
                }
              ],
  "members": [
              {
                "id": "567cbce123e3c00ba43aff99",
                "username": "admin4"
              },
              {
                "id": "567cbcf223e3c00ba43aff9a",
                "username": "admin3"
              }
             ],
  "owner": {
            "id": "567cbcf923e3c00ba43aff9b",
            "username": "admin2"
           }
}
```


> **NOTE:**

>- `team_id` is the Id of the team in database.
>- "contests"  is contests with acception status and they are from {"accepted" , "pending" , "rejected"}.
>- If response status code is **406** then the team does not exist.

------- 


Join request
=================

Resource URL
>POST
**/team/join_request/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "contest_id": "5661814323e3c023fc57aed8",
  "team_name": "new_team"
}
```

> **NOTE:**
>
>- If response status code is **200** then team is successfully sends join request.
>- If the person who has sent join request is not team owner response status code is **403** and you will have errors like **'user is not team owner'**
>- If team owner or one of the team members is joined in contest, response code is **409** and you will have errors like **'user salar is in contest'**
>- If join request has been sent before and waites for owner's answer, response code is **406** and you will have errors like **'please wait for checking your join request'**
>- If the team  already exists in contest, status code will be **409** and you will have errors like **'team already exists in contest!'**.
>- If join request has been sent for rejected team,join request will send again and status code will be **409** and you will have errors like **'join request not accepted -> Re_sent'**.
>- If there are errors like a required field response status code will be **406** and you will have errors like "Contest or Team does not exist!".
>- If response status code is **201** then the join request sent successfully.

--------


Contest API
========


View contest details page page
===================

Resource URL
>GET
> **'/contest/```string:contestName```/details_page/'**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template.
>- contestName is the name of the contest.

-------



Creating new contest
===============

Resource URL
>post
> **/contest/**

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
> **/contest/```string:contest_id```/problem/**

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
>- Problems can not be added to contest after its start time and there will be errors like "Problem can not be added right now!" and status code will be **406** .
>- The header, footer and tastcases fields are optional (but if there is a test case, both of its fields are required.)
>- Just the owner of contest can add new problems, if the loged in user is not the owner of contest, status code will be **403**.
>- If there are errors like a required field response status code will be **406** .

--------



Edit Contest
============

Resource URL
>PUT
> **/contest/```<string:contest_id>```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "name":"new name",
  "starts_on":2000 ,
  "ends_on":2000 ,
  "problems": [{ "id":1 ,
                 "order":1 ,
                 "title":"new title" ,
                 "time_limit":10 ,
                 "space_limit":10 ,
                 "header":"new header" ,
                 "body":"new body" ,
                 "footer":"new footer" ,
                 "testcaases": [ {"id":1 ,
                                  "order":1 ,
                                  "input":"new input" ,
                                  "output":"new output" } ,
                                 {"id":2 ,
                                  "order":2 ,
                                  "input":"new input 2" ,
                                  "output":"new output 2"} ] }
                { "id":2 ,
                 "order":2 ,
                 "title":"new title 2" ,
                 "time_limit":20 ,
                 "space_limit":20 ,
                 "header":"new header 2" ,
                 "body":"new body 2" ,
                 "footer":"new footer 2" ,
                 "testcaases": [ {"id":1 ,
                                  "order":1 ,
                                  "input":"new input 3" ,
                                  "output":"new output 3" } ,
                                 {"id":2 ,
                                  "order":2 ,
                                  "input":"new input 4" ,
                                  "output":"new output 4"} ] } ] }
```

> **NOTE:**
>
>- All fields are optional!
>- Problems and test cases are sorted by the value of order field .
>- If there are new starts_on and new ends_on and new starts_on is biger than new ends_on then status code will be **406** and there will be errors like **'Start date must be earlier than end date!'** . 
>- If there is new starts_on but no new ends_on and new starts_on is biger than the ends_on we had before then status code will be **406** and there will be errors like **'Start date must be earlier than end date!'** . 
>- If there is new ends_on but no new starts_on and new ends_on is lower than the starts_on we had before then status code will be **406** and there will be errors like **'End date must be later than start date!'** .
>- If there is new starts_on and new starts_on is biger than created_on then status code will be **406** and there will be errors like **'Start date must be later than creation time!!'** . 
>- If the logged in user is not the owner of contest, status code will be **403** and there will be errors like **'User is not owner!'**
>- If there is new name and this name already exists, the status code will be **409** and there will be errors like **'Contest with this name already exists!'** .
>- If contest is already started, it can not be edited and there will be errors with editing it like **'Contest can not be edited at this time!'** and response status code will be **406**.
>- If none of errors above occurs, the status code will be 200 .

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
  "contests":[
              {
                "created_on": "2014-02-04 08:02:27",
                "starts_on": "2017-07-14 07:10:00", 
                "ends_on": "2027-01-15 11:30:00", 
                "id": "566179cb23e3c01f40fc6432", 
                "name": "new_contest", 
                "owner": {
                          "id": "566179cb23e3c01f40fc6431", 
                          "username": "admin2"
                          }   
              }, 
              {
                "created_on": "2015-12-04 12:04:19", 
                "starts_on": "2017-07-14 07:10:00",
                "ends_on": "2027-01-15 11:30:00", 
                "id": "5661814323e3c023fc57aed8", 
                "name": "another_contest", 
                "owner": {
                          "id": "566179cb23e3c01f40fc6431", 
                          "username": "admin2"
                         } 
                
              }
            ]
}
```

> **NOTE:**
>- Type of "create_from" and "create_to" and "start_from" and "start_to" is float:timestamp.
>- default value of "start_from" and "create_from" is 0.
>- default value of "create_to" is current time.
>- default value of "start_to" is infinity.
>- If response status code is **200** then the ContestsList returned successfully.

--------


View contest page
=================

Resource URL
>GET > 
> **/contest/```string:contest_name```/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|PAGE|YES (must be authenticated)|


> **NOTE:**
>
>- This url returns a html template and the id of the contest in database as contest_id.
>- contset_name is the name of the contest.
>- If response status code is **406** then the contest does not exists.

--------


get contest info by id
===============

Resource URL
>GET
> **/contest/by_id/<id>**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
/contest/by_id/563dcee823e3c01d38a73502/
```
Example Response
```
{
"created_on": "2015-11-07 10:14:00", 
"ends_on": "2015-11-07 15:42:40", 
"id": "563dcee823e3c01d38a73502", 
"name": "maincontest", 
"owner": {
          "id": "563d03c623e3c01694ee7291",
          "username": "admin"
        }
}
```

> **NOTE:**
>- If response status code is **200** then the Contest_info returned successfully.
>- If there are errors like a required value response status code will be **406** .

--------


get contest info by name
===============

Resource URL
>GET
> **/contest/by_name/<name>**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
/contest/by_name/maincontest/
```
Example Response
```
{
"created_on": "2015-11-07 10:14:00", 
"ends_on": "2015-11-07 15:42:40", 
"id": "563dcee823e3c01d38a73502", 
"name": "maincontest", 
"owner": {
          "id": "563d03c623e3c01694ee7291",
          "username": "admin"
        }
}
```

> **NOTE:**
>- If response status code is **200** then the Contest_info returned successfully.
>- If there are errors like a required value response status code will be **406** .

--------


Upload testcases for a problem
===============

Resource URL
>POST
> **/contest/<string:contest_id>/testcase/<int:number>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

> **NOTE:**
>- If response status code is **200** then the file is uploaded successfully.
>- If contest_id does not exist in data base response status code will be **406** and you will have errors like "Contest does not exist!".
>- If number is bigger than number of problems or it is lower than 1 the response status code will be **406** and you have errors like "Invalid problem number!".
>- If the extinsion of uploading  file is not **.zip** , response status code will be **406** and there will be errors like "Bad zip file!".
>- Zipped document will get unziped automatically and any thing except **.txt** files or **.tc** files will be removed, including zip file itself.

--------


contest detail
===============

Resource URL
>GET
> **/contest/<contest_id>/details/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
/contest/565dfe6823e3c00e88c0f18c/details/
```
Example Response
```
{
  "problem_num": 3,
  "teams": [
            {
              "penalty": 459, 
              "problems_list": [{
                                  "order": 1, 
                                  "problem_id": 1, 
                                  "solved": true,
                                  "solved_on": "Wed, 02 Dec 2015 16:30:00 GMT", 
                                  "failed_tries": 15
                                }, 
                                {
                                  "order": 2, 
                                  "problem_id": 2, 
                                  "solved": true, 
                                  "solved_on": "Wed, 02 Dec 2015 14:30:00 GMT",
                                  "failed_tries": 0
                                }, 
                                {
                                  "order": 3, 
                                  "problem_id": 3, 
                                  "solved": true, 
                                  "solved_on": "Wed, 02 Dec 2015 16:30:00 GMT", 
                                  "failed_tries": 0
                                }], 

              "solved_problem_counter": 3, 

              "team": {
                      "id": "565ee15223e3c01ca02e0a7a", 
                      "name": "new_team3", 
                      "owner": {
                                "id": "565df07323e3c00dfca5f8af", 
                                "username": "admin"
                               }
                      }
            }, 

            {
              "penalty": 299, 
              "problems_list": [{
                                  "order": 1, 
                                  "problem_id": 1, 
                                  "solved": true,
                                  "solved_on": "Wed, 02 Dec 2015 13:30:00 GMT", 
                                  "failed_tries": 4
                                }, 
                                {
                                  "order": 2, 
                                  "problem_id": 2, 
                                  "solved": true,
                                  "solved_on": "Wed, 02 Dec 2015 16:30:00 GMT", 
                                  "failed_tries": 0
                                }, 
                                {
                                  "order": 3, 
                                  "problem_id": 3, 
                                  "solved": false,
                                  "solved_on": null,
                                  "failed_tries": 6
                                }],

              "solved_problem_counter": 2, 

              "team": {
                      "id": "565df1df23e3c00dfca5f8b5", 
                      "name": "new_team", 
                      "owner": {
                                "id": "565df07323e3c00dfca5f8af", 
                                "username": "admin"
                               }
                      } 
            }
           ]
}
```

> **NOTE:**
>- If response status code is **200** then the contest details returned successfully.
>- If there are errors like contest does not exists response status code will be **406** and you will have errors like "Contest does not exist!".
>- response is sorted.

--------

Submission Progress
===============

Resource URL
>POST
> **'submit/<string:contest_id>/<string:team_id>/<int:number>/<string:file_type>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

> **NOTE:**
>- If response status code is **200** then the file is whether accepted or the submission progress has encountered an error. Error type will be returned as response's status.
>- ErrorTypes ==> Wrong Answer, Compile Error, Runtime Error, Restricted Function, Time Exceeded
>- If the sender is not a team member, response status code will be **406** and you will have errors like "You are not a member of this team".
>- If contest_id does not exist in data base response status code will be **406** and you will have errors like "Contest does not exist!".
>- If team_id does not exist in data base response status code will be **406** and you will have errors like "Team does not exist!".
>. Files can only be submitted during the contest time otherwise response status code will be **406** and you will have errors like "Contest is not stated yet!" or "Contest is finished".
>- If number is bigger than number of problems or it is lower than 1 the response status code will be **406** and you have errors like "Invalid problem number!".
>- The file_type should be **py** ,**cpp** or **java** otherwise the response status code will be **406** and there will be errors like "Extension Error".

--------


Contest problem
===============

Resource URL
>GET
> **/contest/<string:contest_id>/<string:team_id>/problems/<int:problem_id>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
/contest/565dfe6823e3c00e88c0f18c/problems/1/
```
Example Response
```

{
  "body": "body",
  "footer": "footer",
  "header": "header",
  "id": 1,
  "order": 1,
  "space_limit": 1000,
  "testcases": [
                {
                "id": 1,
                "input": "1",
                "order": 1,
                "output": "9"
                },
               {
                "id": 2,
                "input": "6",
                "order": 2,
                "output": "4"
              }
              ],
  "time_limit": 1000,
  "title": "problem1"
}

> **NOTE:**
>- If everything goes well, response status code is **200**.
>- If the requested contest does not exist in data base, status code will be **406** and you will have errors like  **'Contest does not exist!' ** .
>- If the requested prolem does not exist in data base, status code will be **406** and you will have errors like  **'Problem does not exist!' ** .
>- Just owner can see problems befor contest starts, and if request is from someone else there will be errors like **'You can not see problems right now!'** and respons status code will be **403** .
>- You can not see a problem if you are not a member of an accepted team, in that case response status code will be **406** and you will have errors like **"You Are Not A Member Of This Team"**
>- If there is no team with given id, status code will be **406** and you will have errors like **"Team does not exist!"**
>- If your team is not accepted in contest, status code will be **406** and you will have errors like **"You are not allowed to see problems"**

--------


All contest problems
===============

Resource URL
>GET
> **/contest/<string:contest_id>/<string:team_id>/problems/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
/contest/565dfe6823e3c00e88c0f18c/problems/
```
Example Response
```

{
  "problems": [
               {
                "id": 1,
                "order": 1,
                "title": "problem1"
              },
               {
                "id": 2,
                "order": 2,
                "title": "problem2"
              },
              {
                "id": 3,
                "order": 3,
                "title": "problem3"
              },
             {
                "id": 4,
                "order": 4,
                "title": "problem4"
              }
            ] 
}

> **NOTE:**
>- If everything goes well, response status code is **200**.
>- If the requested contest does not exist in data base, status code will be **406** and you will have errors like  **'Contest does not exist!' ** .
>- Just owner can see problems befor contest starts, and if request is from someone else there will be errors like **'You can not see problems right now!'** and respons status code will be **403** .
>- You can not see a problem if you are not a member of an accepted team, in that case response status code will be **406** and you will have errors like **"You Are Not A Member Of This Team"**
>- If there is no team with given id, status code will be **406** and you will have errors like **"Team does not exist!"**
>- If your team is not accepted in contest, status code will be **406** and you will have errors like **"You are not allowed to see problems"**

--------


Pending request
===============

Resource URL
>GET
> **/contest/<string:contest_id>/pending_teams/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Response
```
{
  "teams": [
            {
              "id": "5662ba0823e3c01da4c9e2b1",
              "members": [
                           {
                             "id": "5662b70823e3c01da4c9e2af",
                             "username": "admin"
                           },
                           {
                             "id": "5662b71023e3c01da4c9e2b0",
                             "username": "admin3"
                           }
                         ],
              "name": "new_team",
              "owner": {
                        "id": "566179cb23e3c01f40fc6431",
                        "username": "admin2"
                       }
            },
            {
              "id": "5662d0a023e3c00a5cc9d8b4",
              "members": [
                          {
                            "id": "5662bca323e3c0208ce1cbd4",
                            "username": "admin4"
                          }
                         ],
              "name": "new_team6",
              "owner": {
                        "id": "5662bca323e3c0208ce1cbd4",
                        "username": "admin4"
                       }
            }
          ]
}

> **NOTE:**
>- If everything goes well, response status code is **200**.
>- If the requested contest does not exist in data base, status code will be **406**.
>- If loged in user is not contest owner, status code will be **403** and you will have errors like **User is not owner'**.

--------


Accept and reject join request
===============

Resource URL
>PUT
> **/contest/<string:contest_id>/team_acceptation/<string:team_id>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "acceptation" : false
}
```
> **NOTE:**
>- If team was accepted before or not, and acceptation value is **false**, response status code is **200** and team will reject.
>-If team was accepted befor and acceptation value is **true**, response status code is** 409** and you will have errors like **'this team was accepted before!'**.
>- If team rejected,response status code is** 409** and you will have errors like **'this team was rejected before!'**. 
>- If the requested contest or team does not exist in data base, status code will be **406** and you will have errors like **'Team or Contest does not exist!'**. .
>- If loged in user is not contest owner, status code will be **403** and you will have errors like **User is not owner'**.
>- If team does not in contest, status code will be **406** and you will have errors like "this team does not exists in contest".

--------

Get team results
===============

Resource URL
>Get
'<string:contest_id>/results/team/<string:team_id>/'
> **/contest/<string:contest_id>/results/team/<string:team_id>/**

Resource Information
>|Response formats|Requires authentication?|
|:-:|:-:|
|JSON|YES (must be authenticated)|

Example Request
```
{
  "results" : [
        {
          "problem_id" : 2,
          "status" : "Wrong Answer",
          "failed_tries" : 15,
          "solved" : false
        },
        {
          "problem_id" : 3,
          "status" : "Accepted",
          "failed_tries" : 0,
          "solved_on" : ISODate("2016-02-23T23:54:08.784Z"),
          "solved" : true
        },
        {
          "problem_id" : 4,
          "status" : "Accepted",
          "failed_tries" : 1,
          "solved_on" : ISODate("2016-02-24T00:03:14.437Z"),
          "solved" : true
        },
        {
          "problem_id" : 5,
          "status" : "Accepted",
          "failed_tries" : 0,
          "solved_on" : ISODate("2016-02-24T00:16:48.763Z"),
          "solved" : true
        },
        {
          "problem_id" : 6,
          "status" : "Accepted",
          "failed_tries" : 0,
          "solved_on" : ISODate("2016-02-24T00:17:01.970Z"),
          "solved" : true
        },
        {
          "failed_tries" : 0,
          "problem_id" : 1,
          "solved" : true,
          "solved_on" : ISODate("2016-02-24T00:19:28.218Z"),
          "status" : "Accepted"
        }
      ]
}
```
> **NOTE:**
>- 

--------

