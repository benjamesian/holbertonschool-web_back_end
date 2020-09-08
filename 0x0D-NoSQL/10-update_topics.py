#!/usr/bin/env python3
"""10. update document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """update documetnt in coll"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    ).inserted_id
