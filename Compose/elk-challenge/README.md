deploy elasticsearch and kibana

```
docker-compose up -d elasticsearch kibana
```

metricbeat init to create elasticsaerch index and create kibana dashboards. Run until exit:

```
docker-compose up metricbeat-init
```

run metricbeat to start sending metrics to elasticsearch:

```
docker-compose up -d metricbeat
```

To stop and delete containers and volumes:

```
docker-compose down -v
```
