//sign up
$(document).ready(function () {
$("#signupbtn").click(function() { 


var username = $("input#username_signup").val();
var password = $("input#password_signup").val();  
var password2 = $("input#re-password_signup").val();  
var email = $("input#email_signup").val(); 
if (password===password2) {
  $.ajax({
            type: "POST",
            url : '/user/signup/',
            contentType: "application/json",
            dataType: "html",
            data: '{"username": "' + username + '", "password" : "' + password + '", "email" : "' + email + '"}',
            success: function (data) {
     					window.location.replace("/user/");
            },
            error: function (request, status, error) {            
         
        
              
      		 if (request.status===409) 
             {
					alert(" this username or is already taken ");             
             }
				else if (request.status===406) 
             {
					alert("Please fill in all fields");             
             }
          }
              

                            });
      }
      else
      {
			alert(" passwords don't match");      
      }
        $("input#username_signup").reset();
		 $("input#password_signup").value(" ");  
		 $("input#re-password_signup").value()=' ';  
		 $("input#email_signup").value()=" "; 
  });
});
//end sign up
//login
$(document).ready(function () {
$("#loginbtn").click(function() { 

var username = $("input#username_login").val();
var password = $("input#password_login").val();  

  $.ajax({
            type: "POST",
            url : '/user/login/',
            contentType: "application/json",
            dataType: "html",
            data: '{"username": "' + username + '", "password" : "' + password + '"}',
            success: function (data) {
                window.location.replace("/user/home/");
            },
            error: function (request, status, error) {
                    
      		 if (request.status===401) 
             {
					alert(" Username or password is incorrect ");             
             }
				else if (request.status===406) 
             {
					alert("Please fill in all fields");             
             }
              

            }
    });
  });
});
//end login
function showLogin(){
  document.title = "Login";
  document.getElementById('signup').style.display = 'none';
  document.getElementById('login').style.display = 'block';
}
function showSignUp(){
  document.title = "Sign Up";
  document.getElementById('login').style.display = 'none';
  document.getElementById('signup').style.display = 'block';
}

$(document).ready(function () {

    $("#team").click(function() {
        $('.post').css('display', 'none');
        $('.settingcontent').css('display', 'none');
        $('#titlePage').html("Team");
        $('.close-page').removeClass('close-page').addClass('open-page');
    });

  $("#setting").click(function() { 
    $('#usernameitem').css('background-color', '#312736');
    $('#setting').css('background-color', '#6C6368');
    $('.post').css('display', 'none');
    $('.open-page').removeClass('open-page').addClass('close-page');
      $('#titlePage').html("News");
    $('.settingcontent').css('display', 'block');

  });
});

$(document).ready(function () {
  $("#usernameitem").click(function() { 
    $('#setting').css('background-color', '#312736');
    $('#usernameitem').css('background-color', '#6C6368');
    $('.settingcontent').css('display', 'none');
      $('.open-page').removeClass('open-page').addClass('close-page');
      $('#titlePage').html("News");
    $('.post').css('display', 'block');

  });
});
//logout
$(document).ready(function () {
$("#logout").click(function() { 


  $.ajax({
            type: "GET",
            url : '/user/logout/',
            dataType: "html",  				
            success: function () {
           	window.location.replace("/user/");
            },
          error: function (request, status, error) {
                    
					alert(request.message);             

            }
    });
  });
});
//end logout
//show username
$(document).ready(function () {
$("#usernameitem").click(function() { 
 
  $.ajax({
            type: "GET",
            url : '/user/get_profile/',
            dataType: "html", 
 				
            success: function (data) {
           $( '#getusername ' ).html(data.records.username); 
			alert("hello");
				alert(data.records.username);
            },
           error: function (request) {
                   
				alert("this user not found");
			 	      
	      		
      		}
  
    });
  });
});
//end show username

//change password
$(document).ready(function () {
  $("input#changeSettingbtn").click(function() { 
    var email = $("input#change_email").val();
    var password_old = $("input#change_password_old").val();
    var password_new = $("input#change_password_new").val();
    $.ajax({

      type: "PUT",
      url : '/user/change_password/',
      contentType: "application/json",
      dataType: "json",
      data: '{"old_password" : "' + password_old + '", "new_password" : "' + password_new + '"}',
      success: function (data) {
                
      },
      error: function (request, status, error) {
        if (request.status === 200) {
          alert(" Password changed successfully ");
        } else if (request.status === 401) {
          alert(" Wrong password! ");
        } else if (request.status === 406) {
          alert(" fields required! ");
        }
      }


    });

  });
});
//end change password