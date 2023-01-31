import os

from utils.k8s import (Namespace,
                       Deployment)
from utils.accessors import Accessors
from source.consts import (IMAGES_LIST,
                           NAMESPACE,
                           OUTPUT_DIR,
                           JINJA_TEMPLATE,
                           SHARE_DIR)


class Executor:
    def __init__(self, arguments):
        self.arguments = arguments
        self.kube_config = self.arguments['--kubeConfig']

        # Set the 'KUBECONFIG' as env variable
        if self.arguments['--orcType'] in ['aks', 'gke']:
            os.environ["KUBECONFIG"] = self.kube_config

        # Initialize the class objects
        self.namespace_obj = Namespace(config_file=self.kube_config)
        self.deployment_obj = Deployment()
        self.accessors = Accessors()

        # Fetch the number of worker nodes
        self.replica = self.namespace_obj.get_nodes_count()

    def cleanup_target_dir(self):
        # Cleanup the 'target' dir
        self.accessors.remove_existing_target_dir(output_dir=OUTPUT_DIR)

    def cleanup_workloads(self):
        self.accessors.render_deployment_manifests(images_config=IMAGES_LIST,
                                                   deployment_template=JINJA_TEMPLATE,
                                                   output_dir=OUTPUT_DIR,
                                                   share_dir=SHARE_DIR,
                                                   replica=self.replica)
        # TODO: Verify whether jinja rendering is successful or not

        self.deployment_obj.delete_deployments(output_dir=OUTPUT_DIR,
                                               namespace=NAMESPACE)
        # TODO: Verify whether deployments/pods deleted successfully or not

        self.namespace_obj.delete_namespace(namespace=NAMESPACE)
        # TODO: Verify whether namespace deleted successfully or not

    def scale_deployment_pods(self):
        self.namespace_obj.create_namespace(namespace=NAMESPACE)

        self.accessors.render_deployment_manifests(images_config=IMAGES_LIST,
                                                   deployment_template=JINJA_TEMPLATE,
                                                   output_dir=OUTPUT_DIR,
                                                   share_dir=SHARE_DIR,
                                                   replica=self.replica)
        # TODO: Verify whether namespace created successfully or not

        result = self.deployment_obj.create_deployments(output_dir=OUTPUT_DIR,
                                                        namespace=NAMESPACE)

        # TODO: Verify whether deployments/pods created successfully or not
        # verify_cmd_result(cmd_output=result,
        #                   message='None')
