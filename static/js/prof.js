

function go() {
   document.getElementById("img_form").submit();

}
function prof() {
    document.getElementById("id_image").onchange=go;
    console.log("Сработало?");
    console.log(document.getElementById("id_image").onchange);
}