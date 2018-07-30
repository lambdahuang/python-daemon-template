import yaml
import sys
from services.service import MyService


def load_config(config_path, **param):
    """ load service config
        :param config_path: path to the service config

        :return a dictionary contains service config
    """
    if len(sys.argv) != 2:
        sys.exit('Syntax: %s COMMAND' % sys.argv[0])
    cmd = sys.argv[1].lower()
    with open(config_path, 'r') as stream:
        config = yaml.load(stream)
    config = {**config['srv_config'], **param}
    config['SERVICE'] = MyService(config['service_name'], pid_dir='/tmp')
    config['CMD'] = cmd
    return config


def start_service(config):
    """ Kick off service instance """
    config['SERVICE'].start()


def stop_service(config):
    """ Soft terminate a service """
    config['SERVICE'].stop()


def get_service_status(config):
    """ get service status """
    if config['SERVICE'].is_running():
        print('Service is running.')
    else:
        print('Service is not running.')


def get_default_action():
    """ get default actions """
    action = dict()
    action['start'] = start_service
    action['stop'] = stop_service
    action['status'] = get_service_status

    return action


def execute_action(actions, config):
    """ trigger the execution """
    cmd = config['CMD']
    if cmd not in actions:
        print('Unknown command')
        return
    actions[cmd](config)
