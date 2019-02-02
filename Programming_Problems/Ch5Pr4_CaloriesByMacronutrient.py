# Programming Practice 5.4 Calories by Macronutrient
"""
A nutritionist who works for a fitness club helps members by evaluating
their diets. As part of her evaluation, she asks members for the number
of fat grams, carbohydrate grams, and protein grams that they consumed
in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
    calories from fat = fat grams X 9

Next, she calculates the number of calories that result from the
carbohydrates, using the following formula:
    calories from carbs = carb grams X 4

Next, she calculates the number of calories that result from the proteins,
using the following formula:
    calories from protein = protein grams X 4
"""


def main():
    print("Please enter grams eaten for each category.")
    cal_fats = calc_cal_fats(float(input("  Fats? ")))
    cal_carbs = calc_cal_carbs(float(input("  Carbs? ")))
    cal_proteins = calc_cal_protein(float(input("  Protein? ")))
    total_cal = cal_fats + cal_carbs + cal_proteins
    print()

    print(
        "Here are the calories consumed: \n"
        "  ... from fats: {f:,.0f} calories \n"
        "  ... from carbohydrates: {c:,.0f} calories \n"
        "  ... from protein: {p:,.0f} calories \n"
        "Total: {total:,.0f} calories"
        .format(f=cal_fats, c=cal_carbs, p=cal_proteins, total=total_cal)
    )


def calc_cal_fats(grams):
    return grams * 9


def calc_cal_carbs(grams):
    return grams * 4


def calc_cal_protein(grams):
    return grams * 4


main()
