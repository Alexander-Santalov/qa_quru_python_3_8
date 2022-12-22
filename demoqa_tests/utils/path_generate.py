import os
import demoqa_tests.upload


def generate_path_upload(name_file):
    return os.path.abspath(os.path.join(os.path.dirname(demoqa_tests.upload.__file__), name_file))

