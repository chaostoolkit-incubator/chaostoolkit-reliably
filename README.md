# Chaos Toolkit extension for Reliably

![Build](https://github.com/chaostoolkit-incubator/chaostoolkit-reliably/workflows/Build/badge.svg)

[Reliably][reliably] support for the [Chaos Toolkit][chaostoolkit].

[reliably]: https://reliably.com
[chaostoolkit]: http://chaostoolkit.org/

## Install

To be used from your experiment, this package must be installed in the Python
environment where [chaostoolkit][] already lives.

[chaostoolkit]: https://github.com/chaostoolkit/chaostoolkit

```
$ pip install chaostoolkit-reliably
```

## Usage

## Authentication

To use this package, you must create have registered with Reliably services
through their [CLI][configreliably].

[configreliably]: https://reliably.com/docs/getting-started/login/

You have two ways to pass on the credentials information.

The first one by specifying the path to the Reliably's configuration file,
which defaults to `$HOME/.config/reliably/config.yaml`.

```json
{
    "configuration": {
        "reliably_config_path": "~/.config/reliably/config.yaml"
    }
}
```

Because we use the default path, you may omit this configuration's entry
altogether unless you need a specific different path.


The second one is by setting some environment variables as secrets:

* `RELIABLY_TOKEN`: the token to authenticate against Reliably's API
* `RELIABLY_HOST:`: the hostname to connect to, default to `reliably.com`

```json
{
    "secrets": {
        "reliably": {
            "token": {
                "type": "env",
                "key": "RELIABLY_TOKEN"
            },
            "host": {
                "type": "env",
                "key": "RELIABLY_HOST",
                "default": "reliably.com"
            }
        }
    }
}
```

### Probes

## Contribute

If you wish to contribute more functions to this package, you are more than
welcome to do so. Please, fork this project, make your changes following the
usual [PEP 8][pep8] code style, sprinkling with tests and submit a PR for
review.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

### Develop

If you wish to develop on this project, make sure to install the development
dependencies. But first, [create a virtual environment][venv] and then install
those dependencies.

[venv]: http://chaostoolkit.org/reference/usage/install/#create-a-virtual-environment

```console
$ pip install -r requirements-dev.txt -r requirements.txt 
```

Then, point your environment to this directory:

```console
$ python setup.py develop
```

Now, you can edit the files and they will be automatically be seen by your
environment, even when running from the `chaos` command locally.

### Test

To run the tests for the project execute the following:

```
$ pytest
```
