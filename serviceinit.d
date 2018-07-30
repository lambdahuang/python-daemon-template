#! /usr/bin/env python
import sys
from util import serviceinitlib

if __name__ == '__main__':
    config = serviceinitlib.load_config('./config.yaml')
    actions = serviceinitlib.get_default_action()
    
    serviceinitlib.execute_action(actions, config)
