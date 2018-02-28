from abc import ABCMeta, abstractmethod
from dateutil.parser import parse


class ValidatorException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Validator(metaclass=ABCMeta):
    types = {}
    @abstractmethod
    def validate(value):
        pass

    @classmethod
    def get_instance(cls, name, *args, **kwargs):
        klass = cls.types.get(name) #передали имя валидатора, хотим получить объект от сабкласса
        if klass is None:
            raise ValidatorException("Validator with name {} not found'".format(name))
        return klass(*args, **kwargs) # возвращаем объект дочернего класса-реализатора

    @staticmethod
    def add_type(name, klass):
        if not name:
            raise ValidatorException("Validator must have a name!")
        if not issubclass(klass, Validator):
            raise ValidatorException("Class {} is not Validator!".format(klass))
        Validator.types[name] = klass #

class EMailValidator(Validator):
    def validate(self, value):
        if "@" in value:
            return True
        else:
            return False

class DateTimeValidator(Validator):
    def validate(self, value):
        try:
            parse(value)
            return True
        except ValueError:
            return False

# Validator.add_type("email", EMailValidator)
# Validator.add_type("datetime", DateTimeValidator)
# valid = Validator.get_instance("datetime")
# valid.validate("2017-09-01xxx")
# valid.validate("2017-09-01xx")
# valid.validate("dmitry.shaurov@gmail.com")
# valid.validate("dmitry.shaurov")
