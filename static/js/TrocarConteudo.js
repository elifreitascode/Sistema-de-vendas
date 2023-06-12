$(document).ready(function(){
    $("#idVen").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: "/vendas",
            success: function(data){
                $("#conteudo").html(data)
            },
            error: function(){

            }
        })
    });
});
$(document).ready(function(){
    $("#idHome").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: "/home",
            success: function(data){
                $("#conteudo").html(data)
            },
            error: function(){

            }
        })
    });
});