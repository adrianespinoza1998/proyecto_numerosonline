$(document).ready(function () {
    //Fade in Body
    $('body').css('display','none');
    $('body').fadeIn(1000);
    //$('body').fadeOut(1000);

    $('#btnIngresar').click(function () {
        var email=$('#mail').val();
        var password=$('#password').val();

        if(email=='' || password==''){
            alert('Uno o más campos vacios');
        }else{
            if(email=='correo@prueba' && password=='12345'){
                //$('body').fadeOut(500);
                window.location = "home.html"; // Redirige a otra pagina.
                return false;
            }else{
                alert('Correo o contraseña incorrectos');
            }
        }
    });
});
