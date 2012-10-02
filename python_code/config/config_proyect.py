<<<<<<< HEAD
__author__ = 'ernesto'
=======
import ConfigParser,io


DEFAULT_NAME='SETTINGS.conf'
DEFAULT_FILENAME='./'.join(DEFAULT_NAME)


setting_template=[]

class settingBuilder():
    """Simple wrapper for the ConfigParser module used in this """

    def __init__(self,filename=DEFAULT_FILENAME):
        self.config_parser=ConfigParser.RawConfigParser()

    def build_defaultsettings(self,save=False):
        for section in setting_template:
            self.config_parser.add_section(section[0])
            for value in  section[1]:
                self.config_parser.set(section[0],)

    def get_settings(self,filename=DEFAULT_FILENAME,flow=False):
        if flow:
           f=io.BytesIO(filename)
        else:
            f=filename
        self.config_parser.readfp(f)

    @staticmethod
    def get(self,section,key):
        """staticmethod that returns value from section and option from default file"""
        c=settingBuilder()
        return c.get_value(section,key)


    def get_value(self,section,key):
        try:
            return self.config_parser.get(section,key)
        except ConfigParser.NoOptionError,ConfigParser.NoSectionError:
            raise ConfigError()

#TODO: Migrate to exception file in root folder
class ConfigError(Exception):
    pass

>>>>>>> 094543a9598238fd130ed326e7c9237d4f3ad463
