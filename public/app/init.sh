#!/bin/bash

echo "Import Blog models"
echo " * Import Categories"
python manage.py loaddata category.json
echo " * Import Posts"
python manage.py loaddata post.json
echo " * Import Pages"
python manage.py loaddata page.json