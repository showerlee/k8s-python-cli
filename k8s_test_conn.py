import k8s_auth

v1 = k8s_auth.login()

print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" %
          (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

