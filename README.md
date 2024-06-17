# Pregnancy Weeks Calculator

This is a Pregnancy Week Calculator to determine how many weeks pregnant you are on a specific date.


Follow the steps below to clone the repository, create the necessary Docker network, build the backend and frontend services, and run the containers.

## Clone the Repository

0. Clone the Repository
    ```bash
    git clone <repository-url>
    cd pregweek-calc
    ```

## Instructions to Run All Services at Once

1. Run docker-compose
    ```bash
    docker-compose up
    ```
2. Access the Application

The application should now be available at [http://localhost:8501](http://localhost:8501)



## Instructions to Run Each Service Separately

1. Create Docker Network

    ```bash
    docker network create pregweek-network
    ```

2. Build Backend Service

    ```bash
    cd backend
    docker build . -t pregweek-backend
    ```

3. Build Frontend Service

    ```bash
    cd ../frontendPython
    docker build . -t pregweek-frontend
    ```

4. Run the Containers

    ```bash
    docker rm -f backend
    docker rm -f frontend
    docker run -d --network pregweek-network --name backend -p 8000:8000 pregweek-backend
    docker run -d --network pregweek-network --name frontend -p 8501:8501 -e URL_BASE=http://backend:8000 pregweek-frontend
    ```

5. Access the Application

The application should now be available at [http://localhost:8501](http://localhost:8501)
