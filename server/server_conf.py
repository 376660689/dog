import logging
class server_conf:
    listen = '0.0.0.0'
    server = '127.0.0.1'

    server_port = 10001
    agent_port = 10002

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)