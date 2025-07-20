from fileMapping.core import Class
from fileMapping.core import parameterApplication
from fileMapping.core import multithreading
from fileMapping.core import decorators

@parameterApplication.wrapper
class ReadManagement(Class.ParameterApplication):
    def __init__(self, self_info: Class.File):
        super().__init__(self_info)
        self.self_info.multithreading

    def init(self):
        pass

    def end(self):
        pass


def init(fileMapping: Class.File):
    pass



__level__ = 5



