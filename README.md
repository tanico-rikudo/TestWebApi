# PythonTester

This project sets up services like FastAPI, PostgreSQL, Prometheus, Grafana, Alertmanager, and Node Exporter using Podman Compose.

## Services
### Suite
- **FastAPI**: Main application service.
- **PostgreSQL**: Database service.
- **Prometheus**: Monitoring service.
- **Grafana**: Dashboard service.
- **Alertmanager**: Alert management service.
- **Node Exporter**: Node metrics collection service.
- **mail**: mail server  **DEFAULT DISABLED**
- **loki** Log storage and query service **DEFAULT DISABLED**
  
## Setup

1. Clone the repository.

    ```sh
    git clone https://github.com/tanico-rikudo/TestWebApi.git
    cd TestWebApi
    ```

2. Set up the necessary environment variables. Create a `.env` file and add the following content:

    ```env
    DATABASE_URL=postgresql://user:password@db:5432/fastapi_db
    ```

3. Use Podman Compose to start the services.

    ```sh
    podman-compose up -d
    ```
4. **optional** uncomment `mail` and update your mail addresses
   ```
   vi alertmanager_data/config.yaml
   vi podman-compose.yml
   ```

   

## Service Details

### FastAPI

- **Build Context**: `./app/Dockerfile`
- **Ports**: `8000:8000`
- **Volumes**: 
  - `.:/app`
  - `./app/logs:/app/logs`

### PostgreSQL

- **Image**: `postgres:15`
- **Ports**: `5432:5432`
- **Volumes**: 
  - `pgdata:/var/lib/postgresql/data`
  - `./postgres_data/logs/db:/etc/log/postgresql`
  - `./postgres_data/config/postgresql.conf:/etc/postgresql/postgresql.conf`

### Prometheus

- **Image**: `prom/prometheus`
- **Ports**: `9090:9090`
- **Volumes**: `./prometheus_data/config:/etc/prometheus`

### Grafana

- **Image**: `grafana/grafana`
- **Ports**: `3000:3000`
- **Volumes**: `./grafana_data:/var/lib/grafana`
- **Environment File**: `./grafana_data/config/grafana.env`

### Alertmanager

- **Image**: `prom/alertmanager`
- **Ports**: `9093:9093`
- **Volumes**: `./alertmanager_data:/etc/alertmanager`

### Node Exporter

- **Image**: `prom/node-exporter:latest`
- **Ports**: `9100`

### Stopping the Services

To stop the services, run the following command:

```sh
podman-compose down
```

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

