for file in abyss isles last sierra; do
    python3 code/plot.py results/${file}.json -o figures/${file}.png
done