# NODE # 
# $ERVER$Y$TEM # 

# Network
# contains network related functions

import logging

#==============================================================================================#
class tpls_server:
    '''
    This class will create a socket server with the handshake 
    interface from the tpls_server module. This class replaces the 
    functional implementation of the tpls server. 
    
    '''
    import sys
    import socket as soc

    from threading import Thread

    def __init__(self, ip, port):
        self.logger = logging.getLogger('Tpls_Server')
        self._ip = ip
        self._port = port
        self._socket_tup = (self._ip, self._port)
        self.__trusted_hashes = ['tpls']
        self.chash = self.open_socket()

    def _decode(self, arg):
        return arg.decode('utf-8')
    
    def _encode(self, arg):
        return arg.encode('utf-8')
    
    def _check_size(self, bytes_object, MAX_BUFFER_SIZE = 4096):
        return self.sys.getsizeof(bytes_object)

    def open_socket(self):
        self._socket = self.soc.socket(self.soc.AF_INET, self.soc.SOCK_STREAM)
        self._socket.setsockopt(self.soc.SOL_SOCKET, self.soc.SO_REUSEADDR, 1)
        self._socket.bind(self._socket_tup)
        self._socket.listen(10)
        self.conn , self.addr = self._socket.accept()
        self.__ip , self.__port = str(self.addr[0]), str(self.addr[1])
        return self.Thread(target=self.client_thread, args=(self.conn, self.__ip, self.__port)).start()
        
    def client_thread(self, conn, ip, port, MAX_BUFFER_SIZE = 4096):
        self.incoming_client_hash = self.conn.recv(MAX_BUFFER_SIZE)
        self.incoming_client_hash_size = self._check_size(self.incoming_client_hash)
        self.client_hash = self._decode(self.incoming_client_hash)
        print(self.client_hash)
        return self.client_hash

    def _client_hash_analyzer(self):
        for i in range(0, len(self.__trusted_hashes)) or self.chash == self.__trusted_hashes[i]:
            if self.chash != self.__trusted_hashes[i]:
                return False
            elif self.chash == self.__trusted_hashes[i]:
                return True
            else:
                return False

        

