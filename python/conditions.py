

# a = 19
# b = "pakistani"
# if a>18 or not b =="canadian":
#     print("your are eligible for vote and for job")
# elif a==18 :
#     print("you are eligible for vot not for job: ")
# else:
#     print("you are not eligible")


# day = input("enter value:")
# day = int(day)
# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("invalid input please enter between 1 to 7: ")

user = input("Enter your age")
user = int(user)


if user >= 18:
    nat = input("Enter your country")
    if nat == "Pakistan":
        print("you are eligible for vote: ")
    else:
        print("you are not pakistani so that you are not eligible for vote")
else:
    print("you are not 18 above so that you are not eligible for vote")