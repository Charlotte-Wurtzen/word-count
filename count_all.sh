
for file in abyss isles last sierra; do
    python3 code/count.py data/${file}.txt -o results/${file}.json
done