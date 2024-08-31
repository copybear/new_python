from __future__ import print_function
import platform
import pyinputplus as pyip


def classtree(cls, depth=0):
    if depth == 0:
        prefix = ''
    else:
        prefix = '.' * (depth * 3) + ' '
    if cls.__name__.lower() == 'error':
        print('{0}{1} ({2})'.format(prefix, cls.__name__, cls))
    else:
        print('{0}{1}'.format(prefix, cls.__name__))
    for subcls in sorted(cls.__subclasses__(), key=lambda c: c.__name__):
        classtree(subcls, depth+1)


if __name__ == '__main__':
    print('Python Version: {0}'.format(platform.python_version()))
    print()
    classtree(pyip.Exception)
