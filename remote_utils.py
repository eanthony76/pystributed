
import os
from config import DOCKER_IMAGE_NAME, DOCKER_REGISTRY, REMOTE_SERVER, REMOTE_WORKDIR

def run_on_remote():
    commands = [
        f"docker pull {DOCKER_REGISTRY}/{DOCKER_IMAGE_NAME}",
        f"docker run --gpus all {DOCKER_REGISTRY}/{DOCKER_IMAGE_NAME}"
    ]
    for cmd in commands:
        #You will need to change the keypair to reflect the .pem file associated with the remote instance
        os.system(f" ssh -i ~/.ssh/keypair.pem {REMOTE_SERVER} '{cmd}'")

def fetch_results(local_dir="./results"):
    os.system(f"scp -r {REMOTE_SERVER}:{REMOTE_WORKDIR}/results {local_dir}")
