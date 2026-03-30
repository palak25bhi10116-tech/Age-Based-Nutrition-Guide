def get_nutrition_guidelines(age):
    """
    Determines nutritional focus and food recommendations based on age.
    This module handles the core logic of the life-stage mapping.
    """
    # Structured data: (Upper Age Limit, Life Stage, Primary Focus, Recommendations)
    nutritional_data = [
        (12,  "Childhood",       "Growth and Bone Density", "Milk, Eggs, Berries"),
        (19,  "Adolescence",     "Hormonal Balance", "Lean Meats, Spinach, Walnuts"),
        (39,  "Adulthood",       "Metabolic Foundation", "Avocado, Salmon, Kale"),
        (59,  "Mid-Adulthood",   "Heart Health", "Almonds, Olive Oil, Beets"),
        (120, "Senior Years",    "Cognitive Health", "Kefir, Turmeric, Beans")
    ]
    
    # Using a generator expression to find the first matching age bracket
    # This meets the requirement for efficient data processing logic.
    return next((details for limit, *details in nutritional_data if age <= limit), None)

def main():
    """
    Main entry point for the application. 
    Handles user interaction and input validation.
    """
    print("--- Age-Based Nutrition Guide ---")
    
    try:
        user_input = input("Please enter your age: ")
        age = int(user_input)
        
        # Input validation for realistic age ranges
        if age < 0 or age > 120:
            print("Error: Please enter an age between 0 and 120.")
            return

        guidelines = get_nutrition_guidelines(age)
        
        if guidelines:
            stage, focus, foods = guidelines
            print(f"\nLife Stage: {stage}")
            print(f"Nutritional Focus: {focus}")
            print(f"Recommended Foods: {foods}")
            
    except ValueError:
        print("Error: Invalid input. Please enter a numerical value for age.")

if __name__ == "__main__":
    main()
