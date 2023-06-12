import cherrypy

class MyForm(object):
    @cherrypy.expose
    def index(self):
        return '''
            <html>
                <head></head>
                <body>
                    <form method="post" action="submit">
                        <input type="text" name="name" />
                        <input type="submit" value="Submit" />
                    </form>
                </body>
            </html>
        '''

    @cherrypy.expose
    def submit(self, name=None):
        if name:
            return "Hello, {}!".format(name)
        else:
            return "Please enter a name."

if __name__ == '__main__':
    cherrypy.quickstart(MyForm())
