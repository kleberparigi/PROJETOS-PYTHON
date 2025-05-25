SENHAS:
senha: python2024 da primeira aula
senha: analisedados2024 da segunda aula 
senha: ia2024python da terceira aula
senha: 

JÁ INSTALADO E IMPORTAR AS BIBLIOTECAS:

import pyautogui
pip install openpyxl
import pandas as pd 

PIP INSTALL PANDAS NUMPY OPENPYXL
exemplo: !pip install pandas numpy openpyxl 
import pandas 

from flask import Flask
import numpy as np
from powerbiclient import Report, models
import pyodbc

************************************************************
--AULA 01;

Para fazer o download do Arquivo da Aula: 
https://drive.google.com/drive/folder...

Para acessar o controle de estoque fictício da Hashtag:
https://dlp.hashtagtreinamentos.com/p...

Instalando o VSCode para Python: https://www.youtube.com/watch?v=Zy3ia...
Instalando o Jupyter dentro do VSCode: https://www.youtube.com/watch?v=2a87x...

Programando horário para rodar seu código: https://www.youtube.com/watch?v=SxEjH...

IMPORTAR A BIBLIOTECA 

import pyautogui

01- instalar vscode (admin e na versão do note)
02- instalar extensão python em vscode (pode usar ctrl + shift + P 

ctrl + shift + p 
Abre configurações e atalhos


03- instalar python (python download)
04- instalar extensão dentro do vscode o jupyter
05- instalar anaconda 
06- pip install pandas 
pip install openpyxl

07- 
import pandas as pd 
tabela = pd.dataframe()
display(tabela)

08- 

import pandas as pd 
tabela = pd.dataframe(
{"Nome": ["Kleber Parigi", "Jamile Couto"],
"idade": [35, 32]}
)
display(tabela)

*******************************************

importando bibliotecas:
REQUESTS - INTERAÇÃO ENTRE APIS

pip install requests

import requests

Depois de importar a biblioteca requests, você pode usar suas funcionalidades, como fazer solicitações HTTP. Por exemplo:

import requests

url = 'https://www.exemplo.com'
response = requests.get(url)

print(response.text)

*********************************************
PIP INSTALL PANDAS NUMPY OPENPYXL
exemplo: !pip install pandas numpy openpyxl 

import pandas 

********************************************

flask criar apis e sites 

pip install Flask

from flask import Flask

Em um script Python, você colocaria a importação no início do arquivo. Em um notebook Jupyter, você pode colocar a importação em uma célula de código e executá-la.

Aqui está um exemplo mínimo de como você pode criar uma aplicação Flask:

python
Copy code
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
    
 ***************************************
 
 pip install numpy
 
 import numpy as np
 
 Em um script Python, você colocaria a importação no início do arquivo. Em um notebook Jupyter, você pode colocar a importação em uma célula de código e executá-la.

Aqui está um exemplo básico de como você pode usar NumPy para criar um array:

python
Copy code
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
Este é um exemplo mínimo, mas NumPy oferece muitas funcionalidades poderosas para trabalhar com arrays multidimensionais e realizar operações matemáticas eficientes. Adapte o código conforme necessário para atender aos seus requisitos específicos.

*****************************************
pip install powerbiclient

from powerbiclient import Report, models

Lembre-se de que a interação com o Power BI geralmente envolve autenticação e uso de tokens de acesso. Certifique-se de seguir as instruções e documentação fornecidas pela Microsoft e pela biblioteca powerbiclient para configurar corretamente a autenticação.

Observe que novas bibliotecas podem ser lançadas após a minha última atualização em janeiro de 2022, portanto, sempre verifique a documentação mais recente e os recursos disponíveis.

****************************************

SQL COM PYTHON:

para integração com sql e python preciso de uma biblioteca
python odbc
pyodbc

pip install pyodbc 

import pyodbc
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=AURUM\\SQL2019;"
    "Database=THEMIS_KLEBER"
)

conexao = pyodbc.connect(dados_conexao)
print("conexão bem sucedida")

APÓS ISSO ESTÁ CONECTADO COM O BANCO DE DADOS EM QUESTÃO.

************************
DEPOIS:

comando_sql = "select id_processo, pasta , numproc, titproc, status, DATA_ENTRADA, DATA_INICIO, DATA_ENCER from processo"

dados = pd.read_sql(comando_sql,conexao)

************************
DEPOIS:

display(dados)

************************

dados.groupby(nome da field).o que desejar exemplo count ou max ()

dados.groupby(status).count()

resultado_agrupado = dados2.groupby('nm_area').count()
Se você quiser contar o número de ocorrências de cada valor único na coluna 'nm_area', você pode fazer o seguinte:

python
Copy code
contagem_por_area = dados2['nm_area'].value_counts()


ARMAZENAR O RESULTADO DA CONSULTA EM PYTHON PARA CRIAR UM GRÁFICO

df.dados3

display(df)

GRÁFICO:

df.plot
df.plot(kind="bar")

funcionou:

resultado_agrupado = dados3.groupby('area').count()

display(resultado_agrupado)

df=resultado_agrupado

display(df)

df.plot(kind="bar")


tudo que for lista dentro do python é com []


********************************************************************************************************************************************************************
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Sim, você pode criar um executável em Python (por exemplo, usando PyInstaller ou cx_Freeze) e, em seguida, chamar esse executável de um programa Java. Da mesma forma, se você criar um serviço ou API em Python, um programa Java pode interagir com esse serviço ou API.

1. Executável Python chamado por Java:
Criar Executável Python:

Use ferramentas como PyInstaller ou cx_Freeze para criar um executável a partir do seu script Python.
Chamando o Executável Python de Java:

No Java, você pode usar a classe ProcessBuilder para chamar um executável externo. Aqui está um exemplo simples:

import java.io.IOException;

public class ChamarPython {
    public static void main(String[] args) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("caminho_para_seu_executavel_python.exe", "argumento1", "argumento2");
            Process process = processBuilder.start();

            // Aguarda até que o processo termine
            int exitCode = process.waitFor();
            System.out.println("O processo Python terminou com código de saída: " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}


2. API Python chamada por Java:
Criar uma API em Python:

Use frameworks como Flask ou Django para criar uma API em Python.
Chamando a API Python de Java:

No Java, você pode usar bibliotecas como HttpClient para fazer solicitações HTTP à sua API. Aqui está um exemplo básico:

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ChamarAPIPython {
    public static void main(String[] args) {
        HttpClient httpClient = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://seu_servidor_python:porta/sua_api"))
                .build();

        try {
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Resposta da API: " + response.body());

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}



Sim, você pode criar um executável em Python (por exemplo, usando PyInstaller ou cx_Freeze) e, em seguida, chamar esse executável de um programa Java. Da mesma forma, se você criar um serviço ou API em Python, um programa Java pode interagir com esse serviço ou API.

1. Executável Python chamado por Java:
Criar Executável Python:

Use ferramentas como PyInstaller ou cx_Freeze para criar um executável a partir do seu script Python.
Chamando o Executável Python de Java:

No Java, você pode usar a classe ProcessBuilder para chamar um executável externo. Aqui está um exemplo simples:

java
Copy code
import java.io.IOException;

public class ChamarPython {
    public static void main(String[] args) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("caminho_para_seu_executavel_python.exe", "argumento1", "argumento2");
            Process process = processBuilder.start();

            // Aguarda até que o processo termine
            int exitCode = process.waitFor();
            System.out.println("O processo Python terminou com código de saída: " + exitCode);

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
2. API Python chamada por Java:
Criar uma API em Python:

Use frameworks como Flask ou Django para criar uma API em Python.
Chamando a API Python de Java:

No Java, você pode usar bibliotecas como HttpClient para fazer solicitações HTTP à sua API. Aqui está um exemplo básico:

java
Copy code
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class ChamarAPIPython {
    public static void main(String[] args) {
        HttpClient httpClient = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://seu_servidor_python:porta/sua_api"))
                .build();

        try {
            HttpResponse<String> response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Resposta da API: " + response.body());

        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
Melhor Maneira:
A escolha entre um executável Python ou uma API dependerá dos requisitos específicos do seu sistema e da arquitetura que você deseja implementar. Se você precisa de comunicação mais flexível e interativa, uma API pode ser mais adequada. Se a execução é mais simples e não requer interação em tempo real, um executável pode ser suficiente.

Lembre-se de considerar a segurança, a escalabilidade e outros requisitos específicos do seu projeto ao tomar decisões sobre a arquitetura.


