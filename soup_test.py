from bs4 import BeautifulSoup
import requests
import json
import sys
import pokepy



def main():
    page = requests.get("https://www.smogon.com/dex/sm/pokemon/articuno/")
    status = page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    scripts = soup.find_all('script')
    body = scripts[0]
    body_text = str(body)
    lines = body_text.splitlines()
    info_line = lines[1]
    split_line = info_line.split("= ")
    json_dict = json.loads(split_line[1])
    #print(type(json_dict['injectRpcs'][2]))
    #print(len(json_dict['injectRpcs'][2]))

    #print(type((json_dict['injectRpcs'][2])[1]))


    #print(((json_dict['injectRpcs'][2])[1])['strategies'])

    #print(len(((json_dict['injectRpcs'][2])[1])['strategies'])) give us a list of dict
    strats_list = (((json_dict['injectRpcs'])[2])[1])['strategies']
    #print(strats_list)
    #print(json.dumps(strats_list[0]))

    client = pokepy.V2Client()
    #print(client.get_pokemon(5).name)

    new_dict = dict()
    new_dict['name'] = "articuno"
    new_dict['presets'] = []
    print(new_dict['name'])


def old():
    print("TESTING")
    page = requests.get("https://www.smogon.com/dex/sm/pokemon/articuno/")
    print("STATUS: " + str(page.status_code))
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_children = list(soup.children)
    html = soup_children[3] #3 is the index of the html apparently?
    html_children = list(html.children)  
    
    good_stuff = html_children[1]
    
    good_children = good_stuff.find_all('script')
    print(len(good_children))


def test(str): 
    print(str)

main()
