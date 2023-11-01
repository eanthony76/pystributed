
import os
from config import DOCKER_IMAGE_NAME, DOCKER_REGISTRY, REMOTE_SERVER, REMOTE_WORKDIR

def run_on_remote():
    commands = [
        f"docker pull {DOCKER_REGISTRY}/{DOCKER_IMAGE_NAME}",
        f"docker run --gpus all {DOCKER_REGISTRY}/{DOCKER_IMAGE_NAME}"
    ]
    for cmd in commands:
        os.system(f"ssh {REMOTE_SERVER} '{cmd}'")

def fetch_results(local_dir="./results"):
    os.system(f"scp -r {REMOTE_SERVER}:{REMOTE_WORKDIR}/results {local_dir}")
