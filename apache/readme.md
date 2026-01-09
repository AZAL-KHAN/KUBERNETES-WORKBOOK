I have created a local Kubernetes cluster with kind. Following are changes you need to get metric-server running on Kind.

Deploy latest metric-server release.

```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.5.0/components.yaml
```

Within existing arguments to metric-server container, you need to add argument  --kubelet-insecure-tls.

You can create file ```metric-server-patch.yaml``` with following content,

```
spec:
  template:
    spec:
      containers:
      - args:
        - --cert-dir=/tmp
        - --secure-port=443
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
        - --kubelet-insecure-tls
        name: metrics-server
```
Patch ```metric-server``` deployment,

```
kubectl patch deployment metrics-server -n kube-system --patch "$(cat metric-server-patch.yaml)"
```