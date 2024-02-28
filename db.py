import psycopg2
import bcrypt
import os
from dotenv import load_dotenv

dotenv_path = 'config.env'
load_dotenv(dotenv_path)

def get_db_connection():
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host
    )
    return conn

def save_user(login,senha,name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        tabela = 'users'
        colunas = '(login, password,name)'

        senha_hashed = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        valores = (login, senha_hashed,name) 

        query = f"INSERT INTO {tabela} {colunas} VALUES (%s, %s, %s);"

        cur.execute(query, valores)
        
        conn.commit()
        cur.close()
        conn.close()
        
    except psycopg2.Error as e:
        print("Error when entering data:", e)


def read_user(login, password):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT password, initcap(name) FROM users WHERE login = %s", (login,))
                result = cur.fetchone()
                if result:
                    stored_password, user_name = result
                    stored_password_bytes = stored_password.encode('utf-8')
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password_bytes):
                        return True, user_name
    except psycopg2.Error as e:
        print("Error verifying user:", e)

    return False, None

def save_chat(login, caminho_conversa):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE users SET conversation_path = %s WHERE login = %s", (caminho_conversa, login))
        conn.commit()
    except psycopg2.Error as e:
        print("Error updating conversation path:", e)
    finally:
        if conn is not None:
            conn.close()


def read_chat(login):
    caminho_conversa = None
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(f"""SELECT conversation_path FROM users WHERE login = '{login}'""")
        result = cur.fetchone()
        
        if result:
            caminho_conversa = result[0]
    except psycopg2.Error as e:
        print("Error reading the conversation path:", e)
    finally:
        if conn is not None:
            conn.close()
    
    return caminho_conversa 