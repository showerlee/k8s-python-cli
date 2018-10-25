from kubernetes import client, config


def main():
    Token = "xxx"
    # Create a configuration object
    APISERVER = "xxx"

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
    # aConfiguration.api_key_prefix['authorization'] = 'Bearer'
    # aConfiguration.ssl_ca_cert = 'ca.crt'
    # Create a ApiClient with our config
    client.Configuration.set_default(configuration)

    print("Supported APIs (* is preferred version):")
    print("%-20s %s" %
          ("core", ",".join(client.CoreApi().get_api_versions().versions)))
    for api in client.ApisApi().get_api_versions().groups:
        versions = []
        for v in api.versions:
            name = ""
            if v.version == api.preferred_version.version and len(
                    api.versions) > 1:
                name += "*"
            name += v.version
            versions.append(name)
        print("%-40s %s" % (api.name, ",".join(versions)))


if __name__ == '__main__':
    main()