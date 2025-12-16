import pytest
from project import get_nutrition_data, display_nutrition_summary, ask_to_continue

def mock_response(food_name, weight):
    return {
        "name": food_name,
        "calories": 165.0,
        "protein": 31.0,
        "carbs": 0.0,
        "fat": 3.6
    }

def test_get_nutrition_data(monkeypatch):
    def mock_post(url, headers=None, json=None):
        class MockResponse:
            def raise_for_status(self): pass
            def json(self):
                return {
                    "foods": [{
                        "food_name": "chicken breast",
                        "serving_weight_grams": 100,
                        "nf_calories": 165,
                        "nf_protein": 31,
                        "nf_total_carbohydrate": 0,
                        "nf_total_fat": 3.6
                    }]
                }
        return MockResponse()
    monkeypatch.setattr("requests.post", mock_post)

    result = get_nutrition_data("chicken breast", 100)
    assert result["calories"] == 165.0
    assert result["protein"] == 31.0
    assert result["carbs"] == 0.0
    assert result["fat"] == 3.6

def test_display_nutrition_summary(capsys):
    food_list = [
        {"calories": 100, "protein": 10, "carbs": 20, "fat": 5},
        {"calories": 200, "protein": 20, "carbs": 30, "fat": 10}
    ]
    display_nutrition_summary(food_list)
    captured = capsys.readouterr()
    assert "Calories: 300" in captured.out
    assert "Protein: 30" in captured.out

def test_ask_to_continue(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "no")
    result = ask_to_continue()
    assert result == False
