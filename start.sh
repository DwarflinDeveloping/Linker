#!/bin/bash

# enter the bot token below!
export TOKEN=bottoken

if [ $TOKEN == "bottoken" ];
then
  echo You have not set the token. Set it in line 4 and try again.
  exit 1
fi

./bot.py
