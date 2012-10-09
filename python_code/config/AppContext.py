import ConfigParser,io,inspect
from singleton import Singleton

DEFAULT_NAME='SETTINGS.conf'
DEFAULT_FILENAME='./'.join(DEFAULT_NAME)
OBJECTSECTION="OBJECTS"

setting_template=[('NoSQL',[('COUCH_DB_NAME','http://localhost:5984')]),
                ('General',[('SHOW_DEBUG_INFO',0)])]

class appContext():
    """Simple wrapper for the ConfigParser module used in this proyect. It also stores reference to objects"""

    __metaclass__=Singleton

    def __init__(self,filename=DEFAULT_FILENAME):
        self.config_parser=ConfigParser.RawConfigParser()
        self.get_settings(filename)

    @staticmethod
    def build_defaultsettings(save=False):
        appC=appContext
        for section in setting_template:
            appC.config_parser.add_section(section[0])
            for value in  section[1]:
                appC.set_property(section[0],value[0],value[1])
        if save:
            with open(DEFAULT_FILENAME,'wb') as file:
                appC.config_parser.write(file)

    def get_settings(self,filename=DEFAULT_FILENAME,flow=False):
        if flow:
           f=io.BytesIO(filename)
        else:
            f=filename
        self.config_parser.readfp(f)

    @staticmethod
    def sectionExists(section):
        try:
            appContext().get(section,"a")
            return True
        except ConfigParser.NoOptionError:
            return True
        except ConfigParser.NoSectionError,Exception:
            return False

    @staticmethod
    def set_object(self,klass,object):
        appC=appContext()
        if inspect.isclass(klass) and isinstance(object,klass):
            if not appContext.sectionExists(OBJECTSECTION):
                appC.config_parser.add_section(OBJECTSECTION)
            appContext.set_property(OBJECTSECTION,klass,object)


    @staticmethod
    def set_property(section,key,value):
        appC=appContext()
        lkey,lvalue=appC.sanitizeKeyValue(key,value)
        appC.config_parser.set(section,lkey,lvalue)

    def sanitizeKeyValue(self,key,value):
        return key.encode('ascii','xmlcharrefreplace'),value.encode('ascii','xmlcharrefreplace')

    @staticmethod
    def getObject(klass):
        return appContext.get(OBJECTSECTION,klass)

    @staticmethod
    def get(section,key):
        """staticmethod that returns value from section and option from default file"""
        appC=appContext() #getinstance of appcontext
        return appC.get_value(section,key)


    def get_value(self,section,key):
        try:
            return self.config_parser.get(section,key)
        except ConfigParser.NoOptionError,ConfigParser.NoSectionError:
            raise ConfigError()

class ConfigError(Exception):
    pass

