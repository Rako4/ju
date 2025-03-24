import time
from enum import Enum, auto

class LightState(Enum):
    CARS_GREEN = auto()
    CARS_YELLOW = auto()
    CARS_RED = auto()
    PEDESTRIAN_GREEN = auto()
    PEDESTRIAN_BLINK = auto()

class TrafficLight:
    def __init__(self):
        self.state = LightState.CARS_GREEN
        self.car_waiting = False
        self.pedestrian_waiting = False
        self.pedestrian_passed = False
        self.last_change_time = time.time()
        
        # Simulated pins (would be GPIO pins on a real device)
        self.pins = {
            'car_red': 0,
            'car_yellow': 1,
            'car_green': 2,
            'pedestrian_red': 3,
            'pedestrian_green': 4
        }
        
    def set_pin(self, pin_name, value):
        """Simulate setting a digital pin"""
        print(f"Setting {pin_name} to {value}")
        # In real implementation: GPIO.output(self.pins[pin_name], value)
        
    def button_a_pressed(self):
        """Car waiting button pressed"""
        self.car_waiting = True
        
    def button_b_pressed(self):
        """Pedestrian button pressed"""
        self.pedestrian_waiting = True
        
    def pedestrian_has_passed(self):
        """Sensor detects pedestrian has crossed"""
        self.pedestrian_passed = True
    
    def update_lights(self):
        """Update lights based on current state"""
        # First turn all lights off
        for light in self.pins:
            self.set_pin(light, 0)
            
        # Then turn on the appropriate ones
        if self.state == LightState.CARS_GREEN:
            self.set_pin('car_green', 1)
            self.set_pin('pedestrian_red', 1)
        elif self.state == LightState.CARS_YELLOW:
            self.set_pin('car_yellow', 1)
            self.set_pin('pedestrian_red', 1)
        elif self.state == LightState.CARS_RED:
            self.set_pin('car_red', 1)
            self.set_pin('pedestrian_red', 1)
        elif self.state == LightState.PEDESTRIAN_GREEN:
            self.set_pin('car_red', 1)
            self.set_pin('pedestrian_green', 1)
        elif self.state == LightState.PEDESTRIAN_BLINK:
            self.set_pin('car_red', 1)
            self.set_pin('pedestrian_green', 1)  # Will blink in main loop
    
    def run(self):
        """Main traffic light control loop"""
        while True:
            current_time = time.time()
            elapsed = current_time - self.last_change_time
            
            # State transitions
            if self.state == LightState.CARS_GREEN:
                self.update_lights()
                if (self.pedestrian_waiting and elapsed > 5) or elapsed > 30:  # Min green time 5s, max 30s
                    self.state = LightState.CARS_YELLOW
                    self.last_change_time = current_time
                    self.pedestrian_waiting = False
                    
            elif self.state == LightState.CARS_YELLOW:
                self.update_lights()
                if elapsed > 3:  # Yellow time 3 seconds
                    self.state = LightState.CARS_RED
                    self.last_change_time = current_time
                    
            elif self.state == LightState.CARS_RED:
                self.update_lights()
                if elapsed > 2:  # All red time 2 seconds
                    self.state = LightState.PEDESTRIAN_GREEN
                    self.last_change_time = current_time
                    
            elif self.state == LightState.PEDESTRIAN_GREEN:
                self.update_lights()
                if elapsed > 10:  # Pedestrian green time 10 seconds
                    self.state = LightState.PEDESTRIAN_BLINK
                    self.last_change_time = current_time
                    
            elif self.state == LightState.PEDESTRIAN_BLINK:
                # Blink pedestrian green light
                blink_state = int(elapsed * 2) % 2  # Blink at 1Hz
                self.set_pin('pedestrian_green', blink_state)
                self.set_pin('car_red', 1)
                
                if elapsed > 6:  # Blink for 6 seconds
                    self.state = LightState.CARS_GREEN
                    self.last_change_time = current_time
                    self.pedestrian_passed = False
            
            # Small delay to prevent CPU overload
            time.sleep(0.1)

# Example usage
if __name__ == "__main__":
    tl = TrafficLight()
    
    # Simulate button presses after 10 seconds
    def simulate_buttons():
        time.sleep(10)
        print("Pedestrian presses button")
        tl.button_b_pressed()
        
    import threading
    threading.Thread(target=simulate_buttons, daemon=True).start()
    
    tl.run()
