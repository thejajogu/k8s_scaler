import subprocess

from kubernetes import client, config


class Namespace:
    def __init__(self, config_file):
        config.load_kube_config(config_file=config_file)
        self.v1 = client.CoreV1Api()

    def get_nodes_count(self):
        # Get the nodes
        node_list = self.v1.list_node()
        # TODO: Validate response code
        return len(node_list.items)

    def create_namespace(self, namespace):
        # Create the namespace
        namespace_config = client.V1Namespace(metadata=client.V1ObjectMeta(name=namespace))
        self.v1.create_namespace(namespace_config)
        # TODO: Validate response code

    def delete_namespace(self, namespace):
        # Create the namespace
        self.v1.delete_namespace(name=namespace)
        # TODO: Validate response code


class Deployment:
    @staticmethod
    def create_deployments(output_dir,
                           namespace):
        # Schedule the deployment on all the nodes via manifest files
        command = ['kubectl', 'apply', '-f', output_dir, '-n', namespace]
        output = subprocess.run(command, capture_output=True)
        print(output)
        # TODO: Validate response code

    @staticmethod
    def delete_deployments(output_dir,
                           namespace):
        # Schedule the deployment on all the nodes via manifest files
        command = ['kubectl', 'delete', '-f', output_dir, '-n', namespace]
        output = subprocess.run(command, capture_output=True)
        print(output)
        # TODO: Validate response code
