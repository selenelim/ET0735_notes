import employee_info as EMPI
from employee_info import employee_data as EMPDATA


def test_calc_average_salary():
    expected_result = 60166.67
    test_result = EMPI.calculate_average_salary()
    assert (test_result == expected_result)


def test_get_employee_by_dept_Sales():
    expected_result = [ EMPDATA[0], EMPDATA[-1]]
    test_result = EMPI.get_employees_by_dept('Sales')
    assert (test_result == expected_result)


def test_get_employee_by_dept_Marketing():
    expected_result = [ EMPDATA[1], EMPDATA[2]]
    test_result = EMPI.get_employees_by_dept('Marketing')
    assert (test_result == expected_result)


def test_get_by_age():
    expected_result = [ EMPDATA[0], EMPDATA[4]]
    lower_limit=26
    upper_limit=33
    test_result = EMPI.get_employees_by_age_range(lower_limit, upper_limit)
    assert (test_result == expected_result)



def test_get_by_age_20_28():
    expected_result = [ EMPDATA[1], EMPDATA[2]]
    lower_limit=20
    upper_limit=28
    test_result = EMPI.get_employees_by_age_range(lower_limit, upper_limit)
    assert (test_result == expected_result)
