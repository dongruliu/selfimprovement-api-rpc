# client.py

from gen.example import MyService, ttypes
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket("localhost", 9090)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    client = MyService.Client(protocol)

    transport.open()

    result_add = client.add(5, 3)
    result_concatenate = client.concatenate("Hello, ", "World!")

    print(f"调用add方法的结果: {result_add}")
    print(f"调用concatenate方法的结果: {result_concatenate}")

    transport.close()

except Thrift.TException as tx:
    print(f"Thrift异常: {tx}")
