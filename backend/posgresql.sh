#!/bin/bash

sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo systemctl status postgresql
sudo systemctl start postgresql
sudo -u postgres psql
CREATE DATABASE devopshub;
\l
\q
sudo -u postgres psql
ALTER USER postgres WITH PASSWORD 'postgres';
\q