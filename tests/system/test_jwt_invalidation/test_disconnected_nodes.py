# Copyright (C) 2015-2021, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import os
import time

import pytest
from cyb3rhq_testing.tools.system import HostManager


pytestmark = [pytest.mark.agentless_cluster_env]

test_hosts = ['cyb3rhq-master', 'cyb3rhq-worker1', 'cyb3rhq-worker2']
inventory_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                              'provisioning', 'agentless_cluster', 'inventory.yml')
default_api_conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'api_configurations', 'default.yaml')

host_manager = HostManager(inventory_path)


def control_cyb3rhq_services(node, state=None):
    """Control Cyb3rhq services with `command` instead of `service` due to incompatibility."""
    host_manager.get_host(node).ansible('command', f'service cyb3rhq-manager {state}', check=False)
    host_manager.get_host(node).ansible('command', f'service cyb3rhq-api {state}', check=False)
    if 'start' in state:
        time.sleep(10)


# Clean environment in case the test fails
@pytest.fixture(scope='module')
def clean_environment():
    yield

    token = host_manager.get_api_token('cyb3rhq-master')
    response = host_manager.make_api_call('cyb3rhq-master', method='DELETE',
                                          endpoint='/security/users?user_ids=all', token=token)

    assert response['status'] == 200, f'Failed to clean environment: {response}'
    for host in test_hosts[1:]:
        control_cyb3rhq_services(host, state='restart')


def test_create_user_when_node_is_disconnected(set_default_api_conf, clean_environment):
    """Check that user information is not lost when different nodes from the cluster disconnect and reconnect."""
    # Disconnect both workers from cluster and API
    control_cyb3rhq_services('cyb3rhq-worker1', state='stop')
    control_cyb3rhq_services('cyb3rhq-worker2', state='stop')

    # Get token in the master node
    master_token = host_manager.get_api_token('cyb3rhq-master')

    # Create user in the master node
    test_user = 'NewTestUser'
    test_pass = 'NewPassword1*'
    response = host_manager.make_api_call('cyb3rhq-master', method='POST', endpoint='/security/users',
                                          request_body={'username': test_user,
                                                        'password': test_pass},
                                          token=master_token)
    assert response['status'] == 200, f'Failed to create user: {response}'
    test_user_id = response['json']['data']['affected_items'][0]['id']

    # Reconnect worker1 and check that the user is created
    control_cyb3rhq_services('cyb3rhq-worker1', state='start')
    host_manager.get_api_token('cyb3rhq-worker1', user=test_user, password=test_pass)

    # Remove the user in the master node
    response = host_manager.make_api_call('cyb3rhq-master', method='DELETE',
                                          endpoint=f'/security/users?user_ids={test_user_id}',
                                          token=master_token)
    assert response['status'] == 200, f'Failed to delete user: {response}'

    # Reconnect worker2 and check that the user does not exist
    control_cyb3rhq_services('cyb3rhq-worker2', state='start')
    # 'KeyError' since the `get_api_token` tries to return `response['json']['token']`
    with pytest.raises(KeyError):
        host_manager.get_api_token('cyb3rhq-worker2', user=test_user, password=test_pass)
        raise ValueError('Unexpected token. This user should not exist.')
