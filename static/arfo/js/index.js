/*
Theme Name: Arfon Personal Portfolio & Resume HTML5 Template
Theme URI:
Desing by: R T Suvro
Developed by: Abdullah Al Numan
Version: 1.0
License:
Tags:
*/

(function($) {
    "use strict";
    queryloader2()
    parallaxBanner();
    manuScroll()
    isotope()
    bottomTop()

    /*====== Active Plugins ======
	
		1 Queryloader2
		
		2 Parallax Banner

        3 Manu Scroll

        5 Isotope

        9 Bottom Top   

    =============================*/

    /*=====================
        1 Queryloader2
    =======================*/
    function queryloader2() {
        "use strict";
        window.addEventListener('DOMContentLoaded', function() {
            QueryLoader2(document.querySelector("body"), {
                barColor: "#efefef",
                backgroundColor: "#111",
                percentage: true,
                barHeight: 1,
                minimumTime: 200,
                fadeOutTime: 1000
            });
        });
    }

    /*=====================
        2 Parallax Banner
    =======================*/
    function parallaxBanner() {
        "use strict";
        $(".parallaxie").parallaxie({
            speed: 0.5,
            offset: 0,
        });
    }

    /*=====================
        3 Manu Scroll
    =======================*/

    function manuScroll() {
        "use strict";
        smartScroll.init({
            speed: 900,
            offset: 0,
            addActive: true,
            activeClass: "active",
        });
    }

    /*==================
        5 Isotope
    ==================*/

    function isotope() {
        "use strict";
        var portfolioFilterBtn = $(".arfo-demo-btn button"),
            portfolioGalleryWrap = $(".arfo-demo-btn");

        // Porfolio Filtering Click Events
        portfolioFilterBtn.on("click", function() {
            portfolioFilterBtn.removeClass('active');
            $(this).addClass('active');
        });

        // Portfolio Masonary Gallery
        portfolioGalleryWrap.imagesLoaded(function() {
            var $grid = $(".arfo-demo").isotope({
                itemSelector: ".arfo-item",
                percentPosition: true,
            });
            portfolioFilterBtn.on("click", function() {
                var filterValue = $(this).attr('data-filter');
                $grid.isotope({
                    filter: filterValue
                });
            });
        });
    }

    /*==================
        9 Bottom Top
    ==================*/
    function bottomTop() {
        "use strict";
        var bottomTop = ".main-footer .btton-top-btn a";
        // Smooth bottom to top
        $(bottomTop).on("click", function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000); // The number here represents the speed of the scroll in milliseconds
                    return false;
                }
            }
        });
    }

})(jQuery);