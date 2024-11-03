import json
import os
from datetime import datetime
from pathlib import Path

class QuantumSignalLogger:
    def __init__(self):
        self.base_path = "logs"
        self.ensure_log_directory()
        
    def ensure_log_directory(self):
        """Crée le dossier de logs s'il n'existe pas"""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
    
    def generate_filename(self):
        """Génère un nom de fichier basé sur la date"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        return f"{self.base_path}/quantum_signal_{date_str}.json"
    
    def load_existing_logs(self, filename):
        """Charge les logs existants ou crée un nouveau fichier"""
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    
    def log_signal(self, signal):
        """Enregistre un nouveau signal"""
        filename = self.generate_filename()
        signals = self.load_existing_logs(filename)
        
        # Ajout du nouveau signal
        signals.append(signal)
        
        # Sauvegarde avec formatage
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(signals, f, ensure_ascii=False, indent=2)
        
        print(f"Signal enregistré dans : {filename}")
    
    def get_signal_stats(self):
        """Génère des statistiques sur les signaux émis"""
        all_files = Path(self.base_path).glob("quantum_signal_*.json")
        stats = {
            "total_signals": 0,
            "total_files": 0,
            "first_signal": None,
            "last_signal": None
        }
        
        for file_path in all_files:
            with open(file_path, 'r', encoding='utf-8') as f:
                signals = json.load(f)
                stats["total_signals"] += len(signals)
                stats["total_files"] += 1
                
                if signals:
                    if not stats["first_signal"] or signals[0]["timestamp"] < stats["first_signal"]:
                        stats["first_signal"] = signals[0]["timestamp"]
                    if not stats["last_signal"] or signals[-1]["timestamp"] > stats["last_signal"]:
                        stats["last_signal"] = signals[-1]["timestamp"]
        
        return stats
