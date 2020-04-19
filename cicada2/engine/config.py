import os


CONTAINER_NETWORK = os.getenv("CONTAINER_NETWORK", "cicada-2")
CREATE_NETWORK = os.getenv("CREATE_NETWORK", True)
HEALTHCHECK_INITIAL_WAIT = os.getenv("HEALTHCHECK_INITIAL_WAIT", 2)
HEALTHCHECK_MAX_RETRIES = os.getenv("HEALTHCHECK_MAX_RETRIES", 5)
INITIAL_STATE_FILE = os.getenv("INITIAL_STATE_FILE")
REPORTS_FOLDER = os.getenv("REPORTS_FOLDER", "/reports")
TASK_TYPE = os.getenv("TASK_TYPE", "docker")
TESTS_FOLDER = os.getenv("TESTS_FOLDER", "/tests")
