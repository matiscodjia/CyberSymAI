#!/usr/bin/env fish

set duration_minutes 60
set duration 0.083
set pipe "signal.pipe"
set python_capture "capture_network.py"

# Crée le pipe si besoin
if not test -p $pipe
    mkfifo $pipe
end

for i in (seq 1 (math "$duration_minutes / $duration"))
    echo "🎧 Capture $i..."
    python3 $python_capture

    echo "OK" > $pipe  # Envoie un simple signal
    sleep 1
end