#!/usr/bin/env bash


curl -X POST http://fastapi_proj-fastapi-1:8000/receive \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer insertbearer" \
  -d '{
    "receiver": "webhook",
    "status": "sleeeping",
    "orgId": 1,
    "alerts": [
      {
        "status": "firing",
        "labels": {
          "alertname": "TestAlert",
          "grafana_folder": "Test Folder",
          "instance": "Grafana"
        },
        "annotations": {
          "summary": "Notification test"
        },
        "startsAt": "2025-08-05T08:10:00Z",
        "endsAt": "0001-01-01T00:00:00Z"
      }
    ],
    "version": "4",
    "groupKey": "...",
    "title": "**Firing**",
    "state": "alerting",
    "message": "Value: B=22, C=1",
    "dashboardURL": "http://localhost:3000/d/dashboard_uid",
    "panelURL": "http://localhost:3000/d/dashboard_uid?viewPanel=1"
  }'
