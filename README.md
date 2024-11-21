# Mini-Blockchain für Datei-Integritätsprüfung

Ein Python-Skript zur Überwachung und Sicherung der Integrität von Dateien durch die Verwendung eines Blockchain-ähnlichen Ansatzes. Das Skript berechnet Hash-Werte von Dateien, speichert sie in einer Blockchain und überprüft die Kette auf Manipulationen.

## Funktionen
- **Datei-Hashing**: Erzeugt SHA-256-Hashes für Dateien.
- **Blockchain**: Speichert Datei-Hashes in einer Blockchain mit verketteten Blöcken.
- **Integritätsprüfung**: Erkennt Manipulationen an Dateien oder der Blockchain.
- **Chronologische Änderungsverfolgung**: Dokumentiert Änderungen an Dateien über Zeit.

## Anforderungen
- Python 3.6 oder höher
- Keine zusätzlichen Bibliotheken (nur Standardbibliothek)

## Installation
1. **Repository klonen**:
   ```bash
   git clone https://github.com/<dein-benutzername>/file-integrity-blockchain.git
   cd file-integrity-blockchain
