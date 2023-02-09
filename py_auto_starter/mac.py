import os
import plistlib


class MacAutoStarter:

    def __init__(self):
        self.launch_agents = '~/Library/LaunchAgents'
        if not os.path.exists(self.launch_agents):
            os.makedirs(self.launch_agents)

    def _getfilename(self, name):
        """get the filename of an autostart (.plist) file"""
        return os.path.join(self.launch_agents, name + ".plist")

    def add(self, name, app_path):
        """add a new autostart entry"""
        pl = dict(
            Label=name,
            RunAtLoad=True,
            Program=app_path
        )
        with open(self._getfilename(name), 'wb') as fp:
            plistlib.dump(pl, fp)

    def exists(self, name):
        """check if an autostart entry exists"""
        return os.path.exists(self._getfilename(name))

    def remove(self, name):
        """delete an autostart entry"""
        if self.exists(name):
            os.unlink(self._getfilename(name))
