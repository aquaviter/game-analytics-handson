-- Create Database
CREATE DATABASE gamelog;

-- Select database
USE gamelog;

-- Transaction Table
CREATE TABLE transaction (
  transaction_id VARCHAR(40) primary key,
  event_code VARCHAR(10) not null,
  item_id VARCHAR(10) not null,
  user_id VARCHAR(10) not null,
  eventTimestamp DATE not null,
  platform VARCHAR(10) not null
);
