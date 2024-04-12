

class Room():
    """Python class to implement a basic version of a hotel room.

    This Python class implements the basic functionalities of a hotel room in a 
    simple hotel management system.

    Syntax
    ------
    obj = Room(room_type, room_number, room_state, room_price)

    Parameters
    ----------
    [in] room_type : Roomtype
        Valid values are "Individual", "Doble", "Suite".
    [in] room_number : int
        Unique number of the room.
    [in] room_state : str
        Occupancy state of the room. Expected values are "Ocupada" or "Desocupada".
    [in] room_price : float
        Price per night for the room.

    Returns
    -------
    obj : Room
        Python object output parameter that represents an instance of the class Room.

    Attributes
    ----------
    """

    #Here you start your code.

    

from Roomtype import HotelRoomType



class Room:
    def __init__(self, room_type, room_number, room_state, room_price):
        if not isinstance(room_type, HotelRoomType):
            raise ValueError("Tipo de habitación inválido")
        if not isinstance(room_number, int) or room_number <= 0:
            raise ValueError("Número de habitación inválido")
        if room_state not in ["Ocupada", "Desocupada"]:
            raise ValueError("Estado de habitación inválido")
        if not isinstance(room_price, (int, float)) or room_price <= 0:
            raise ValueError("Precio por noche inválido")
        
        self._room_type = room_type
        self._room_number = room_number
        self._room_state = room_state
        self._price_per_night = room_price

    def get_room_type(self):
        return self._room_type

    def get_room_number(self):
        return self._room_number

    def get_room_state(self):
        return self._room_state

    def get_price_per_night(self):
        return self._price_per_night

    def is_occupied(self):
        return self._room_state == "Ocupada"

    def check_in(self):
        if self.is_occupied():
            return "La habitación ya está ocupada."
        else:
            self._room_state = "Ocupada"
            return "Check-in exitoso."

    def check_out(self):
        if not self.is_occupied():
            return "La habitación ya está desocupada."
        else:
            self._room_state = "Desocupada"
            return "Check-out exitoso."

def main():
    # TESTING
    print("=================================================================")
    print("Test Case 1: Create a Room.")
    print("=================================================================")
    room1 = Room(HotelRoomType.DOBLE, 101, "Desocupada", 150)

    if room1.get_room_type() == HotelRoomType.DOBLE:
        print("Test PASS. The parameter room_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_number() == 101:
        print("Test PASS. The parameter room_number has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_room_state() == "Desocupada":
        print("Test PASS. The parameter room_state has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if room1.get_price_per_night() == 150:
        print("Test PASS. The parameter room_price has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")



    print("=================================================================")
    print("Test Case 2: Check-in a Room.")
    print("=================================================================")
    room2 = Room(HotelRoomType.SUITE, 102, "Desocupada", 300)
    check_in_result = room2.check_in()

    if check_in_result == "Check-in exitoso." and room2.is_occupied():
        print("Test PASS. Check-in functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_in().")



    print("=================================================================")
    print("Test Case 3: Check-out a Room.")
    print("=================================================================")
    # Assuming room2 was checked in from the previous test
    check_out_result = room2.check_out()

    if check_out_result == "Check-out realizado con éxito." and not room2.is_occupied():
        print("Test PASS. Check-out functionality has been implemented correctly.")
    else:
        print("Test FAIL. Check the method check_out().")

    print("=================================================================")
    print("Test Case 4: Attempt Check-in on an Occupied Room.")
    print("=================================================================")
    room3 = Room(HotelRoomType.INDIVIDUAL, 103, "Ocupada", 100)
    check_in_result = room3.check_in()

    if check_in_result == "La habitación ya está ocupada.":
        print("Test PASS. Attempted check-in on an occupied room handled correctly.")
    else:
        print("Test FAIL. Check the method check_in() for occupied rooms.")


    print("=================================================================")
    print("Test Case 5: Attempt Check-out on a Vacant Room.")
    print("=================================================================")
    # Assuming room3 was made vacant from the previous operation or is initially vacant
    room4 = Room(HotelRoomType.DOBLE, 104, "Desocupada", 200)
    check_out_result = room4.check_out()

    if check_out_result == "La habitación ya está desocupada.":
        print("Test PASS. Attempted check-out on a vacant room handled correctly.")
    else:
        print("Test FAIL. Check the method check_out() for vacant rooms.")

if __name__ == "__main__":
    main()
