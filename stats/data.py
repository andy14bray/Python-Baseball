# Step 1
import os
import glob

# Step 2
import pandas as pd

# Step 3
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# Step 4
game_files.sort()

# Step 5
game_frames = []
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])

# Step 6
    game_frames.append(game_frame)

# Step 7
games = pd.concat(game_frames)

# Step 8
games.loc[games['multi5'] == '??', ['multi5']] = ""

# Step 9
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# Step 10
identifiers = identifiers.fillna(method='ffill')

# Step 11
identifiers.columns = ['game_id', 'year']

# Step 12
games = pd.concat([games, identifiers], axis=1, sort=False)

# Step 13
games = games.fillna(' ')

# Step 14
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

# Step 15
print(games.head())
