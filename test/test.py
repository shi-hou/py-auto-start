import os

from py_auto_starter import auto_starter

if __name__ == '__main__':
    name = 'test'
    path = os.path.abspath('test.exe')

    assert not auto_starter.exists(name)

    auto_starter.add(name, path)
    assert auto_starter.exists(name)

    auto_starter.remove(name)
    assert not auto_starter.exists(name)
