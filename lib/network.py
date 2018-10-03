# NODE # 
# $ERVER$Y$TEM # 
# NETWORK #


class NetworkClient:
    '''
    NetworkClient class requires the NodeBuild class containing import config data
    '''
    def __init__(self, **NodeBuild):
        #self._nodebuild = NodeBuild
        #self.ip = self._nodebuild._ip
        #self.port = self._nodebuild._port
        self._network_scan = self.__network_scan
        self._pyscanner2 = self.__pyscanner2
        self._pyscanner = self.__pyscanner
        self._reverse_shell = self.__reverse_shell
        self._tpls_server = self.__tpls_server

    def __network_scan(self):
        print('__NetworkClient.__network_scan()')
        from ntwrk import pyscanner3
        return pyscanner3
    
    def __pyscanner2(self):
        print('__NetworkClient.__pyscanner2()')
        from ntwrk import pyscanner2
        return pyscanner2

    def __pyscanner(self):
        print('__NetworkClient.__pyscannern()')
        from ntwrk import pyscanner
        return pyscanner
    
    def __reverse_shell(self):
        print('__NetworkClient.__reverse_shell()')
        from ntwrk import reverseshell
        return reverseshell
    
    def __tpls_server(self):
        print('__NetworkClient.__tpls_server()')
        from ntwrk import tpls_server
        return tpls_server
        
