import cherrypy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.sql import select
from sqlalchemy_plugin import DatabasePlugin
class Root(object):
    @cherrypy.expose
    def index(self):
        Base = automap_base()
        engine = []
        cherrypy.engine.publish('get_con',engine)
        engine = engine.pop()
        Base.prepare(engine, reflect=True)
        tables = Base.classes
        s = select([tables.COMPANY])
        rp = engine.connect().execute(s)
        result = rp.fetchall()
        name = result[0].NAME
        return 'hello {}'.format(name)

    @cherrypy.expose
    def change(self):
        Base = automap_base()
        engine = []
        cherrypy.engine.publish('db-switch','sqlite:///test.db')
        cherrypy.engine.publish('get_con',engine)
        engine = engine.pop()
        Base.prepare(engine, reflect=True)
        tables = Base.classes
        s = select([tables.COMPANY])
        rp = engine.connect().execute(s)
        result = rp.fetchall()
        name = result[0].NAME
        return 'hello {}'.format(name)
def run(con_str):

    conf={
        '/':{'tools.sessions.on': True,}
    }

    DatabasePlugin(cherrypy.engine,con_str).subscribe()
    cherrypy.quickstart(Root(),'/',conf)

if __name__=='__main__':
    run('sqlite:///test1.db')