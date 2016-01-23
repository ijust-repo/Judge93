#! /bin/bash

killall -9 uwsgi
uwsgi --ini ijust.ini

