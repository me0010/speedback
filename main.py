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
  decreaseSpeed = ndb.StringProperty()
  latitude = ndb.FloatProperty()
  lonitude = ndb.FloatProperty()

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
    q = SpeedSign.query().filter(SpeedSign.latitude < -35.6).filter(SpeedSign.latitude > -35.8)
    lat = self.request.get('lat')
    lng = self.request.get('lng')
    """ndb.AND(SpeedSign.latitude < -35.29999, SpeedSign.latitude > -35.29990))"""
    self.response.write("<result>\n")
    for s in q:
        if s.lonitude < 149:
            self.response.write("   <sign>\n")
            self.response.write("       <signId>"+s.signId+"</signId>\n")
            self.response.write("       <roadName>"+s.roadName+"</roadName>\n")
            self.response.write("       <speedLimit>"+s.speedLimit+"</speedLimit>\n")
            self.response.write("       <latitude>"+str(s.latitude)+"</latitude>\n")
            self.response.write("       <lonitude>"+str(s.lonitude)+"</lonitude>\n")
            self.response.write("   </sign>\n")
    """lat = int(self.request.get('lat'))"""
    """lng = int(self.request.get('lng'))"""
    self.response.write('</result>')

class GetFeedback(webapp2.RequestHandler):
  def get(self):
    q = SpeedFeedback.query().filter(SpeedFeedback.latitude < -35.6).filter(SpeedFeedback.latitude > -35.8)
    self.response.write("<SpeedFeedback>\n")
    for r in q:
        if r.lonitude < 149:
            self.response.write("   <Feedback>\n")
            self.response.write("       <DecreaseSpeed>"+r.decreaseSpeed+"</DecreaseSpeed>\n")
            self.response.write("       <latitude>"+str(r.latitude)+"</latitude>\n")
            self.response.write("       <lonitude>"+str(r.lonitude)+"</lonitude>\n")
            self.response.write("   </Feedback>\n")
    self.response.write("</SpeedFeedback>\n")

class PlaceFeedback(webapp2.RequestHandler):
  def get(self):
    lat = self.request.get("lat")
    latN = float(lat)
    lon = self.request.get("lng")
    lonN = float(lon)
    decrease = self.request.get("decrease")
    fb = SpeedFeedback(decreaseSpeed=decrease,latitude=latN,lonitude=lonN)
    fb.put()
    self.response.write("OK")

class DownloadFeedback(webapp2.RequestHandler):
  def get(self):
    q = SpeedFeedback.query()
    self.response.write("<SpeedFeedback>\n")
    for r in q:
        self.response.write("   <Feedback>\n")
        self.response.write("       <DecreaseSpeed>"+r.decreaseSpeed+"</DecreaseSpeed>\n")
        self.response.write("       <latitude>"+str(r.latitude)+"</latitude>\n")
        self.response.write("       <lonitude>"+str(r.lonitude)+"</lonitude>\n")
        self.response.write("   </Feedback>\n")
    self.response.write("</SpeedFeedback>\n")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/newsign', AddNewSign),
    ('/signdata', GetSpeedSignData),
    ('/feedback', GetFeedback),
    ('/newfeedback', PlaceFeedback),
    ('/dload.xml', DownloadFeedback)
], debug=True)
