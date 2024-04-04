# Edge Device Simulation

Before you begin, ensure you have met the following requirements:
- Docker installed on your machine.

### Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/nee1k/ckn_edge_device_data_simulator.git
    ```

2. **Navigate to the project directory**
    ```bash
    cd ckn_edge_device
    ```

3. **Create a Docker volume**
    Before building the Docker image, create a Docker volume named `icicle` to persist logs:

    ```bash
    docker volume create icicle
    ```

4. **Build the Docker image**

    Build the Docker image with the tag `edge`:

    ```bash
    docker build -t ckn_edge_device .
    ```

5. **Run the Docker container**

    Finally, run your Docker container named `edge`, mounting the `icicle` volume to `/app/logs`:

    ```bash
    docker run --name ckn_edge_device -v icicle:/app/logs ckn_edge_device
    ```

## Development

For development purposes, you can make changes to docker volume rmthe `main.py` script to alter the message production logic. Ensure to rebuild the Docker image and rerun the container to test your changes:

```bash
docker build -t ckn_edge_device . && docker rm -f ckn_edge_device || true  && docker run --name ckn_edge_device -v icicle:/app/logs ckn_edge_device
```

```bash
docker rm -f ckn_edge_device && docker rmi -f ckn_edge_device && docker volume rm icicle && docker build -t ckn_edge_device . && docker run --name ckn_edge_device -v icicle:/app/logs ckn_edge_device
```