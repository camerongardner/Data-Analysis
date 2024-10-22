import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
dataset = pd.read_csv("dataset.csv")

# ------------------ Question 1: App usage based on age and battery drain ------------------

def plot_app_usage_vs_age(ax):
    # Bar plot of App Usage Time vs Age in groups of ten
    age_groups = pd.cut(dataset['Age'], bins=range(0, 71, 10))
    grouped_data = dataset.groupby(age_groups)['App Usage Time (min/day)'].mean()
    grouped_data.plot(kind='bar', ax=ax)
    ax.set_title('User age associated with app usage')
    ax.set_xlabel('Age Groups (10-year intervals)')
    ax.set_ylabel('Average App Usage Time (min/day)')
    ax.grid(False)

def plot_app_usage_vs_battery_drain(ax):
    # Scatter plot of App Usage Time vs Battery Drain
    ax.scatter(dataset['Battery Drain (mAh/day)'], dataset['App Usage Time (hour/day)'] / 60, alpha=0.6)
    ax.set_title('App Usage associated with Battery Drain')
    ax.set_xlabel('Battery Drain (mAh/day)')
    ax.set_ylabel('App Usage Time (hours/day)')
    ax.grid(True)

def calculate_correlation_1():
    # Correlation between App Usage Time, Age, and Battery Drain
    correlation_1 = dataset[['App Usage Time (min/day)', 'Age', 'Battery Drain (mAh/day)']].corr()
    print("Correlation for Question 1:\n", correlation_1)

# ------------------ Question 2: Data usage in relation to app usage time and device model ------------------

def plot_app_usage_vs_data_usage(ax):
    # Bar plot of App Usage Time vs Data Usage in groups of ten
    app_usage_groups = pd.cut(dataset['App Usage Time (min/day)'] / 60, bins=range(0, int(dataset['App Usage Time (min/day)'].max() / 60) + 1, 1), labels=[str(i) for i in range(len(range(0, int(dataset['App Usage Time (min/day)'].max() / 60) + 1, 1)) - 1)])
    grouped_data = dataset.groupby(app_usage_groups)['Data Usage (MB/day)'].mean()
    grouped_data.plot(kind='bar', ax=ax)
    ax.set_title('App Usage associated with Data Usage')
    ax.set_xlabel('App Usage Time (hours/day)')
    ax.set_ylabel('Data Usage (MB/day)')
    ax.grid(True)

def plot_device_model_usage(ax):
    # Group by Device Model and calculate average App Usage Time and Data Usage
    device_model_usage = dataset.groupby('Device Model').agg(
        {'App Usage Time (min/day)': 'mean', 'Data Usage (MB/day)': 'mean'}
    )
    # Bar plot for App Usage Time and Data Usage by Device Model
    device_model_usage.plot(kind='bar', ax=ax)
    ax.set_title('Average App Usage associated with  Data Used by Device Model')
    ax.set_ylabel('Time (minuets/day) / Data (MB/day)')
    ax.grid(True)
    ax.set_xticklabels(device_model_usage.index, rotation=45)

def calculate_correlation_2():
    # Correlation between App Usage Time and Data Usage
    correlation_2 = dataset[['App Usage Time (min/day)', 'Data Usage (MB/day)']].corr()
    print("Correlation for Question 2:\n", correlation_2)

# ------------------ Question 3: Impact of the number of installed apps on data usage and app usage time ------------------

def plot_num_apps_vs_data_usage(ax):
    # Scatter plot of Number of Apps Installed vs Data Usage
    # ax.scatter(dataset['Number of Apps Installed'], dataset['Data Usage (MB/day)'], alpha=0.6)
    app_usage_groups = pd.cut(
        dataset['Number of Apps Installed'],
        bins=range(0, dataset['Number of Apps Installed'].max() + 2, 1),
        labels=[str(i) for i in range(dataset['Number of Apps Installed'].max() + 1)]
    )
    grouped_data = dataset.groupby(app_usage_groups)['Data Usage (MB/day)'].mean()
    grouped_data.plot(kind='bar', ax=ax)
    ax.set_title('Number of Apps Installed associated with Data Usage')
    ax.set_xlabel('Number of Apps Installed')
    ax.set_ylabel('Data Usage (MB/day)')
    ax.grid(True)
    ax.set_xticklabels(grouped_data.index, rotation=0, ha='right', fontsize=10)

def plot_num_apps_vs_app_usage_time(ax):
    # Scatter plot of Number of Apps Installed vs App Usage Time
    ax.scatter(dataset['Number of Apps Installed'], dataset['App Usage Time (min/day)'] / 60, alpha=0.6)
    ax.set_title('Number of Apps Installed associated with App Usage Time')
    ax.set_xlabel('Number of Apps Installed')
    ax.set_ylabel('App Usage Time (hours/day)')
    ax.grid(True)

def calculate_correlation_3():
    # Correlation between Number of Apps Installed, Data Usage, and App Usage Time
    correlation_3 = dataset[['Number of Apps Installed', 'Data Usage (MB/day)', 'App Usage Time (min/day)']].corr()
    print("Correlation for Question 3:\n", correlation_3)

def main():
    while True:
        print("\nPlease select which question's data you want to analyze:")
        print("1: App usage based on age and battery drain")
        print("2: Data usage in relation to app usage time and device model")
        print("3: Impact of the number of installed apps on data usage and app usage time")
        print("4: Quit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            fig1, axs1 = plt.subplots(1, 2, figsize=(16, 6))
            plot_app_usage_vs_age(axs1[0])
            plot_app_usage_vs_battery_drain(axs1[1])
            plt.tight_layout()
            plt.show()
            calculate_correlation_1()
        elif choice == '2':
            fig2, axs2 = plt.subplots(1, 2, figsize=(16, 6))
            plot_app_usage_vs_data_usage(axs2[0])
            plot_device_model_usage(axs2[1])
            plt.tight_layout()
            plt.show()
            calculate_correlation_2()
        elif choice == '3':
            fig3, axs3 = plt.subplots(1, 2, figsize=(16, 6))
            plot_num_apps_vs_data_usage(axs3[0])
            plot_num_apps_vs_app_usage_time(axs3[1])
            plt.tight_layout()
            plt.show()
            calculate_correlation_3()
        elif choice.lower() == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or '4' to quit.")

if __name__ == "__main__":
    main()
