# X-Jacking - Ferramenta de Identificação de Clickjacking

![image](https://github.com/user-attachments/assets/60eb483b-7e69-4615-9fc0-87ed1a3244e5)

## Descrição
O **X-Jacking** é uma ferramenta desenvolvida para identificar vulnerabilidades de **Clickjacking**, verificando se um site possui a proteção adequada através do cabeçalho `X-Frame-Options`. Essa falha pode permitir que atacantes manipulem iframes para capturar interações do usuário em aplicações web, levando a ataques de roubo de credenciais, engenharia social e comprometimento da sessão.

---

## 🔥 Para quem essa ferramenta é destinada?

- **Profissionais de Red Team** - Identifica possíveis vetores de ataque em aplicações vulneráveis.
- **Pesquisadores de Segurança (Pentesters)** - Automatiza a detecção de Clickjacking para auditorias.
- **Bug Bounty Hunters** - Auxilia na busca por falhas em sites e plataformas que podem levar a recompensas.

---

## 🚨 O que é Clickjacking?

O **Clickjacking** é um ataque onde um atacante insere um site dentro de um **iframe invisível** e induz o usuário a clicar em botões ou links sem perceber. Isso pode ser explorado para:

- Roubo de credenciais
- Autorização de transações indevidas
- Execução de ações maliciosas sem o consentimento do usuário

Exemplo de PoC:
```html
<iframe src="https://vulnerable-site.com/login" style="opacity: 0; position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
```

Esse código embute um site vulnerável de forma invisível e pode capturar cliques sem que o usuário perceba.

---

## 🛠️ Como funciona a ferramenta?

O **X-Jacking** percorre uma lista de sites e verifica se o cabeçalho `X-Frame-Options` está presente na resposta HTTP. Se esse cabeçalho estiver ausente, a aplicação é considerada **vulnerável ao Clickjacking**.

### 🔹 Execução da ferramenta:

1. **Crie um arquivo** contendo as URLs a serem testadas:
   ```sh
   echo "https://exemplo.com" > urls.txt
   ```

2. **Execute a ferramenta:**
   ```sh
   python3 X-Jacking.py urls.txt
   ```

### 📌 Exemplo de Saída:
```
 __   __         _            _    _             
 \ \ / /        | |          | |  (_)            
  \ V /_____    | | __ _  ___| | ___ _ __   __ _
   > <______|   | |/ _` |/ __| |/ / | '_ \ / _` |
  / . \    | |__| | (_| | (__|   <| | | | | (_| |
 /_/ \_\    \____/ \__,_|\___|_|\_\_|_| |_|\__, |
                                            __/ |
                                           |___/  

   By David A. Mascaro
==================================================
[i] Iniciando varredura de X-Frame-Options...
==================================================
[+] Site: https://exemplo.com
    ╰──> Status: Vulnerável! (Sem X-Frame-Options)
[-] Site: https://google.com
    ╰──> Status: Seguro (X-Frame-Options: SAMEORIGIN)
==================================================
[i] Varredura finalizada.
==================================================
```

---

## 📖 Referências de Segurança

### 🛡️ OWASP - A05:2021 (Security Misconfiguration)
A falta de proteção contra Clickjacking está relacionada à categoria **OWASP A05:2021 - Security Misconfiguration**. Aplicativos que permitem serem embutidos em iframes sem restrições podem levar a ataques de Clickjacking.

🔗 [OWASP A05:2021 - Security Misconfiguration](https://owasp.org/Top10/A05_2021-Security_Misconfiguration/)

### 🕵️‍♂️ MITRE ATT&CK - T1608.005 (Supply Chain Compromise: Web Domain Infrastructure)
Essa falha também pode ser explorada dentro do framework **MITRE ATT&CK**, mais especificamente na técnica **T1608.005**, onde atacantes podem comprometer sites para serem utilizados em ataques de Clickjacking.

🔗 [MITRE ATT&CK - T1608.005](https://attack.mitre.org/techniques/T1608/005/)

---

## 🔐 Como se proteger do Clickjacking?

1. **Configurar o cabeçalho `X-Frame-Options` corretamente**:
   - `DENY` → Impede que o site seja carregado em iframes.
   - `SAMEORIGIN` → Permite iframes apenas do mesmo domínio.

   **Exemplo em um servidor Apache:**
   ```sh
   Header always set X-Frame-Options "DENY"
   ```

   **Exemplo em um servidor Nginx:**
   ```nginx
   add_header X-Frame-Options "SAMEORIGIN";
   ```

2. **Utilizar `Content-Security-Policy (CSP)`** para prevenir ataques modernos:
   ```sh
   Content-Security-Policy: frame-ancestors 'none';
   ```

---

## 🤝 Contribuição
Sinta-se à vontade para abrir **Issues** e enviar **Pull Requests** com melhorias para a ferramenta!

👨‍💻 Autor: **David A. Mascaro**

---

## ⚠️ Aviso Legal
Esta ferramenta é destinada apenas para **fins educacionais** e **testes de segurança autorizados**. O uso indevido desta ferramenta para acessar sistemas sem permissão é ilegal e pode resultar em processos criminais. O autor não se responsabiliza pelo mau uso desta ferramenta.

## Versão compilada com interface grafica: 
![print](https://github.com/user-attachments/assets/9f1159eb-7c73-47eb-8e7e-3d6ab27dc209)

[Download!](https://github.com/Hackingstati0n/X-Jacking/releases/tag/Binario)
