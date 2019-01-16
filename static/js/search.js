$("#search").click(start_search);

var datas;

function help(index_ar, i) {    //получаем индекс массива, и номе строки в таблие, куда занесём данные
        var id1 = datas[index_ar]; // получем id в БД из массива
        data_to_ajax = {  //генерируем данные для запроса
            dep: $("#id_dep").val(),
            arr: $("#id_arr").val(),
            dep_time: $("#id_ddt").val(),
            id1: id1,

        };
        ajaxxx("search_view/", function (data) { //сам запрос
            var info=JSON.parse(data); //полученный объект парсим
            console.log(info);
            $("#dtm".concat(i)).html(info[0].time); //по айди элементов заносим данные
            $("#atm".concat(i)).html(info[0].time2); //если что это JSON поиск
            $("#dpt".concat(i)).html(info[0].from); //он круто парсит html
            $("#apt".concat(i)).html(info[0].to);
        }, function (){}, data_to_ajax)//конец вызова ф-ии ajaxxx
    }

function get_info(index_ar) {  //генератор функций, принимает индекс массива айдишек рейсов изБД
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
    data_to_ajax = {dep: $("#id_dep").val(), //Здесь задаём данные для отправки запроса
            arr: $("#id_arr").val(),
            dep_time: $("#id_ddt").val()};

    let res1 = ajaxxx("search_view/", function (data) { //Это модифицированный аякас запрос из соседнего файла, ему мы передаём: адрес
        datas=JSON.parse(data);                                     // ему мы передаём: адрес, две функции и наши данные
        if (datas.length == 0){                                 //Функции мы объвляем прямо внутри вызова айакс функции
        $("#error").html("0 результатов:'(")}                   //в основном работает 1-я функции, потому что она вызывается при
        else{                                                    //успешном зпросе аякс
            $("#my_form").css("display","none");                //мы получаем данные (data), но они данны как строка, потому парсим
            $("#table_rez").css("display", "block");            //затем мы проверяем не пустой ли массив пришёл
            var j = 1;                                          //если нет мы по id ищем форму и скрываем её
            var b = document.createElement("input");    //по айди ищем таблицу и наоборот отображаем её
            b.onclick = (get_info(0));          //затем мы создаём кнопку и цепляем на неё свойства, в том
            b.type = ("button");                                    //числе действие при нажатии
            b.value = (j);
            b.click();      //здесь мы сразу нажимаем кнопку, чтоб отобразить первую страницу
            document.getElementById("btns").appendChild(b); //созданную кнпку нужно обязательно куда-то прикрепить
            for (var i=0; i < datas.length; i++)        //иначе она не отобразиться
            {
                console.log(i);
                if ((i) % 4 == 0 && i != 0)  //повторяем нескольк раз
                {
                    j++;
                    b = document.createElement("input");
                    b.onclick = (get_info(i)); //тут и цепляем действие: функция возвращает функцию!
                    b.type = ("button");
                    b.value = (j);
                    document.getElementById("btns").appendChild(b);
                }

            }
        }

        }, function () {alert("err");}, data_to_ajax); //только здесь мы заканчиваем передавать аргуементы в функцию
    return res1;
}

function start_search() {
    searcher1()
}