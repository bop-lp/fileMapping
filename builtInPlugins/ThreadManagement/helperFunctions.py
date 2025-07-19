from symtable import Function

from fileMapping.core import decorators

from . import config


reg = decorators.tagAppRegistration(config.__name__)


@reg()
def task(func: Function, *args, **kwargs):
    pass

