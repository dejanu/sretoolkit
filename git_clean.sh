#!/usr/bin/bash
# some local cleanup:delete refs not local branches
git fetch -p
#display all remotes associated with origin git remote show origin
echo -e "-------> Checking remote...\nListing MERGED branches:"
git remote -v && git branch -r --merged | grep -v HEAD | xargs -L1 git --no-pager log --pretty=tformat:'%Cgreen%d%Creset | %h | %an | %Cblue%ar%Creset' -1 | column -t -s '|'
if [ $? -eq 0 ]; then
        read -p 'Delete REMOTE MERGED branches: yes/no ' anw
fi
if [ $anw == "yes" ];then
        git branch -r --merged master | grep -vE "develop|master|release" | awk -F'/' '{print $2}'|xargs -n 1 git push --delete origin
else
        echo Nothing to do
fi
