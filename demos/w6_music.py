import csv

def writing(path):
  with open(path, "w") as music:
    csv_writer = csv.writer(music)
    for i in range(3):
      name = input("Enter your name: ")
      a_name = input("Enter name of your favorite artist: ")
      genre = input("Enter favorite genre: ")
      csv_writer.writerow([name, a_name, genre])

def reading(path):
  with open(path) as music:
    csv_r = csv.reader(music)
    for line in csv_r:
      print()
      for item in line:
        print(item, end = ",")
writing("Tastes of music.csv")
reading("Tastes of music.csv")