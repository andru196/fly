var errs= [1,1,1];


function checker() {
    if (errs[0] == 0 && errs[1] == 0 && errs[2] == 0)
    {
        document.getElementById("error").innerHTML = "";
        document.getElementById("click").style.backgroundColor = "#3caa3c";
        document.getElementById("click").disabled = false;
    }
    else {
        document.getElementById("click").disabled = true;
        document.getElementById("click").style.backgroundColor = "lightgrey";
    }


}

function verification_reg_pswrd() {
    if (document.getElementById("id_password").value !== document.getElementById("id_password_ver").value)
    {
        document.getElementById("click").style.backgroundColor = "lightgrey";
        document.getElementById("error").innerHTML = "Пароли не совпадают!!";
        errs[0] = 1;
        return;
    }
    if (document.getElementById("id_password").value.length < 6)
    {
        document.getElementById("error").innerHTML = "Не достаточно символов";
        document.getElementById("click").style.backgroundColor = "lightgrey";
        errs[0] = 1;
        return;
    }
    if (document.getElementById("error").innerHTML=="Не достаточно символов" || document.getElementById("error").innerHTML=="Пароли не совпадают!!"){
        document.getElementById("error").innerHTML = "";

    }
    errs[0] = 0;
    checker();
}

function prof() {
    document.getElementById("id_password_ver").onchange=verification_reg_pswrd;
    document.getElementById("id_password").onchange=verification_reg_pswrd;
    document.getElementById("id_password").oninput=verification_reg_pswrd;
    document.getElementById("id_password_ver").oninput=verification_reg_pswrd;
    document.getElementById("id_email").onchange=check_reg_mail;
    document.getElementById("id_username").onchange=check_reg_login;
    document.getElementById("click").disabled = true;
    console.log("отработал");
}



function check_reg_mail()
{
    data_a = {
            email: $("#id_email").val()
    }
    ajaxxx("check_email/", function (data) {
        if (data == "OK")
        {$("#error").html("");
        errs[1] = 0;
        checker();
        }
        else{
            $("#error").html("email занят(");
            $("#error").css("color", "red");
            errs[1] = 1;

        }

    }, function () {
        $("#error").html("Не сработало(");
        $("#error").css("color", "red");
        errs[1] = 1;
    }, data_a )
}
function check_reg_login()
{
    data_a = {
            log: $("#id_username").val()
    }
    ajaxxx("check_login/", function (data) {
        if (data == "OK")
        {
            $("#error").html("");
            errs[2] = 0;
            checker();
        }
        else{
            $("#error").html("логин занят(");
            $("#error").css("color", "red");
            errs[2] = 1;

        }

    }, function () {
        $("#error").html("Не сработало(");
        $("#error").css("color", "red");
        errs[2] = 1;
    }, data_a )
}