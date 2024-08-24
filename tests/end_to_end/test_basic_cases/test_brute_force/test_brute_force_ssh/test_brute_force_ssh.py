'''
copyright: Copyright (C) 2015-2022, Cyb3rhq Inc.

           Created by Cyb3rhq, Inc. <info@cyb3rhq.com>.

           This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

type: end_to_end

brief: This test will verify that the detection of brute force attacks is working correctly.

components:
    - logcollector

targets:
    - manager
    - agent

daemons:
    - cyb3rhq-logcollector
    - cyb3rhq-analysisd

os_platform:
    - linux

os_version:
    - CentOS 8

references:
    - https://github.com/cyb3rhq/cyb3rhq-automation/wiki/Cyb3rhq-demo:-Execution-guide#brute-force
    - https://documentation.cyb3rhq.com/current/proof-of-concept-guide/detect-brute-force-attack.html

tags:
    - demo
    - brute_force_attack
    - ssh
'''
import os
import json
import re
import pytest

import cyb3rhq_testing as fw
from cyb3rhq_testing.tools import configuration as config
from cyb3rhq_testing import end_to_end as e2e
from cyb3rhq_testing import event_monitor as evm
from cyb3rhq_testing.modules import TIER0, LINUX

# Test cases data
test_data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
test_cases_file_path = os.path.join(test_data_path, 'test_cases', 'cases_brute_force_ssh.yaml')

# Playbooks
events_playbooks = ['generate_events.yaml']
teardown_playbooks = None

# Configuration
configurations, configuration_metadata, cases_ids = config.get_test_cases_data(test_cases_file_path)

# Marks
pytestmark = [TIER0, LINUX]


@pytest.mark.filterwarnings('ignore::urllib3.exceptions.InsecureRequestWarning')
@pytest.mark.parametrize('metadata', configuration_metadata, ids=cases_ids)
def test_brute_force_ssh(metadata, get_indexer_credentials, get_manager_ip, generate_events, clean_alerts_index):
    '''
    description: Check that an alert is generated and indexed when a brute force attack is perfomed.

    test_phases:
        - Set a custom Cyb3rhq configuration.
        - Run ssh command to attempt an invalid SSH connection and generate event.
        - Check in the alerts.json log that the expected alert has been triggered and get its timestamp.
        - Check that the obtained alert from alerts.json has been indexed.

    cyb3rhq_min_version: 4.4.0

    tier: 0

    parameters:
        - metadata:
            type: dict
            brief: Cyb3rhq configuration metadata.
        - get_indexer_credentials:
            type: fixture
            brief: Get the cyb3rhq indexer credentials.
        - generate_events:
            type: fixture
            brief: Generate events that will trigger the alert according to the generate_events playbook.
        - clean_alerts_index:
            type: fixture
            brief: Delete obtained alerts.json and alerts index.

    assertions:
        - Verify that the alert has been triggered.
        - Verify that the same alert has been indexed.

    input_description:
        - The `generate_events.yaml`file provides the function configuration for this test.
    '''
    rule_id = metadata['extra_vars']['rule_id']
    rule_level = metadata['extra_vars']['rule_level']
    rule_description = metadata['extra_vars']['rule_description']
    rule_mitre_technique = metadata['extra']['mitre_technique']
    timestamp_regex = r'\d+-\d+-\d+T\d+:\d+:\d+\.\d+[+|-]\d+'

    expected_alert_json = fr'\{{"timestamp":"({timestamp_regex})","rule"\:{{"level"\:{rule_level},' \
                          fr'"description"\:"{rule_description}","id"\:"{rule_id}".*'

    expected_indexed_alert = fr'.*"rule":.*"level": {rule_level},.*"description": "{rule_description}"' \
                             fr'.*"mitre":.*"{rule_mitre_technique}".*"id": "{rule_id}".*'

    # Check that alert has been raised and save timestamp
    raised_alert = evm.check_event(callback=expected_alert_json, file_to_monitor=e2e.fetched_alerts_json_path,
                                   timeout=fw.T_5, error_message='The alert has not occurred').result()
    raised_alert_timestamp = raised_alert.group(1)

    query = e2e.make_query([
        {
            "term": {
                "rule.id": f"{rule_id}"
            }
        },
        {
            "term": {
                "timestamp": f"{raised_alert_timestamp}"
            }
        }
    ])

    # Check if the alert has been indexed and get its data
    response = e2e.get_alert_indexer_api(query=query, credentials=get_indexer_credentials, ip_address=get_manager_ip)
    indexed_alert = json.dumps(response.json())

    # Check that the alert data is the expected one
    alert_data = re.search(expected_indexed_alert, indexed_alert)
    assert alert_data is not None, 'Alert triggered, but not indexed'
