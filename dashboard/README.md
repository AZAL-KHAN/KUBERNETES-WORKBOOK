KIND Cluster Setup Guide
---
1. Installing KIND and kubectl
---
Install KIND and kubectl using the provided script:

2. Setting Up the KIND Cluster
---
Create a kind-cluster.yaml file:

```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4

nodes:
- role: control-plane
  image: kindest/node:v1.34.0
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP

- role: worker
  image: kindest/node:v1.34.0

- role: worker
  image: kindest/node:v1.34.0

- role: worker
  image: kindest/node:v1.34.0
```

Create the cluster using the configuration file:
```
kind create cluster --name mycluster --config kind-cluster.yaml
```

verify the cluster:
```
kubectl get nodes
kubectl cluster-info
```

3. Setting Up the Kubernetes Dashboard
---
Deploy the Dashboard Apply the Kubernetes Dashboard manifest:

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml
```

Create an Admin User Create a dashboard-admin-user.yml file with the following content:

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user-binding
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin

```

Apply the configuration:

```
kubectl apply -f dashboard-admin-user.yml
```

Get the Access Token Retrieve the token for the admin-user:

```
Get the Access Token Retrieve the token for the admin-user:
```

Copy the token for use in the Dashboard login.

Access the Dashboard Start the Dashboard using kubectl proxy:

```
kubectl proxy
```

Open the Dashboard in your browser:

```
http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
```

4. Access the Dashboard (Port Forwarding)
---
Kind does not expose NodePorts by default, so port-forwarding is the cleanest approach.

```
kubectl port-forward -n kubernetes-dashboard service/kubernetes-dashboard 8443:443
```

Now open your browser:
```
https://localhost:8443
```

5. Deleting the Cluster
---

Delete the KIND cluster:

```
kind delete cluster --name my-kind-cluster
```