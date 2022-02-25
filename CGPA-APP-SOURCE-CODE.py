#programming software engine to calculate the total CGPA of students per semester
def CGPA():
    print('Always calculate your CGPA every semester to know your status')
    print('A code project by WHITEKID / BACKEND ENGINEER & COMPUTER OPERATOR\n Please follow the instructions below to calculate your CGPA\n Thanks!!!')

def login():
    name = input('Enter your full name >>>')
    gmail = input('Enter your email address >>>')
    password = input('Input a valid password to login >>>')
    print(f'Welcome {name}')

def grade():
    num = int(input('Enter number of core courses offered this semester >>>'))
    a = 0
    sum_1 = 0
    sum_2 = 0
    for a in range(num):
       course_code = str(input('Enter course codes here:'))
       course_unit = int(input('Enter course unit >>> '))
       grade = str(input('Enter your gotten grade of this course:'))
       if course_unit <= 10 and grade == 'A':
          a = course_unit * 5
       elif course_unit <= 10 and grade == 'B':
          a = course_unit * 4
       elif course_unit <= 10 and grade == 'C':
          a = course_unit * 3
       elif course_unit <= 10 and grade == 'D':
          a = course_unit * 2
       elif course_unit <= 10 and grade == 'E':
          a = course_unit * 1.
       else:
          a = course_unit * 0
       sum_1+=a
       sum_2+=course_unit
    CGPA = sum_1/sum_2
    print(f'Your total credit point for this semester is:{sum_1}')
    print(f'Your total CGPA/GP for this semester is:{CGPA}')
    print(f'Thanks for accessing, kindly log out\n ... .. . logging out ... .. .')




while True:
 login()
 CGPA()
 grade()

print()
