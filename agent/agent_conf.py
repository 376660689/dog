import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class agent_conf:
    listen = '0.0.0.0'
    maxclient = 100
    log_file = 'info.log'
    connect = '127.0.0.1'
    server_port = 10001
    agent_port = 10002

model = [
    'ipaddr.public',
    'cpu.count',
    'cpu.person',
]