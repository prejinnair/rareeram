$(document).ready(function() {

    $('.graph_slider').slick({
      slidesToShow:1,
      dots: false,
      arrows: true,
      autoplay: false
    });

    $('.icon_slider').slick({
      slidesToShow:5,
      dots: false,
      arrows: true,
      autoplay: false
    });
  
    $('.user-manu').on("click", function(e){
        $('.user-login').toggleClass("show-nav");
    });

     $('.mob-menu').on("click", function(e){
        $(this).toggleClass("show-nav");
        $("header").toggleClass("show_nav");
    });

      if ($('.hide_sideMenu').length){
        $('.hide_sideMenu').on("click", function(e){
            $('.side_nav').addClass("hide_nav");
            $('.fullwidth_dashboard').addClass("show_dashboard");
        });
    };

     if ($('.side-menu').length){

        $('.side_menu').on("click", function(e){
            $('.fullwidth_dashboard').removeClass("show_dashboard");
            $('.side_nav').removeClass("hide_nav");
        });

        $(".side-menu nav li").on('click',function(){ 
            if($(this).hasClass("navSelected")){
                $(this).removeClass('navSelected'); 
            } else{
                $('.side-menu nav li').removeClass('navSelected'); 
                $(this).addClass('navSelected');    
            }              
         });
    };
    
     if ($('.data-upload').length){
        $(".data-upload input[type=radio]").on("click", function(e) {
            $(this).parent().parent().toggleClass('selected');
        })
    };
  
    if ($('.icon_slider').length){
        $(".icon_slider img").on("click", function(e) {
            $(this).parent().toggleClass('selected');
        })
    };    

  
       
    if ($('.nav-tabs').length){

        $(".nav-tabs li a").on("click", function(e) { 
            $('.icon_slider').slick('unslick');
            $('.icon_slider').slick({
              slidesToShow:5,
              dots: false,
              arrows: true,
              autoplay: false
            });  

            $(".icon_slider img").on("click", function(e) {
                $(this).parent().toggleClass('selected');
            })
                  
        })

    };

    
    $('[data-toggle="tooltip"]').tooltip()


});



// Select with checkboxes
    var show = true;
  
    function showCheckboxes() {
        var checkboxes = 
            document.getElementById("checkBoxes");

        if (show) {
            checkboxes.style.display = "block";
            show = false;
        } else {
            checkboxes.style.display = "none";
            show = true;
        }
    }

    // Select with checkboxes
    var show = true;
  
    function showCheckboxes1() {
        var checkboxes1 = 
            document.getElementById("checkBoxes1");

        if (show) {
            checkboxes1.style.display = "block";
            show = false;
        } else {
            checkboxes1.style.display = "none";
            show = true;
        }
    }