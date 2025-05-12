# პროგრამა1
# Num1 =  int(input("enter number: "))
# Num2 =  int(input("enter number: "))
# if Num1 > Num2:
#     print("უფრო მეტია",Num1)
# elif Num2 > Num1:
#     print("უფრო მეტია",Num2)
# elif Num1 == Num2:
#     print(Num1,"ტოლია",Num2, "ის")

# პროგრამა2

questions = [
    {"question":"რამდენია 10_ის კვადრატი?", "answer":"100"},
    {"question": "რომელია საქართველოს დედაქალაქი?", "answer": "თბილისი"},
    {"question": "რომელია მსოფლიოს ყველაზე დიდი ოკეანე? ", "answer": "წყნარი ოკეანე"},
    {"question": "რამდენია 8 x 2 - 12", "answer": "4"},
    {"question": "რომელ კონტინენტზე მდებარეობს იტალია", "answer": "ევროპა"}
]

score = 10

for question in questions:
    correct_answers = question["answer"]
    while True:
        user_answer = input(f"{question['question']}: ")
        if user_answer.lower() == correct_answers.lower():
            print("ეს პასუხი სწორია!!")
            break
        else:
            score -= 1
            print(f"არასწორია! დარჩენილი ქულა: {score}\n")
            print(f"პროგრამის დასრულების შემდეგ თქვენი საბოლოო ქულა: {score}")
