# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import uuid

import gslib.tests.testcase as testcase
from gslib.tests.util import ObjectToURI as suri


class TestNotification(testcase.GsUtilIntegrationTestCase):
  """Integration tests for notification command."""

  def test_watch_bucket(self):
    bucket_uri = self.CreateBucket()
    self.RunGsUtil([
        'notification', 'watchbucket', 'https://localhost/notify',
        suri(bucket_uri)])

    identifier = str(uuid.uuid4())
    token = str(uuid.uuid4())
    stderr = self.RunGsUtil([
        'notification', 'watchbucket', '-i', identifier, '-t', token,
        'https://localhost/notify', suri(bucket_uri)], return_stderr=True)
    self.assertIn('token: %s' % token, stderr)
    self.assertIn('identifier: %s' % identifier, stderr)

  def test_stop_channel(self):
    bucket_uri = self.CreateBucket()
    stderr = self.RunGsUtil([
        'notification', 'watchbucket', 'https://localhost/notify',
        suri(bucket_uri)], return_stderr=True)

    channel_id = re.findall(r'channel identifier: (?P<id>.*)', stderr)
    self.assertEqual(len(channel_id), 1)
    resource_id = re.findall(r'resource identifier: (?P<id>.*)', stderr)
    self.assertEqual(len(resource_id), 1)

    channel_id = channel_id[0]
    resource_id = resource_id[0]

    self.RunGsUtil(['notification', 'stopchannel', channel_id, resource_id])

  def test_invalid_subcommand(self):
    stderr = self.RunGsUtil(['notification', 'foo', 'bar', 'baz'],
                            return_stderr=True, expected_status=1)
    self.assertIn('Invalid subcommand', stderr)
