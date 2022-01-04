import ezgmail, os
import random

os.chdir("chapter-18")
ezgmail.init()

chores = []
emails = []

print("Enter the chores, enter blank to finish entering: ")
while True:
    chore = input("Chore #%s:"%(len(chores) + 1))
    if not chore:
        break
    chores.append(chore)

print("\nEnter the Emails: ")
for n in range(len(chores)):
    email = input("Email #%s:"%(n + 1))
    emails.append(email)

print("\n")

for email in emails:
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    print(randomChore, "  assigned to  ", email)
    ezgmail.send(email, 'Chore', randomChore)