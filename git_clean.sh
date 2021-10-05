#!/usr/bin/bash
echo -e "Checking remote...\nListing MERGED branches:"
git remote -v && git branch -r --merged | grep -v HEAD | xargs -L1 git --no-pager log --pretty=tformat:'%Cgreen%d%Creset | %h | %an | %Cblue%ar%Creset' -1 | column -t -s '|'
if [ $? -eq 0 ]; then
	read -p 'Delete merged branches: yes/no ' anw
fi
if [ $anw == "yes" ];then
	#git branch -r --merged master | grep -vE "develop|master|release" | awk -F'/' '{print $2}'|xargs -n 1 git push --delete origin
	git branch -r --merged master | grep -vE "develop|master|release"
else
	echo Nothing to do
fi
