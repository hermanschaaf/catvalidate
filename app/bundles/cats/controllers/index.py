#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import redirect, request
from decanter.lib.decorator import get, post, validate_schema
from app.bundles.cats import validations

@get('/', apply='jinja2')
def new_cat():
    return redirect('/cat')


@get('/cat', apply='jinja2')
def new_cat():
    return {}


@post('/api/cat', apply='json', skip='jinja2')
@validate_schema(validations.valid_cat)
def api_new_cat():
    # the request.cleaned_data is added by validate_schema
    data = request.cleaned_data
    # ... do things
    return {}