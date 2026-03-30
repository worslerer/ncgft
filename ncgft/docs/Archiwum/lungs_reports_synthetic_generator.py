import random
import pandas as pd

# -----------------------------
# 1. Define synonyms / positive findings
# -----------------------------
positive_terms = [
    'nodule', 'mass', 'cyst', 'lesion', 'opacity',
    'tumor', 'growth', 'swelling', 'node', 'focal density',
    'rounded shadow', 'cavitary lesion', 'solid lesion',
    'subpleural nodule', 'ground-glass opacity', 'soft tissue density', 
    'popcorn calcification', 'fat-containing nodules', 'complete central calcification'
]

locations = [
    'right upper lobe', 'left upper lobe', 'right lower lobe', 'left lower lobe',
    'right middle lobe', 'left lingula', 'bilateral lungs', 'apical segment', 'basal segment'
]

sizes = ['3 mm', '5 mm', '7 mm', '10 mm', '12 mm', '15 mm', 'small', 'tiny', 'subcentimeter']

# Negation phrases for No class
negative_phrases = [
    'Lungs are clear', 'No pulmonary nodules', 'No masses detected',
    'No suspicious lesions', 'Lungs are unremarkable', 'No cysts or growths',
    'No focal density', 'No opacity identified', 
    'No nodules, or nodules with benign features or fat-containing nodules.',
    'No nodules, or nodules with benign features like complete central or popcorn calcification, or fat-containing nodules.',
    'No nodules, or nodules with benign features like popcorn calcification, or fat-containing nodules.'
]

# -----------------------------
# 2. Generate synthetic positive examples
# -----------------------------
def generate_positive_example():
    term = random.choice(positive_terms)
    loc = random.choice(locations)
    size = random.choice(sizes)
    
    templates = [
        f'A {size} {term} is noted in the {loc}.',
        f'{size} {term} observed in the {loc}.',
        f'{term.capitalize()} measuring {size} present in {loc}.',
        f'CT shows a {size} {term} in the {loc}.',
        f'Impression: {size} {term} located in the {loc}.',
        f'{term.capitalize()} detected in the {loc}, size approximately {size}.',
        f'Imaging reveals {size} {term} in {loc}.'
    ]
    
    return random.choice(templates)

# -----------------------------
# 3. Generate synthetic negative examples
# -----------------------------
def generate_negative_example():
    return random.choice(negative_phrases)

# -----------------------------
# 4. Generate dataset
# -----------------------------
NUM_POSITIVE = 500
NUM_NEGATIVE = 500

data = []

for _ in range(NUM_POSITIVE):
    data.append({'text': generate_positive_example(), 'label': 1})

for _ in range(NUM_NEGATIVE):
    data.append({'text': generate_negative_example(), 'label': 0})

# Shuffle dataset
random.shuffle(data)

# -----------------------------
# 5. Convert to pandas DataFrame
# -----------------------------
df = pd.DataFrame(data)
print(df.head(10))

# -----------------------------
# 6. Save to CSV (optional)
# -----------------------------
df.to_csv('data/synthetic_lung_findings.csv', index=False)
print('Synthetic dataset saved to synthetic_lung_findings.csv')
