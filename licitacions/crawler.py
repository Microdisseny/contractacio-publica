import os
from urllib.parse import parse_qs

import pprint
import requests
from bs4 import BeautifulSoup
from slugify import slugify


from .models import Contractant


os.environ['REQUESTS_CA_BUNDLE'] = os.path.join('/etc/ssl/certs/', 'ca-certificates.crt')


def obtenir_contingut(url):
    ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
    headers = ({'User-Agent': ua})
    response = requests.get(url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    return html_soup


def obtenir_links(url, selector, selector_paginacio=None, base_url_paginacio=None):
    html_soup = obtenir_contingut(url)
    links = []
    for a in html_soup.select(selector):
        try:
            link = {}
            link['text'] = (a.text or '').strip()
            link['url'] = a['href']
        except ValueError:
            raise
        else:
            links.append(link)
    if selector_paginacio is not None:
        for a in html_soup.select(selector_paginacio):
            url = '%s%s' % (base_url_paginacio, a['href'])
            links += obtenir_links(url, selector)

    return links


def obtenir_atributs(dl):
    atributs = {}
    for dt in dl.select('dt'):
        text = (dt.text or '').strip()
        valor = sibling_exist(dl, dt.text)
        atributs[slugify(text)] = valor
    return atributs


def sibling_exist(dom, element_text):
    element = dom.find('dt', text=element_text)
    if element:
        if hasattr(element.nextSibling.nextSibling, 'text'):
            return element.nextSibling.nextSibling.text.replace('\t', '').replace('\r', '').replace('\n', '')
    return ''


def obtenir_dades_licitacio(url):
    html = obtenir_contingut(url)
    item = {}
    item['id'] = parse_qs(url.split('?')[1])['idDoc'][0]
    item['url'] = url
    item['title'] = html.find('h2').text.strip()
    item['estat'] = None
    estat = html.find('li', id='actiu')
    if estat is not None:
        item['estat'] = estat.text.strip()
    else:
        estat = html.find('li', id='anulatactiu')
        if estat is not None:
            item['estat'] = estat.text.strip()
        else:
            print('############## Revisar estat a %s' % url)
    denominacio_contracte = html.find('dl', id="denominacio-contracte")
    item.update(obtenir_atributs(denominacio_contracte))

    dades_contracte = html.find('div', "dades-contracte")
    item.update(obtenir_atributs(dades_contracte))

    return item


base_hostame = 'https://contractaciopublica.gencat.cat'
base_url = '%s/ecofin_pscp/AppJava/' % base_hostame
url_contractants = '%s%s' % (
    base_url, 'cap.pscp?pagingNumberPer=100&reqCode=search&sortDirection=1&pagingPage=1&ambit=5')
url_contractant = '%s%s' % (base_url, 'cap.pscp?reqCode=viewDetail&idCap=%s&ambit=5')


def cercar_licitacions():
    claus = []
    contractants = obtenir_links(url_contractants, 'dl#llista-caps a', '#paginacio a', base_url)
    for perfil in contractants:
        perfil['id'] = parse_qs(perfil['url'].split('?')[1])['idCap'][0]

    for perfil in contractants:
        print('########################## %s' % perfil['text'])
        contractant, _ = Contractant.objects.get_or_create(
            codi=perfil['id'], nom=perfil['text'].strip())
        if not contractant.descartat:
            url = url_contractant % perfil['id']
            links_per_mirar = obtenir_links(url, 'div.caixa-enllacos ul a')
            for link_per_mirar in links_per_mirar:
                urls_pagina_licitacions = '%s%s' % (base_hostame, link_per_mirar['url'])
                urls_licitacions = obtenir_links(urls_pagina_licitacions, 'dl dt a', '#paginacio a', base_hostame)
                for url_licitacio in urls_licitacions:
                    url_licitacio = '%s%s' % (base_url, url_licitacio['url'])
                    id_doc = parse_qs(url_licitacio.split('?')[1])['idDoc'][0]
                    # Cal mirar que no estigui descartada
                    licitacio = obtenir_dades_licitacio(url_licitacio)
                    claus += list(licitacio.keys())
    print(list(set(claus)))
