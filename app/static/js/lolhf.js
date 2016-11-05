$(function () {
    $("a.btn-ladder").click(function () {
        $(this).removeClass("btn-default");
        $(this).addClass("btn-primary");
        $(this).siblings().removeClass("btn-primary");
        $(this).siblings().addClass("btn-default");
        var url = this.href;
        var args = {"type": this.id};
        $(".table-ladder").empty().load(url, args);
        return false;
    });
});
$(function () {
    var t = document.getElementsByClassName("defaultimg");
    for (var i = 0; i < t.length; i++) {
        t.item(i).onerror = function () {
            this.src = "/static/img/gameid/defaultimg.png";
            this.onerror = null;
        }
    }
});
