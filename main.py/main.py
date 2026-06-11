import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data/network_logs.csv')

# Dataset Overview
print('=== DATASET OVERVIEW ===')
print(f'Rows: {len(data)}')
print(f'Columns: {len(data.columns)}')

# Column Names
print('\n=== COLUMN NAMES ===')
for col in data.columns:
    print(col)
    
# Attack Distribution
print('\n=== ATTACK DISTRIBUTION ===')
print(data['attack_detected'].value_counts())

# Analyze Failed Logins
print('\n=== FAILED LOGIN ANALYSIS ===')
failed_login_analysis = data.groupby('attack_detected')['failed_logins'].mean()
print(failed_login_analysis)

# Analyze Login Attempts
print('\n=== LOGIN ATTEMPT ANALYSIS ===')
login_attempt_analysis = data.groupby('attack_detected')['login_attempts'].mean()
print(login_attempt_analysis)

# Analyze IP Reputation Score
print('\n=== REPUTATION SCORE ANALYSIS ===')
reputation_analysis = data.groupby('attack_detected')['ip_reputation_score'].mean()
print(reputation_analysis)

# Analyze unusual access times
print('\n=== UNUSUAL TIME ACCESS ===')
print(
    data.groupby('attack_detected')['unusual_time_access'].mean()
)

# Create Graph
print('\nCreating Visualizations...')
attack_groups = data.groupby('attack_detected')[
    ['failed_logins', 'login_attempts']
].mean()

# Generate Visualization
attack_groups.plot(kind='bar')

# Add labels and title
plt.title('Attack vs Non-Attack Session Characteristics')
plt.xlabel('Attack Detected')
plt.ylabel('Average Value')
plt.tight_layout()

# Save the Graph
plt.savefig('images/attack_comparison.png')

# Display the Graph
plt.show()

# Create Threat Score
print('\n=== THREAT SCORING ===')

data['threat_score'] = (
    data['failed_logins'] * 2
    + data['login_attempts']
    + data['ip_reputation_score'] * 3
)

# Highest Risk Sessions
top_threats = data.sort_values(
    by='threat_score',
    ascending=False
)

print(top_threats[
    [
        'session_id',
        'threat_score',
        'failed_logins',
        'login_attempts',
        'attack_detected'
    ]
].head(10))

# Analyze Threat Score by Group
print('\n=== THREAT SCORE COMPARISON ===')

print(
    data.groupby('attack_detected')[
        'threat_score'
        ].mean()
)

# Threat Score Visualization
plt.figure()

data.groupby('attack_detected')[
    'threat_score'
].mean().plot(kind='bar')

plt.title('Average Threat Score by Attack Status')
plt.xlabel('Attack Detected')
plt.ylabel('Average Threat Score')

plt.tight_layout()

plt.savefig('images/threat_score_comparison.png')

plt.show()

# Anomaly Detection

# Analyze packet sizes
print('\n=== PACKET SIZE ANALYSIS ===')
print(data['network_packet_size'].describe())

# Anomoly Threshold
packet_mean = data['network_packet_size'].mean()
packet_std = data['network_packet_size'].std()

packet_threshold = packet_mean + (2 * packet_std)

print('\nPacket Size Threshold:')
print(packet_threshold)

# Identify Anomalous Sessions
anomalies = data[
    data['network_packet_size'] > packet_threshold
]

print('\n=== PACKET SIZE ANOMALIES ===')
print(f'Anomalies Found: {len(anomalies)}')

# Examine Top Anomalies
print(
    anomalies[
        [
            'session_id',
            'network_packet_size',
            'attack_detected'
        ]
    ].head(10)
)

# Visualize Anomalies
plt.figure()

data['network_packet_size'].hist(bins=30)

plt.axvline(
    packet_threshold,
    linestyle='--',
    label='Anomaly Threshold'
)

plt.title('Network Packet Size Distribution')
plt.xlabel('Packet Size')
plt.ylabel('Frequency')

plt.legend()

plt.tight_layout()

plt.savefig('images/packet_size_distribution.png')

plt.show()

# Anomaly Attack Rate
print('\n=== ANOMALY ATTACK RATE ===')
print(anomalies['attack_detected'].value_counts(normalize=True) * 100)