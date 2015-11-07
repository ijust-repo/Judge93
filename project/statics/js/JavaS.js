
$(document).ready(function () {
$("#signupbtn").click(function() { 


var username = $("input#username").val();
var password = $("input#password").val();  

  $.ajax({
            type: "POST",
            url : '/user/signup/',
            contentType: "application/json",
            dataType: "json",
            data: '{"username": "' + username + '", "password" : "' + password + '"}',
            success: function (data) {
              $("#result").text(data.username + data.password);     
            },
            error: function (request, status, error) {
        
              alert( request.status );

            }
    });
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
              $("#result").text(data.username + data.password);     
            },
            error: function (request, status, error) {
        
              alert( request.status );

            }
    });
  });
});

$(document).ready(function(){
    $('.leftMenu').css("height",$('.mainWrapper').height());
});

/* show hide login or signup
*/
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