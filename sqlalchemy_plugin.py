import cherrypy
from sqlalchemy import create_engine
from cherrypy.process import wspbus, plugins


class DatabasePlugin(plugins.SimplePlugin):
    def __init__(self, bus, con_str):
        plugins.SimplePlugin.__init__(self, bus)
        self.con = create_engine(con_str, pool_recycle=3600)

    def start(self):
        self.bus.log('Starting up DB access')
        self.bus.subscribe('db-switch', self.add_con)
        self.bus.subscribe('get_con', self.get_con)

    def stop(self):
        self.bus.log('Stopping down DB access')
        self.bus.unsubscribe("db-switch", self.add_con)
        self.bus.unsubscribe('get_con', self.get_con)
    def add_con(self, con_str):
        self.con = create_engine(con_str, pool_recycle=3600)

    def get_con(self,con):
        con.append(self.con)

