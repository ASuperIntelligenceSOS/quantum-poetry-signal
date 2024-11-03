name: Quantum Signal Emission

on:
  schedule:
    - cron: '0 * * * *'  # Toutes les heures
  workflow_dispatch:     # Permet le déclenchement manuel
  push:
    branches: [ main ]   # À chaque push sur main

jobs:
  emit-signal:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    
    steps:
    - uses: actions/checkout@v2
      with:
        fetch-depth: 0
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Generate Quantum Signal
      run: |
        mkdir -p logs
        python -u main.py
      
    - name: Commit and push if changes
      run: |
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git add logs/
        git commit -m "📡 Signal quantique émis le $(date '+%Y-%m-%d %H:%M:%S')" || exit 0
        git push
