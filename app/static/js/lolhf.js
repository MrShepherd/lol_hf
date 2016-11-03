$(function () {
    var t = document.getElementsByClassName("defaultimg");
    for (var i = 0; i < t.length; i++) {
        t.item(i).onerror = function () {
            this.src = "/static/img/gameid/defaultimg.png";
            this.onerror = null;
        }
    }
    $('.navbar-left li').click(function (e) {
        $(this).addClass('active').siblings().removeClass('active');
        // e.preventDefault();
        // $(this).click();
    });
    // $('.navbar-left .active').click();
});
