
function verification_reg_pswrd() {
    if (document.getElementById("id_password").value !== document.getElementById("id_password_ver").value)
    {
        document.getElementById("click").style.backgroundColor = "lightgrey";
        document.getElementById("error").innerHTML = "Пароли не совпадают!!";
        return document.getElementById("error").disabled = disabled;
    }
    if (document.getElementById("id_password").value.length < 6)
    {
        document.getElementById("error").innerHTML = "Не достаточно символов";
        document.getElementById("click").style.backgroundColor = "lightgrey";
        return document.getElementById("error").disabled = disabled;

    }
    document.getElementById("error").innerHTML = "";
    document.getElementById("click").style.backgroundColor = "#3caa3c";
    document.getElementById("click").disabled = false;
}
function prof() {
    document.getElementById("id_password_ver").onchange=verification_reg_pswrd;
    document.getElementById("id_password").onchange=verification_reg_pswrd;
    document.getElementById("id_password").oninput=verification_reg_pswrd;
    document.getElementById("id_password_ver").oninput=verification_reg_pswrd;
    console.log("отработал");
}
