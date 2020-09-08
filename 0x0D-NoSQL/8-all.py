#!/usr/bin/env python3
"""8. list all documents"""
import pymongo


def list_all(mongo_collection):
    """list all documetns in coll"""
    return [doc for doc in mongo_collection.find()]
