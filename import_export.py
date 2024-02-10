import psycopg2
import csv
import os
import datetime
import glob

# Parâmetros de conexão para o banco de dados inicial
db_initial_params = {
    "host": "localhost",
    "database": "northwind",
    "user": "northwind_user",
    "password": "thewindisblowing",
    "port": "5432"
}

# Parâmetros de conexão para o banco de dados final
db_final_params = {
    "host": "localhost",
    "database": "northwind_final",
    "user": "northwind_user",
    "password": "thewindisblowing",
    "port": "5433"
}

# Diretório de saída para os arquivos CSV
output_base_directory = os.path.join(os.path.dirname(__file__), "data", "postgres")

try:
    # Conexão com o banco de dados inicial
    conn_initial = psycopg2.connect(**db_initial_params)
    cursor_initial = conn_initial.cursor()

    # Obter a lista de tabelas no banco de dados inicial
    cursor_initial.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';")
    tables = [table[0] for table in cursor_initial.fetchall()]

    # Iterar sobre as tabelas
    for table in tables:
        # Criar diretório para a tabela
        table_directory = os.path.join(output_base_directory, table)
        os.makedirs(table_directory, exist_ok=True)

        # Criar diretório com a data atual
        now = datetime.datetime.now()
        date_folder = now.strftime("%Y-%m-%d")
        date_directory = os.path.join(table_directory, date_folder)
        os.makedirs(date_directory, exist_ok=True)

        # Caminho do arquivo CSV
        csv_filename = table + ".csv"
        csv_file_path = os.path.join(date_directory, csv_filename)

        # Exportar dados da tabela para o arquivo CSV
        cursor_initial.execute(f"SELECT * FROM {table};")
        with open(csv_file_path, "w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(cursor_initial.fetchall())
            print(f"Dados da tabela {table} exportados para {csv_file_path}")

    # Fechar conexão com o banco de dados inicial
    conn_initial.close()

    # Conexão com o banco de dados final
    conn_final = psycopg2.connect(**db_final_params)
    cursor_final = conn_final.cursor()

    # Obter a lista de arquivos CSV
    csv_files = glob.glob(os.path.join(output_base_directory, "*", "*", "*.csv"))

    # Iterar sobre os arquivos CSV
    for csv_file in csv_files:
        table_name = os.path.splitext(os.path.basename(csv_file))[0]

        # Importar dados do arquivo CSV para o banco de dados final
        with open(csv_file, "r") as csv_file:
            cursor_final.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", csv_file)
            print(f"Dados do arquivo {csv_file} importados para o banco de dados final.")

    # Fechar conexão com o banco de dados final
    conn_final.close()

except (Exception, psycopg2.Error) as error:
    print("Erro durante a exportação/importação dos dados:", error)
finally:
    # Fechar conexões
    if conn_initial:
        cursor_initial.close()
        conn_initial.close()
    if conn_final:
        cursor_final.close()
        conn_final.close()
