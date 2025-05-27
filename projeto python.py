O que você está tentando fazer é criar um programa em Python que pode conectar a diferentes bancos de dados, executar scripts SQL em ordem e depois alimentar uma base de destino que está configurada no arquivo 'application.ini'. Para realizar essa tarefa, você pode seguir os passos abaixo:

FRONT END pyqt5

Configuração inicial:

Comece importando as bibliotecas necessárias, como pyodbc ou pymysql para conectar a diferentes bancos de dados.
Leia as configurações do arquivo 'application.ini' para obter as informações de conexão da base de destino.
Conexão com o banco de origem:

Conecte-se ao banco de dados de origem. Dependendo do banco de dados, você precisará de uma string de conexão específica.
Certifique-se de lidar com diferentes tipos de bancos de dados (por exemplo, MySQL, PostgreSQL, SQL Server) com os módulos apropriados.
Execução dos scripts SQL:

Armazene seus scripts SQL em uma lista ou arquivo. Você pode carregá-los dinamicamente, se necessário.
Use um loop para iterar através dos scripts e execute-os no banco de origem.
Lide com exceções e erros de execução dos scripts, se ocorrerem.
Conexão com a base de destino:

Use as informações lidas do 'application.ini' para conectar-se à base de destino.
Transferência de dados:

Após a execução de cada script, você pode extrair dados do banco de origem, transformá-los (se necessário) e inseri-los na base de destino.
Finalização:

Feche todas as conexões e recursos adequadamente.
Lide com erros e exceções de forma apropriada para garantir a integridade dos dados.
Aqui está um exemplo simples para te dar uma ideia geral:

python
Copy code

import configparser
import pymysql

# Leitura das configurações da base de destino do 'application.ini'
config = configparser.ConfigParser()
config.read('application.ini')

db_host = config['database']['host']
db_user = config['database']['user']
db_password = config['database']['password']
db_database = config['database']['database']

# Conexão com o banco de origem (exemplo: MySQL)
source_conn = pymysql.connect(host='source_host', user='source_user', password='source_password', database='source_db')
source_cursor = source_conn.cursor()

# Lista de scripts SQL
sql_scripts = ['script1.sql', 'script2.sql', 'script3.sql']

# Execução dos scripts
for script in sql_scripts:
    with open(script, 'r') as file:
        sql_query = file.read()
    try:
        source_cursor.execute(sql_query)
        source_conn.commit()
        # Processar e inserir dados na base de destino aqui
    except Exception as e:
        print(f"Erro na execução do script {script}: {str(e)}")

# Conexão com a base de destino (usando as informações do 'application.ini')
destination_conn = pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_database)
destination_cursor = destination_conn.cursor()

# Fechar conexões
source_cursor.close()
source_conn.close()
destination_cursor.close()
destination_conn.close()
Lembre-se de que este é apenas um exemplo simplificado e genérico. Você precisará adaptar o código de acordo com suas necessidades específicas e os SGBDs que você está usando. Além disso, considere a segurança, manipulação de erros e tratamento de dados cuidadosamente em seu aplicativo real.

--********************************************************

Para importar os resultados de cada script SQL para a base de destino em tabelas específicas, você pode seguir as etapas a seguir:

Definir mapeamento entre resultados e tabelas de destino:
Antes de executar os scripts SQL, você precisa definir um mapeamento que indique qual tabela de destino deve receber os resultados de cada script. Você pode criar um dicionário Python que associe cada script a uma tabela de destino.
python
Copy code
# Mapeamento entre scripts e tabelas de destino
script_table_mapping = {
    'script1.sql': 'tabela_destino1',
    'script2.sql': 'tabela_destino2',
    'script3.sql': 'tabela_destino3',
}
Após executar cada script SQL, insira os resultados na tabela de destino correspondente:
Após a execução bem-sucedida de cada script SQL, você pode usar os resultados para inserir os dados na tabela de destino apropriada. Para isso, você precisará de informações sobre a estrutura da tabela de destino e usar instruções SQL de inserção para transferir os dados.

Aqui está um exemplo simplificado para inserir resultados em uma tabela de destino usando a biblioteca pymysql:

python
Copy code
# Após a execução de cada script SQL
for script in sql_scripts:
    with open(script, 'r') as file:
        sql_query = file.read()
    try:
        source_cursor.execute(sql_query)
        source_conn.commit()
        
        # Obtenha os resultados da consulta (substitua isso pelo seu código de obtenção de resultados)
        results = source_cursor.fetchall()
        
        # Determine a tabela de destino com base no mapeamento
        destination_table = script_table_mapping.get(script)
        
        if destination_table:
            # Insira os resultados na tabela de destino
            for row in results:
                # Construa a instrução SQL de inserção (substitua isso pelo seu código)
                insert_query = f"INSERT INTO {destination_table} (coluna1, coluna2, ...) VALUES (%s, %s, ...)"
                destination_cursor.execute(insert_query, row)
            
            destination_conn.commit()
    except Exception as e:
        print(f"Erro na execução do script {script}: {str(e)}")
Certifique-se de personalizar as instruções SQL de inserção de acordo com a estrutura da tabela de destino e os resultados que você está obtendo dos scripts SQL.

Lembre-se de que este é um exemplo simplificado e genérico. Você precisará adaptar o código às suas necessidades específicas e garantir que a estrutura das tabelas de destino esteja de acordo com os resultados dos scripts SQL.

https://www.youtube.com/watch?v=Mdg1D-Kdmrw -- integrar sql python

https://blp.hashtagtreinamentos.com/python/inscricao-intensivao-de-python-yt-m?origemurl=165331992468&origemads=684635482260&gclid=Cj0KCQiAkKqsBhC3ARIsAEEjuJgGuxK4ci7-1F32sMo6IlwZ-KjNn1Zp9-Eu2X1T6J3qMv0y-XkopNEaAsf1EALw_wcB