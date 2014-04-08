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
      MenuItem('Hooroo', callback=e)
    ]
  ),
  (
    'Staging',
    [
      MenuItem('Qantas', callback=e),
      MenuItem('Jetstar', callback=e),
      MenuItem('Hooroo', callback=e)
    ]
  ),
  (
    'Development',
    [
      MenuItem('Qantas', callback=e),
      MenuItem('Jetstar', callback=e),
      MenuItem('Hooroo', callback=e)
    ]
  )
]

app.run()
