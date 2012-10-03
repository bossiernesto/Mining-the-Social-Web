import couchdb
from base_nosql import *

couch_objects = []

class CouchEntity(NosqlEntity):

    collection = couch_objects

class Session(BaseNosqlSession):

    def set_up(self, settings, storage_name):

        BaseNosqlSession.set_up(self, settings, storage_name)
        server = couchdb.Server(self.db_host)
        #TODO: Log connection --> logger.log(INFO,'DBCouch version {1} connection at {2}'.format(self.server.version(),self.db_host))

        try:
            self.db = server[settings.COUCH_DB_NAME]
        except Exception:
            self.db = server.create(settings.COUCH_DB_NAME)
        #TODO: log db connect --> logger.log(INFO,'DBCouch: connected to DB {1}'.format(settitngs.COUCH_DB_NAME))


    def commit(self):

        for entity, obj in couch_objects:

            if self.settings.SHOW_DEBUG_INFO:
                print obj

            self.db.save(obj)

    def close(self):
        pass


couch_session = Session()
