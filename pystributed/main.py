
from .docker_utils import build_image, push_image
from .remote_utils import run_on_remote, fetch_results


def main(file_path=None):
    # Build and push Docker image
    build_image()
    push_image()

    # Run on the remote server
    run_on_remote(file_path)

    # Fetch the results
    fetch_results()
