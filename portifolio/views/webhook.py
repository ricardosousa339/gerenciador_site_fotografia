from base import settings
"""
Webhook endpoint for automated deployment via GitHub webhooks.
This view handles incoming webhook requests from GitHub to automatically deploy updates
to a Python Anywhere hosted Django application. It performs the following steps:
1. Validates the incoming request using a secret token
2. Pulls the latest changes from the git repository
3. Updates dependencies via pip
4. Triggers a reload of the WSGI application
Args:
    request: The HTTP request object containing webhook data
Returns:
    HttpResponse: Response indicating success (200) or failure (403, 500)
        - 200: Successful deployment
        - 403: Unauthorized access (invalid token)
        - 500: Deployment error
Security:
    - Uses CSRF exemption as GitHub webhooks don't support CSRF tokens
    - Validates requests using a secret token in X-Secret-Token header
    - Token must match WEBHOOK_DEPLOY_TOKEN in settings
Dependencies:
    - GitPython for repository operations
    - Django for HTTP handling
    - Settings module for configuration
"""
import git
import os
import sys
import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def webhook_deploy(request):
    # Validação do token de segurança
    if request.headers.get('X-Secret-Token') != settings.WEBHOOK_DEPLOY_TOKEN:
        return HttpResponse('Acesso não autorizado', status=403)
    
    try:
        repo = git.Repo('/home/criadordeportifolio/gerenciador_site_fotografia')
        origin = repo.remotes.origin
        origin.pull('master')
        
        # Atualização de dependências usando subprocess com a flag --user
        command = [sys.executable, '-m', 'pip', 'install', '--user', '-r', 'requirements.txt']
        if 'uwsgi' in sys.executable.lower():
            command = ['python3', '-m', 'pip', 'install', '--user', '-r', 'requirements.txt']

        subprocess.check_call(command)
        
        # Recarregamento do aplicativo
        wsgi_path = '/var/www/gerencia_ricardomachado_me_wsgi.py'
        os.utime(wsgi_path, None)
        
        return HttpResponse('Deploy realizado com sucesso', status=200)
    except Exception as e:
        return HttpResponse(f'Erro no deploy: {e}', status=500)
