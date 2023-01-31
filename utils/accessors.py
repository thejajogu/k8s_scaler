import os
import shutil
import yaml

from jinja2 import Environment, FileSystemLoader


class Accessors:
    @staticmethod
    def remove_existing_target_dir(output_dir,
                                   create_target_dir=False):
        # Check the images_dir if exists and create the new one
        if os.path.exists(output_dir):
            shutil.rmtree(output_dir, ignore_errors=True)
        if create_target_dir:
            os.mkdir(output_dir)

    def render_deployment_manifests(self,
                                    images_config,
                                    deployment_template,
                                    output_dir,
                                    share_dir,
                                    replica):
        # Remove the existing target dir
        self.remove_existing_target_dir(output_dir=output_dir,
                                   create_target_dir=True)

        # Load the images.yaml
        with open(images_config, 'r') as file:
            values = yaml.safe_load(file)

        # Load template file
        env = Environment(loader=FileSystemLoader(share_dir),
                          trim_blocks=True,
                          lstrip_blocks=True)
        template = env.get_template(deployment_template)

        # Render the deployment yaml's with image list
        for image in values["images"]:
            image['node_count'] = replica
            image_file = os.path.join(output_dir, image['name'] + '.yaml')
            file = open(image_file, "w")
            file.write(template.render(image))
            file.close()

    @staticmethod
    def verify_cmd_result(cmd_output,
                          message):
        print(cmd_output)
        print(message)
        # CompletedProcess(args=['kubectl', 'apply', '-f', '/Users/thejajogu/K8S_Scaling/images_dir', '-n', 'interop-scale'], returncode=0, stdout=b'deployment.apps/1-nginx created\ndeployment.apps/2-apache2 created\ndeployment.apps/3-mongo created\ndeployment.apps/4-bitnami created\n', stderr=b'')

