import shutil
import zipfile
import pytest
import os

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
root_dir = os.path.dirname(current_dir)
files_path = os.path.join(root_dir, 'tmp')
archive_path = os.path.join(root_dir, 'resource')
archive = os.path.join(archive_path, 'zip_file_hw_7.zip')


@pytest.fixture(scope='session', autouse=True)
def create_zip():
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)
    with zipfile.ZipFile(archive, 'w') as zf:
        for file in os.listdir(files_path):
            full_file_path = os.path.join(files_path, file)
            zf.write(full_file_path, os.path.basename(full_file_path))
    yield
    shutil.rmtree(archive_path)  # удаляем папку с архивом после завершения тестов

