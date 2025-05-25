pip install gdown
pip install gspread

import gdown
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configurações para acesso à API do Google Drive
credentials = ServiceAccountCredentials.from_json_keyfile_name('sua-chave-de-credencial.json', ['https://spreadsheets.google.com/feeds'])
gc = gspread.authorize(credentials)

# Baixa o programa do Google Drive
programa_url = 'https://drive.google.com/uc?id=1_kPgm-X81aHTJcbunsAR4-RI_KudZFT4'
gdown.download(programa_url, output='nome_do_programa.exe')

# Abre a planilha do Google Sheets
planilha_url = 'https://docs.google.com/spreadsheets/d/1bYUaNZ6rgZ0pOp1iIxMCFNf5p5n5o1mK/edit#gid=0'
planilha = gc.open_by_url(planilha_url)

# Faz o que você precisa com a planilha (exemplo: obtém os valores da primeira folha)
folha = planilha.sheet1
valores = folha.get_all_values()

# Faça o que você precisa com os valores da planilha
print(valores)



*********************************************************************************************
Para criar um arquivo JSON de credenciais para autenticação com a API do Google, você precisará configurar um projeto no Google Cloud Console e habilitar a API que você deseja usar. Aqui estão os passos gerais:

Acesse o Google Cloud Console:

Vá para Google Cloud Console.
Se você não tiver uma conta do Google Cloud, crie uma nova conta e siga as instruções para configurar um projeto.
Crie um novo projeto:

No canto superior direito, clique no menu suspenso e selecione "Novo Projeto".
Siga as instruções para criar um novo projeto.
Ative as APIs:

No painel de navegação à esquerda, clique em "APIs e Serviços" > "Biblioteca".
Pesquise e ative as APIs que você precisará, como "Google Drive API" e "Google Sheets API".
Crie credenciais:

No painel de navegação à esquerda, clique em "APIs e Serviços" > "Credenciais".
Clique em "Criar credenciais" e selecione o tipo de chave que você precisa.
Configure as permissões adequadas para a chave.
Faça o download do arquivo JSON de credenciais.
Forneça permissões no Google Drive:

Certifique-se de que o e-mail associado à sua chave de credencial tenha as permissões adequadas para acessar os arquivos no Google Drive.
A chave de credencial JSON contém as informações necessárias para autenticar seu aplicativo com a API do Google. Essa chave deve ser mantida em segredo e tratada com cuidado, pois dá acesso aos recursos associados ao seu projeto no Google Cloud.

Depois de obter a chave de credencial, você pode usá-la em seu script Python como mostrado no exemplo anterior. Substitua 'sua-chave-de-credencial.json' pelo caminho correto para o seu arquivo JSON de credenciais.