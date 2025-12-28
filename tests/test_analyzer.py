import pytest
import pandas as pd
import sys
import os

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from analyzer import StudentAnalyzer  # noqa: E402


@pytest.fixture
def sample_data():
    data = {
        'student_id': [1, 2, 3],
        'name': ['Alice', 'Bob', 'Charlie'],
        'math_score': [80, 60, 90],
        'science_score': [85, 55, 95],
        'attendance_rate': [0.9, 0.8, 1.0]
    }
    return pd.DataFrame(data)


def test_calculate_average_scores(sample_data):
    analyzer = StudentAnalyzer()
    analyzer.data = sample_data

    averages = analyzer.calculate_average_scores()

    assert averages['math_score'] == pytest.approx(76.666, 0.01)
    assert averages['science_score'] == pytest.approx(78.333, 0.01)


def test_identify_at_risk_students(sample_data):
    analyzer = StudentAnalyzer()
    analyzer.data = sample_data

    # Bob has average (60+55)/2 = 57.5
    at_risk = analyzer.identify_at_risk_students(threshold=60)

    assert len(at_risk) == 1
    assert at_risk.iloc[0]['name'] == 'Bob'
    assert at_risk.iloc[0]['average_score'] == 57.5


def test_empty_data():
    analyzer = StudentAnalyzer()
    assert analyzer.calculate_average_scores() is None
