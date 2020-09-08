#!/usr/bin/env python3
"""101. query document"""
import pymongo


def top_students(mongo_collection):
    """quert documetnts in coll"""
    return mongo_collection.aggregate([
        {"$topics": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"$averageScore": -1}}
    ])
