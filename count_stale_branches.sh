#!/bin/bash


git fetch --all

# Get the current date
current_date=$(date +%s)

# Set the stale period (3 months in seconds)
stale_period=$((90 * 24 * 60 * 60))

# Initialize stale branch count
stale_count=0

# Loop through each remote branch
for branch in $(git branch -r | grep -v '\->'); do
    # Get the last commit date for the branch
    last_commit_date=$(git log -1 --format=%ct $branch)
    
    # Calculate the age of the branch
    branch_age=$((current_date - last_commit_date))
    
    # Check if the branch is stale
    if [ $branch_age -gt $stale_period ]; then
        stale_count=$((stale_count + 1))
    fi
done

# Output the count of stale branches or a message if none are found
if [ $stale_count -gt 0 ]; then
    echo "Number of stale branches: $stale_count"
else
    echo "No stale branches found"
fi
