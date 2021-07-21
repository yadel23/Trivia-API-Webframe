import unittest
from app import user_input, getUrl, getJson, toDict
from flask import Flask, render_template, session, redirect, url_for, jsonify, request


class TestFileName(unittest.TestCase):

    
