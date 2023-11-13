#!/usr/bin/env bash

# the key will be stored into ~/.ssh defaults to id_rsa

az vm create --name demovm --resource-group demodeal --image Ubuntu2204 --generate-ssh-keys
