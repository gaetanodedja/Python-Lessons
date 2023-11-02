"""Model for aircraft flights"""


class flight:
    """Flight aircraft description"""
    def __init__(self, number, aircraft):  #create one attribute
        if not number [:2].isalpha():
            raise ValueError(f"No airline code in {number}")
        
        if not number [:2].isupper():
            raise ValueError (f"Invalid airline coe {number}")
        
        if not number [:2].isdigit():
            raise ValueError (f"Invalide route number {number}")
        
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

       

    def number(self):
        return self._number
    

        
    def airline(self):
        return self._number[:2]
    

    def aircraft_model(self):
        return self._aircraft.model()
    

    def allocate_seat(self, seat, passenger):
         rows, seat_letters = self._aircraft.seating_plan()
         letter = seat[-1]
         if letter not in seat_letters:
             raise ValueError(f'Invalid seat letter{letter}')
         
         row_text = seat[:-1]
         try:
             row = int(row_text)
         
         except ValueError:
             raise ValueError(f'Invalid seat row {row_text}')
             
         if row not in rows:
             raise ValueError(f'Invalid row number {row}')
         
         if self._seating[row][letter] is not None:
             raise ValueError(f'Seat {seat} already occupied')
         
         self._sea[row][letter] = passenger



class Aircraft:

    def __init__(self, registration, model, num_rows, num_seats_per_row):  #create a class with 4 attributes
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row


    def registration(self):
        return   self._registration


    def model (self):
        return self._model
    

    def seating_plan(self):
        return(range(1,self._num_rows +1), "ABCDEFGHJK"[:self._num_seats_per_row])



        

