peoples = ["Karim", "Tantawy", "Ahmed", "Mohamed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

  print('*'*(len(name)+13))
  print(f"'{name}' Skills Is: ")
  print('*'*(len(name)+13))
  
  for skill in skills:
      print(f"- {skill}")
 
  print('*'*(len(name)+13))


people = {
  "Karim": {
    "C++": "70%",
    "Python": "80%",
  },
  "Ahmed": {
    "Html": "90%",
    "Css": "80%",
    "Js": "90%"
  },
  "Tantawy": {
    "mySQL": "70%",
    "Django": "60%",
    "WebDevelopment": "90%"
  }
}


for person, skills in people.items():    # here the compiler expect 'person' as a 'Tuple'  and  'skills' as a 'Dictionary'
    # Print header with dynamic length
    print('-' * (len(person) + 13))
    print(f"'{person}' Skills Is:")
    print('-' * (len(person) + 13))

    max_hash = 0

    for skill, score in skills.items():   # here the compiler expect 'skill' as a 'Tuple'  and  'score' as a 'Dictionary'
        # Loop through each skill and score
        print(f"- {skill} with score of {score}")
        
        # Update max_hash if the current skill + score length is greater
        if max_hash < len(skill) + len(score):
            max_hash = len(skill) + len(score)
    
    # Print # based on the maximum length calculated
    print('#' * (max_hash + 17))