import git
import os
import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def webhook_deploy(request):
    # Validação do token de segurança
    if request.headers.get('X-Secret-Token') != settings.WEBHOOK_DEPLOY_TOKEN:
        return HttpResponse('Acesso não autorizado', status=403)
    
    try:
        repo_path = '/home/ricardoh/ricardoh.pythonanywhere.com'
        repo = git.Repo(repo_path)
        origin = repo.remotes.origin
        origin.pull('master')
        
        # Atualização de dependências com subprocess
        requirements_path = os.path.join(repo_path, 'requirements.txt')
        pip_result = subprocess.run(
            ['pip', 'install', '-r', requirements_path],
            capture_output=True, 
            text=True
        )
        
        # Log do resultado
        with open('/tmp/update.log', 'w') as f:
            f.write(f"PIP STDOUT:\n{pip_result.stdout}\n\nPIP STDERR:\n{pip_result.stderr}")
        
        # Verificar se a instalação foi bem sucedida
        if pip_result.returncode != 0:
            raise Exception(f"Falha na instalação de dependências: {pip_result.stderr}")
        
        # Recarregamento do aplicativo
        wsgi_path = '/var/www/ricardoh_pythonanywhere_com_wsgi.py'
        os.utime(wsgi_path, None)
        
        return HttpResponse('Deploy realizado com sucesso', status=200)
    except Exception as e:
        return HttpResponse(f'Erro no deploy: {e}', status=500)
