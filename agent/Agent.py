import eventlet
from agent_conf import agent_conf
from agent_conf import model
from agent_conf import logger

from agent_model import cpu_count,cpu_person

def handle(sock):
    while True:
        rec = sock.recv(1024)
        if not rec:
            break

        if rec.decode() in model:
            data = eval(rec.decode().replace('.', '_'))()
            logger.debug('execute function %s' % rec.decode().replace('.', '_'))
            if isinstance(data, int) or isinstance(data, float):
                sock.send(str(data).encode())
            elif isinstance(data, str):
                sock.sendall(data.encode())
        else:
            sock.sendall(b'no')

try:
    server = eventlet.listen((agent_conf.listen, agent_conf.agent_port))
    pool = eventlet.GreenPool(agent_conf.maxclient)
except Exception as msg:
    raise msg
finally:
    logger.info("listen %s:%s" % (agent_conf.listen, agent_conf.agent_port))

while True:
    try:
        sock, address = server.accept()
        pool.spawn_n(handle, sock)
        logger.info(address)
    except Exception as msg:
        raise msg