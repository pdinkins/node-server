# NODE #
# $ERVER$Y$TEM #

from lib import tpls_server
import os
from lib import ipfs
import time
import ipfsapi

# local bool variable to control what the node server launches on start up
_b_http = True
_b_ipfs = True
_b_cli = True
_b_tpls = True

# node networking variables
__node_ip = '192.168.1.7'
__node_port = 1423

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
        self._cli_dir = self.__client_interface_dir

    def __http_server(self):
        # host files bound to tcp port
        #_0_sxc
        os.system("start py -m http.server --bind 192.168.1.7")


    def __ipfs_node(self):
        # ipfs node connection through py-ipfs-api
        #_0_sxc
        __debug = False

        if __debug:
            os.system("start ipfs daemon --debug")
        else:
            os.system("start ipfs daemon")
        time.sleep(3)
        ipfs.Ipfs_API()

    def __client_interface(self):
        # cli or menu based backend interface
        #
        self.__ipfs_client = ipfsapi.client.Client()
        return self.__ipfs_client
   
    def __tpls_server(self, _type):
        # transport layer security server
        if _type == 0:
            tpls_server.start_handshake()
        elif _type == 1:
            while True:
                tpls_server.start_handshake()
        else:
            return 0
    
    def __client_interface_dir(self):
        return dir(self._client_interface())


#########_NODE_##########

node = NodeServer()

def __b00l_launch():
    if _b_ipfs:
        node._ipfs_node()
    elif _b_cli:
        node._client_interface()
    elif _b_http:
        node._http_server()
    elif _b_tpls:
        node._tpls_server(0)

def bl():
    __b00l_launch()
