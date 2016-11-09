$(function () {
    var listpage = 1;
    var scroll_flag = 1;
    var imgpage = 0;
    var previous_able = 0;
    var next_able = 1;
    //handel lost img error
    var t = document.getElementsByClassName("defaultimg");
    for (var i = 0; i < t.length; i++) {
        t.item(i).onerror = function () {
            this.src = "/static/img/gameid/defaultimg.png";
            this.onerror = null;
        }
    }
    //hadle ladder page button click event
    $("a.btn-ladder").click(function () {
        listpage = 1;
        scroll_flag = 1;
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
    //handel click event for left filter of query page
    $(".left_filter a").click(function () {
        $(this).parent().siblings().children().removeClass("active");
        $(this).addClass("active");
        imgpage = 0;
        previous_able = 0;
        next_able = 1;
        listpage = 1;
        scroll_flag = 1;
        $(".nav-pager .forward").removeClass("disabled");
        $(".nav-pager .backward").addClass("disabled");
        var url = '/query';
        var args1 = {};
        var args2 = {};
        $(".left_filter .active").each(function () {
            args1[$(this).parent().parent().attr("class")] = $(this).text();
            args2[$(this).parent().parent().attr("class")] = $(this).text();
        });
        args1['region'] = 'list';
        args1['listpage'] = 0;
        args2['region'] = 'img';
        args2['imgpage'] = 0;
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
                // alert('指定条件没有查询到数据');
                return false;
            }
        });
    });
    //handle scroll event for player table list of query page
    $(window).scroll(function () {
        var pageurl = window.location.pathname;
        if (pageurl.indexOf('ladder') > 0 || pageurl.indexOf('query') > 0) {
            var url = $('.btn-primary.btn-ladder').attr('href');
            var args = {'listpage': listpage};
            if (url == '' || url == undefined || url == null) {
                url = '/query';
                $(".left_filter .active").each(function () {
                    args[$(this).parent().parent().attr("class")] = $(this).text();
                });
                args['listpage'] = listpage;
                args['region'] = 'list';
            }
            if ($(document).height() - $(this).scrollTop() - $(this).height() < 1 && scroll_flag == 1) {
                $.post(url, args, function (data) {
                    if (data) {
                        $(".ladder-row").append(data);
                        listpage++;
                    } else {
                        // alert('no more data');
                        scroll_flag = 0;
                        return false;
                    }
                });
            }
        }
    });
    //handle pager click event for player img list of query page
    $(".nav-pager a").click(function () {
        if (!$(this).parent().hasClass("disabled") && imgpage >= 0) {
            var url = '/query';
            var args = {};
            $(".left_filter .active").each(function () {
                args[$(this).parent().parent().attr("class")] = $(this).text();
            });
            if ($(this).text() == '上一页' && previous_able == 1) {
                imgpage--;
                next_able = 1;
                $(".nav-pager .forward").removeClass("disabled");
            }
            if ($(this).text() == '下一页' && next_able == 1) {
                imgpage++;
                previous_able = 1;
                $(".nav-pager .backward").removeClass("disabled");
            }
            args['region'] = 'img';
            args['imgpage'] = imgpage;
            $.post(url, args, function (data) {
                if (data) {
                    $(".player_list").empty().append(data);
                } else {
                    // alert('指定条件没有查询到数据');
                    if (imgpage > 0) {
                        next_able = 0;
                        imgpage--;
                        $(".nav-pager .forward").addClass("disabled");
                    }
                    if (imgpage <= 0) {
                        previous_able = 0;
                        imgpage++;
                        $(".nav-pager .backward").addClass("disabled");
                    }
                    return false;
                }
            });
        }
    });
    //handel help button click event from help page
    var payamount = 0;
    $(".btn-help").click(function () {
        var amount = $(this).siblings("span").text();
        if (!amount) {
            amount = $(this).siblings("input").val();
            amount = parseFloat(amount).toFixed(2);
        }
        payamount = Math.round(amount);
        if (amount) {
            $(".modal-footer .btn-amount").text("￥" + amount);
            $(".modal-footer .btn-pay-amount").text("￥" + amount);
            $('#myModal').modal();
        }
    });
    $(".btn-weixin").click(function () {
        $(".moday-pay-footer .p-pay").text("微信支付");
        $(".moday-pay-footer .p-pay-tip").text("使用微信扫描二维码完成支付");
        var imgpath = "/static/img/help/weixinpay-" + payamount + ".png";
        $(".modal-pay-body img").attr('src', imgpath);
        $(".modal-pay-body img").error(function () {
            imgpath = "/static/img/help/weixinpay.png";
            $(this).attr('src', imgpath);
        });
        $('#payModal').modal();
        var url = '/help';
        var args = {};
        args['from'] = $("#from").val();
        args['name'] = $("#name").val();
        args['server'] = $("#server").val();
        args['gameid'] = $("#gameid").val();
        var mydate = new Date();
        args['date'] = mydate.toLocaleDateString();
        args['amount'] = $(".btn-amount").text();
        args['media'] = $(this).text();
        $.post(url, args,function () {
        });
    });
    $(".btn-zhifubao").click(function () {
        $(".moday-pay-footer .p-pay").text("支付宝支付");
        $(".moday-pay-footer .p-pay-tip").text("使用支付宝扫描二维码完成支付");
        var imgpath = "/static/img/help/alipay-" + payamount + ".jpg";
        $(".modal-pay-body img").attr('src', imgpath);
        $(".modal-pay-body img").error(function () {
            imgpath = "/static/img/help/alipay.jpg";
            $(this).attr('src', imgpath);
        });
        $('#payModal').modal();
        var url = '/help';
        var args = {};
        args['from'] = $("#from").val();
        args['name'] = $("#name").val();
        args['server'] = $("#server").val();
        args['gameid'] = $("#gameid").val();
        var mydate = new Date();
        args['date'] = mydate.toLocaleDateString();
        args['amount'] = $(".btn-amount").text();
        args['media'] = $(this).text();
        $.post(url, args,function () {
        });
    });
});
