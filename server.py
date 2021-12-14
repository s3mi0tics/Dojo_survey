from flask_app import app
from flask import Flask, render_template, session, request,redirect, flash
app.secret_key = "rootroot"
from flask_app.controllers import controller_routes


if __name__=="__main__":
    app.run(debug=True)

