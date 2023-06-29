* Python instrumentation for Prometheus [client librar][def]

* The exporter looks for `projects` file in the `/tmp` dir,  containing the domains that needs to be scraped
```bash
docker run -p 8081:8088 -v /tmp:/tmp dejanualex/synergy_exporter:1.0
```

[def]: https://pypi.org/project/prometheus-client/