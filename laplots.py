#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 16:39:34 2021

@author: cabrown802
"""

# Library imports
import matplotlib.pyplot as plt
import pandas as pd

# Define neccesary constants
stat_file = "teacherratings.csv"

# Read CSV data for use in program
school_goodnesses = []
teacher_value = []

with open(stat_file, "r") as textfile:
    for r in textfile:
        datalist = r.split(",")
        try:
            school_goodnesses.append(float(datalist[10]))
            teacher_value.append(int(datalist[6]))
        except ValueError:
            pass
        
# Parse data to be plotted
topIndicies = []

for i in range(len(teacher_value)):
    if teacher_value[i] > 3:
        topIndicies.append(i)

midIndicies = []

for k in range(len(teacher_value)):
    if teacher_value[k] == 3:
        midIndicies.append(k)
        
lowIndicies = []

for q in range(len(teacher_value)):
    if teacher_value[q] < 3:
        lowIndicies.append(q)

topTeachers = []
topTeacherSchools = []

for j in topIndicies:
    topTeachers.append(teacher_value[j])
    topTeacherSchools.append(school_goodnesses[j])
    
midTeachers = []
midTeacherSchools = []

for l in midIndicies:
    midTeachers.append(teacher_value[l])
    midTeacherSchools.append(school_goodnesses[l])
    
lowTeachers = []
lowTeacherSchools = []

for w in lowIndicies:
    lowTeachers.append(teacher_value[w])
    lowTeacherSchools.append(school_goodnesses[w])

teachahs = pd.read_csv(stat_file)

lowschools = teachahs.sort_values('Delta Score').iloc[0:24]
midschools = teachahs.sort_values('Delta Score').iloc[24:48]
highschools = teachahs.sort_values('Delta Score').iloc[48:]

# Plot data
def firstPlot(level, schoolList):
    plt.hist(schoolList)
    plt.title(level + "-Rated Teacher Distribution Across LA Schools\n by "\
              + "School's Difference from Average Standardized Test Score")
    plt.xlabel("School's Difference from Average Standardized Test Score\n" \
               + "(for same year and grade level)")
    plt.ylabel("Number of " + level + "-Rated Teachers")
    plt.draw()

def secondPlot(level, panda):
    plt.hist(panda['Value Added'], bins=[1,2,3,4,5,6], align = 'left', \
             rwidth=0.8)
    plt.xticks([1,2,3,4,5])
    plt.title("Rating of Teachers at " + level + "-Rated Schools")
    plt.xlabel("Teacher Rating")
    plt.ylabel("Number of Teachers")
    plt.draw()
    
def main():
    firstPlot("Top", topTeacherSchools)
    firstPlot("Mid", midTeacherSchools)
    firstPlot("Low", lowTeacherSchools)
    secondPlot("Low", lowschools)
    secondPlot("Mid", midschools)
    secondPlot("Top", highschools)
    
# main()