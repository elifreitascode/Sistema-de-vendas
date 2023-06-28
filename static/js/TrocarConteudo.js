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
$(document).ready(function(){
    $("#idProd").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: "/produtos",
            success: function(data){
                $("#conteudo").html(data)
            },
            error: function(){

            }
        })
    });
});
$(document).ready(function(){
    $("#idClie").click(function(event) {
        event.preventDefault();
        $.ajax({
            url: "/clientes",
            success: function(data){
                $("#conteudo").html(data)
            },
            error: function(){

            }
        })
    });
});