# views.py
import git
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook_deploy(request):
    # Validação do token de segurança
    if request.headers.get('X-Secret-Token') != os.getenv('DEPLOY_TOKEN'):
        return HttpResponse('Acesso não autorizado', status=403)
    
    try:
        repo = git.Repo('/home/ricardoh/ricardoh.pythonanywhere.com')
        origin = repo.remotes.origin
        origin.pull('master')
        
        # Atualização de dependências
        with open('/tmp/update.log', 'w') as f:
            f.write(str(repo.git.execute(['pip', 'install', '-r', 'requirements.txt'])))
        
        # Recarregamento do aplicativo
        wsgi_path = 'var/www/ricardoh_pythonanywhere_com_wsgi.py'
        os.utime(wsgi_path, None)
        
        return HttpResponse('Deploy realizado com sucesso', status=200)
    except Exception as e:
        return HttpResponse(f'Erro: {str(e)}', status=500)
