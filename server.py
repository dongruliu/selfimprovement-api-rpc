# server.py

from gen.example import MyService, ttypes
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class MyHandler:
    def add(self, arg1, arg2):
        return arg1 + arg2

    def concatenate(self, s1, s2):
        return s1 + s2

handler = MyHandler()
processor = MyService.Processor(handler)
transport = TSocket.TServerSocket(host="localhost", port=9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Thrift RPC服务器正在监听端口9090...")
server.serve()
