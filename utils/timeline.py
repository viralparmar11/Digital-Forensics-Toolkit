import pandas as pd

def create_timeline(file_data):
    df = pd.DataFrame(file_data)
    timeline = df[['File', 'Created', 'Modified']]
    timeline = timeline.sort_values(by='Modified')
    return timeline
