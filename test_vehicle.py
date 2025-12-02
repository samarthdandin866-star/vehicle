from vehicle import vehicle_info
def test_vehicle_info():
    expected_output = (
        "Vehicle Number: KA01AB5430\n"
        "Owner Name: Samarth\n"
        "Vehicle Type: Car\n"
        "Year of Manufacture: 2020"
    )
    result= vehicle_info("KA01AB5430", "Samarth", "Car", 2020) 
    assert result== expected_output
