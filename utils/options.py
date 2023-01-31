"""
K8S Scaling

Usage:
  launcher.py --orcType=<orcType> --kubeConfig=<KUBECONFIG> [--workloadsCleanup] [--targetDirCleanup]
  launcher.py [--workloadsCleanup] [--targetDirCleanup]
  launcher.py (-h | --help)
  launcher.py (-v | --version)

Examples:
    launcher.py --orcType=eks --kubeConfig=/home/usr/config.yaml --workloadsCleanup --targetDirCleanup
    launcher.py --orcType=eks --kubeConfig=/home/usr/config.yaml --targetDirCleanup
    launcher.py --orcType=eks --kubeConfig=/home/usr/config.yaml
    launcher.py --workloadsCleanup --targetDirCleanup
    launcher.py --targetDirCleanup

Arguments:
  orcType     -  Type of Orchestration [aks|eks|gke]
  kubeConfig  -  K8S kubeconfig abs file path

Options:
  -h --help           -  Show this Screen
  -v --version        -  Show the Version
  --workloadsCleanup  -  Flag to clean the created workloads
  --targetDirCleanup  -  Flag to clean the target directory
"""
