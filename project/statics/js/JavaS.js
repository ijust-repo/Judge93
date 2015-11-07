
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
              	
            },
            error: function (request, status, error) {
      	if (request.status===201) {
      		alert( request.status );
      		window.location.replace("{{ url_for('/') + 'user/home/'}}");
      		}
              

            }
		});
	});
});
$(document).ready(function(){
    $('.leftMenu').css("height",$('.mainWrapper').height());
});
/*****************************************slideshow*********************************/

/*************************************slideshow*********************************/