
from Room import Room
from Employee import Employee
from Roomtype import HotelRoomType

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.employees = []
        self.services = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        for room in self.rooms:
            if room._room_number == room_number:
                self.rooms.remove(room)
                return
        print("Room not found")

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                return
        print("Employee not found")

    def add_service(self, service):
        self.services.append(service)

    def reserve_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_reserved:
                    room.reserve()
                    print(f"Room {room_number} reserved successfully.")
                    return
                else:
                    print(f"Room {room_number} is already reserved.")
                    return
        print("Room not found")

    def check_in(self, guest_name, room_number):
        for room in self.rooms:
            if room._room_number == room_number:
                if room.is_reserved:
                    print(f"Checking in {guest_name} to room {room_number}.")
                    room.unreserve()
                    return
                else:
                    print(f"Room {room_number} is not reserved.")
                    return
        print("Room not found")

    def check_out(self, room_number, nights):
        for room in self.rooms:
            if room._room_number == room_number:
                if room.is_occupied:
                    total_cost = room._price_per_night * nights
                    print(f"Checking out from room {room_number}. Total cost: {total_cost}.")
                    room.check_out()
                    return
                else:
                    print(f"Room {room_number} is not reserved.")
                    return
        print("Room not found")


    


def main():
# TESTING
    print("=================================================================")
    print("Test Case 1: Create a Hotel.")
    print("=================================================================")
    hotel = Hotel("Grand Hotel")
    if hotel.name == "Grand Hotel":
        print("Test PASS. The parameter name has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================")
    print("Test Case 2: Add a Room to the Hotel.")
    print("=================================================================")

    room1 = Room(HotelRoomType.DOBLE, 101, "Desocupada", 150)
    hotel.add_room(room1)

    if hotel.rooms[0] == room1:
        print("Test PASS. Room has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_room().")

    print("=================================================================")
    print("Test Case 3: Remove a Room from the Hotel.")
    print("=================================================================")

    hotel.remove_room(101)
    if len(hotel.rooms) == 0:
        print("Test PASS. Room has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_room().")


    print("=================================================================")
    print("Test Case 4: Add an Employee to the Hotel.")
    print("=================================================================")

    emp1 = Employee(1, "John Doe", "Receptionist", 30000)
    hotel.add_employee(emp1)

    if hotel.employees[0] == emp1:
        print("Test PASS. Employee has been successfully added to the hotel.")
    else:
        print("Test FAIL. Check the method add_employee().")

    
    print("=================================================================")
    print("Test Case 5: Remove an Employee from the Hotel.")
    print("=================================================================")

    hotel.remove_employee(1)
    if len(hotel.employees) == 0:
        print("Test PASS. Employee has been successfully removed from the hotel.")
    else:
        print("Test FAIL. Check the method remove_employee().")
    
    print("=================================================================")
    print("Test Case 6: Check-in a Guest.")
    print("=================================================================")

    room2 = Room(HotelRoomType.SUITE, 102, "Desocupada", 300)
    hotel.add_room(room2)
    check_in_result = hotel.check_in(102, "Alice")

    if check_in_result == "Check-in successful for Alice in room 102." and room2.room_state == "Ocupada":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")

    print("=================================================================")
    print("Test Case 7: Check-out a Guest.")
    print("=================================================================")

    check_out_result = hotel.check_out(102, 3)

    if check_out_result == "Check-out successful for Alice from room 102." and room2.room_state == "Desocupada":
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")
  
    print("=================================================================")
    print("Test Case 8: Attempt Check-in on an Occupied Room.")
    print("=================================================================")

    check_in_result = hotel.check_in(102, "Bob")
    if check_in_result == "Room not available or already occupied.":
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")



if __name__ == "__main__":
    main()