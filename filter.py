#!/usr/bin/python
# coding=utf-8

from abc import abstractmethod
import define

class Filter:

    def __init__(self):
        pass

    @abstractmethod
    def analyze(self, request):
        pass