python3 update.py

now=(date "+%H:%M:%S   %d/%m/%y")

git add .
git commit -m "$now"
git push -u