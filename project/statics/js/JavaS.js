
$(document).ready(function () {
	
//logout
$("#logout").click(function() { 
	
  $.ajax({
            type: "GET",
            url : '/user/logout/',
            dataType: "html",  				
            success: function () {
           	window.location.replace("/user/");
            },
          error: function (request, status, error) { 
			  if(request.status===405){    
					alert("Please login first"); 
				}            
            }
            
    });
  });
 

});
