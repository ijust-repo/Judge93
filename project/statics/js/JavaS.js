
$(document).ready(function () {

//show create team
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
  $("#usernameitem").click(function() { 
    $('#setting').css('background-color', '#312736');
    $('#usernameitem').css('background-color', '#6C6368');
    $('.settingcontent').css('display', 'none');
      $('.open-page').removeClass('open-page').addClass('close-page');
      $('#titlePage').html("News");
    $('.post').css('display', 'block');

  });
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
//show username
      	      		   		
  $.ajax({
            type: "GET",
            url : '/user/get_profile/',
            dataType: "html", 				
            success: function (data) {
           $( '#getusername ' ).html((JSON.parse(data)).username); 			
            },
           error: function (request) {                
				alert("this user not found");	      	      		
      		}
		});
//end show username
//change profile
function changeprofile(username){
  document.title = username;
  document.getElementById('usernameitem').style.display = 'none';
			document.getElementById('usernameprofitem').style.display = 'block';
			document.getElementById('backtoprofile').style.display = 'block';
			document.getElementById('logout').style.display = 'none';
			document.getElementById('users').style.display = 'none';
			document.getElementById('setting').style.display = 'none';
			$( '#getusernameprof ' ).html(username); 
			 
}
//go to profile
$("#usernamecontact").click(function() { 
 var username = $("#usernamecontact").text();
  $.ajax({
            type: "GET",
            url : "/user/get_profile/by_username/"+ username + "/",
            contentType: "application/json",
            dataType: "html",
            success: function (data) {
			$( '#getidprof ' ).html((JSON.parse(data)).id); 	
            changeprofile(username);
             window.history.replaceState(username,username, "/user/"+ username  );  
            },
            error: function (request, status, error) {
                    
      		 if (request.status===406) 
             {
					alert(" the user id does not exist ");             
             }  

            }
          });          
  });

// back to profile
$("#backtoprofile").click(function() { 
           	window.location.replace("/user/home/");
              document.title = "home";
			document.getElementById('usernameitem').style.display = 'block';
			document.getElementById('usernameprofitem').style.display = 'none';
			document.getElementById('backtoprofile').style.display = 'none';
			document.getElementById('logout').style.display = 'block';
			document.getElementById('users').style.display = 'block';
			document.getElementById('setting').style.display = 'block';
			  });
 
  });
