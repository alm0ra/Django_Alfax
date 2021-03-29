/*!
 * jquery.counterup.js 2.1.0
 *
 * Copyright 2013, Benjamin Intal http://gambit.ph @bfintal
 * Released under the GPL v2 License
 *
 * Amended by Jeremy Paris, Ciro Mattia Gonano and others
 *
 * Date: Feb 24, 2017
 */
!function(e){"use strict";e.fn.counterUp=function(t){var m,g=e.extend({time:400,delay:10,offset:100,beginAt:0,formatter:!1,context:"window",callback:function(){}},t);return this.each(function(){var p=e(this),h={time:e(this).data("counterup-time")||g.time,delay:e(this).data("counterup-delay")||g.delay,offset:e(this).data("counterup-offset")||g.offset,beginAt:e(this).data("counterup-beginat")||g.beginAt,context:e(this).data("counterup-context")||g.context};p.waypoint(function(t){!function(){var t=[],e=h.time/h.delay,a=p.attr("data-num")?p.attr("data-num"):p.text(),n=/[0-9]+,[0-9]+/.test(a),u=((a=a.replace(/,/g,"")).split(".")[1]||[]).length;h.beginAt>a&&(h.beginAt=a);var o=/[0-9]+:[0-9]+:[0-9]+/.test(a);if(o){var r=a.split(":"),i=1;for(m=0;0<r.length;)m+=i*parseInt(r.pop(),10),i*=60}for(var c=e;c>=h.beginAt/a*e;c--){var s=parseFloat(a/e*c).toFixed(u);if(o){s=parseInt(m/e*c);var f=parseInt(s/3600)%24,l=parseInt(s/60)%60,d=parseInt(s%60,10);s=(f<10?"0"+f:f)+":"+(l<10?"0"+l:l)+":"+(d<10?"0"+d:d)}if(n)for(;/(\d+)(\d{3})/.test(s.toString());)s=s.toString().replace(/(\d+)(\d{3})/,"$1,$2");g.formatter&&(s=g.formatter.call(this,s)),t.unshift(s)}p.data("counterup-nums",t),p.text(h.beginAt);p.data("counterup-func",function(){p.data("counterup-nums")?(p.html(p.data("counterup-nums").shift()),p.data("counterup-nums").length?setTimeout(p.data("counterup-func"),h.delay):(p.data("counterup-nums",null),p.data("counterup-func",null),g.callback.call(this))):g.callback.call(this)}),setTimeout(p.data("counterup-func"),h.delay)}(),this.destroy()},{offset:h.offset+"%",context:h.context})})}}(jQuery);