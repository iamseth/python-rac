#!/usr/bin/env python

import urllib2

class RAC(object):

    def __init__(self, host, username, password):
        self.sid = None
        self.host = host
        self.username = username
        self.password = password

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_value, ex_tb):
        self._logout()

    def _inject_header(self, data):
        if data is not None:
            return "<?xml version='1.0'?>" + data

    def _extract_value(self, data, value):
        if data is None:
            return
        try:
            return data.split('<%s>' % value)[1].split('</%s>' % value)[0]
        except KeyError:
            raise Exception('unable to extract %s' % value)

    def _extract_sid(self, data):
        return self._extract_value(data, 'SID')

    def _extract_cmd_output(self, data):
        return self._extract_value(data, 'CMDOUTPUT')

    def _make_request(self, uri, data=None):
        opener = urllib2.build_opener()
        if self.sid:
            opener.addheaders.append(('Cookie', 'sid=%s' % self.sid))
        return opener.open('https://%s/cgi-bin/%s' % (self.host, uri),
                self._inject_header(data)).read()

    def _login(self):
        data = '<LOGIN><REQ><USERNAME>%s</USERNAME><PASSWORD>%s</PASSWORD></REQ></LOGIN>' % (self.username, self.password)
        resp = self._make_request('/login', data)
        self.sid = self._extract_sid(resp)

    def _logout(self):
        self._make_request('/logout')
        self.sid = None
    def run_command(self, cmd):
        if self.sid is None:
            self._login()
        try:
            data = '<EXEC><REQ><CMDINPUT>racadm %s</CMDINPUT><MAXOUTPUTLEN>0x0fff</MAXOUTPUTLEN></REQ></EXEC>' % cmd
            return self._extract_cmd_output(self._make_request('/exec', data)).strip()
        finally:
            self._logout()

    def get_group_config(self, group):
        return self.run_command('getconfig -g %s' % group)

    def pxeboot(self):
        self.run_command('config -g cfgServerInfo -o cfgServerFirstBootDevice pxe')
        self.run_command('config -g cfgServerInfo -o cfgServerBootOnce 1')
        return self.powercycle()

    def powercycle(self):
        return self.run_command('serveraction powercycle')

    def powerdown(self):
        return self.run_command('serveraction powerdown')

    def powerup(self):
        return self.run_command('serveraction powerup')

