## K8s access API cluster via python client 

#### Create k8s user-admin service-account on k8s master

    kubectl create -f CreateServiceAccount.yaml
    kubectl create -f RoleBinding.yaml

#### Grab beared token of admin-user for python client

    Token=$(kubectl describe secret $(kubectl get secret -n kube-system | grep ^admin-user | awk '{print $1}') -n kube-system | grep -E '^token'| awk '{print $2}')

#### Grab api server URL

    APISERVER=$(kubectl config view --minify | grep server | cut -f 2- -d ":" | tr -d " ")

#### Install python client package

    pip install kubernetes

#### alter Token and APISERVER in k8s_auth.py for portal authentication


#### Run the test connection script
    
    python ./k8s_test_conn.py
    
```
Listing pods with their IPs:
172.31.40.96    kube-system     etcd-minikube
172.31.40.96    kube-system     kube-addon-manager-minikube
172.31.40.96    kube-system     kube-apiserver-minikube
172.31.40.96    kube-system     kube-controller-manager-minikube
172.17.0.3      kube-system     kube-dns-86f4d74b45-m9g95
172.31.40.96    kube-system     kube-proxy-zhf9q
172.31.40.96    kube-system     kube-scheduler-minikube
172.17.0.2      kube-system     kubernetes-dashboard-5498ccf677-l7xxz
172.31.40.96    kube-system     storage-provisioner
```