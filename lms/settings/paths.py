import os
from path import path

############################# SET PATH INFORMATION #############################
PROJECT_ROOT = path(__file__).abspath().dirname().dirname()  # /mitx/lms
REPO_ROOT = PROJECT_ROOT.dirname()
COMMON_ROOT = REPO_ROOT / "common"
COMMON_TEST_DATA_ROOT = COMMON_ROOT / "test" / "data"
ENV_ROOT = REPO_ROOT.dirname()  # virtualenv dir /mitx is in
TEST_ROOT = REPO_ROOT / 'test_root'
COURSES_ROOT = ENV_ROOT / "data"

DATA_DIR = COURSES_ROOT
