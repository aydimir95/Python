File I/O is all about writing code that can read from and write to the file itself

List - that store multiple values 

lists are stored in the computer's memory and once the program exits even the context of those disapear but lets give ourselves a starting point:

1. create a simple program names.py that collects people's names

2. write a csv file of those names and read from it 

3. append to the list more names and create a loop 

4. add another column to the csv file and append the house the names are from
5. format the list to make it readable for people by separating the name and the house to their own variables and adding a logical connection - lile the "name" is from "house"

6. the sorted function will use the value of key - "get_name/house" in this case calling that function on every dictionary in the list that it's supposed to sort and that function "get_name/house" returns the string that sorted will actually use whether things go left-right or in right-left it alphabetizes things based on the return value. Notice that "get_name/house is not passed in with brackets () - we are passing it only by it's name so that the sorted function can call that "get_name/house" function for us.

7. Turns out if we define a function "get_name" for example and end up using it right away, we can get rid of "get_name" function - and instead of passing key "get_name" - we can pass lambda function

8. lambda - is an anonymous function - lets you do it all in one breath. you can use lambda twice if you want - to pass a function to some other function that itself does not need a name. if your lambda function takes multiple parameters is also fine, after coma.

9. ValueError - how do we split the csv files other than with "," we can use someone else's library = csv. And the function "reader" from the csv library reads the csv and figures out where are all the commas, quotes and spaces etc, to split properly. 

docs.python.org/3/library/csv.html

9.1 so in order to split the csv properly use the quotes in places with commas in the text while using the csv library + reader function = it will figure out.

10. Storing the name of columns as headers - you can bake it into the file - add "name,home" to the top of the csv file, and change the "reader" to "DictReader" + change the rows to read "name and home".

    10.1 Then your code becomes smarter and lets you swap the csv or excel columns while keeping the output of the code the exact same.

11. you can also write into the csv file by importing the csv library and using the "csv.writer" function 

12. binary file - 0's and 1'
    12.1 pillow.readthedocs.io - library 
    12.2 Opens and saves binary files - to create a gif, a video, an audio file and much more.



Just finished writing my first 1000+ lines of code:


Here is how I counted it - using terminal:

$files = git ls-files
$totalLines = 0
foreach ($file in $files) {
    $lineCount = (Get-Content $file | Measure-Object -Line).Lines
    Write-Output "${file}: ${lineCount}"
    $totalLines += $lineCount
}
Write-Output "Total lines: ${totalLines}"


Here is an output:

Week_0-Functions&Variables/calculator.py: 18
Week_0-Functions&Variables/calculator_defined.py: 6
Week_0-Functions&Variables/define_function.py: 15
Week_0-Functions&Variables/hello_world.py: 51
Week_1_Conditionals/1_compare.py: 35
Week_1_Conditionals/2_grade.py: 34
Week_1_Conditionals/3_parity.py: 46
Week_1_Conditionals/4_house.py: 38
Week_1_Conditionals/freecodecamp.py: 6
Week_1_Conditionals/scrimba.py: 6
Week_2_Loops/1_cat.py: 55
Week_2_Loops/2_hogwarts.py: 22
Week_2_Loops/3_students.py: 13
Week_2_Loops/4_Lists-of-Dics.py: 17
Week_2_Loops/5_mario.py: 48
Week_3_Exceptions/1_number.py: 98
Week_4_Libraries/1_generate.py: 84
Week_4_Libraries/2_itunes-api.py: 22
Week_4_Libraries/say.py: 4
Week_4_Libraries/sayings.py: 9
Week_5_Unit-Tests/.DS_Store: 7
Week_5_Unit-Tests/calculator.py: 11
Week_5_Unit-Tests/hello.py: 9
Week_5_Unit-Tests/test/__init__.py: 0
Week_5_Unit-Tests/test/test-hello.py: 7
Week_5_Unit-Tests/test_calculator.py: 74
Week_5_Unit-Tests/test_hello.py: 11
Week_6_File_I-O/ReadME.txt: 20
Week_6_File_I-O/costume1.gif: 14
Week_6_File_I-O/costume2.gif: 17
Week_6_File_I-O/costumes.gif: 37
Week_6_File_I-O/costumes.py: 10
Week_6_File_I-O/names.csv: 4
Week_6_File_I-O/names.py: 53
Week_6_File_I-O/names.txt: 4
Week_6_File_I-O/students.csv: 5
Week_6_File_I-O/students.py: 132
Week_6_File_I-O/write-students.csv: 5
PS C:\Users\aydim\OneDrive\Desktop\Python\CS50 - Python - Copy> Write-Output "Total lines: ${totalLines}"
Total lines: 1053