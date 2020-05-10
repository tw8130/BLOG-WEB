from flask import render_template,request,redirect,url_for,abort,flash
from . import blogs
from flask_login import login_required,current_user
from ..models import User,Blog,Comment
from .forms import PostForm ,CommentForm
from .. import db