$("#search").click(start_search);

var datas;

function help(index_ar, i) {
        var id1 = datas[index_ar];
        data_to_ajax = {
            dep: $("#id_dep").val(),
            arr: $("#id_arr").val(),
            dep_time: $("#id_ddt").val(),
            id1: id1,

        };
        ajaxxx("search_view/", function (data) {
            var info=JSON.parse(data);
            console.log(info);
            $("#dtm".concat(i)).html(info[0].time);
            $("#atm".concat(i)).html(info[0].time2);
            $("#dpt".concat(i)).html(info[0].from);
            $("#apt".concat(i)).html(info[0].to);
        }, function (){}, data_to_ajax)
    }

function get_info(index_ar) {
    return function () {
        for (var i = 0; (i < 4) & (datas.length > index_ar + i); i++){
            help(index_ar + i, i + 1);

        }
        if (i < 4){
            for (i = i; i < 4; i++){
            $("#dtm".concat(i)).html("");
            $("#atm".concat(i)).html("");
            $("#dpt".concat(i)).html("");
            $("#apt".concat(i)).html("");
        }
        }
    }
}

function searcher1() {
    data_to_ajax = {dep: $("#id_dep").val(),
            arr: $("#id_arr").val(),
            dep_time: $("#id_ddt").val()};

    let res1 = ajaxxx("search_view/", function (data) {
        datas=JSON.parse(data);
        if (datas.length == 0){
        $("#error").html("0 результатов:'(")}
        else{
            $("#my_form").css("display","none");
            $("#table_rez").css("display", "block");
            var j = 1;
            var b = document.createElement("input");
            b.onclick = (get_info(0));
            b.type = ("button");
            b.value = (j);
            b.click();
            document.getElementById("btns").appendChild(b);
            for (var i=0; i < datas.length; i++)
            {
                console.log(i);
                if ((i) % 4 == 0 && i != 0)
                {
                    j++;
                    b = document.createElement("input");
                    b.onclick = (get_info(i));
                    b.type = ("button");
                    b.value = (j);
                    document.getElementById("btns").appendChild(b);
                }

            }
        }

        }, function () {alert("err");}, data_to_ajax);
    return res1;
}

function start_search() {
    searcher1()
}