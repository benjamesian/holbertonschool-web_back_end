#!/usr/bin/env python3
"""9. insert document"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert documetnt in coll"""
    return mongo_collection.insert_one(kwargs).inserted_id
