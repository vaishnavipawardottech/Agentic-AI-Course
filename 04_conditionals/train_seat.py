seat_type = input("Enter the seat type(sleeper/AC/general/luxury): ").lower()

match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds are available.")
    case "ac":
        print("AC - Air conditioning, comfy ride.")
    case "general":
        print("General - Cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats with meals")
    case _:
        print("Invalid seat type")