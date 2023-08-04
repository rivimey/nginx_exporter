"""Prometheus Jinja2 filters"""
import re


AM_SYSTEM =  {
    'Linux': 'linux',
    'Darwin': 'darwin',
    'FreeBSD': 'freebsd',
    'NetBSD': 'netbsd',
    'OpenBSD': 'openbsd'
}

AM_ARCHITECTURE = {
    'x86_64': 'amd64',
    'i386': '386',
    'aarch64': 'arm64',
    'armv7l': 'armv7',
    'armv6l': 'armv6',
    'armv5l': 'armv5',
    's390x': 's390x',
    'powerpc': 'ppc64',
}


def nginx_exporter_release_build(hostvars, promrelease):

    architecture = hostvars['ansible_architecture']
    system = hostvars['ansible_system']
    version = re.sub('^v(.*)$', '\\1', promrelease)

    pat = 'nginx-prometheus-exporter_' + version + '_' + AM_SYSTEM[system] + '_' + AM_ARCHITECTURE[architecture]
    print(pat)
    return pat


class FilterModule(object):


    def filters(self):
        return {
            'nginx_exporter_release_build': nginx_exporter_release_build
        }
