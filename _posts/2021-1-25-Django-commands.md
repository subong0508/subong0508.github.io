---
layout: post
title: Django 기본 명령어 모음
date:  2021-1-25
author: Jung Jaeeun
categories: Backend
tags: python django backend server
comments: true
---

```python3
# run server
> python manage.py runserver {port_number}

# app 만들기
> python manage.py startapp {app_name}

# migration
> python manage.py makemigrations {app_name}
> python manage.py migrate {app_name}

# check
> python manage.py sqlmigrate {app_name} 0001_initial
> python manage.py dbshell
> python manage.py showmigrations {app_name}
```