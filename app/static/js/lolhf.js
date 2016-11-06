$(function () {
    var t = document.getElementsByClassName("defaultimg");
    for (var i = 0; i < t.length; i++) {
        t.item(i).onerror = function () {
            this.src = "/static/img/gameid/defaultimg.png";
            this.onerror = null;
        }
    }
});
$(function () {
    $("a.btn-ladder").click(function () {
        $(this).removeClass("btn-default");
        $(this).addClass("btn-primary");
        $(this).siblings().removeClass("btn-primary");
        $(this).siblings().addClass("btn-default");
        if ($(".btn-ladder.btn-primary").text() == '只看路人王') {
            $("th").remove('.withpro');
        } else {
            $("th").remove();
            var th1 = '<th>#</th>';
            var th2 = '<th class="withpro">比赛ID</th>';
            var th3 = '<th class="withpro">队伍</th>';
            var th4 = '<th class="withpro">位置</th>';
            var th5 = '<th>游戏ID</th>';
            var th6 = '<th>分数</th>';
            var th7 = '<th>隐藏分</th>';
            var th8 = '<th>胜场</th>';
            var th9 = '<th>胜率</th>';
            var th10 = '<th>近20场胜率</th>';
            var th11 = '<th>近20场KDA</th>';
            var th12 = '<th>近20场击杀参与率</th>';
            $("thead>tr").append(th1, th2, th3, th4, th5, th6, th7, th8, th9, th10, th11, th12);
        }
        var url = this.href;
        $(".ladder-row").empty().load(url);
        return false;
    });
});
$(function () {
    var page = 1;
    $(window).scroll(function () {
        var url = $('.btn-primary.btn-ladder').attr('href');
        var args = {'page': page};
        if (url == '' || url == undefined || url == null) {
            url = '/query';
            $(".left_filter .active").each(function () {
                args[$(this).parent().parent().attr("class")] = $(this).text();
            });
            args['page'] = page;
        }
        if ($(document).height() - $(this).scrollTop() - $(this).height() < 1) {
            $.post(url, args, function (data) {
                if (data) {
                    $(".ladder-row").append(data);
                    page++;
                } else {
                    // alert('no more data');
                    return false;
                }
            });
        }
    });
});
$(function () {
    $(".left_filter a").click(function () {
        $(this).parent().siblings().children().removeClass("active");
        $(this).addClass("active");
        var url = '/query';
        var args1 = {};
        var args2 = {};
        $(".left_filter .active").each(function () {
            args1[$(this).parent().parent().attr("class")] = $(this).text();
            args2[$(this).parent().parent().attr("class")] = $(this).text();
        });
        args1['region'] = 'list';
        args2['region'] = 'img';
        $.post(url, args1, function (data) {
            if (data) {
                $(".ladder-row").empty().append(data);
            } else {
                alert('指定条件没有查询到数据');
                return false;
            }
        });
        $.post(url, args2, function (data) {
            if (data) {
                $(".player_list").empty().append(data);
            } else {
                alert('指定条件没有查询到数据');
                return false;
            }
        });
    });
});




