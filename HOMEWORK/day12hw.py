def customer_feedback_system():
    try:
        
        name = input("Enter your name: ").strip()
        feedback = input("Enter your feedback: ").strip()

        
        if not name:
            raise ValueError("Error: Name cannot be empty.")
        if not feedback:
            raise ValueError("Error: Feedback cannot be empty.")

        
        print(f"Thank you, {name}! We appreciate your feedback: \"{feedback}\"")

    except ValueError as ve:
        
        print(ve)

    finally:
    
        print("Feedback system execution completed.")



customer_feedback_system()