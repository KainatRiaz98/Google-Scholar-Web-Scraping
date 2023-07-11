from bs4 import BeautifulSoup
import requests, lxml, os, json


def google_scholar_pagination():
  # https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    # https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
    # params = {
    #     'start': 0        # page number ⚠
    # }

    # JSON data will be collected here
    data = []

    while True:
        html = requests.get('https://scholar.google.com/scholar?oi=bibs&hl=en&cites=9975675337329173168', headers=headers).text
        soup = BeautifulSoup(html, 'lxml')

        # print(f'extrecting {params["start"] + 10} page...')

        # Container where all needed data is located
        for result in soup.select('.gs_r.gs_or.gs_scl'):
            # title = result.select_one('.gs_rt').text
            # title_link = result.select_one('.gs_rt a')['href']
            publication_info = result.select_one('.gs_a').text
            # snippet = result.select_one('.gs_rs').text
            # cited_by = result.select_one('#gs_res_ccl_mid .gs_nph+ a')['href']
            # try:
            #     pdf_link = result.select_one('.gs_or_ggsm a:nth-child(1)')['href']
            # except: 
            #     pdf_link = None

            data.append({
                publication_info,
            })

        # check if the "next" button is present
        if soup.select('.gs_ico_nav_next'):
            print('f')
        else:
            break
    print(data)
    # print(json.dumps(data, indent = 2, ensure_ascii = False))

google_scholar_pagination()