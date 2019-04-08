import pdb
import eventlet
from server_conf import server_conf

try:
    agent_connect = eventlet.connect(('127.0.0.1', server_conf.agent_port))
except Exception as msg:
    raise msg

sock_opts = agent_connect.getpeername()

for i in [b'cpu.person', b'cpu.count']:
    agent_connect.send(i)
    data = agent_connect.recv(1024)
    print(data)
agent_connect.close()