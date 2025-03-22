#!/bin/sh

#RED='\033[0;31m' #red
RED='\033[1;31m'  # Bright red
LG='\033[1;32m'
NC='\033[0m'  # No Color

wip() {
  secs=$1
  total=$secs
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  printf "\r\n" 
  while [ $secs -gt 0 ]; do
    progress=$(( (total - secs) * 50 / total ))  # Scale progress to 50 chars
    bar=$(printf "%-${progress}s" "#" | tr ' ' '#')
    #printf "\r⏳ [%s%-*s] %d seconds remaining..." "$bar" $((50 - progress)) "" "$secs"
    printf "\r [%s%-*s]  loading ..." "$bar" $((50 - progress)) "" 
    sleep 1
    : $((secs--))
  done
  echo -e "\r [##################################################] ${LG} #techtakeovers${NC}" 
  sleep 6	
}

alias wip=wip
