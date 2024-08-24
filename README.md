# Kubernetes for Modern Data Engineering

This project involves setting up a Kubernetes cluster, deploying Apache Airflow with Helm Charts, and managing the cluster with Kubernetes Dashboard. The setup was guided by the YouTube video [Kubernetes for Modern Data Engineering: An End to End Data Engineering Project](https://www.youtube.com/watch?v=ISftrpAImHA) by Yusuf Ganiyu.

## Project Overview

In this project, I followed the tutorial video to:

1. **Set Up Kubernetes on Docker**: Starting with the basics of setting up Kubernetes on Docker Desktop.
2. **Master kubectl**: Learned how to effectively use kubectl to manage the Kubernetes cluster.
3. **Deploy the Kubernetes Dashboard**: Set up the Kubernetes Dashboard, a user-friendly interface for managing Kubernetes clusters.
4. **Run Apache Airflow with Helm Charts**: Deployed Apache Airflow on Kubernetes using Helm Charts, configured it, and connected DAGs to Kubernetes.

### Prerequisites

- Docker Desktop installed with Kubernetes enabled.
- kubectl configured and ready to use.
- Helm installed for managing Kubernetes applications.

## Step-by-Step Setup

### 1. Setting Up Kubernetes on Docker

- **Docker Configuration**: Configured Docker to allow enough resources for Kubernetes to run efficiently.
- **Kubernetes Enablement**: Enabled Kubernetes from Docker Desktop settings.

**Image Reference:**
![Getting YAML File](path/to/getting_yaml_file.png)

### 2. Deploying Kubernetes Dashboard

- **Namespace Creation**: Created a namespace for the Kubernetes Dashboard.
- **Applying Recommended YAML**: Downloaded and applied the recommended YAML file for setting up the dashboard.

**Image Reference:**
![Kubernetes Dashboard](path/to/kubernetes_dashboard_airflow.png)

### 3. Running Apache Airflow with Helm Charts

- **Helm Installation**: Installed Apache Airflow using Helm Charts.
- **DAG Deployment**: Placed the DAG in the appropriate directory and ensured it appeared in the Airflow UI.

**Image Reference:**
![DAG in Airflow](path/to/dag_in_airflow.png)

### 4. Accessing the Cluster and Dashboard

- **kubectl Proxy**: Used `kubectl proxy` to access the Kubernetes Dashboard.
- **Kubernetes Dashboard**: Managed resources via the Kubernetes Dashboard interface.

**Image Reference:**
![Cluster Activity](path/to/cluster_activity_airflow.png)

## Bugs and Issues

During the setup and execution of this project, I encountered several issues. Below are the details of these bugs and their solutions.

### 1. DAG Not Appearing in Airflow UI

**Problem:**  
The `hello.py` DAG was not visible in the Airflow UI despite being correctly placed in the `dags/` folder in the Git repository.

**Solution:**  
- Corrected the `values.yaml` configuration for `mountPath`.
- Fixed syntax errors in the `hello.py` DAG.
- Restarted the Airflow scheduler.
- Checked scheduler logs and DAG directory in the Airflow pod.

**Image Reference:**
![Hello World Success](path/to/hello_world_succes.png)

### 2. Port Binding Issue When Accessing Airflow UI

**Problem:**  
An error occurred when trying to access the Airflow UI due to a port binding issue.

**Solution:**  
- Identified and terminated the process using port 8080.
- Forwarded the port again to access the Airflow UI.

**Image Reference:**
![Run Proxy to Make Link Work Again](path/to/run_proxy_to_make_link_work_again.png)

### 3. Persistent Issues with DAG Syncing

**Problem:**  
Even after the above steps, DAGs were still not visible in the Airflow UI.

**Solution:**  
- Verified Git sync configuration.
- Restarted the scheduler.
- Checked Git sync logs and verified DAG presence in the Airflow pod.

### 4. Helm Install Fails with `repo apache-airflow not found`

**Problem:**  
During the installation of Airflow using Helm, the repository `apache-airflow` was not found.

**Solution:**  
- Added and updated the Apache Airflow Helm repository before installing Airflow.

### 5. Kubernetes Dashboard Does Not Show the `airflow` Namespace

**Problem:**  
The `airflow` namespace and its resources did not appear in the Kubernetes Dashboard.

**Solution:**  
- Granted admin access to the Kubernetes Dashboard.
- Restarted the Kubernetes Dashboard to reflect the changes.

### 6. `airflow-create-user` Job Not Found

**Problem:**  
The `airflow-create-user` job was not found even though it should be part of the deployment.

**Solution:**  
- Checked Helm hooks and reran the job by forcing a Helm upgrade.

### 7. Accessing the Airflow Web Server

**Problem:**  
Needed to access the Airflow Web UI after deployment.

**Solution:**  
- Used `kubectl port-forward` to access the Airflow web server locally.

## Troubleshooting and Known Issues

Below are some general troubleshooting commands and solutions for common issues encountered during the project.

### General Commands

- **Check resource status in a namespace:**
  ```bash
  kubectl get all --namespace airflow
  ```

- **View logs for a specific pod:**
  ```bash
  kubectl logs <pod-name> --namespace airflow
  ```

- **Check Helm release status:**
  ```bash
  helm status airflow --namespace airflow
  ```

**Image Reference:**
![kubectl Cluster Info](path/to/cubectl_cluster_info.png)

## Credits

This project was guided by the video tutorial "[Kubernetes for Modern Data Engineering: An End to End Data Engineering Project](https://www.youtube.com/watch?v=ISftrpAImHA)" by Yusuf Ganiyu.
