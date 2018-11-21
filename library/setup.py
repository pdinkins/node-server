# NODE $ERVER$Y$TEM ## SETUP #
'''
# SETUP
#
# sniffs current build and generates current config file
# configures and installs ipfs
#
# import setup
# 
# user = setup.UserBuild()
'''
# ------ IMPORTS ------ #
# python module imports
import platform

# local lib imports
try:
    from library._log import log
    from library.writer import FileObject, Write2file
except ModuleNotFoundError:
    from _log import log
    from writer import FileObject, Write2file

# third party package imports
from requests import get


# USER BUILD 
class UserBuild:
    '''
        # sniff current cpu system configuration 
        # establish configuration information
        1. ip address
        2. operating system
        3. cpu information
        4. python config 
        5. ipfs config
        6. requirements config
        # TODO: check for corrupted or out of date software
    '''
    def __init__(self):
        self.operating_sys = self.os_sys()
        self.location = Location()
        self.node_ip = self.get_ip()

    def os_sys(self):
        return platform.system()
    
    def get_ip(self):
        log('obtaining ip info')
        self.__0_node_ip = self.location.ip
        log(self.__0_node_ip)
        return self.__0_node_ip


class Location:
    """
    virtual and physical location class
    """
    def __init__(self):
        self.location = self.__location()
        self.ip = self.__get_ip()


    def __location(self):
        self._location = []
        return self._location

    def __get_ip(self):
        try:
            self._0_node_ip = get('http://ip.42.pl/raw').text
        except:
            self._0_node_ip = 'No network connection'
        return self._0_node_ip  




if __name__ == "__main__":
    Node = UserBuild()

