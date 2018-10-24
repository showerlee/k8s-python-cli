from os import path

import yaml

from kubernetes import client, config

import k8s_auth_v1beta1

def main():

    api = k8s_auth_v1beta1.login()

    with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
        dep = yaml.load(f)
        resp = api.create_namespaced_deployment(
            body=dep, namespace="default")
        print("Deployment created. status='%s'" % str(resp.status))


if __name__ == '__main__':
    main()