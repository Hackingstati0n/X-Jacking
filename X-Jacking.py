import requests
import argparse
from colorama import Fore, Style, init

# Inicializa o colorama para colorir a saída no terminal
init(autoreset=True)

# ASCII Art no estilo SQLMap
ascii_art = r"""
 __   __         _            _    _
 \ \ / /        | |          | |  (_)
  \ V /______   | | __ _  ___| | ___ _ __   __ _
   > <______ |  | |/ _` |/ __| |/ / | '_ \ / _` |
  / . \    | |__| | (_| | (__|   <| | | | | (_| |
 /_/ \_\    \____/ \__,_|\___|_|\_\_|_| |_|\__, |
                                            __/ |
                                           |___/
"""
separator = "=" * 50

def check_x_frame_options(url):
    """Verifica se o site possui o cabeçalho X-Frame-Options."""
    try:
        response = requests.get(url, timeout=5)
        x_frame_options = response.headers.get("X-Frame-Options")

        if x_frame_options is None:
            print(f"{Fore.GREEN}[+] Site: {url}\n    ╰──> Status: {Fore.RED}Vulnerável! (Sem X-Frame-Options){Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Site: {url}\n    ╰──> Status: {Fore.GREEN}Seguro ({x_frame_options}){Style.RESET_ALL}")

    except requests.RequestException as e:
        print(f"{Fore.YELLOW}[!] Erro ao acessar {url}:\n    ╰──> {e}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Verifica se sites possuem a proteção X-Frame-Options.")
    parser.add_argument("file", help="Caminho para o arquivo .txt contendo as URLs")
    args = parser.parse_args()

    # Exibe o banner estilizado no estilo SQLMap
    print(Fore.CYAN + ascii_art + Style.RESET_ALL)
    print(Fore.MAGENTA + "   By David A. Mascaro\n" + Style.RESET_ALL)
    print(Fore.YELLOW + separator + Style.RESET_ALL)
    print(Fore.YELLOW + "[i] Iniciando varredura de X-Frame-Options..." + Style.RESET_ALL)
    print(Fore.YELLOW + separator + Style.RESET_ALL)

    try:
        with open(args.file, "r") as f:
            urls = [line.strip() for line in f if line.strip()]

        if not urls:
            print(f"{Fore.YELLOW}[!] Nenhuma URL encontrada no arquivo.{Style.RESET_ALL}")
            return

        for url in urls:
            check_x_frame_options(url)

    except FileNotFoundError:
        print(f"{Fore.RED}[!] Erro: Arquivo '{args.file}' não encontrado.{Style.RESET_ALL}")

    print(Fore.YELLOW + separator + Style.RESET_ALL)
    print(Fore.YELLOW + "[i] Varredura finalizada.\n" + separator + Style.RESET_ALL)

if __name__ == "__main__":
    main()
