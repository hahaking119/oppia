# coding: utf-8
#
# Copyright 2014 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Provides a seam for taskqueue-related operations."""

from google.appengine.ext import deferred

# NOTE: The following constants should match the queue names in queue.yaml.
# Default queue for processing tasks (including MapReduce ones).
QUEUE_NAME_DEFAULT = 'default'
# Deferred queue for processing events outside the request/response cycle.
QUEUE_NAME_EVENTS = 'events'


def defer(fn, *args, **kwargs):
    """Adds a new task to the default deferred queue."""
    deferred.defer(fn, *args, **kwargs)


def defer_to_events_queue(fn, *args, **kwargs):
    """Adds a new task to the deferred queue for processing events."""
    # See https://developers.google.com/appengine/articles/deferred for
    # details on the _queue kwarg.
    deferred.defer(fn, *args, _queue=QUEUE_NAME_EVENTS, **kwargs)


# A special exception that ensures that the task is not tried again, if it
# fails.
PermanentTaskFailure = deferred.PermanentTaskFailure
