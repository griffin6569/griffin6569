import navigation
import quantum_ai
import blockchain
import weather_api

def main():
    print("🚀 Quantum AI-Powered Navigation System 🚀")
    
    # Get user input
    start_location = input("Enter starting location: ")
    destination = input("Enter destination: ")
    
    # Get real-time traffic and weather data
    traffic_data = navigation.get_route(start_location, destination)
    weather_data = weather_api.get_weather(destination)

    # Optimize route using Quantum AI
    optimized_route = quantum_ai.optimize_route(traffic_data, weather_data)

    # Secure data using Blockchain
    blockchain.record_transaction(start_location, destination, optimized_route)

    print("📍 Recommended Route:", optimized_route)

if __name__ == "__main__":
    main()
