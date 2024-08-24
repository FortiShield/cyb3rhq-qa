# Copyright (C) 2015-2023, Cyb3rhq Inc.
# Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.
# This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

import pytest

from cyb3rhq_testing import LOG_FILE_PATH
from cyb3rhq_testing.tools.file import truncate_file
from cyb3rhq_testing.tools.monitoring import FileMonitor
from cyb3rhq_testing.tools.services import control_service
from cyb3rhq_testing.modules.fim.event_monitor import detect_initial_scan, detect_realtime_start, detect_whodata_start


@pytest.fixture(scope='module')
def restart_syscheckd(get_configuration, request):
    """
    Reset ossec.log and start a new monitor.
    """
    control_service('stop', daemon='cyb3rhq-syscheckd')
    truncate_file(LOG_FILE_PATH)
    file_monitor = FileMonitor(LOG_FILE_PATH)
    setattr(request.module, 'cyb3rhq_log_monitor', file_monitor)
    control_service('start', daemon='cyb3rhq-syscheckd')


@pytest.fixture(scope='module')
def wait_for_fim_start(get_configuration, request):
    """
    Wait for realtime start, whodata start or end of initial FIM scan.
    """
    file_monitor = FileMonitor(LOG_FILE_PATH)
    mode_key = 'fim_mode' if 'fim_mode2' not in get_configuration['metadata'] else 'fim_mode2'

    try:
        if get_configuration['metadata'][mode_key] == 'realtime':
            detect_realtime_start(file_monitor)
        elif get_configuration['metadata'][mode_key] == 'whodata':
            detect_whodata_start(file_monitor)
        else:  # scheduled
            detect_initial_scan(file_monitor)
    except KeyError:
        detect_initial_scan(file_monitor)
