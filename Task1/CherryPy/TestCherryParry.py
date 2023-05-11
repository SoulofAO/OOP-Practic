
import cherrypy
from jinja2 import Environment, FileSystemLoader

class TablePage:
    @cherrypy.expose
    def index(self):
        return  """<html>
          <head></head>
          <body>
            <form method="get" action="generate">
              <button type="submit">Give it now!</button>
            </form>
          </body>
        </html>"""

if __name__ == '__main__':
    cherrypy.quickstart(TablePage())
