# Copyright 2019 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <https://www.gnu.org/licenses/>.

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os
import json
import pytest
from mock import ANY
from ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios import FortiOSHandler

try:
    from ansible_collections.fortinet.fortios.plugins.modules import fortios_firewall_ssl_ssh_profile
except ImportError:
    pytest.skip("Could not load required modules for testing", allow_module_level=True)


@pytest.fixture(autouse=True)
def connection_mock(mocker):
    connection_class_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.modules.fortios_firewall_ssl_ssh_profile.Connection')
    return connection_class_mock


fos_instance = FortiOSHandler(connection_mock)


def test_firewall_ssl_ssh_profile_creation(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_ssl_ssh_profile': {
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'caname': 'test_value_3',
        'comment': 'Optional comments.',
        'mapi-over-https': 'enable',
        'name': 'default_name_6',
                'rpc-over-https': 'enable',
                'server-cert': 'test_value_8',
                'server-cert-mode': 're-sign',
                'ssl-anomalies-log': 'disable',
                'ssl-exemptions-log': 'disable',
                'untrusted-caname': 'test_value_12',
                'use-ssl-server': 'disable',
                'whitelist': 'enable'
    }

    set_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200


def test_firewall_ssl_ssh_profile_creation_fails(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'POST', 'http_status': 500}
    set_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_ssl_ssh_profile': {
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'caname': 'test_value_3',
        'comment': 'Optional comments.',
        'mapi-over-https': 'enable',
        'name': 'default_name_6',
                'rpc-over-https': 'enable',
                'server-cert': 'test_value_8',
                'server-cert-mode': 're-sign',
                'ssl-anomalies-log': 'disable',
                'ssl-exemptions-log': 'disable',
                'untrusted-caname': 'test_value_12',
                'use-ssl-server': 'disable',
                'whitelist': 'enable'
    }

    set_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 500


def test_firewall_ssl_ssh_profile_removal(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    delete_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    delete_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.delete', return_value=delete_method_result)

    input_data = {
        'username': 'admin',
        'state': 'absent',
        'firewall_ssl_ssh_profile': {
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    delete_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', mkey=ANY, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200


def test_firewall_ssl_ssh_profile_deletion_fails(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    delete_method_result = {'status': 'error', 'http_method': 'POST', 'http_status': 500}
    delete_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.delete', return_value=delete_method_result)

    input_data = {
        'username': 'admin',
        'state': 'absent',
        'firewall_ssl_ssh_profile': {
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    delete_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', mkey=ANY, vdom='root')
    schema_method_mock.assert_not_called()
    assert is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 500


def test_firewall_ssl_ssh_profile_idempotent(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'error', 'http_method': 'DELETE', 'http_status': 404}
    set_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_ssl_ssh_profile': {
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'caname': 'test_value_3',
        'comment': 'Optional comments.',
        'mapi-over-https': 'enable',
        'name': 'default_name_6',
                'rpc-over-https': 'enable',
                'server-cert': 'test_value_8',
                'server-cert-mode': 're-sign',
                'ssl-anomalies-log': 'disable',
                'ssl-exemptions-log': 'disable',
                'untrusted-caname': 'test_value_12',
                'use-ssl-server': 'disable',
                'whitelist': 'enable'
    }

    set_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert not changed
    assert response['status'] == 'error'
    assert response['http_status'] == 404


def test_firewall_ssl_ssh_profile_filter_foreign_attributes(mocker):
    schema_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.schema')

    set_method_result = {'status': 'success', 'http_method': 'POST', 'http_status': 200}
    set_method_mock = mocker.patch('ansible_collections.fortinet.fortios.plugins.module_utils.network.fortios.fortios.FortiOSHandler.set', return_value=set_method_result)

    input_data = {
        'username': 'admin',
        'state': 'present',
        'firewall_ssl_ssh_profile': {
            'random_attribute_not_valid': 'tag',
            'caname': 'test_value_3',
            'comment': 'Optional comments.',
            'mapi_over_https': 'enable',
            'name': 'default_name_6',
            'rpc_over_https': 'enable',
            'server_cert': 'test_value_8',
            'server_cert_mode': 're-sign',
            'ssl_anomalies_log': 'disable',
            'ssl_exemptions_log': 'disable',
            'untrusted_caname': 'test_value_12',
            'use_ssl_server': 'disable',
            'whitelist': 'enable'
        },
        'vdom': 'root'}

    is_error, changed, response = fortios_firewall_ssl_ssh_profile.fortios_firewall(input_data, fos_instance)

    expected_data = {
        'caname': 'test_value_3',
        'comment': 'Optional comments.',
        'mapi-over-https': 'enable',
        'name': 'default_name_6',
                'rpc-over-https': 'enable',
                'server-cert': 'test_value_8',
                'server-cert-mode': 're-sign',
                'ssl-anomalies-log': 'disable',
                'ssl-exemptions-log': 'disable',
                'untrusted-caname': 'test_value_12',
                'use-ssl-server': 'disable',
                'whitelist': 'enable'
    }

    set_method_mock.assert_called_with('firewall', 'ssl-ssh-profile', data=expected_data, vdom='root')
    schema_method_mock.assert_not_called()
    assert not is_error
    assert changed
    assert response['status'] == 'success'
    assert response['http_status'] == 200