import winreg


class WinAutoStarter:

    def _get_key(self):
        return winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Run',
                              0, winreg.KEY_ALL_ACCESS)

    def add(self, name, app_path):
        """add a new autostart entry"""
        key = self._get_key()
        try:
            winreg.SetValueEx(key, name, 0, winreg.REG_SZ, app_path)
        finally:
            winreg.CloseKey(key)

    def exists(self, name):
        """check if an autostart entry exists"""
        key = self._get_key()
        try:
            winreg.QueryValueEx(key, name)
            return True
        except FileNotFoundError:
            return False
        finally:
            winreg.CloseKey(key)

    def remove(self, name):
        """delete an autostart entry"""
        if self.exists(name):
            key = self._get_key()
            try:
                winreg.DeleteValue(key, name)
            finally:
                winreg.CloseKey(key)
