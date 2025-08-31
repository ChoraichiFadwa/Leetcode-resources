12. How data engineers process data
03:19 - 04:38
In terms of data processing, data engineers have different responsibilities. They perform data manipulation, cleaning, and tidying tasks that can be automated, and that will always need to be done, regardless of the analysis anyone wants to do with them. For example, rejecting corrupt song files, or deciding what happens with missing metadata. What should we do when the genre is missing? Do we reject the file, do we leave the genre blank, or do we provide one by default? They also ensure that the data is stored in a sanely structured database, and create views on top of the database tables for easy access by analysts. Views are the output of a stored query on the data. 

apache spark : a processing tool 


Great job connecting the dots! As you can see, most of the data processing steps are transformation steps including selecting, encoding, calculating new values, sorting and ordering, joining data from multiple sources, aggregating, pivoting tables, splitting one table into several ones, removing duplicate values.

Depending on the context, validating data can be considered part of the extract step (you don't extract if it's not necessary), or the transform step (you check that your results make sense before saving them).

OK, now that you know about processing tasks, let's see how to schedule them!