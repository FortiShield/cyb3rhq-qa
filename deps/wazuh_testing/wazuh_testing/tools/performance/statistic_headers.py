analysisd_events_header =  ["Timestamp",
                            "API Timestamp",
                            "Interval (Timestamp-Uptime)",
                            "Events processed",
                            "Events received",

                            "Decoded from azure",
                            "Decoded from ciscat",
                            "Decoded from command",
                            "Decoded from docker",
                            "Decoded from logcollector eventchannel",
                            "Decoded from logcollector eventlog",
                            "Decoded from logcollector macos",
                            "Decoded from logcollector others",
                            "Decoded from osquery",
                            "Decoded from rootcheck",
                            "Decoded from sca",
                            "Decoded from syscheck",
                            "Decoded from syscollector",
                            "Decoded from vulnerability",
                            "Decoded from agentd",
                            "Decoded from dbsync",
                            "Decoded from monitor",
                            "Decoded from remote",

                            "Dropped from azure",
                            "Dropped from ciscat",
                            "Dropped from command",
                            "Dropped from docker",
                            "Dropped from logcollector eventchannel",
                            "Dropped from logcollector eventlog",
                            "Dropped from logcollector macos",
                            "Dropped from logcollector others",
                            "Dropped from osquery",
                            "Dropped from rootcheck",
                            "Dropped from sca",
                            "Dropped from syscheck",
                            "Dropped from syscollector",
                            "Dropped from vulnerability",
                            "Dropped from agentd",
                            "Dropped from dbsync",
                            "Dropped from monitor",
                            "Dropped from remote",

                            "Written alerts",
                            "Written archives",
                            "Written firewall",
                            "Written fts",
                            "Written stats",

                            "EDPS from azure",
                            "EDPS from ciscat",
                            "EDPS from command",
                            "EDPS from docker",
                            "EDPS from logcollector eventchannel",
                            "EDPS from logcollector eventlog",
                            "EDPS from logcollector macos",
                            "EDPS from logcollector others",
                            "EDPS from osquery",
                            "EDPS from rootcheck",
                            "EDPS from sca",
                            "EDPS from syscheck",
                            "EDPS from syscollector",
                            "EDPS from vulnerability",
                            "EDPS from agentd",
                            "EDPS from dbsync",
                            "EDPS from monitor",
                            "EDPS from remote"
                        ]
analysisd_header = ["Timestamp",
                    "Total Events",
                    "Syscheck Events Decoded",
                    "Syscollector Events Decoded",
                    "Rootcheck Events Decoded",
                    "SCA Events Decoded",
                    "WinEvt Events Decoded",
                    "DBSync Messages dispatched",
                    "Other Events Decoded",
                    "Events processed (Rule matching)",
                    "Events received",
                    "Events dropped",
                    "Alerts written",
                    "Firewall alerts written",
                    "FTS alerts written",
                    "Syscheck queue usage",
                    "Syscheck queue size",
                    "Syscollector queue usage",
                    "Syscollector queue size",
                    "Rootcheck queue usage",
                    "Rootcheck queue size",
                    "SCA queue usage",
                    "SCA queue size",
                    "Hostinfo queue usage",
                    "Hostinfo queue size",
                    "Winevt queue usage",
                    "Winevt queue size",
                    "DBSync queue usage",
                    "DBSync queue size",
                    "Upgrade queue usage",
                    "Upgrade queue size",
                    "Event queue usage",
                    "Event queue size",
                    "Rule matching queue usage",
                    "Rule matching queue size",
                    "Alerts log queue usage",
                    "Alerts log queue size",
                    "Firewall log queue usage",
                    "Firewall log queue size",
                    "Statistical log queue usage",
                    "Statistical log queue size",
                    "Archives log queue usage",
                    "Archives log queue size"
                    ]
logcollector_header = ["Timestamp",
                       "Location",
                       "Events",
                       "Bytes",
                       "Target",
                       "Target Drops"
                    ]
remoted_header = ["Timestamp",
                "Queue size",
                "Total Queue size",
                "TCP sessions",
                "Events count",
                "Control messages",
                "Discarded messages",
                "Bytes received"]

remoted_api_header = ["Timestamp",
                    "API Timestamp",
                    "Interval (Timestamp-Uptime)",
                    "Queue size",
                    "Queue usage",
                    "TCP sessions",
                    "Keys reload count",

                    "Control messages",
                    "Control keepalives",
                    "Control requests",
                    "Control shutdown",
                    "Control startup",

                    "Dequeued messages",
                    "Discarded messages",
                    "Events count",
                    "Ping messages",
                    "Unknown messages",

                    "Sent ack",
                    "Sent ar",
                    "Sent discarded",
                    "Sent request",
                    "Sent sca",
                    "Sent shared",

                    "Metrics-Bytes received",
                    "Metrics-Bytes sent"]

agentd_header = ["Timestamp",
                 "Status",
                 "Last Keepalive",
                 "Last ACK",
                 "Number of generated events",
                 "Number of messages",
                 "Number of events buffered"]

vulns_header = ["Timestamp",
                "Total vulnerabilities"]

alerts_header = ["Timestamp",
                 "Total alerts"]


wazuhdb_header = ["Timestamp",
                    "API Timestamp",
                    "Interval (Timestamp-Uptime)",
	                ## QUERIES COUNTS
                    "Received queries",
                    "Agent queries",
		            ## Agent QueriesBreakdown
                    "db-begin",
                    "db-close",
                    "db-commit",
                    "db-remove",
                    "db-sql",
                    "db-vacuum",
                    "db-get_fragmentation",
		            ## Agent Tables Breakdown
                    "Table CisCat",
                    "Table Rootcheck",
                    "Table SCA",
                    "Table dbsync",
                    "Table Syscheck",
                    "Table Syscheck file",
                    "Table Syscheck registry",
                    "Table Syscheck registry_key",
                    "Table Syscheck registry_value",
                    "Table Syscollector hotfixes",
                    "Table Syscollector hwinfo",
                    "Table Syscollector network_address",
                    "Table Syscollector network_iface",
                    "Table Syscollector network_protocol",
                    "Table Syscollector os_info",
                    "Table Syscollector packages",
                    "Table Syscollector ports",
                    "Table Syscollector processes",
                    "Table Vulnerability CVEs",

                    "Global queries",
		             ## Global Queries Breakdown
                    "db-backup",
                    "db-sql",
                    "db-vacuum",
                    "db-get_fragmentation",

                    "agent-delete-agent",
                    "agent-disconnect-agents",
                    "agent-find-agent",
                    "agent-get-agent-info",
                    "agent-get-agents-by-connection-status",
                    "agent-get-all-agents",
                    "agent-get-distinct-groups",
                    "agent-get-groups-integrity",
                    "agent-insert-agent",
                    "agent-reset-agents-connection",
                    "agent-select-agent-group",
                    "agent-select-agent-name",
                    "agent-set-agent-groups",
                    "agent-sync-agent-groups-get",
                    "agent-sync-agent-info-get",
                    "agent-sync-agent-info-set",
                    "agent-update-agent-data",
                    "agent-update-agent-name",
                    "agent-update-connection-status",
                    "agent-update-status-code",
                    "agent-update-keepalive",

		            "belongs-get-group-agents",
                    "belongs-select-group-belong",

		            "group-delete-group",
                    "group-find-group",
                    "group-insert-agent-group",
                    "group-select-groups",
        		    "labels-get-labels",

		            "MITRE",
                    "Tasks",
                    ## tasks breakdown
                    "tasks-delete old task",
                    "tasks-set timeout",
                    "tasks-upgrade",
                    "tasks-upgrade cancel",
                    "tasks-upgrade custom",
                    "tasks-upgrade get status",
                    "tasks-upgrade results",
                    "tasks-upgrade update status",
                    "Wazuhdb",

                    ## QUERIES TIME METRICS - IN MILISECONDS
                    "Total Execution Time",	
                    "Agent ExecTime",
                    ## Agent Time Breakdown
                    "db-open",
                    "db-begin",
                    "db-close",
                    "db-commit",
                    "db-remove",
                    "db-sql",
                    "db-vacuum",
                    "db-get_fragmentation",
		            ## Agent Tables Breakdown
                    "Table CisCat",
                    "Table Rootcheck",
                    "Table SCA",
                    "Table dbsync",
                    "Table Syscheck",
                    "Table Syscheck file",
                    "Table Syscheck registry",
                    "Table Syscheck registry_key",
                    "Table Syscheck registry_value",
                    "Table Syscollector hotfixes",
                    "Table Syscollector hwinfo",
                    "Table Syscollector network_address",
                    "Table Syscollector network_iface",
                    "Table Syscollector network_protocol",
                    "Table Syscollector os_info",
                    "Table Syscollector packages",
                    "Table Syscollector ports",
                    "Table Syscollector processes",
                    "Table Vulnerability CVEs",

                    ## Global Queries Time Breakdown
                    "Global Queries ExecTime",
                    "db-open",
                    "db-backup",
                    "db-sql",
                    "db-vacuum",
                    "db-get_fragmentation",
                    ## Global Tables breakdown
                    "agent-delete-agent",
                    "agent-disconnect-agents",
                    "agent-find-agent",
                    "agent-get-agent-info",
                    "agent-get-agents-by-connection-status",
                    "agent-get-all-agents",
                    "agent-get-distinct-groups",
                    "agent-get-groups-integrity",
                    "agent-insert-agent",
                    "agent-reset-agents-connection",
                    "agent-select-agent-group",
                    "agent-select-agent-name",
                    "agent-set-agent-groups",
                    "agent-sync-agent-groups-get",
                    "agent-sync-agent-info-get",
                    "agent-sync-agent-info-set",
                    "agent-update-agent-data",
                    "agent-update-agent-name",
                    "agent-update-connection-status",
                    "agent-update-status-code",
                    "agent-update-keepalive",
                    "belongs-get-group-agents",
                    "belongs-select-group-belong",
                    "group-delete-group",
                    "group-find-group",
                    "group-insert-agent-group",
                    "group-select-groups",
                    "labels-get-labels",

                    "MITRE",
                    "Tasks",
                    ## tasks breakdown
                    "tasks-delete old task",
                    "tasks-set timeout",
                    "tasks-upgrade",
                    "tasks-upgrade cancel",
                    "tasks-upgrade custom",
                    "tasks-upgrade get status",
                    "tasks-upgrade results",
                    "tasks-upgrade update status",
                    "Wazuhdb"
                ]
