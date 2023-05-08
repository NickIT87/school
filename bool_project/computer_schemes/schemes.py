""" computer schemes library. School project by 10b. """
import logging

# configure log settings
logging.basicConfig(
    filename='computer_schemes.log',
    encoding='utf-8',
    level=logging.DEBUG
)


class CSMethods():
    """ elementary base class """

    def con(self,
            signal_a: bool | int,
            signal_b: bool | int) -> bool | int:
        """ conjunction """
        return signal_a and signal_b

    def des(self,
            signal_a: bool | int,
            sigal_b: bool | int) -> bool | int:
        """ desjunction """
        return signal_a or sigal_b

    def inv(self, signal_a: bool | int) -> bool | int:
        """ inverter """
        return not signal_a


class CSchemes(CSMethods):
    """ logical schemes implementation """

    def emergency_shutdown(self,
                           signal_x: bool | int,
                           signal_y: bool | int,
                           signal_z: bool | int ) -> int:
        """
        normal state 1 0 1
        if y == 0 -> shutdown
        """
        l_side_of_equation = self.con(
            self.inv(self.des(signal_x, signal_y)),
            self.con(signal_x, signal_y)
        )
        r_side_of_equation = self.con(
            self.con(signal_x, self.inv(signal_y)),
            signal_z
        )
        return int(self.des(l_side_of_equation, r_side_of_equation))

    def decoder(self,
                signal_x: bool | int,
                signal_y: bool | int) -> list[bool | int]:
        """ byte decoder for 2 inputs and 4 outputs """
        responce = []
        responce.append(int(self.con(self.inv(signal_x), self.inv(signal_y))))
        responce.append(int(self.con(self.inv(signal_x), signal_y)))
        responce.append(int(self.con(signal_x, self.inv(signal_y))))
        responce.append(int(self.con(signal_x, signal_y)))
        return responce

    def encoder(self,
                signal_x: bool | int,
                signal_y: bool | int,
                signal_z: bool | int,
                signal_f: bool | int) -> list[bool | int]:
        """ 
        byte encoder for 4 inputs and 2 outputs 
        signal_x not modulated
        """
        logging.info("signal_x is: %s", signal_x)
        responce = []
        responce.append(int(self.des(signal_z, signal_f)))
        responce.append(int(self.des(signal_y, signal_f)))
        return responce

    def multiplexer(self,
                    channells: list[bool | int],
                    signal_x0: bool | int,
                    signal_x1: bool | int) -> int:
        """ byte multiplexer on 4 inputs and 1 output """
        data_dc = self.decoder(signal_x0, signal_x1)
        responce_signals = []
        for i in range(4):
            responce_signals.append(self.con(channells[i], data_dc[i]))
        return int(any(responce_signals))

    # def multiplexer_formula(self, c_p1, c_p2, c_p3, c_p4, s_x0, s_x1) -> int:
    #     """
    #     !x0 & !x1 & p1 or !x0 & !x1 & p2 or !x0 & !x1 & p3 or !x0 & !x1 & p4 or
    #     """
    #     res = not s_x0 and not s_x1 and c_p1 or not s_x0 and not s_x1 and c_p2 or \
    #         not s_x0 and not s_x1 and c_p3 or not s_x0 and not s_x1 and c_p4
    #     return int(res)

# точка входу в програму
if __name__ == '__main__':
    scheme = CSchemes()
    print(scheme.multiplexer([1, 0, 0, 0], 0, 0))
    print(scheme.multiplexer([0, 1, 0, 0], 0, 1))
    print(scheme.multiplexer([0, 0, 1, 0], 1, 0))
    print(scheme.multiplexer([0, 0, 0, 1], 1, 1))
    print(scheme.multiplexer([0, 0, 0, 1], 0, 1))

    # print(scheme.encoder(0, 0, 0, 1))
    # print(scheme.encoder(0, 0, 1, 0))
    # print(scheme.encoder(0, 1, 0, 0))
    # print(scheme.encoder(1, 0, 0, 0))
