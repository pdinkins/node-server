# NODE # 
# $ERVER$Y$TEM # 
# NETWORK #


try:
    from lib.ntwrk import pyscanner
    from lib.ntwrk import pyscanner2
    from lib.ntwrk import pyscanner3
    from lib.ntwrk import reverseshell
    from lib.ntwrk import slowloris
    from lib.ntwrk import testclient
    from lib.ntwrk import tpls_server
except ModuleNotFoundError:
    from ntwrk import pyscanner
    from ntwrk import pyscanner2
    from ntwrk import pyscanner3
    from ntwrk import reverseshell
    from ntwrk import slowloris
    from ntwrk import testclient
    from ntwrk import tpls_server    

class NetworkClient:
    '''
    NetworkClient class requires the NodeBuild class containing import config data
    '''
    def __init__(self, NodeBuild):
        self._nodebuild = NodeBuild
        self.ip = self._nodebuild._ip
        self.port = self._nodebuild._port
        self._network_scan = self.__network_scan
        self._pyscanner2 = self.__pyscanner2
        self._pyscanner = self.__pyscanner
        self._reverse_shell = self.__reverse_shell
        self._slow_loris = self.__slow_loris
        self._test_client = self.__test_client
        self._tpls_server = self.__tpls_server

    def __network_scan(self):
        return pyscanner3.main()
    
    def __pyscanner2(self):
        return pyscanner2.main()

    def __pyscanner(self):
        return pyscanner.main()
    
    def __reverse_shell(self):
        return reverseshell

    def __slow_loris(self):
        return slowloris.main()
    
    def __test_client(self):
        return testclient
    
    def __tpls_server(self):
        return tpls_server.start_handshake()
        
