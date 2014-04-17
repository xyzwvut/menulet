from rumps import *
import urllib
import webbrowser
import json

def load_url(sender):
  webbrowser.open(links[sender.key])

def create_menu(title, callback_function, lookup_key):
  menu_item = MenuItem(title, callback=callback_function)
  menu_item.key = lookup_key
  return menu_item

def load_config_json():
  json_data = open('hooroo-links.json')
  data = json.load(json_data)
  json_data.close()
  return data

app = App('HoorooMenu', icon='hooroo-logo.png')
links = load_config_json()
app.menu = [
  (
    'Production',
    [
      create_menu('Qantas', load_url, 'production-qantas'),
      create_menu('Jetstar', load_url, 'production-jetstar'),
      create_menu('Hooroo', load_url, 'production-hooroo'),
      create_menu('Extranet', load_url, 'production-extranet')
    ]
  ),
  (
    'Staging',
    [
      create_menu('Qantas', load_url, 'staging-qantas'),
      create_menu('Jetstar', load_url, 'staging-jetstar'),
      create_menu('Hooroo', load_url, 'staging-hooroo'),
      create_menu('Extranet', load_url, 'staging-extranet')
    ]
  ),
  (
    'Development',
    [
      create_menu('Qantas', load_url, 'dev-qantas'),
      create_menu('Jetstar', load_url, 'dev-jetstar'),
      create_menu('Hooroo', load_url, 'dev-hooroo'),
      create_menu('Extranet', load_url, 'dev-extranet')
    ]
  ),
  None,
  (
    'Paperboy',
    [
      create_menu('Hotels', load_url, 'paperboy-hotels'),
      create_menu('Places', load_url, 'paperboy-places'),
      create_menu('Flightbooking', load_url, 'paperboy-fb')
    ]
  ),
  None,
  create_menu('Spunk', load_url, 'splunk'),
  create_menu('AWS OpsWorks', load_url, 'opsworks'),
  create_menu('Nagios', load_url, 'nagios'),
  None
]

app.run()
