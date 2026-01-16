# NGINX Ingress Controller on kind Kubernetes

This guide shows how to install **NGINX Ingress Controller on a kind cluster** and access services using **port-forwarding**.

---


## Install NGINX Ingress Controller (kind)

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

---

Verify Installation
```
kubectl get pods -n ingress-nginx
kubectl get svc -n ingress-nginx
kubectl get ingressclass
```

---

 Access Ingress in kind (IMPORTANT)

Since kind does not provide an external LoadBalancer,
use port-forwarding to access ingress services:

```
kubectl port-forward svc/ingress-nginx-controller -n ingress-nginx 8080:80
```