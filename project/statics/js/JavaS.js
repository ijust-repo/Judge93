
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
$(document).ready(function(){
    $('.leftMenu').css("height",$('.mainWrapper').height());
});
/*****************************************slideshow*********************************/

/*************************************slideshow*********************************/