function enviar_respuesta_peticion(idpet,acept){
    $.post(url_tramitar_peticion_partida+"?"+acept+"="+idpet,function(data, status) {
        $($('#idpet'+idpet)[0]).html("La batalla contra "+data[0][0]+" ha sido "+data[0][1]);
    })
    .error(function(e) {
        $($('#idpet'+idpet)[0]).html("No se puede acceder al servidor");
    });
}

function enviarpeticion(formulario){
    var lista= formulario.oponente
    var elegida = lista.options[lista.selectedIndex]
    var cadena = 'oponente='+elegida.value;
    $.post(url_nueva_peticion_partida,cadena,function(data,status){
        
        $(formulario).parent().html('<blockquote><p class="">'+data+'</p></blockquote>');
    });
}
