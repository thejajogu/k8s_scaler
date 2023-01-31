from docopt import docopt

from utils import options
from utils.executor import Executor


if __name__ == '__main__':
    arguments = docopt(options.__doc__, version='K8S Scaling 1.0')
    print(arguments)

    executor_obj = Executor(arguments=arguments)

    # Cleanup the 'target' dir
    if arguments['--targetDirCleanup']:
        executor_obj.cleanup_target_dir()

    # Cleanup the workloads
    if arguments['--workloadsCleanup']:
        executor_obj.cleanup_workloads()

    # Schedule the deployment with 1 pod on all the worker nodes
    if ('--orcType' and '--kubeConfig') is not None in arguments:
        executor_obj.scale_deployment_pods()
