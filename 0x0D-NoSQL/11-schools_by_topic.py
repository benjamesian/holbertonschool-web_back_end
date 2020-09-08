#!/usr/bin/env python3
"""11. query document"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """quert documetnts in coll"""
    return mongo_collection.find(
        {"topics": topic}
    )
