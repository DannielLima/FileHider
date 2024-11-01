import os
import shutil
import stat
import json
from getpass import getpass
import tkinter as tk
from tkinter import messagebox

# Caminho para configurações do usuário
CONFIG_FILE = "config.json"

# Define configurações padrão, incluindo caminhos originais
DEFAULT_CONFIG = {
    "original_paths": [
        r"C:\Users\Link\Para\Arquivo1",
        r"C:\Users\Link\Para\Arquivo2",
        r"C:\Users\Link\Para\Arquivo3"
    ],
    "hidden_folder": f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\AppPath",
    "password_protection": False,
    "password": ""
}

def load_config():
    # Carrega o arquivo de configuração
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

def save_config(config):
    # Salva as configurações em um arquivo JSON
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def create_hidden_folder(path):
    # Cria a pasta oculta se não existir
    if not os.path.exists(path):
        os.makedirs(path)
        os.system(f'attrib +h "{path}"')
        print(f"Pasta oculta criada em: {path}")

def verify_password(config):
    if config["password_protection"]:
        if os.path.exists(config["hidden_folder"]):
            attempts = 3
            while attempts > 0:
                password = getpass("Digite a senha: ")
                if password == config["password"]:
                    return True
                else:
                    attempts -= 1
                    print(f"Senha incorreta. Tentativas restantes: {attempts}")
            print("Acesso negado.")
            return False
        else:
            # Salva a senha dentro da pasta oculta (AppPath) na primeira vez que ela for criada
            with open(os.path.join(config["hidden_folder"], "password.txt"), "w") as f:
                f.write(config["password"])
    return True

def move_files_to_hidden(config):
    # Move arquivos para a pasta oculta após a verificação da senha
    if verify_password(config):
        hidden_folder = config["hidden_folder"]
        for original_path in config["original_paths"]:
            try:
                if os.path.exists(original_path):
                    hidden_path = os.path.join(hidden_folder, os.path.basename(original_path))
                    shutil.move(original_path, hidden_path)
                    os.chmod(hidden_path, stat.S_IWUSR)
                    print(f"Arquivo movido: {original_path} para {hidden_path}")
                else:
                    print(f"Arquivo não encontrado: {original_path}")
            except Exception as e:
                print(f"Erro ao mover {original_path}: {e}")

def restore_files(config):
    # Restaura os arquivos para seus caminhos originais após a verificação da senha
    if verify_password(config):
        hidden_folder = config["hidden_folder"]
        for original_path in config["original_paths"]:
            try:
                hidden_path = os.path.join(hidden_folder, os.path.basename(original_path))
                if os.path.exists(hidden_path):
                    shutil.move(hidden_path, original_path)
                    print(f"Arquivo restaurado: {hidden_path} para {original_path}")
                else:
                    print(f"Arquivo oculto não encontrado: {hidden_path}")
            except Exception as e:
                print(f"Erro ao restaurar {hidden_path}: {e}")

def main():
    config = load_config()
    create_hidden_folder(config["hidden_folder"])

    # Interface gráfica para escolha de operações
    root = tk.Tk()
    root.withdraw()
    action = messagebox.askquestion("Ação", "Deseja mover arquivos para a pasta oculta?")
    if action == "yes":
        move_files_to_hidden(config)
    else:
        action = messagebox.askquestion("Ação", "Deseja restaurar arquivos?")
        if action == "yes":
            restore_files(config)
        else:
            messagebox.showinfo("Encerrado", "Nenhuma ação selecionada.")

if __name__ == "__main__":
    main()
