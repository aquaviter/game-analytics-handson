#!/bin/bash

aws s3 cp master.yaml s3://game-analytics-handson-jp/
aws s3 cp infrastructure/ s3://game-analytics-handson-jp/infrastructure/ --recursive
