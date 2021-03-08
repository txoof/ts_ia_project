#!/bin/bash
~/bin/develtools/pycodesign.py codesign.ini

if [[ $? == 0 ]]; then
  echo "sign and staple succeeded; pushing update to github"
  git commit -m "add updated pkg"
  git push
else
  echo "sign and staple failed -- see previous errors"
  exit 1
fi
  
