'''
copyright: Copyright (C) 2015-2022, Cyb3rhq Inc.

           Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.

           This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

type: integration

brief: File Integrity Monitoring (FIM) system watches selected files and triggering alerts when these
       files are modified. Specifically, these tests will verify that when the 'cyb3rhq-syscheckd' daemon
       is disabled, no FIM events are generated.
       The FIM capability is managed by the 'cyb3rhq-syscheckd' daemon, which checks configured files
       for changes to the checksums, permissions, and ownership.

components:
    - fim

suite: files_basic_usage

targets:
    - agent
    - manager

daemons:
    - cyb3rhq-syscheckd

os_platform:
    - linux
    - windows

os_version:
    - Arch Linux
    - Amazon Linux 2
    - Amazon Linux 1
    - CentOS 8
    - CentOS 7
    - Debian Buster
    - Red Hat 8
    - Ubuntu Focal
    - Ubuntu Bionic
    - Windows 10
    - Windows Server 2019
    - Windows Server 2016

references:
    - https://documentation.cyb3rhq.com/current/user-manual/capabilities/file-integrity/index.html
    - https://documentation.cyb3rhq.com/current/user-manual/reference/ossec-conf/syscheck.html

pytest_args:
    - fim_mode:
        realtime: Enable real-time monitoring on Linux (using the 'inotify' system calls) and Windows systems.
        whodata: Implies real-time monitoring but adding the 'who-data' information.
    - tier:
        0: Only level 0 tests are performed, they check basic functionalities and are quick to perform.
        1: Only level 1 tests are performed, they check functionalities of medium complexity.
        2: Only level 2 tests are performed, they check advanced functionalities and are slow to perform.

tags:
    - fim_basic_usage
'''
import os

import pytest
from cyb3rhq_testing import T_10, LOG_FILE_PATH
from cyb3rhq_testing.tools import PREFIX
from cyb3rhq_testing.tools.configuration import load_cyb3rhq_configurations
from cyb3rhq_testing.tools.monitoring import FileMonitor
from cyb3rhq_testing.modules.fim.event_monitor import callback_detect_end_scan
from cyb3rhq_testing.modules.fim.utils import generate_params, regular_file_cud

# Marks

pytestmark = pytest.mark.tier(level=0)

# variables

test_directories = [os.path.join(PREFIX, 'testdir')]
directory_str = test_directories[0]
cyb3rhq_log_monitor = FileMonitor(LOG_FILE_PATH)
test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
configurations_path = os.path.join(test_data_path, 'cyb3rhq_conf_disabled.yaml')
testdir = test_directories[0]

# configurations

conf_params = {'TEST_DIRECTORIES': directory_str}
p, m = generate_params(extra_params=conf_params)

configurations = load_cyb3rhq_configurations(configurations_path, __name__, params=p, metadata=m)


# fixtures

@pytest.fixture(scope='module', params=configurations)
def get_configuration(request):
    """Get configurations from the module."""
    return request.param


# tests

def test_disabled(get_configuration, configure_environment, restart_syscheckd):
    '''
    description: Check if the 'cyb3rhq-syscheckd' daemon generates FIM events when it is disabled
                 in the main configuration file. For this purpose, the test will monitor a testing
                 folder and finally verifies that no FIM events have been generated.

    cyb3rhq_min_version: 4.2.0

    tier: 0

    parameters:
        - get_configuration:
            type: fixture
            brief: Get configurations from the module.
        - configure_environment:
            type: fixture
            brief: Configure a custom environment for testing.
        - restart_syscheckd:
            type: fixture
            brief: Clear the 'ossec.log' file and start a new monitor.

    assertions:
        - Verify that when the 'cyb3rhq-syscheckd' daemon is disabled, no FIM events are generated.

    input_description: A test case is contained in external YAML file (cyb3rhq_conf_disabled.yaml) which
                       includes configuration settings for the 'cyb3rhq-syscheckd' daemon and, it is combined
                       with the testing directory to be monitored defined in this module.

    expected_output:
        - No FIM events should be generated.

    tags:
        - scheduled
    '''
    # Expect a timeout when checking for syscheckd initial scan
    with pytest.raises(TimeoutError):
        event = cyb3rhq_log_monitor.start(timeout=T_10, callback=callback_detect_end_scan)
        raise AttributeError(f'Unexpected event {event}')

    # Use 'regular_file_cud' and don't expect any event
    regular_file_cud(testdir, cyb3rhq_log_monitor, min_timeout=T_10, triggers_event=False)
