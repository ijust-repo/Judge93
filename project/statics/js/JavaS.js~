$(function() {
    $('button').click(function() {
        var username = $('#username').val();
        var password = $('#password').val();
        $.ajax({
            url: '/do_signup',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
               
  				{
                alert("alert2:messageServer = "+response);
                if (data !=null)
                {
                  alert("alert3:messageServer = "+response);
                  messageServer=response;
                  $('#UID_afficheTest').val(messageServer);
                  document.getElementById('UID_afficheTest').innerHTML = messageServer;

                }
              }/*success : function() {}*/
            });/*$.ajax*/
          alert("alert4:after ajax request");
          }
 /***************** slideshow**********************/
    jQuery(document).ready(function ($) {
            
            var jssor_1_options = {
              $AutoPlay: true,
              $SlideWidth: 600,
              $Cols: 2,
              $Align: 100,
              $ArrowNavigatorOptions: {
                $Class: $JssorArrowNavigator$
              },
              $BulletNavigatorOptions: {
                $Class: $JssorBulletNavigator$
              }
            };
            
            var jssor_1_slider = new $JssorSlider$("jssor_1", jssor_1_options);
            
            //responsive code begin
            //you can remove responsive code if you don't want the slider scales while window resizes
            function ScaleSlider() {
                var refSize = jssor_1_slider.$Elmt.parentNode.clientWidth;
                if (refSize) {
                    refSize = Math.min(refSize, 800);
                    jssor_1_slider.$ScaleWidth(refSize);
                }
                else {
                    window.setTimeout(ScaleSlider, 30);
                }
            }
            ScaleSlider();
            $(window).bind("load", ScaleSlider);
            $(window).bind("resize", ScaleSlider);
            $(window).bind("orientationchange", ScaleSlider);
            //responsive code end
        });
     /***************** slideshow**********************/   