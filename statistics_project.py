import statistics

# Sample data
scores = [12, 15, 18, 20, 25]

# Calculate descriptive statistics
mean_score = statistics.mean(scores)
median_score = statistics.median(scores)
sample_std = statistics.stdev(scores)

print("Statistics Practice Project")
print("---------------------------")
print("Scores:", scores)
print("Mean:", round(mean_score, 2))
print("Median:", round(median_score, 2))
print("Sample standard deviation:", round(sample_std, 2))
