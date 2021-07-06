#!/bin/bash

# create dir structure needed for provisioning
mkdir -p provisioning/{datasources,notifiers,dashboards/backup}

# write all.yml config for dashboards - more info here https://grafana.com/docs/grafana/latest/administration/provisioning/
tee -a ./provisioning/dashboards/all.yml << END
- name: 'default'       # name of this dashboard configuration (not dashboard itself)
  org_id: 1             # id of the org to hold the dashboard
  folder: ''            # name of the folder to put the dashboard (http://docs.grafana.org/v5.0/reference/dashboard_folders/)
  type: 'file'          # type of dashboard description (json files)
  options:
    # where dashboards are
    #folder: '/var/lib/grafana/dashboards'
    # <string, required> path to dashboard files on disk. Required when using the 'file' type
    path: /var/lib/grafana/dashboards
    # <bool> use folder names from filesystem to create folders in Grafana
    foldersFromFilesStructure: true

END
