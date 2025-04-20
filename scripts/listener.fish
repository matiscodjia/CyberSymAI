#!/usr/bin/env fish

set duration_minutes 5
set pipe "signal.pipe"
set python_capture "capture_network.py"

# Crée le pipe si besoin
if not test -p $pipe
    mkfifo $pipe
end

for i in (seq 1 $duration_minutes)
    echo "🎧 Capture $i/$duration_minutes..."
    python3 $python_capture

    echo "OK" > $pipe  # Envoie un simple signal
    sleep 1
end