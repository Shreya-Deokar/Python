"""
Take name, roll number and field of interest from user and print in the below format :
Hey, my name is xyz and my roll number is xyz. My field of interest is xyz
"""

name = input("Enter Name:")
roll_no = int(input("Enter Roll No:"))
interest = input("Enter Field of Interest:")

print("My name id {0} and my roll number is {1}. My field of interest is {2}".format(name,roll_no,interest))