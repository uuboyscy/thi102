# thi102

### Build a new Python virtual environment

- Install pipenv
  ```shell
  pip install pipenv
  ```

- Create virtual environment
  ```shell
  pipenv --python 3.11
  ```

- Activate virtual environment
  ```shell
  pipenv shell
  ```

- Install Python package in virtual environment
  - pip install {package1} {package2} ...
  ```shell
  pip install requests bs4
  ```
  Packages does not be maintained in Pipfile

- Maintain packages in Pipfile
  - pipenv install {package1} {package2} ...
  ```shell
  pipenv install requests bs4
  ```
  This also output a lock file

- Deactivate virtual environment
  ```shell
  deactivate
  ```

### Re-build a Python environment from a Pipfile

- Output lock file
  ```shell
  pipenv lock
  ```

- Output requirements.txt, which is used by pip
  ```shell
  pipenv requirements > requirements.txt
  ```

- Install packages via requirements.txt
  ```shell
  pip install -r requirements.txt
  ```
