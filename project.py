import requests

API_URL = "https://trackapi.nutritionix.com/v2/natural/nutrients"
HEADERS = {
    "x-app-id": "72107dde",
    "x-app-key": "e0ae4c711a1436f7fdf6aba7ca339593",
    "Content-Type": "application/json"
}

def get_nutrition_data(food_name, weight_grams):
    payload = {
        "query": food_name,
        "timezone": "US/Eastern"
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    foods = response.json()["foods"]

    if not foods:
        raise ValueError("Food not found.")

    food = foods[0]
    multiplier = weight_grams / food["serving_weight_grams"]

    return {
        "name": food["food_name"],
        "calories": round(food["nf_calories"] * multiplier, 2),
        "protein": round(food["nf_protein"] * multiplier, 2),
        "carbs": round(food["nf_total_carbohydrate"] * multiplier, 2),
        "fat": round(food["nf_total_fat"] * multiplier, 2)
    }

def display_nutrition_summary(nutrition_list):
    """Display total macros from a list of food items."""
    total = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}

    for item in nutrition_list:
        total["calories"] += item["calories"]
        total["protein"] += item["protein"]
        total["carbs"] += item["carbs"]
        total["fat"] += item["fat"]

    print("\nTotal Nutrition:")
    print(f"Calories: {total['calories']} kcal")
    print(f"Protein: {total['protein']} g")
    print(f"Carbs: {total['carbs']} g")
    print(f"Fat: {total['fat']} g")

def ask_to_continue():
    while True:
        cont = input("Do you want to add another food? (yes/no): ").strip().lower()
        if cont in ["yes", "y"]:
            return True
        elif cont in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")

def main():
    print("Welcome to the Food Macro & Calorie Tracker!\n")
    nutrition_data = []

    while True:
        food = input("Enter a food name (e.g., 'banana', 'chicken breast'): ").strip()
        try:
            weight = float(input("Enter the weight in grams: "))
        except ValueError:
            print("Invalid weight. Please enter a number.")
            continue

        try:
            data = get_nutrition_data(food, weight)
            nutrition_data.append(data)
            print(f"\n{data['name'].title()} - {weight}g")
            print(f"Calories: {data['calories']} kcal")
            print(f"Protein: {data['protein']} g")
            print(f"Carbs: {data['carbs']} g")
            print(f"Fat: {data['fat']} g\n")
        except Exception as e:
            print(f"Error: {e}")

        if not ask_to_continue():
            break

    display_nutrition_summary(nutrition_data)

if __name__ == "__main__":
    main()
