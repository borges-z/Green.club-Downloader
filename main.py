import requests
import os
from dotenv import load_dotenv
import json
import re
from yt_dlp import YoutubeDL
import urllib.parse

load_dotenv()

class GreenClub:
    def __init__(self, email, senha, source):
        self.email = email
        self.senha = senha
        self.source = source
        self.session = self.login()
        self.categorias = self.get_categorias()

        # Plataforma
        self.titulo_plataforma

        # Categoria
        self.titulo_categoria = ''
        self.id_order_categoria = ''

        # Curso
        self.titulo_curso = ''
        self.id_curso = ''
        self.id_order_curso = ''
        self.image_curso = ''

        # Modulo
        self.id_modulo = ''
        self.titulo_modulo = ''
        self.id_order_modulo = ''

        # Aula
        self.id_aula = ''
        self.titulo_aula = ''
        self.id_order_aula = ''
        self.link_aula = ''

    def files_download(self, aula):
        files = aula['attachments']
        for file in files:
            titulo_arquivo = file['title']
            cdn_url = urllib.parse.unquote(file['cdn_url'])
            titulo_url = cdn_url.split('/')[-1]
            titulo_url_parse = urllib.parse.quote(cdn_url.split('/')[-1])
            cdn_url = cdn_url.replace(titulo_url, titulo_url_parse)
            pdf = requests.get(cdn_url).content
            path = f"Cursos/{self.titulo_plataforma}/{self.id_order_categoria}. {self.titulo_categoria}/{self.id_order_curso}. {self.titulo_curso}/{self.id_order_modulo}. {self.titulo_modulo}/{self.id_order_aula}. {self.titulo_aula}"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"{path}/{titulo_arquivo}", 'wb') as f:
                f.write(pdf)


    def parse_modulo(self):
        modulo = self.session.get(f'https://api.greenn.club/course/{self.id_curso}/watch?data[]=course&data[]=modules&data[]=currentModule&data[]=currentModuleLessons&current_module_id={self.id_modulo}').json()
        aulas = modulo['currentModuleLessons']
        for aula in aulas:
            self.id_aula = aula['id']
            self.titulo_aula = self.normalize_str(aula['title'])
            print(f"\t\t\t\t{self.titulo_aula}")
            self.id_order_aula = aula['order']
            if not aula['source']:
                self.files_download(aula)
                continue
            self.link_aula = aula['source'].replace('embed/?v=', '') + "/playlist.m3u8"
            path = f"Cursos/{self.titulo_plataforma}/{self.id_order_categoria}. {self.titulo_categoria}/{self.id_order_curso}. {self.titulo_curso}/{self.id_order_modulo}. {self.titulo_modulo}/{self.id_order_aula}. {self.titulo_aula}"
            if not os.path.exists(path):
                os.makedirs(path)
            if os.path.isfile(f"{path}/ext.mp4"):
                continue
            os.system(f'yt-dlp {self.link_aula} -N50 --referer "{self.source}/" -o "{path}/ext.mp4" --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"')

    def parse_curso(self):
        curso = self.session.get(f'https://api.greenn.club/course/{self.id_curso}/watch?data[]=course&data[]=modules&data[]=currentModule&data[]=currentModuleLessons')
        if curso.status_code == 422:
            return
        else:
            curso = curso.json()
        modulos = curso['modules']
        for modulo in modulos:
            self.id_modulo = modulo['id']
            self.titulo_modulo = self.normalize_str(modulo['title'])
            print(f"\t\t\t{self.titulo_modulo}")
            self.id_order_modulo = modulo['order']
            self.parse_modulo()


    def get_cursos(self, categoria):
        cursos = categoria['courses']
        for curso in cursos:
            self.titulo_curso = self.normalize_str(curso['title'])
            print(f"\t\t{self.titulo_curso}")
            self.id_curso = curso['id']
            self.image_curso = curso['cover']['large_horizontal']
            self.id_order_curso = curso['order']
            self.parse_curso()

    @staticmethod
    def normalize_str(normalize_me):
        return " ".join(re.sub(r'[<>:!"/\\|?*]', '', normalize_me)
                        .replace('\t', '')
                        .replace('\n', '')
                        .replace('.', '')
                        .split(' ')).strip()

    def get_categorias(self):
        categorias = self.session.get('https://api.greenn.club/home').json()
        self.titulo_plataforma = categorias['name']
        print(self.titulo_plataforma)
        categorias = categorias['categories']
        for categoria in categorias:
            self.titulo_categoria = self.normalize_str(categoria['title'])
            print(f"\t{self.titulo_categoria}")
            self.id_order_categoria = categoria['order']
            self.get_cursos(categoria)
            

    def login(self):
        session = requests.Session()
        
        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7,la;q=0.6',
            'cache-control': 'no-cache',
            'content-type': 'application/json;charset=UTF-8',
            'origin': f'{self.source}',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': f'{self.source}/',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        json_data = {
            'email': self.email,
            'password': self.senha,
            'captcha': '',
        }

        response = session.post('https://api.greenn.club/member/login', headers=headers, json=json_data).json()['sites'][0]['Auth']
        session.headers.update({"Authorization": response})
        return session


if __name__ == '__main__':
    GreenClub(os.getenv('email'), os.getenv('senha'), os.getenv('source'))

