# nosetests --nocapture  tests/test_field.py

from fit_tool.base_type import BaseType
from fit_tool.definition_message import DefinitionMessage
from fit_tool.endian import Endian
from fit_tool.field_definition import FieldDefinition
from fit_tool.profile.messages.workout_step_message import WorkoutStepMessage
from fit_tool.profile.profile_type import WorkoutStepDuration


def test_definition_message_conversions():
    dm1 = DefinitionMessage(global_id=555, local_id=20,
                            field_definitions=[FieldDefinition(field_id=100, size=5, base_type=BaseType.STRING)])
    bytes1 = dm1.to_bytes()
    dm2 = DefinitionMessage.from_bytes(bytes1)
    bytes2 = dm2.to_bytes()

    assert bytes2 == bytes1


def test_big_endian_conversion():
    dm1 = DefinitionMessage(global_id=555, local_id=20,
                            endian=Endian.BIG,
                            field_definitions=[FieldDefinition(field_id=100, size=5, base_type=BaseType.STRING)])

    bytes1 = dm1.to_bytes()
    dm2 = DefinitionMessage.from_bytes(bytes1)
    bytes2 = dm2.to_bytes()

    assert bytes2 == bytes1
    assert dm2.endian == Endian.BIG


def test_to_row():
    dm1 = WorkoutStepMessage()
    dm1.workoutStepName = 'test'
    dm1.durationType = WorkoutStepDuration.DISTANCE

    definition = DefinitionMessage.from_data_message(dm1)
    row = definition.to_row()
    print(row)
