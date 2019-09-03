$(document).ready(function () {
    //Fade in Body
    $('body').css('display','none');
    $('body').fadeIn(1000);
    //$('body').fadeOut(1000);

    $('#btnIngresar').click(function () {
        var email=$('#mail').val();
        var password=$('#password').val();

        if(email=='' || password==''){
            alert('Uno o mas campos vacios');
        }else{
            if(email=='correo@prueba' && password=='12345'){
                alert('Usuario correcto');
            }else{
                alert('Correo o contraseña incorrectos');
            }
        }
    });
});
