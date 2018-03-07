from abc import ABCMeta, abstractmethod

class CommandException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class Menu(object):
    commands = {}
    index = 0

    @classmethod
    def add_command(cls, name, klass):
        if not name:
            raise CommandException("Command must have a name!")
        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not a command!'.format(klass))
        cls.commands[name] = klass

    @classmethod
    def execute(cls, name, *args, **kwargs):
        klass = cls.commands.get(name)
        if klass is None:
            raise CommandException('Command with name "{}" not found'.format(name))
        return klass.execute

    def __next__(self):
        if self.index < len(self.commands.items()):
            item = list(self.commands.items())[self.index]
            self.index += 1
            return item
        else:
            self.index = 0 # для дальнейшей возможности проитерировать объект
            raise StopIteration()

    def __iter__(self):
        return self

class ShowCommand(Command):
    def __init__(self, task_id):
        pass
    def execute(self):
        pass

class ListCommand(Command):
    def __init__(self):
        pass
    def execute(self):
        pass


menu = Menu()
menu.add_command("show", ShowCommand)
menu.add_command("list", ListCommand)
