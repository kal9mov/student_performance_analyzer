import os
import sys
from analyzer import StudentAnalyzer
from visualizer import plot_score_distribution


def main():
    # Define paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, 'data', 'students.csv')
    output_plot_path = os.path.join(base_dir, 'data', 'score_distribution.png')

    # Initialize analyzer
    analyzer = StudentAnalyzer()

    # Load data
    print(f"Loading data from {data_path}...")
    if not analyzer.load_data(data_path):
        sys.exit(1)

    # Calculate averages
    print("\nCalculating average scores...")
    averages = analyzer.calculate_average_scores()
    print(averages)

    # Identify at-risk students
    print("\nIdentifying at-risk students (threshold < 60)...")
    at_risk = analyzer.identify_at_risk_students(threshold=60)
    if not at_risk.empty:
        print(at_risk)
    else:
        print("No students found at risk.")

    # Generate visualization
    print(f"\nGenerating visualization to {output_plot_path}...")
    plot_score_distribution(analyzer.data, output_plot_path)
    print("Done.")


if __name__ == "__main__":
    main()
