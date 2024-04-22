import platform
import sys
from collections import UserString

from yoolib import __version__


class YooClientUserAgent(UserString):
    """
    # UserAgent string for yoolib request.

    Генерирует строку User Agent для передачи в HTTP-заголовок.
    В общем случае, вам нужно указать в качестве параметра название
    вашего приложения и вызвать метод .generic(), который добавит необходимую
    информацию о среде и версии библиотеки:

    >>> YooClientUserAgent('com.mycomany.myapp').generic()

    Однако, можно указать по цепочке свойств только нужные вам данные, например:

    >>> YooClientUserAgent('MySuperApp').platform.yoolib_version

    Доступны следующие свойства:
    - platform: имя операционной системы
    - core_arch: тип процессора
    - python_sigver: версия Python
    - yoolib_version: версия yoolib

    При вызове generic() используются все свойства после переданной вами строки,
    как если бы вы указали:

    >>> YooClientUserAgent('MyApp').platform.core_arch.python_sigver.yoolib_version

    Возможно передать пустую строку в качестве параметра.
    """

    @property
    def platform(self):
        self.data = f'{self.data} {platform.uname().system}/{platform.uname().release}'
        return self.strip()

    @property
    def core_arch(self):
        self.data = f'{self.data} {platform.uname().machine}'
        return self.strip()

    @property
    def python_sigver(self):
        self.data = (
            f'{self.data} {platform.python_implementation()}/'
            + '.'.join(map(str, sys.implementation.version[:3]))
        )
        return self.strip()

    @property
    def yoolib_version(self):
        self.data = f'{self.data} YooLib/{__version__}'
        return self.strip()

    def generic(self):
        return self.platform.core_arch.python_sigver.yoolib_version
