# NODE #
# $ERVER$Y$TEM #

import tpls_server
import os
from lib import ipfs
import time
import ipfsapi


###### 0_NODE_SERVER ######
class NodeServer:
    """
    The node server adopts from multiple different classes.
    Gate keeper for private networks. Facilitates custom user functions. 

    IPFS Daemon must be running 
    IPFSAPI_IP: 127.0.0.1:5001/5002

    Config file is required
        > network config
        > ipfs id
        > node wallet
            > trusted peers
            > data store hashes

    > Node
        -client interface
            -user input

        -httpserver
            -filehosting
            -filestorage

        -ipfs node(daemon)
            -read
            -write

        -tpls_server
            -config security settings

    """

    def __init__(self):
        self._http_server = self.__http_server
        self._ipfs_node = self.__ipfs_node
        self._client_interface = self.__client_interface
        self._tpls_server = self.__tpls_server

    def __http_server(self):
        # host files bound to tcp port
        #_0_sxc
        os.system("start py -m http.server --bind 192.168.1.2")


    def __ipfs_node(self):
        # ipfs node connection through py-ipfs-api
        #_0_sxc
        __debug = False

        if __debug:
            os.system("start ipfs daemon --debug")
        else:
            os.system("start ipfs daemon")
        #time.sleep(3)
        #ipfs.Ipfs_API()

    def __client_interface(self):
        # cli or menu based backend interface
        #
        self.__ipfs_client = ipfsapi.client.Client()
        return self.__ipfs_client.bitswap_stat()
   
    def __tpls_server(self, _type):
        # transport layer security server
        if _type == 0:
            tpls_server.start_handshake()
        elif _type == 1:
            while True:
                tpls_server.start_handshake()
        else:
            return 0

###################
node = NodeServer()
node._ipfs_node()
