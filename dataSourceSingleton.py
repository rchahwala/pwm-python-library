class DataSourceSingleton:

    def get_name(self):
        print(self.__class__.__name__)


d = DataSourceSingleton()
d.get_name()
