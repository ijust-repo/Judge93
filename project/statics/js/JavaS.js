
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
            dataType: "json",
            data: '{"username": "' + username + '", "password" : "' + password + '", "email" : "' + email + '"}',
            success: function (data) {
     
            },
            error: function (request, status, error) {            
         
        
               if (request.status===201) {
	      
	      		window.location.replace("/user/");
      		}
      		else if (request.status===409) 
             {
					alert(" this username is already taken ");             
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
  });
});

$(document).ready(function () {
$("#loginbtn").click(function() { 


var username = $("input#username_login").val();
var password = $("input#password_login").val();  

  $.ajax({
            type: "POST",
            url : '/user/login/',
            contentType: "application/json",
            dataType: "json",
            data: '{"username": "' + username + '", "password" : "' + password + '"}',
            success: function (data) {
                
            },
            error: function (request, status, error) {
        
              if (request.status===200) {
	      		window.location.replace("/user/home/");
      		}
      		else if (request.status===401) 
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

$(document).ready(function () {
$("#logout").click(function() { 


  $.ajax({
            type: "GET",
            url : '/user/logout/',
            dataType: "jsonp", 
        		jsonp:"skywardDetails",
 				
            success: function () {
           
            },
          error: function (request, status, error) {
        
              if (request.status===200) {
	      
	      		window.location.replace("/user/");
      		}
             {
					alert(request.message);             
             }
          
          

            }
    });
  });
});