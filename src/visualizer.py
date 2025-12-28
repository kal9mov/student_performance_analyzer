import matplotlib.pyplot as plt


def plot_score_distribution(df, output_path):
    """Plots the distribution of average scores and saves it."""
    if df is None or df.empty:
        print("No data to plot.")
        return

    subjects = [col for col in df.columns if 'score' in col]
    if 'average_score' not in df.columns:
        df['average_score'] = df[subjects].mean(axis=1)

    plt.figure(figsize=(10, 6))
    plt.hist(df['average_score'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Student Average Scores')
    plt.xlabel('Average Score')
    plt.ylabel('Number of Students')
    plt.grid(axis='y', alpha=0.75)
    
    try:
        plt.savefig(output_path)
        print(f"Plot saved to {output_path}")
    except Exception as e:
        print(f"Error saving plot: {e}")
    finally:
        plt.close()
