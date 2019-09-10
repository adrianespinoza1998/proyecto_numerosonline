$(document).ready(function () {
    $('#registrarse').click(function () {
        var pNombre=$('#pNombre').val();
        var apPaterno=$('#apPaterno').val();
        var apMaterno=$('#apMaterno').val();
        var email=$('#email').val();
        var rut=$('#rut').val();

        if(pNombre=='' || apPaterno=='' || apMaterno=='' || email=='' || rut==''){
            alert('Faltan uno o mas campos');
        }
    });
});