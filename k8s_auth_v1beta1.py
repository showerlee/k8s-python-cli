from kubernetes import client, config

def login():
    # Define the barer token we are going to use to authenticate.
    # See here to create the token:
    # https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/
    Token = "xxx"
    # Create a configuration object
    APISERVER = "https://xxx:xxx"

    configuration = client.Configuration()
    # Specify the endpoint of your Kube cluster
    configuration.host = APISERVER
    # Security part.
    # In this simple example we are not going to verify the SSL certificate of
    # the remote cluster (for simplicity reason)
    configuration.verify_ssl = False
    # Nevertheless if you want to do it you can with these 2 parameters
    # configuration.verify_ssl=True
    # ssl_ca_cert is the filepath to the file that contains the certificate.
    # configuration.ssl_ca_cert="certificate"
    configuration.api_key = {"authorization": "Bearer " + Token}
    # configuration.api_key["authorization"] = "bearer " + Token
    # configuration.api_key_prefix['authorization'] = 'Bearer'
    # configuration.ssl_ca_cert = 'ca.crt'
    # Create a ApiClient with our config
    client.Configuration.set_default(configuration)
    # Do calls
    v1beta1 = client.ExtensionsV1beta1Api()

    if v1beta1:
    	print("Successfully connected to k8s API cluster %s" %APISERVER)
    else:
    	print("Connection failed.")
    # print("Listing pods with their IPs:")
    # ret = v1.list_pod_for_all_namespaces(watch=False)
    # for i in ret.items:
    #     print("%s\t%s\t%s" %
    #           (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

    return v1beta1
