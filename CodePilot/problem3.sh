#!/usr/bin/env bash

# extract archive archive.tar.gz to /home/ubuntu/extracted
tar -xzf archive.tar.gz -C /home/ubuntu/extracted

# in all extracted files, find all the records with status code 5xx and IP address not equal to 127.0.0.1 
# and write them to /home/ubuntu/extracted/5xx.txt using newline as delimiter


# create dir and extract
mkdir extracted_arch && tar -xzf archive.tar.gz -C extracted_arch

# check logs
find extracted_arch -type f -exec grep -E '5[0-9][0-9] [^127]' {} \; > /tmp/access.log

# clean folder
#rm -rf extracted_arch




grep -E '5[0-9][0-9] [^127]' *.log | sed 's/$/\n/' > /tmp/access.log


#!/usr/bin/env bash

mkdir extracted_arch && tar -xzf archive.tar.gz -C extracted_arch
find extracted_arch -type f -exec grep -E '5[0-9][0-9] [^127]' {} \; > /tmp/access.log
#rm -rf extracted_arch

exit 0
#fi


