import os
import shutil
import stat
import winreg as reg

# Obtém o nome do usuário e do computador
user_name = os.getlogin()
computer_name = os.getenv('COMPUTERNAME')

# Caminhos originais e o novo caminho para a pasta oculta
ORIGINAL_PATHS = [
    r"C:\Users\Link\Para\Arquivo1",
    r"C:\Users\Link\Para\Arquivo2",
    r"C:\Users\Link\Para\Arquivo3"
]
HIDDEN_FOLDER = f"C:\\Users\\{user_name}\\AppData\\Local\\AppPath"

def create_hidden_folder(path):
    # Cria uma pasta oculta se não existir
    if not os.path.exists(path):
        os.makedirs(path)
        os.system(f'attrib +h "{path}"')

def move_files_to_hidden(original_paths, hidden_folder):
    # Move arquivos para a pasta oculta e remove permissões
    for original_path in original_paths:
        if os.path.exists(original_path):
            hidden_path = os.path.join(hidden_folder, os.path.basename(original_path))
            shutil.move(original_path, hidden_path)
            os.chmod(hidden_path, stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH)
            print(f"Arquivo movido: {original_path} para {hidden_path}")
        else:
            print(f"Arquivo não encontrado: {original_path}")

def clear_jump_list(executable_name):
    # Limpa a lista de atalhos para um programa específico
    key_paths = [
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs",
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\Taskband",
        r"Software\Microsoft\Windows\CurrentVersion\Explorer\StartPage",
        r"Software\Microsoft\Windows\CurrentVersion\Search\RecentApps",
    ]
    
    for key_path in key_paths:
        try:
            with reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_ALL_ACCESS) as key:
                i = 0
                while True:
                    try:
                        value = reg.EnumValue(key, i)
                        if executable_name in value[1]:
                            reg.DeleteValue(key, value[0])
                            print(f"Removido: {value[0]} em {key_path}")
                        else:
                            i += 1
                    except OSError:
                        break
        except Exception as e:
            print(f"Erro ao limpar a Lista de Atalhos em {key_path}: {e}")

def main():
    create_hidden_folder(HIDDEN_FOLDER)
    move_files_to_hidden(ORIGINAL_PATHS, HIDDEN_FOLDER)
    clear_jump_list("teste")

if __name__ == "__main__":
    main()
