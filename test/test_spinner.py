import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from spinner import Spinner

@pytest.fixture
def valid_probs():
    return {'outcome': ['A', 'B'], 'probability': [0.5, 0.5]}

@pytest.fixture
def invalid_probs_sum():
    return {'outcome': ['A', 'B'], 'probability': [0.3, 0.3]}

@pytest.fixture
def invalid_probs_range():
    return {'outcome': ['A', 'B'], 'probability': [1.2, -0.2]}

def test_spinner_init_valid(valid_probs):
    s = Spinner(valid_probs)
    assert s.probabilities == valid_probs

# def test_spinner_init_invalid_sum(invalid_probs_sum, capsys):
#     s = Spinner(invalid_probs_sum)
#     captured = capsys.readouterr()
#     assert "Invalid probabilities" in captured.out
#     assert s.probabilities is None

# def test_spinner_init_invalid_range(invalid_probs_range, capsys):
#     s = Spinner(invalid_probs_range)
#     captured = capsys.readouterr()
#     assert "Invalid probabilities" in captured.out
#     assert s.probabilities is None

def test_spinner_init_empty():
    s = Spinner()
    assert s.probabilities == {'outcome': [], 'probability': []}

def test_spin_returns_outcome(valid_probs):
    s = Spinner()
    s.update_probabilities(valid_probs)
    result = s.spin()
    assert result in valid_probs['outcome']

def test_update_probabilities_valid(valid_probs):
    s = Spinner()
    s.update_probabilities(valid_probs)
    assert s.probabilities == valid_probs

# def test_update_probabilities_invalid_sum(valid_probs, invalid_probs_sum, capsys):
#     s = Spinner()
#     s.update_probabilities(valid_probs)
#     s.update_probabilities(invalid_probs_sum)
#     captured = capsys.readouterr()
#     assert "Invalid probabilities" in captured.out
#     # Should not update to invalid
#     assert s.probabilities == valid_probs

# def test_update_probabilities_invalid_range(valid_probs, invalid_probs_range, capsys):
#     s = Spinner()
#     s.update_probabilities(valid_probs)
#     s.update_probabilities(invalid_probs_range)
#     captured = capsys.readouterr()
#     assert "Invalid probabilities" in captured.out
#     # Should not update to invalid
#     assert s.probabilities == valid_probs

