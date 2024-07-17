import math

def euclidean_distance(user_data, county_data):
    sum_all = 0
    for i in range(3):
        sum_all += (user_data[i]-county_data[i])**2
    d = math.sqrt(sum_all)
    return round(d,2)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key[1] < arr[j][1]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def print_format(distances, k):
    print("\nNearest counties based on the input data:")
    print('-' * 50)
    print(f"{'Rank':<5}| {'County':<30}| {'Distance':<10}|")
    print('-' * 50)
    # Get the nearest county
    for i in range(k):
        county_name = distances[i][0]
        county_dis = distances[i][1]
        print(f"{i+1:<5}| {county_name:<30}| {county_dis:<10.2f}|")
    print('-' * 50)

def print_info():
    print("\nEuclidean Distance Calculation for Counties Environmental Data")
    print("To determine the county closest to the user's input environmental data (temperature, humidity, and AQI) using the Euclidean distance")
    print()
    # humidity info
    print('---------------------------------------------------------')
    print("|                       Humidity                        |")
    print('---------------------------------------------------------')
    print('| Uncomfortably |     Comfort Range     | Uncomfortably |')
    print('|      Dry      |                       |      Wet      |')
    print('---------------------------------------------------------')
    print('0%             20%                     60%             100%')
    print()
    # air quality idex info
    print('---------------------------------------------------------------------------------------------')
    print("|                                  Air Quality Idex (AQI)                                   |")   
    print('---------------------------------------------------------------------------------------------')
    print("| Good | Moderate | Unhealthy for sensitive groups | Unhealthy | Very unhealthy | Hazardous |")
    print("| 0-50 |  51-100  |           101-150              |  151-200  |    201-300     |    301+   |")
    print('---------------------------------------------------------------------------------------------')
    print()


def main():

    counties_data =[['Zürich, Switzerland', 22, 72, 9],
                    ['Sydney, Australia', 11, 52, 22],
                    ['Oslo, Norway', 15, 87, 28],
                    ['Rome, Italy', 31, 41, 32],
                    ['Osaka, Japan', 25, 91, 38],
                    ['London, UK', 17, 67, 44],
                    ['Amsterdam, Netherlands', 19, 70, 46],
                    ['New York, USA', 25, 87, 54],
                    ['Singapore, Singapore', 30, 72, 58],
                    ['Bangkok, Thailand', 31, 67, 65],
                    ['Hanoi, Vietnam', 32, 75, 70],
                    ['Beijing, China', 29, 60, 80],
                    ['Cairo, Egypt', 32, 50, 94],
                    ['Jakarta, Indonesia', 32, 44, 154],
                    ['Dubai, UAE', 36, 67, 164]]

    while True:
        print_info()

        # temperature
        print("Enter Temperature (Celsius): ", end=" ")
        user_t = int(input().strip())

        # humidity
        print("Enter Humidity (%): ", end=" ")
        user_h = int(input().strip())

        # air quality idex (AQI)
        print("Enter Air Quality Idex: ", end=" ")
        user_a = int(input().strip())

        # k
        while True:
            try:
                print("Enter k (1 - 15): ", end=" ")
                k = int(input().strip())
                if 0 < k <= 15:
                    break
                else:
                    print("Invalid input. Please enter a value from 1 to 15.")
            except ValueError:
                print("Invalid input. Please enter a numeric value from 1 to 15.")


        # distances
        distances = []
        for county in counties_data:
            name = county[0]
            data = county[1:]
            distance = euclidean_distance([user_t, user_h, user_a], data)
            distances.append([name, distance])

        # sort distances
        insertion_sort(distances)

        # print
        print_format(distances, k)

        # run again
        run_again = input("Do you want to run the code again? (y/n): ").strip().lower()
        if run_again != 'y':
            print("Exiting program")
            break

if __name__ == "__main__":
    main()

