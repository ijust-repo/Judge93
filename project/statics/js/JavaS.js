
$(document).ready(function () {
$("#signupbtn").click(function() { 


var username = $("input#username").val();
var password = $("input#password").val();  

	$.ajax({
            type: "POST",
            url : '/user/do_signup/',
				contentType: "application/json",
            dataType: "json",
            data: '{"username": "' + username + '", "password" : "' + password + '"}',
            success: function (data) {
              $("#result").text(data.username + data.password);
    			

            },
            error: function (request, status, error) {
            	
              alert( request.status);
             
              
            }
		});
	});
});
/*****************************************slideshow*********************************/

/*****************************************slideshow*********************************/