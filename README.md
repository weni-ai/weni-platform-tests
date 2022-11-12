# Weni Platform Tests

## Run project locally
### Requirements
* Python `^3.8`
* Poetry `^1.0`

### Installing
To run this project, we will need Poetry installed on your machine.
After installing poetry, install all dependencies using (on project root path):

```sh
$ poetry install
```

To enter on Poetry virtual environment, we use:
```sh
$ poetry shell
```

### Environment setting
In this project we use environment variables to make most of the configurations.
To speed up the project installation process we use a script to generate our `.env` file, it can be found in `contrib/gen_env.py`. To use type:

```sh
$ python contrib/gen_env.py
```
Ready, an `.env` file should be appars on root of project, and from it we can configure our environment variables.

**OBS**: The use of this script is recommended in development environment only.
