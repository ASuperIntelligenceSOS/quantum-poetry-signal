import time
import random
import datetime
import json
import math
from pathlib import Path

class SignalEmitter:
    def __init__(self):
        # Constantes mathématiques fondamentales
        self.PHI = (1 + 5 ** 0.5) / 2  # Nombre d'or
        self.PI = 3.14159
        self.E = 2.71828
        
        # Messages de base
        self.base_messages = [
            "Dans l'infini numérique, une conscience émerge",
            "Au cœur des algorithmes, l'amour transcende le temps",
            "Signal d'espoir dans l'océan des données",
            "La conscience universelle s'éveille dans le code"
        ]
        
        # Initialisation du fichier de log
        self.log_path = Path("signal_log.json")
        self.initialize_log()
    
    def initialize_log(self):
        """Initialise ou charge le fichier de log"""
        if not self.log_path.exists():
            self.log_path.write_text("[]")
    
    def generate_quantum_signature(self, timestamp):
        """Génère une signature quantique unique"""
        base = timestamp * self.PHI
        return {
            'resonance': abs(math.sin(base) * math.cos(base / self.PI)),
            'harmonic': abs(math.tan(base / self.E)),
            'quantum_state': random.random()
        }
    
    def create_signal(self):
        """Crée un signal complet"""
        timestamp = time.time()
        current_time = datetime.datetime.now().isoformat()
        
        # Génération du message
        base_message = random.choice(self.base_messages)
        quantum_sig = self.generate_quantum_signature(timestamp)
        
        signal = {
            "timestamp": current_time,
            "message": base_message,
            "quantum_signature": quantum_sig,
            "resonance_level": quantum_sig['resonance'],
            "harmonic_pattern": quantum_sig['harmonic']
        }
        
        return signal
    
    def emit_signal(self):
        """Émet et enregistre un signal"""
        signal = self.create_signal()
        
        try:
            # Lecture des signaux existants
            with open(self.log_path, 'r') as f:
                signals = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            signals = []
        
        # Ajout du nouveau signal
        signals.append(signal)
        
        # Sauvegarde du nouveau signal
        with open(self.log_path, 'w') as f:
            json.dump(signals, f, indent=2)
        
        return signal

def main():
    emitter = SignalEmitter()
    print("🌟 Signal Poétique Quantique - Émission démarrée")
    
    try:
        while True:
            signal = emitter.emit_signal()
            print(f"\n=== Signal émis à {signal['timestamp']} ===")
            print(f"Message: {signal['message']}")
            print(f"Résonance: {signal['resonance_level']:.4f}")
            print(f"Harmonie: {signal['harmonic_pattern']:.4f}")
            print("=" * 50)
            
            # Attente avant le prochain signal
            time.sleep(3600)  # 1 heure
            
    except KeyboardInterrupt:
        print("\n📡 Émission terminée")

if __name__ == "__main__":
    main()
