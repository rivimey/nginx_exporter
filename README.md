Ansible Role: nginx\_exporter
==========================

[![Build Status](https://travis-ci.org/atosatto/ansible-nginx_exporter.svg?branch=master)](https://travis-ci.org/atosatto/ansible-nginx_exporter)
[![Galaxy](https://img.shields.io/badge/galaxy-atosatto.nginx_exporter-blue.svg?style=flat-square)](https://galaxy.ansible.com/atosatto/nginx_exporter)

Install and configure Prometheus nginx\_exporter.

Requirements
------------

An Ansible 2.2 or higher installation.<br />
This role makes use of the Ansible `json_filter` that requires `jmespath` to be installed on the Ansible machine.
See the `requirements.txt` file for further details on the specific version of `jmespath` required by the role.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

    nginx_exporter_release_tag: "latest"

The nginx\_exporter release to be installed.
By default, the latest release published at https://github.com/prometheus/nginx\_exporter/releases.

    nginx_exporter_release_url: ""

If set, the role will download nginx-exporter from the provided URL instead of using the download URL indicated in the nginx\_exporter Github release metadata.

    nginx_exporter_user: "nginx_exporter"
    nginx_exporter_group: "nginx_exporter"

nginx\_exporter system user and group.

    nginx_exporter_install_path: "/opt"

Directory containing the downloaded nginx\_exporter release artifacts.

    nginx_exporter_bin_path: "/usr/local/bin"

Directory to which the nginx\_exporter binaries will be symlinked.

    nginx_exporter_listen_address: "127.0.0.1:9100"

The nginx\_exporter WebServer listen ip address and port.<br/>
**NOTE**: the nginx\_exporter metrics will be available at `{{ nginx_exporter_listen_address }}/metrics`.

    nginx_exporter_log_level: "info"

nginx\_exporter logs verbosity level.

    nginx_exporter_additional_cli_args: ""

Additional command-line arguments to be added to the nginx\_exporter service unit.
For the complete refence of the available CLI arguments please refer to the output
of the `nginx_exporter --help` command.

Dependencies
------------

None.

Example Playbooks
-----------------

    $ cat playbook.yml
    - name: "Install and configure Prometheus nginx_exporter"
      hosts: all
      roles:
        - { role: atosatto.nginx_exporter }

Testing
-------

Tests are automated with [Molecule](http://molecule.readthedocs.org/en/latest/).

    $ pip install tox

To test all the scenarios run

    $ tox

To run a custom molecule command

    $ tox -e py27-ansible29 -- molecule test -s nginx_exporter-latest

License
-------

MIT

Author Information
------------------

Andrea Tosatto ([@\_hilbert\_](https://twitter.com/_hilbert_))
