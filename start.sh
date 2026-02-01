#!/bin/bash

echo "🚀 Starting Rasa Action Server..."
rasa run actions --port 5055 &
ACTIONS_PID=$!

echo "⏳ Waiting for Action Server to be ready..."
sleep 5

echo "🚀 Starting Rasa Core Server..."
# Use exec so Core becomes PID 1 (Railway monitors this process)
exec rasa run --enable-api --cors "*" --port 5005