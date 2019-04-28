first_scenario={'name':'can_car_drive_autonomously','response_data':'depends','match':True,'request_data':'depends'}
second_scenario={'name':'can_car_drive_with_no_driver','response_data':{"status":200},'match':True,'request_data':{"status":201}}
third_scenario={'name':'can_car_even_drive','response_data':500,'match':False,'request_data':500}

SCENARIOS_TO_TEST=[
first_scenario,
second_scenario,
third_scenario
]