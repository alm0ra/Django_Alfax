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
    sideBar()
    venobox()
    bottomTop()
    manuScroll()
    banner()
    counterUp()
    isotope()
    clients()
    brand()
    wow()
    parallaxBanner()
    ripples()

    /*====== Active Plugins ======

        1 Queryloader2
		
		2 Side Bar
		
		3 Venobox
		
		4 Bottom Top
		
		5 Manu Scroll

        6 Banner

        7 Counter Up

        8 Isotope

        9 Clients

        10 Brand
		
        11 Wow
		
		12 Parallax Banner

        13 Ripples Banner

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
        2 Side Bar
    =======================*/

    function sideBar() {
        "use strict";

        $(".side-bar .side-btn").on("click", function() {
            $(this).toggleClass("active");
            $(".side-bar, main, footer").toggleClass("active");
        });
        $(".side-bar a").on("click", function() {
            $(".side-bar.active, .side-bar.active .side-btn.active").removeClass("active");
        });
        $(".side-bar .user-panel").on("click", function() {
            $(this).toggleClass("active");
            $(".side-bar .user-content ").animate({
                display: 'block',
                height: 'toggle',
            });
        })
    }

    /*==================
        3 Venobox
    ==================*/

    function venobox() {
        "use strict";
        var popup = $(".venobox");
        $(popup).venobox();
    }

    /*==================
        4 Bottom Top
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

    /*=====================
        5 Manu Scroll
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

    /*=====================
        6 Banner
    =======================*/
    function banner() {
        "use strict";
        $(".banner-img").owlCarousel({
            items: 1,
            nav: false,
            loop: true,
            mouseDrag: false,
            touchDrag: false,
            pullDrag: false,
            freeDrag: false,
            autoplay: true,
            autoplayTimeout: 7000,
            animateIn: "animate__fadeOut",
        });
    }


    /*==================
        7 Counter Up
    ==================*/
    function counterUp() {
        "use strict";
        $(".counter").counterUp({
            delay: 10,
            time: 1000
        });
    }

    /*==================
        8 Isotope
    ==================*/

    function isotope() {
        "use strict";

        var portfolioFilterBtn = $('.portfolio-demo-btn button'),
            portfolioGalleryWrap = $('.portfolio-demo-btn');

        // Porfolio Filtering Click Events
        portfolioFilterBtn.on("click", function() {
            portfolioFilterBtn.removeClass('active');
            $(this).addClass('active');
        });

        // Portfolio Masonary Gallery
        portfolioGalleryWrap.imagesLoaded(function() {
            var $grid = $('.portfolio-demo').isotope({
                itemSelector: '.portfolio-item',
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
        9 Clients
    ==================*/
    function clients() {
        "use strict";
        $(".clients .clind-ariya").slick({
            autoplay: true,
            slidesToShow: 1,
            autoplaySpeed: 7000,
            infinite: true,
            pauseOnFocus: false,
            pauseOnHover: false,
            arrows: true,
            fade: true,
            nextArrow: '<button class="btn-next"><i class="fas fa-long-arrow-alt-right"></i></button>',
            prevArrow: '<button class="btn-prev"><i class="fas fa-long-arrow-alt-left"></i></button>',
        });
        $(".clients .clind-ariya-v2").slick({
            infinite: false,
            dots: false,
            arrows: true,
            slidesToShow: 2,
            autoplay: true,
            autoplaySpeed: 3000,
            speed: 1000,
            pauseOnFocus: false,
            pauseOnHover: false,
            slidesToScroll: 1,
            nextArrow: '<button class="btn-next"><i class="fas fa-long-arrow-alt-right"></i></button>',
            prevArrow: '<button class="btn-prev"><i class="fas fa-long-arrow-alt-left"></i></button>',
            responsive: [{
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 1,
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });
    }

    /*==================
        10 Brand
    ==================*/
    function brand() {
        "use strict";
        $(".brand-logos").slick({
            infinite: true,
            dots: false,
            arrows: false,
            slidesToShow: 5,
            autoplay: true,
            autoplaySpeed: 1000,
            speed: 1000,
            pauseOnHover: true,
            slidesToScroll: 1,
            responsive: [{
                    breakpoint: 1200,
                    settings: {
                        slidesToShow: 4,
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        slidesToShow: 3,
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                    }
                },
                {
                    breakpoint: 481,
                    settings: {
                        slidesToShow: 1,
                    }
                }
            ]
        });
    }

    /*==================
        11 Wow
    ==================*/
    function wow() {
        "use strict";
        wow = new WOW({
            animateClass: "animate__animated",
            offset: 0,
        });
        wow.init();
    }

    /*=====================
        12 Parallax Banner
    =======================*/
    function parallaxBanner() {
        "use strict";
        $(".parallaxie").parallaxie({
            speed: 0.5,
            offset: 0,
        });
    }

    /*=====================
        13 Ripples Banner
    =======================*/
    function ripples() {
        "use strict";
        $('.wAnimated').ripples({
            resolution: 900,
            dropRadius: 5, //px
            perturbance: 0.5,
        });
    }
})(jQuery);