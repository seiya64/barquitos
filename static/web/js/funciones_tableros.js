var temporizador = true;

jQuery(document).ready(function(e) {
    var obtener_tableros = function(e) {
        if (temporizador == true){
            $.post(url_obtener_tableros, function(data,status){
                trae_tableros(data,status);
                setTimeout(obtener_tableros, 5000);
            })
            .error(function(e) {
                $('#tablero_ataque').html("No se puede acceder al servidor");
                $('#tablero').html("No se puede acceder al servidor");
                setTimeout(obtener_tableros, 10000);
            });
        }
        else{
            clarTimeout(obtener_tableros);
        }
    };
    setTimeout(obtener_tableros, 1);
});

function htmlEntities(str) {
    return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

function atacar(id){
    var coordenadas = id.split("_");
    $.post(url_atacar+"?x="+coordenadas[0]+"&y="+coordenadas[1], function(data, status){
        //alert(data);
        trae_tableros();
    });
    
}

function trae_tableros(data, status){
    if (data[0] == "ganas"){
        $('#tablero_ataque').html("<h1><small class=\"text-success\">Has ganado la partida</small></h1>");
        $('#tablero').html("<h1><small class=\"text-success\">Tu oponente pierde la partida</small></h1>");
        temporizador = false;
    }
    else if (data[0] == "pierdes"){
        $('#tablero_ataque').html("<h1><small class=\"text-error\">Tu oponente gana la partida</small></h1>");
        $('#tablero').html("<h1><small class=\"text-error\">Has Perdido la partida</small></h1>");
        temporizador = false;
    }
    else {
        var tablero_ataque = "<table class=\"table table-bordered\">";
        var tablero = "<table class=\"table table-bordered\">";
        var i = 0;
        for (i = 0; i < 10; i++){
            tablero_ataque += "<tr>";
            tablero += "<tr>";
            var j = 0;
            for (j = 0; j < 10; j++){
                tablero_ataque += "<td id ='"+i+"_"+j+"' class=\"";
                if (data[0][i*10 + j] == 0){
                    tablero_ataque += "mar";
                }
                else if (data[0][i*10 + j] == 1){
                    tablero_ataque += "barco";
                }
                else if (data[0][i*10 + j] == 2){
                    tablero_ataque += "tocado";
                }
                else if (data[0][i*10 + j] == 3){
                    tablero_ataque += "agua";
                }
                else {
                    tablero_ataque += "vacio";
                }
                //tablero_ataque += "\">"+data[0][i*10 + j]+"</td>";
                tablero_ataque += "\">&nbsp</td>";

                tablero += "<td class=\"";
                if (data[1][i*10 + j] == 0){
                    tablero += "mar";
                }
                else if (data[1][i*10 + j] == 1){
                    tablero += "barco";
                }
                else if (data[1][i*10 + j] == 2){
                    tablero += "tocado";
                }
                else if (data[1][i*10 + j] == 3){
                    tablero += "agua";
                }
                else {
                    tablero += "vacio";
                }
                //tablero += "\">"+data[1][i*10 + j]+"</td>";
                tablero += "\">&nbsp</td>";
            }
            tablero_ataque += "</tr>";
            tablero += "</tr>";
        }
        tablero_ataque += "</table>";
        tablero += "</table>";
        $('#tablero_ataque').html(tablero_ataque);
        $('#tablero').html(tablero);
        var celdas = $('.mar');
        for (var i = 0; i < celdas.length; i++){
            $(celdas[i]).bind('click', function(){
                atacar($(this).attr('id'));
            });
        }
        if (data[2]=="turno"){
            $('#turno').html('Te toca!');
        }
        else{
            $('#turno').html('Espera a tu oponente');
        }
        
    }
}

function abandonar(){
    $.post(url_abandonar,function(data,status){
        if (data[0] == "ok"){
            $('#tablero_ataque').html("<h1><small class=\"text-error\">Te has rendido</small></h1>");
        }
    });
}
