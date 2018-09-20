# NODE #
# $ERVER$Y$TEM #

# -------- IMPORTS --------- # 
# Local imports
from lib import tpls_server
from lib import ipfs

# python builtin imports
import os
import time

# third party package imports
import ipfsapi
# -------------------------- # 



# local bool variable to control what the node server launches on start up
_b_http = False
_b_ipfs = False
_b_cli = False
_b_tpls = True

# node networking variables
_0_node_ip = "192.168.1.7"
_0_node_port = 1423

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
            -network communications

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
        # spawn different kinds of tpls instances 
        
        # functional transport layer security server
        # begin one time functional tpls instance
        if _type == 0:
            return tpls_server.start_handshake()
        
        # begin an infinite loop of functional tpls instances
        elif _type == 1:
            while True:
                tpls_server.start_handshake() 
        

        # tpls class instance
        elif _type == 2:
            # OOP implementation of the TPLS Server
            tpls_server.TPLS_Server(_0_node_ip, _0_node_port)
        
        else:
            return 0
    

    def __client_interface_dir(self):
        # list of 
        return dir(self._client_interface())


#########_NODE_##########

node = NodeServer()

def __b00l_launch():
    if _b_ipfs:
        node._ipfs_node()
    
    if _b_cli:
        node._client_interface()
    
    if _b_http:
        node._http_server()
    
    if _b_tpls:
        node._tpls_server(2)

# launch the 
# __b00l_launch()

