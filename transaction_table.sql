-- Create Database
CREATE DATABASE gamelog;

-- Select database
USE gamelog;

-- Transaction Table
CREATE TABLE transaction (
  eventId VARCHAR(40) primary key,
  eventTimestamp DATETIME not null,
  eventCode VARCHAR(10) not null,
  userId VARCHAR(10) not null,
  itemId VARCHAR(10) not null,
  platform VARCHAR(10) not null
);
