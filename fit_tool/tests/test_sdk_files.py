import csv
import os
from fit_tool.fit_file import FitFile

def test_developer_data():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/DeveloperData.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_activity(tmpdir):
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/Activity.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        rows = fit_file.to_rows()
    out_path = tmpdir / 'Activity.csv'
    with open(out_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            csv_writer.writerow(row)

def test_activity_developer_data(tmpdir):
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_developerdata.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        rows = fit_file.to_rows()
    out_path = tmpdir / 'activity_developerdata.csv'
    with open(out_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in rows:
            csv_writer.writerow(row)

def test_activity_low_battery():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_lowbattery.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_activity_multi_sport():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_multisport.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_activity_poolswim_with_hr():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_poolswim_with_hr.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_activity_poolswim():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_poolswim.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_activity_truncated():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/activity_truncated.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_monitoring_file():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/MonitoringFile.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_weight_scale_multi_user():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WeightScaleMultiUser.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_weight_scale_single_user():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WeightScaleSingleUser.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_workout_individual_steps():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WorkoutIndividualSteps.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_workout_custom_target_values():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WorkoutCustomTargetValues.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_workout_repeat_greater_than_step():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WorkoutRepeatGreaterThanStep.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()

def test_workout_repeat_steps():
    path = os.path.join(os.path.dirname(__file__), 'data/sdk/WorkoutRepeatSteps.fit')
    with open(path, 'rb') as file_object:
        bytes_buffer = file_object.read()
        fit_file = FitFile.from_bytes(bytes_buffer)
        fit_file.to_rows()
