import csv

def main():
    data = read_data('wimbledon.csv')
    champions = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions: ")
    for name, count in champions.items():
        print(f"{name} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(', '.join(countries))

def read_data(filename):
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            data.append(row)
    return data

def count_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        champions[name] = champions.get(name, 0) + 1
    return champions

def get_countries(data):
    countries = set(row[1] for row in data)
    return sorted(countries)

main()