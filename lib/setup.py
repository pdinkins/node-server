# NODE # 
# $ERVER$Y$TEM # 
# SETUP #

'''
# SETUP
#
# sniffs current build and generates current config file
# configures and installs ipfs dynamically 
#
# import setup
# 
# user = setup.UserBuild()
'''

# python module imports
import hashlib
from requests import get
import platform

# local lib imports
try:
    from lib._log import log
    from lib.writer import FileObject, Write2file
except ModuleNotFoundError:
    from _log import log
    from writer import FileObject, Write2file

class UserBuild:
    '''
        # for testing current cpu system configuration 
        # and checks for corrupted or out of date software
    '''

    def __init__(self):
        self.operating_sys = self.os_sys()
        self.node_ip = self.get_ip()
        self.build = self.user_build()
        self._hash_value = self.__hash(self.build, self.node_ip)
        self.config_file = self._config_file()

    def __hash(self, val1, val2):
        self._hv = str(val1) + str(val2)
        log(type(self._hv))
        log(self._hv)
        self.__hv = hashlib.sha256(self._hv.encode('utf-8')).hexdigest()
        log(type(self.__hv))
        log(self.__hv)
        # reutrn hash value
        return self.__hv

    def os_sys(self):
        return platform.system()
    
    def get_ip(self):
        log('obtaining ip info')
        self.location = Location()
        self.__0_node_ip = self.location.ip
        log(self.__0_node_ip)
        log('network host scan initiating')
        return self.__0_node_ip

    def user_build(self):
        log('user_build')
        # initial import
        log('Initial Imports')
        try:
            import os, sys
            log('import: os, sys') 
            from platform import platform, python_branch, python_compiler, machine, python_build
            log('import: platform')
        except:
            print('FATAL_PYTHON_BUILD_ERROR')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
        try:
            log('0_SYSTEM_PYTHON_CONFIG')
            self.node = platform()
            log(self.node)
            #self._python_build = python_build()
            #log(self._python_build)
            self._python_compiler = python_compiler()
            log(self._python_compiler)
            self.pmachine = machine()
            log(self.pmachine)
            log('0_SYSTEM_CONFIGFILE')
            self.n0osd = [
                self.node,
                self._python_compiler,
                self.pmachine]
            log("USER_BUILD_COMPLETE")
            return self.n0osd
        except:
            log('USER_BUILD_FAILED')
            log('something went horribly wrong')
            error = sys.exc_info()
            print(error)
            print(sys.exc_info()[0])
            raise
    
    def _config_file(self):
        self.__config_file = FileObject(self._hash_value, 'txt')
        Write2file(self.__config_file.file, self.build)
        return self.__config_file


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

