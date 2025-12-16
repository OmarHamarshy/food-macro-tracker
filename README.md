# Food Macro & Calorie Tracker
#### Video Demo: https://www.youtube.com/watch?v=L1h5aNhNGwY
#### Description:

This Python project is a command-line application that allows users to calculate the calorie and macronutrient content (protein, carbohydrates, and fat) of various food items using real-time data from the Nutritionix API. Users can input a food item and its weight in grams, and the program will fetch detailed nutrition data. The user can enter multiple food items, and at the end, the program will display a total nutritional summary based on all entries.

The main goal of this project is to help individuals become more aware of what they eat by making it easier to track their food intake without needing a mobile app or spreadsheet. It’s especially useful for athletes, people on specific diets, or anyone simply trying to maintain a healthy lifestyle.

---

##  Project Structure

This project consists of three main files in the root directory, along with a `requirements.txt` file:

-`project.py`
  This is the main application script. It contains the `main()` function, which drives the user interaction, as well as three top-level helper functions:

  1. `get_nutrition_data(food_name, weight_grams)` – This function sends a POST request to the Nutritionix API to fetch calorie and macronutrient data for the given food name and weight.
  2. `display_nutrition_summary(nutrition_list)` – After all food entries are collected, this function calculates and prints the total calories, protein, carbs, and fat.
  3. `ask_to_continue()` – A small utility that asks the user whether they would like to continue adding food items. It ensures input validation for a smooth user experience.

  These functions are designed for testability and modularity, so the program can be easily extended or modified.

- `test_project.py`
  This file contains automated tests for the three custom functions listed above using `pytest`. To ensure that testing is reliable and does not depend on external API calls, the Nutritionix API is mocked in the test for `get_nutrition_data()` using Python’s `monkeypatch` functionality. The other two tests verify output display and input control flow.

- `requirements.txt`
  This file lists all required dependencies to run the project. Currently, it includes `requests` for making HTTP calls and `pytest` for running the test suite. The project can be set up with a simple `pip install -r requirements.txt`.

---

Design Decisions

This project emphasizes clarity, user-friendliness, and testability. One of the most important design decisions was to make the project interact with a real-world API instead of relying on static or hardcoded data. The **Nutritionix API** was chosen because it supports natural language queries like "2 eggs" or "banana" and provides reliable macro data.

Another key decision was to **separate logic into top-level functions** for ease of testing, as required by the project specification. By doing this, the program avoids tightly coupling logic with user interaction, which made writing `pytest` tests much simpler and cleaner.

The API logic could have been wrapped in a class, but I decided to keep everything functional and top-level to match the course requirements. I also considered caching food responses to avoid repeated API calls for the same items, but this was left out to maintain focus and keep the interface simple for users.

---

Future Improvements

If I were to continue improving this project, I would:
- Add a caching layer to store previously fetched foods.
- Enable the user to save their meals to a file or database.
- Build a web or GUI front-end using Flask or Tkinter.
- Improve error handling to better deal with edge cases like API timeouts or malformed input.

---

This project was an enjoyable way to bring together various skills I've learned in the course: API integration, function design, testing, and user interaction. I hope it serves as a practical and extendable tool for anyone interested in food tracking using Python.
