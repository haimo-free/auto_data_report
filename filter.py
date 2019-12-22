#!/usr/bin/python
# coding=utf-8

from abc import abstractmethod


class Filter:

    def __init__(self):
        pass

    @abstractmethod
    def analyze(self, get, post):
        pass