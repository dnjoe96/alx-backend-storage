#!/usr/bin/env python3
""" Module for top_students function """


def find_average(score_list):
    total_score = 0
    count = 0

    for one in score_list:
        # print(one.get('score'))
        total_score += one['score']
        count += 1
    if total_score == 0:
        return 0
    return total_score / count


def top_students(mongo_collection):
    """ The function returns all documents in a collection"""
    students = mongo_collection.find()
    top = []
    for student in students:
        student['averageScore'] = find_average(student.get('topics'))
        student.pop('topics')
        top.append(student)
    return top
