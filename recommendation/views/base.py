#由於某些程式是直接執行，而非透過伺服器，故需先設定 Django 環境
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'densearch.settings')
django.setup()