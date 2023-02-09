import os


class LinuxAutoStarter:

    def __init__(self):
        _xdg_config_home = os.environ.get("XDG_CONFIG_HOME", "~/.config")
        self._xdg_user_autostart = os.path.join(os.path.expanduser(_xdg_config_home),
                                                "autostart")
        if not os.path.exists(self._xdg_user_autostart):
            os.makedirs(self._xdg_user_autostart)

    def _getfilename(self, name):
        """get the filename of an autostart (.desktop) file"""
        return os.path.join(self._xdg_user_autostart, name + ".desktop")

    def add(self, name, app_path):
        """add a new autostart entry"""
        desktop_entry = "[Desktop Entry]\n" \
                        "Name=%s\n" \
                        "Exec=%s\n" \
                        "Type=Application\n" \
                        "Terminal=false\n" % (name, app_path)
        with open(self._getfilename(name), "w") as f:
            f.write(desktop_entry)

    def exists(self, name):
        """check if an autostart entry exists"""
        return os.path.exists(self._getfilename(name))

    def remove(self, name):
        """delete an autostart entry"""
        if self.exists(name):
            os.unlink(self._getfilename(name))
