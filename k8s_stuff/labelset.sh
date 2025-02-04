#!/usr/bin/env bash




# list all pods with app label
kubectl get po -A -L app --no-headers -o custom-columns=":metadata.labels.app"


# define a list of app labels (based on RASCI matrix)
org1_labels=("app1" "app2" "app3")
org2_labels=("app4" "app5" "app6")
org3_labels=("app7" "app8" "app9")

#  join the app labels in a comma separated string for each org
org1_labels=$(IFS=,; echo "${org1_labels[*]}")
org2_labels=$(IFS=,; echo "${org2_labels[*]}")
org3_labels=$(IFS=,; echo "${org3_labels[*]}")

# get all pods with app labels in org1
kubectl get po -A -l "app in ($org1_labels)" --as=cluster-admin
