
# FileHider

O **FileHider** é uma aplicação simples e eficiente para ocultar arquivos em pastas ocultas no Windows. Ele foi desenvolvido para ajudar os usuários a manterem seus arquivos organizados e protegidos de olhares curiosos.
## Recursos

- Mover múltiplos arquivos de uma vez para uma pasta oculta.
- Limpar a lista de atalhos do Windows relacionada aos arquivos ocultos.
- Criar uma pasta oculta automaticamente se ela não existir.
- Utiliza o nome do computador para personalizar o caminho da pasta oculta.


## Como Usar

1. **Instalação:**
   - Clone o repositório:
     ```bash
     git clone https://github.com/DannielLima/FileHider.git
     cd FileHider
     ```

2. **Pré-requisitos:**
   - Certifique-se de ter o Python 3 instalado em sua máquina.

3. **Configuração:**
   - Altere os caminhos dos arquivos originais na lista `original_paths` dentro do código.
   - Execute o script `olho_magico.py`:
     ```bash
     python olho_magico.py
     ```

4. **Acesso aos Arquivos:**
   - Os arquivos ocultos podem ser encontrados na pasta localizada em:
     ```
     C:\Users\[NOME_DO_COMPUTADOR]\AppData\Local\AppPath
     ```
## Exemplo de Uso

No código-fonte, você pode especificar quais arquivos deseja ocultar:

```python
original_paths = [
    r"C:\Users\SeuUsuario\Desktop\arquivo1.txt",
    r"C:\Users\SeuUsuario\Desktop\arquivo2.txt"
]
```
## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.
