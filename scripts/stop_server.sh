#!/bin/bash
isExistApp=`pgrep httpd |apache2 `
if [[ -n  $isExistApp ]]; then
  service apache2 stop       
fi