from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.

def contacto(request):
    '''
    carga la vista de contactos, y envia un email a
    la casilla de email contenida en email_para
    '''
    contexto = {'title': 'Contacto'}
    if request.method == 'POST':
        email_de = request.POST['email']
        name = cleaner_form(request.POST["nombre"])
        mesaje = cleaner_form(request.POST["mensaje"])
        mensaje = f"De {name}\nEmail: {email_de}\n{mesaje}"
        asunto = cleaner_form(request.POST['asunto'])
        email_para = ['lucianocanales@gmail.com']
        send_mail(asunto, mensaje, email_de, email_para)
        messages.success(
            request,
            "Mensaje enviado correctamente, "
            "pronto nos pondremos en contacto con usted")
        return redirect('/contacto/', contexto)

    return render(request, 'contacto/contacto.html', contexto)


def cleaner_form(argument):
    '''
    limpia el campo de entrada quitando etiquestas script
    '''
    temp = argument.replace("<scirpt>", "")
    argument = temp.replace("</script>", "")
    return(argument)
