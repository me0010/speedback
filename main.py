#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import os
import urllib
import webapp2
from google.appengine.ext import ndb

class SpeedSign(ndb.Model):
  signId = ndb.StringProperty(required=True)
  roadName = ndb.StringProperty()
  speedLimit = ndb.StringProperty()
  latitude = ndb.FloatProperty()
  lonitude = ndb.FloatProperty()

class SpeedFeedback(ndb.Model):
  location = ndb.GeoPtProperty()
  signId = ndb.IntegerProperty()
  decreaseSpeed = ndb.IntegerProperty()
  date = ndb.DateTimeProperty()

class AddNewSign(webapp2.RequestHandler):
  def get(self):
    try:
        lat = self.request.get('lat')
        latN = float(lat)
        lng = self.request.get('lng')
        lngN = float(lng)
        signId = self.request.get('signId')
        sLimit = self.request.get('speedlimit')
        rName = self.request.get('roadname')
        ss = SpeedSign(signId=signId,latitude = latN,lonitude = lngN,speedLimit=sLimit,roadName=rName)
        ss.put()
        self.response.write(lat)
    except (TypeError, ValueError):
        self.response.write("Fail")

class GetSpeedSignData(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello world')
    lat = int(self.request.get('lat'))
    lng = int(self.request.get('lng'))
    self.response.write('OK')

class GetFeedback(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello world')

class PlaceFeedback(webapp2.RequestHandler):
  def get(self):
    lat = self.request.get("lat")
    lon = self.request.get("lon")
    signId = self.request.get("signId")
    decrease = self.request.get("decrease")
    self.response.write(lat)

class DownloadFeedback(webapp2.RequestHandler):
  def get(self):
    self.response.write('Hello world')

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Helloworld!')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newsign', AddNewSign),
    ('/signdata', GetSpeedSignData),
    ('/feedback', GetFeedback),
    ('/newfeedback', PlaceFeedback),
    ('/download', DownloadFeedback)
], debug=True)
