# Library --> stores books and information --> generallly quite

#Python Library --> a file or folder that contaions objects, functions, and data
# that we can access quickly. These collections of logic are created by others
# programmers who wanted to share their code, to make easier for other.

# Modules == Libararies

# to access a library/ module, we use the import keyword

import random

print(random.randrange(1, 10))

# modules/ libraries help us to speed up development time and write less code.
# because someone ready wrote it for us.

import example

student1 = example.student(20, 'college','Billy', False)

print(student1.name)
print(student1.is_in_uniform())