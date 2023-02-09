# py-auto-start

![PyPI](https://img.shields.io/pypi/v/py-auto-start)
![PyPI - Platforms](https://img.shields.io/badge/platform-windows%20%7C%20macos%20%7C%20linux-lightgrey)
![PyPI - License](https://img.shields.io/pypi/l/py-auto-start)

cross-platform auto start

## Install

```
pip install py-auto-start
```

## Usage

```python
import os

from py_auto_start import auto_starter

name = 'test'
path = os.path.abspath('test.exe')

auto_starter.add(name, path)
print(auto_starter.exists(name))
auto_starter.remove(name)

```

## Reference

- [A simple crossplatform autostart helper](https://gist.github.com/kinkerl/301428)
- [typicode/user-startup: Auto start commands when you log in (cross-platform)](https://github.com/typicode/user-startup)

## License

```
MIT License

Copyright (c) 2023 Shihou Kou

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
