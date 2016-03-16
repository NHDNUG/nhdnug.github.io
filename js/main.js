 $(window).load(function() {
     var tfs = document.querySelector(".top-flexslider");
     if (tfs !== null) {
       $(tfs).flexslider({
        directionNav: false,
        slideshowSpeed: 10000  
       });  
     } else { 
        $('.flexslider').flexslider();
     }
  });