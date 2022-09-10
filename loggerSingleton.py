class LoggerSingleton:

    def get_name(self):
        print(self.__class__.__name__)


d = LoggerSingleton()
d.get_name()
