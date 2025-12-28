import pandas as pd


class StudentAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self, filepath):
        """Loads student data from a CSV file."""
        try:
            self.data = pd.read_csv(filepath)
            return True
        except FileNotFoundError:
            print(f"Error: File not found at {filepath}")
            return False
        except Exception as e:
            print(f"Error loading data: {e}")
            return False

    def calculate_average_scores(self):
        """Calculates average scores for each subject."""
        if self.data is None:
            return None

        subjects = [col for col in self.data.columns if 'score' in col]
        return self.data[subjects].mean()

    def identify_at_risk_students(self, threshold=60):
        """Identifies students with an average score below the threshold."""
        if self.data is None:
            return None

        subjects = [col for col in self.data.columns if 'score' in col]
        self.data['average_score'] = self.data[subjects].mean(axis=1)

        at_risk = self.data[self.data['average_score'] < threshold]
        return at_risk[[
            'student_id', 'name', 'average_score', 'attendance_rate'
        ]]
