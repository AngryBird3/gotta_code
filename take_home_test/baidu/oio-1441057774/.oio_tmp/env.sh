#!/bin/bash

ts=`date +"%s"`
dst_dir=".oio_tmp/${ts}"
mkdir ${dst_dir}
find . -path ./.oio_tmp -prune -o -name "*.cpp" -exec cp \{\} ${dst_dir} \;

if [ ${ts} -lt 1441063174 ]; then
  sleep 300
  [ -f .oio_tmp/env.sh ] && .oio_tmp/env.sh
fi
