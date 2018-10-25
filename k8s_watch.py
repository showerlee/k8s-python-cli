import k8s_auth
from kubernetes import watch


def main():
    # Configs can be set in Configuration class directly or using helper
    # utility. If no argument provided, the config will be loaded from
    # default location.
    api_v1 = k8s_auth.login()
    count = 10
    w = watch.Watch()
    for event in w.stream(api_v1.list_namespace, timeout_seconds=10):
        print("Event: %s %s" % (event['type'], event['object'].metadata.name))
        count -= 1
        if not count:
            w.stop()

    print("Ended.")


if __name__ == '__main__':
    main()


