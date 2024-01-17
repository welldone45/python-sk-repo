quiz = {

    1 : {

        "que"   :   "who is prime minister of india ?",
        "ans"   :   "narendra modi",

        },
    

    2 : {

        "que"   :   "most popular programing language ?",
        "ans"   :   "python",

        },
    
    3 : {

        "que"   :   "most pupular cricketer ?",
        "ans"   :   "ms dhoni",

        }
    
}

right = 0
wrong = 0

for k in range(1,len(quiz)+1):
    print("que.",k,"",quiz[k]["que"])
    ans = input("Enter your ans: ")
    if ans == quiz[k]["ans"]:
        print("right ans")
        right += 1
    else:
        print("wrong ans")
        woring += 1
    print()

    print(right)
    print(wrong)