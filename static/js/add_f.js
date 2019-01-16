function add_f()
{
    data_a = {
            dep: $("#id_dep_point").val(),
            arr: $("#id_arr_point").val(),
            dep_time: $("#id_dep_time").val(),
            arr_time: $("#id_arr_time").val()
    }
    ajaxxx("add_f/", function () {
        $("#error").html("Успех:)");
        $("#error").css("color", "green");
        dep: $("#id_dep_point").val("");
        arr: $("#id_arr_point").val("");
        dep_time: $("#id_dep_time").val("");
        arr_time: $("#id_arr_time").val("");
    }, function () {
        $("#error").html("Не сработало(");
        $("#error").css("color", "red");
    }, data_a )
}

$("#btn").click(add_f);
