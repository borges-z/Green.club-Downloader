# Green.club Downloader

Este é um script em Python 3 para baixar cursos da plataforma **Green.club**. O script permite baixar somente os cursos aos quais o usuário tem acesso, com base nas credenciais fornecidas.

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado em sua máquina.
- Uma conta ativa na plataforma **Green.club**.

## ⚙️ Instalação

1. Clone este repositório para sua máquina local:
    
    ```bash
    git clone https://github.com/borges-z/Green.club-Downloader.git
    cd Green.club-Downloader
    ```
    
2. Instale as dependências necessárias:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. Configure o arquivo `.env` com suas informações de acesso:
    
    - Crie um arquivo `.env` no diretório raiz do projeto (ou edite o existente).
    - Adicione as seguintes variáveis, substituindo pelas suas informações:
        
        ```env
        EMAIL=seu-email@exemplo.com
        PASSWORD=sua-senha
        SOURCE=https://link-completo-da-green.club
        ```
        

## 🚀 Uso

1. Execute o script com o seguinte comando:
    
    ```bash
    python main.py
    ```
    
2. O script fará login na plataforma **Green.club** e baixará os cursos disponíveis para a conta configurada.
    

## 🛠️ Funcionalidades

- Baixa somente os cursos aos quais o usuário tem acesso.
- Simples configuração via arquivo `.env`.

## 📝 Observações

- Certifique-se de que o **link completo da plataforma** (iniciado com `https://`) foi inserido corretamente no arquivo `.env`.
- Para evitar problemas de login, verifique se as credenciais fornecidas estão corretas.

## 📜 Licença

Este projeto está sob a licença [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html).

## 🤝 Contribuições

Contribuições são bem-vindas!

1. Faça um fork do projeto.
2. Crie uma branch para sua funcionalidade ou correção:
    
    ```bash
    git checkout -b minha-nova-funcionalidade
    ```
    
3. Commit suas alterações:
    
    ```bash
    git commit -m "Adiciona nova funcionalidade"  
    ```
    
4. Faça o push para a branch:
    
    ```bash
    git push origin minha-nova-funcionalidade  
    ```
    
5. Abra um Pull Request.

## 📧 Contato

Se tiver dúvidas ou sugestões, entre em contato pelo e-mail: **[josebgs@protonmail.com](mailto:josebgs@protonmail.com)**.

Se houver erro ou uma nova funcionalidade dentro da plataforma, que difere da maioria, envie seu login com e-mail e senha em um arquivo em anexo para o e-mail acima. Caso envie, você estará permitindo que **somente eu** terei acesso a sua conta, somente para a implementação da nova funcionalidade.

Esta é minha chave pública RSA. Use-o para criptografar mensagens ou arquivos para comunicação segura comigo.

-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqq4J11oygmzdmkXFQZ5G
pR40mVuvmHY5AFHyM5CKkglkcDEitYoIIWQ1X0E2jH5YKzTfwGhmOKNT8NKZ0lIE
lX3wffFL624Mz4QBNv5bdwF9v3SMDv6NYxvNsTeaTv6BQ6l34pCfXrNMlSUfHo1e
5tj9YkqLa5QXhhXWF69OKAZFmmu0QiJ9j3BPjMhpu+N51eyV5M6Szib3WZP4BkoR
ya4wKNhBUojwxUgXMesqobZU1GhFeURDRklUwNlNxOB2kyw2vB/kNWVcFxVmsL7h
BWJM8y8d1CQK+Av64Q7q1cHchFbFacUFEYSFxMUBF29sajg8I4BxryyuwMEOt3jA
fQIDAQAB
-----END PUBLIC KEY-----

---

Se precisar de mais ajustes ou algo específico, é só avisar!