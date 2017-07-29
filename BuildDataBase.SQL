CREATE TABLE SPEEDSIGN (
  'SignId' INT NOT NULL,
  'Name' VARCHAR(45),
  'Lat' DOUBLE,
  'Lng' DOUBLE
);

CREATE TABLE SpeedFeedback (
  'Lat' DOUBLE,
  'Lng' DOUBLE,
  'SignId' Int,
  'Date' DATETIME(6)
);
