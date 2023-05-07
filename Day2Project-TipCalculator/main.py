print("Tip Calculator!")
bill = float(input("Enter the Total Bill: "))
percent_tip = float(input("Enter Percentage of Bill as Tip: "))
num_people = int(input("Enter Number of Friends to Share the Bill: "))

tip = bill * (percent_tip/100)
bill_with_tip = bill + tip
bill_per_person = round(bill_with_tip/num_people, 2)

print(f"Total Bill is Kes {bill_with_tip} and Tip is Kes {tip} and Bill per Head is Kes {bill_per_person}")


