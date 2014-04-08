from rumps import *
import urllib
import webbrowser

def e(_):
  print 'EEEEEEE'

app = App('HoorooMenu', icon='hooroo-logo.png')
app.menu = [
  (
    'Production',
    [
      MenuItem('Qantas', callback=e),
      MenuItem('Jetstar', callback=e),
      MenuItem('Hooroo', callback=e),
      MenuItem('Extranet', callback=e)
    ]
  ),
  (
    'Staging',
    [
      MenuItem('Qantas', callback=e),
      MenuItem('Jetstar', callback=e),
      MenuItem('Hooroo', callback=e),
      MenuItem('Extranet', callback=e)
    ]
  ),
  (
    'Development',
    [
      MenuItem('Qantas', callback=e),
      MenuItem('Jetstar', callback=e),
      MenuItem('Hooroo', callback=e),
      MenuItem('Extranet', callback=e)
    ]
  ),
  None,
  (
    'Paperboy',
    [
      MenuItem('Hotels', callback=e),
      MenuItem('Places', callback=e),
      MenuItem('Flightbooking', callback=e)
    ]
  ),
  None,
  MenuItem('Spunk', callback=e),
  MenuItem('AWS OpsWorks', callback=e),
  MenuItem('Nagios', callback=e),
  None
]

app.run()
