def vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture):
    result = (
        f"Vehicle Number: {vehicle_number}\n"
        f"Owner Name: {owner_name}\n"
        f"Vehicle Type: {vehicle_type}\n"
        f"Year of Manufacture: {year_of_manufacture}"
    )
    return result
if __name__ == "__main__":
    # Sample Output
    vehicle_number = "KA01AB5430"
    owner_name = "Samarth"
    vehicle_type = "Car"
    year_of_manufacture = 2020
    print(vehicle_info(vehicle_number, owner_name, vehicle_type, year_of_manufacture))